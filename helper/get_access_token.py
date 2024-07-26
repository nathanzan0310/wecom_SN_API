import requests

def get_request():
    url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
    params = {'corpid': 'wxab249edd27d57738',
              'corpsecret': '9f-0OiMRSxQObTJbZff_tfabGlV0pB3Gc1yAfCsG-ro'}

    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            errcode = response.json()['errcode']
            errmsg = response.json()['errmsg']
            access_token = response.json()['access_token']
            expires_in = response.json()['expires_in']
            print("Success:\n", f"Get request resulted in errcode {errcode} with errmsg: {errmsg}.\n Your access token: {access_token}\n expires in {expires_in} seconds.\n")
        else:
            print("Failed with status code:", response.status_code)
    except requests.RequestException as e:
        print("Request failed:", e)

if __name__ == '__main__':
    get_request()