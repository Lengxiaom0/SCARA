# encoding:utf-8
import requests
import base64

from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcore.exceptions.exceptions import ConnectionException
from huaweicloudsdkcore.exceptions.exceptions import RequestTimeoutException
from huaweicloudsdkcore.exceptions.exceptions import ServiceResponseException
from huaweicloudsdkcore.http.http_config import HttpConfig
from huaweicloudsdkimage.v2.image_client import ImageClient
from huaweicloudsdkimage.v2.model.image_main_object_detection_req import ImageMainObjectDetectionReq
from huaweicloudsdkimage.v2.model.run_image_main_object_detection_request import RunImageMainObjectDetectionRequest
from huaweicloudsdkimage.v2.region.image_region import ImageRegion
import os
import json 

os.environ['HUAWEICLOUD_SDK_AK']="54LIZALK5RTX3XSIYI6F"
os.environ['HUAWEICLOUD_SDK_SK']="qS9i5sYULiMk3hEes7FcrjBfCXNb4pI2AiawfIbU"

class ImageMainObjectDetectionDemo:
    def __init__(self):
        pass

    def main(self,real_imagepath):
        # 设置AK和SK
        # 认证用的ak和sk直接写到代码中有很大的安全风险，建议在配置文件或者环境变量中密文存放，使用时解密，确保安全；
        # 本示例以ak和sk保存在环境变量中来实现身份验证为例，运行本示例前请先在本地环境中设置环境变量HUAWEICLOUD_SDK_AK和HUAWEICLOUD_SDK_SK。
        ak = os.environ["HUAWEICLOUD_SDK_AK"]
        sk = os.environ["HUAWEICLOUD_SDK_SK"]
        auth = BasicCredentials(
            ak=ak,
            sk=sk
        )
        config = HttpConfig.get_default_config()
        # config.ignore_ssl_verification = True
        config.proxy_protocol = "http"
        client = ImageClient.new_builder() \
            .with_credentials(credentials=auth) \
            .with_region(region=ImageRegion.value_of(region_id="cn-north-4")) \
            .with_http_config(config=config) \
            .build()
        request = RunImageMainObjectDetectionRequest()
        body = ImageMainObjectDetectionReq()
        # 替换示例中的图像地址
        imagepath =real_imagepath
        with open(imagepath, "rb") as bin_data:
            image_data = bin_data.read()
        image_base64 = base64.b64encode(image_data).decode("utf-8")  # 使用图片的base64编码
        body.image = image_base64
        request.body = body
        boudning_box=[]
        main_object_box=[]
        try:
            response = client.run_image_main_object_detection(request)
            respone_data=json.loads(str(response))
            for result in respone_data['result']:
                label = result['label']
                location = result['location']
                confidence = result['confidence']
            
                if label == 'bounding_box':
                    boudning_box_x = int(location['top_left_x'])
                    boudning_box_y = int(location['top_left_y'])
                    boudning_box_height = int(location['height'])
                    boudning_box_width = int(location['width'])
                    boudning_box=[boudning_box_x,boudning_box_y,boudning_box_width,boudning_box_height,confidence]
                    print(f"bounding_box - top_left_x: {boudning_box_x}, top_left_y: {boudning_box_y}, height: {boudning_box_height}, width: {boudning_box_width}, confidence: {confidence}")
                elif label == 'main_object_box':
                    main_object_box_x = int(location['top_left_x'])
                    main_object_box_y = int(location['top_left_y'])
                    main_object_box_height = int(location['height'])
                    main_object_box_width = int(location['width'])
                    main_object_box=[main_object_box_x,main_object_box_y,main_object_box_width,main_object_box_height,confidence]
                    print(f"main_object_box - top_left_x: {main_object_box_x}, top_left_y: {main_object_box_y}, height: {main_object_box_height}, width: {main_object_box_width}, confidence: {confidence}")
            
            return boudning_box,main_object_box
        except (ConnectionException, RequestTimeoutException) as e:
            print(e.err_message)
        except ServiceResponseException as e:
            print(e.status_code)
            print(e.error_code)
            print(e.error_msg)
        

