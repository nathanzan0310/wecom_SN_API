from WXBizMsgCrypt3 import WXBizMsgCrypt, SHA1
import os
from pathlib import Path
from dotenv import load_dotenv
import base64


env_path = Path('..') / '.env'
load_dotenv(dotenv_path=env_path)

# token = os.environ.get('TOKEN')
# aes_key = os.environ.get('AES_KEY')
# corp_id = os.environ.get('CORP_ID')

# Karim example
# msg_signature = "4a9da54e7b7a156aab9144894104451f0fa5c1bf"
# timestamp = "13500001234"
# nonce = "123412323"
# echostr = "jgjNzK647rH55m+hnKc5Aw"

corpId = "wx5823bf96d3bd56c7"
token = "QDG6eK"
encodingAesKey = "jWmYm7qr5nMoAUwZRjGtBxmz3KA1tkAj3ykkR6q2B2C"

AESKey = base64.b64decode(encodingAesKey + "=")
signature = "477715d11cdb4164915debcba66cb864d751f3e6"
timestamp = "1409659813"
nonce = "1372623149"
msg_encrypt = "RypEvHKD8QQKFhvQ6QleEB4J58tiPdvo+rtK1I9qca6aM/wvqnLSV5zEPeusUiX5L5X/0lWfrf0QADHHhGd3QczcdCUpj911L3vg3W/sYYvuJTs3TUUkSUXxaccAS0qhxchrRYt66wiSpGLYL42aM6A8dTT+6k4aSknmPj48kzJs8qLjvd4Xgpue06DOdnLxAUHzM6+kDZ+HMZfJYuR+LtwGc2hgf5gsijff0ekUNXZiqATP7PF5mZxZ3Izoun1s4zG4LUMnvw2r+KqCKIw+3IQH03v+BCA9nMELNqbSf6tiWSrXJB3LAVGUcallcrw8V2t9EL4EhzJWrQUax5wLVMNS0+rUPA3k22Ncx4XXZS9o0MBH27Bo6BpNelZpS+/uh9KsNlY6bHCmJU9p8g7m3fVKn28H3KDYA5Pl/T8Z1ptDAVe0lXdQ2YoyyH2uyPIGHBZZIs2pDBS8R07+qN+E7Q==";

# sort_str = sorted((token, timestamps, nonce, msg_encrypt))
# sort_str = ''.join(sort_str)

msg_signature = SHA1.getSHA1(token, timestamp, nonce, msg_encrypt)


# wxcrypt = WXBizMsgCrypt(sToken=token, sEncodingAESKey=aes_key, sReceiveId=corp_id)
#
# print(wxcrypt.DecryptMsg(echostr, msg_signature, timestamp, nonce))