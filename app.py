from flask import Flask, request
from helper.WXBizMsgCrypt3 import WXBizMsgCrypt
import logging
import os
from pathlib import Path
from dotenv import load_dotenv


env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

token = os.environ.get('TOKEN')
aes_key = os.environ.get('AES_KEY')
corp_id = os.environ.get('CORP_ID')

app = Flask(__name__)

logging.basicConfig(filename='callback.log', level=logging.INFO, format='%(asctime)s %(message)s')

wx_crypt = WXBizMsgCrypt(token, aes_key, corp_id)

@app.route('/hi')
def hello():
    return 'Hello, World!'

@app.route('/')
def welcome():
    return 'This is Tencent Overseas Midserver for Service Now and WeCom. Please contact @nathanan for more information.'

@app.route('/callback', methods=['POST'])
def handle_message():
    msg_signature = request.args.get('msg_signature')
    timestamp = request.args.get('timestamp')
    nonce = request.args.get('nonce')
    data = request.data

    # Log incoming request
    logging.info("Received POST request with msg_signature=%s, timestamp=%s, nonce=%s, data=%s",
                 msg_signature, timestamp, nonce, data)

    # Decrypt message
    ret, message = wx_crypt.DecryptMsg(data, msg_signature, timestamp, nonce)

    # if ret != 0:
    #     logging.error("Failed to decrypt message: %s", ret)
    #     return jsonify({'error': 'Failed to decrypt message', 'code': ret}), 400
    #
    # decrypted_message = message.decode('utf-8')  # Decode the decrypted message
    # logging.info("Decrypted message: %s", decrypted_message)
    # print("Decrypted message:", decrypted_message)
    #
    # # Return decrypted message as response for verification (test)
    # return jsonify({'decrypted_message': decrypted_message}), 200
    return '', 200

if __name__ == '__main__':
    app.run(debug=True)
