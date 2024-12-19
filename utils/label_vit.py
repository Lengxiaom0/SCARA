import os
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkimage.v2.region.image_region import ImageRegion
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkimage.v2 import *
import base64
import json 

os.environ['CLOUD_SDK_AK']="54LIZALK5RTX3XSIYI6F"
os.environ['CLOUD_SDK_SK']="qS9i5sYULiMk3hEes7FcrjBfCXNb4pI2AiawfIbU"

def label_image(image_path):
    # The AK and SK used for authentication are hard-coded or stored in plaintext, which has great security risks. It is recommended that the AK and SK be stored in ciphertext in configuration files or environment variables and decrypted during use to ensure security.
    # In this example, AK and SK are stored in environment variables for authentication. Before running this example, set environment variables CLOUD_SDK_AK and CLOUD_SDK_SK in the local environment
    ak = os.environ["CLOUD_SDK_AK"]
    sk = os.environ["CLOUD_SDK_SK"]

    credentials = BasicCredentials(ak, sk)

    client = ImageClient.new_builder() \
        .with_credentials(credentials) \
        .with_region(ImageRegion.value_of("cn-north-4")) \
        .build()

    try:
        request = RunImageMediaTaggingDetRequest()
        
        with open(image_path, "rb") as bin_data:
                    image_data = bin_data.read()
        image_base64 = base64.b64encode(image_data).decode("utf-8")  # 使用图片的base64编码
        request.body = ImageMediaTaggingReq(
                    image=image_base64
                )
        response = client.run_image_media_tagging_det(request)
        data = json.loads(str(response))
 
        # 初始化一个空列表来存储结果
        results = []
        
        # 遍历所有标签
        for tag in data['result']['tags']:
            # 遍历标签下的所有实例
            for instance in tag['instances']:
                # 将类别、置信度和坐标添加到结果列表中
                confidence = float(instance['confidence'])
                category = tag['tag']
                bbox = instance['bounding_box']
                coords = [bbox['top_left_x'], bbox['top_left_y'], bbox['width'], bbox['height']]
                results.append((confidence, category, coords))
        
        # 根据置信度降序排序结果列表
        results.sort(reverse=True, key=lambda x: x[0])
        
        # 打印置信度最高的前几个结果（例如，前3个）
        confidence, category, coords = results[0]
        confidence2, category2, coords2 = results[1]
        bbox1=[coords[0],coords[1],coords[2],coords[3],confidence,category]
        bbox2=[coords2[0],coords2[1],coords2[2],coords2[3],confidence2,category2]
        first_center=[(coords[0]+coords[2]/2),(coords[1]+coords[3]/2)]
        second_center=[(coords2[0]+coords2[2]/2),(coords2[1]+coords2[3]/2)]
        print("category1,category2:",category,category2)    
        with open(r"D:\2024_match\huawei\new_robo_Project\txt\identifed_cur.txt","w",encoding='utf-8') as f:
             f.write("我看见了"+category+"和"+category2)
        return bbox1,bbox2,first_center,second_center
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)

