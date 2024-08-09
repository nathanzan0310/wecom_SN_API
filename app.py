from flask import Flask, request
from helper.WXBizMsgCrypt3 import WXBizMsgCrypt
import logging
import os
from pathlib import Path
from dotenv import load_dotenv
from urllib.parse import unquote


env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

token = os.environ.get('TOKEN')
aes_key = os.environ.get('AES_KEY')
service_id = os.environ.get('SERVICE_ID')

app = Flask(__name__)

logging.basicConfig(filename='callback.log', level=logging.INFO, format='%(asctime)s %(message)s')

wx_crypt = WXBizMsgCrypt(token, aes_key, service_id)

@app.route('/hi')
def hello():
    return 'Hello, World!'

@app.route('/')
def welcome():
    return 'This is the Tencent Overseas Midserver for communication from WeCom to Servicenow. Please contact @nathanan for more information.'


@app.route('/callback', methods=['POST', 'GET'])
def handle_message():
    msg_signature = request.args.get('msg_signature')
    timestamp = request.args.get('timestamp')
    # timestamp = '1722375628'
    nonce = request.args.get('nonce')
    # nonce = 'n6dy7shbz19'
    echostr = request.args.get('echostr')
    data = request.data

    if request.method == 'GET':
        # Log incoming request
        logging.info("Received GET request with msg_signature=%s, timestamp=%s, nonce=%s, echostr=%s",
                 msg_signature, timestamp, nonce, echostr)
        
        # Verify URL
        ret, message = wx_crypt.VerifyURL(msg_signature, timestamp, nonce, echostr)

        if ret != 0:
            logging.error("Failed to verify URL: %s", ret)
            return f'error: {ret}', 400
        
        return message, 200

    elif request.method == 'POST':
        # Log incoming request
        logging.info("Received POST request with msg_signature=%s, timestamp=%s, nonce=%s, data=%s",
                 msg_signature, timestamp, nonce, data)

        # Decrypt message
        ret, message = wx_crypt.DecryptMsg(data, msg_signature, timestamp, nonce)

        if ret != 0:
            logging.error("Failed to decrypt message: %s", ret)
            return f'error: {ret}', 400
        
        # decrypted_message = message.decode('utf-8')  # Decode the decrypted message
        # logging.info("Decrypted message: %s", decrypted_message)
        # print("Decrypted message:", decrypted_message)
        
        # return f'decrypted_message: {decrypted_message}', 200
        return message, 200
    return 'what you doing', 405

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)
