import time
import random
from WXBizMsgCrypt3 import WXBizMsgCrypt, SHA1
from helper import ierror

import os
from pathlib import Path
from dotenv import load_dotenv


env_path = Path('..') / '.env'
load_dotenv(dotenv_path=env_path)

token = os.environ.get('TOKEN')
aes_key = os.environ.get('AES_KEY')
corp_id = os.environ.get('CORP_ID')

# Initialize the WXBizMsgCrypt instance
wxcpt = WXBizMsgCrypt(token, aes_key, corp_id)

sReplyMsg = """<xml>
    <ToUserName><![CDATA[wx5823bf96d3bd56c7]]></ToUserName>
    <FromUserName><![CDATA[mycreate]]></FromUserName>
    <CreateTime>1409659813</CreateTime>
    <MsgType><![CDATA[text]]></MsgType>
    <Content><![CDATA[hello]]></Content>
    <MsgId>4561255354251345929</MsgId>
    <AgentID>218</AgentID>
</xml>"""

timestamp = str(int(time.time()))
nonce = str(random.randint(100000, 999999))

ret, encrypted_message = wxcpt.EncryptMsg(sReplyMsg, nonce, timestamp)
if ret != ierror.WXBizMsgCrypt_OK:
    print(f"Encryption failed with error code: {ret}")
else:
    print("Encrypted Message:")
    print(encrypted_message)

    from xml.etree import ElementTree as ET
    xml_tree = ET.fromstring(encrypted_message)
    msg_encrypt = xml_tree.find("Encrypt").text
    msg_signature = xml_tree.find("MsgSignature").text
    timestamp = xml_tree.find("TimeStamp").text
    nonce = xml_tree.find("Nonce").text

    print("Message Signature:", msg_signature)
    print("Timestamp:", timestamp)
    print("Nonce:", nonce)
    print("Encrypted Message:", msg_encrypt)