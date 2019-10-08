import requests
from datetime import datetime
import binascii


phoneNumber = '0000000000' # enter phone number here

message = 'Hello, world!'


gsm = ("@£$¥èéùìòÇ\nØø\rÅåΔ_ΦΓΛΩΠΨΣΘΞ\x1bÆæßÉ !\"#¤%&'()*+,-./0123456789:;<=>?"
       "¡ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÑÜ`¿abcdefghijklmnopqrstuvwxyzäöñüà")
ext = ("````````````````````^```````````````````{}`````\\````````````[~]`"
       "|````````````````````````````````````€``````````````````````````")

def get_sms_time():
    return datetime.now().strftime("%y;%m;%d;%H;%M;%S;+2")

def gsm_encode(plaintext):
    res = bytearray()
    for c in plaintext:
        res.append(0)
        idx = gsm.find(c)
        if idx != -1:
            res.append(idx)
            continue
        idx = ext.find(c)
        if idx != -1:
            res.append(27)
            res.append(idx)
    return binascii.hexlify(res)

def get_cookie():
    cookies = {
        'stok': '',
    }

    headers = {
        'Origin': 'http://192.168.0.1',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Referer': 'http://192.168.0.1/home.htm',
        'X-Requested-With': 'XMLHttpRequest',
        'Connection': 'keep-alive',
    }

    data = {
        'password': 'YWRtaW4=',  # equal to 'admin' as password in router
        'goformId': 'LOGIN_EXCLUSIVE'
    }
    response = requests.post('http://192.168.0.1/goform/goform_set_cmd_process', headers=headers, cookies=cookies,
                             data=data, verify=False)

    return str(response.cookies).replace('<RequestsCookieJar[<Cookie stok=', '').replace(' for 192.168.0.1/>]>', '')




def send_sms(phoneNumber, messageEncoded):
    cookies = {
        'stok': get_cookie(),
    }

    headers = {
        'Origin': 'http://vodafonemobile.wifi',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Referer': 'http://vodafonemobile.wifi/home.htm',
        'X-Requested-With': 'XMLHttpRequest',
        'Connection': 'keep-alive',
    }

    data = {
        'goformId': 'SEND_SMS',
        'Number': phoneNumber,
        'sms_time': get_sms_time(),
        'MessageBody': messageEncoded,
        'ID': '-1',
        'encode_type': 'GSM7_default',
    }

    print('sending sms...')
    response = requests.post('http://vodafonemobile.wifi/goform/goform_set_cmd_process', headers=headers,
                             cookies=cookies, data=data, verify=False)
    return response.content


messageEncoded = gsm_encode(message)

# send SMS
print(send_sms(phoneNumber, messageEncoded))
