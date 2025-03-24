import requests
from pynocaptcha import HcaptchaCracker

address = ''
cracker = HcaptchaCracker(
    user_token="***",
    sitekey="65e4c3a2-66f6-4316-b670-ddfe81fc1a56",
    referer="https://faucet.dev.gblend.xyz/",
    debug=False,
    show_ad=False
)
ret = cracker.crack()
if ret:
    url = "https://faucet.dev.gblend.xyz/api/claim"

    payload = {"address": address}
    headers = {
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9",
        "content-type": "application/json",
        "h-captcha-response": ret['data']['generated_pass_UUID']
    }
    response = requests.request("POST", url, json=payload, headers=headers)
    print(response.text)
