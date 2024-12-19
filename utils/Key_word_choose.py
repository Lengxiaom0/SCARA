# coding: utf-8

import os
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdknlp.v2.region.nlp_region import NlpRegion
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdknlp.v2 import *
import json 

os.environ['CLOUD_SDK_AK']="54LIZALK5RTX3XSIYI6F"
os.environ['CLOUD_SDK_SK']="qS9i5sYULiMk3hEes7FcrjBfCXNb4pI2AiawfIbU"


def extract_keywords(text):
# The AK and SK used for authentication are hard-coded or stored in plaintext, which has great security risks. It is recommended that the AK and SK be stored in ciphertext in configuration files or environment variables and decrypted during use to ensure security.
# In this example, AK and SK are stored in environment variables for authentication. Before running this example, set environment variables CLOUD_SDK_AK and CLOUD_SDK_SK in the local environment
    ak = os.environ["CLOUD_SDK_AK"]
    sk = os.environ["CLOUD_SDK_SK"]

    credentials = BasicCredentials(ak, sk)

    client = NlpClient.new_builder() \
        .with_credentials(credentials) \
        .with_region(NlpRegion.value_of("cn-north-4")) \
        .build()
    try:
        request = RunKeywordExtractRequest()
        request.body = KeywordExtractReq(
            text=text,
        )
        response = client.run_keyword_extract(request)
        response_data=json.loads(str(response))
        word_list=response_data['words']
        print(word_list)
        return word_list
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)
