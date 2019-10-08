import requests
from datetime import datetime


now = datetime.now()
phoneNumber = '0000000000' # enter phone number here
message = '0074006500730074' # TODO message encoding rawMessage = 'test'



print(message)

smsTime = now.strftime("%y;%m;%d;%H;%M;%S;+2")

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
  'password': 'YWRtaW4=', # equal to 'admin' as password in router
  'goformId': 'LOGIN_EXCLUSIVE'
}
response = requests.post('http://192.168.0.1/goform/goform_set_cmd_process', headers=headers, cookies=cookies, data=data, verify=False)

# get a admin login cookie, to emulate an admin user accessing web interface
validCookie = str(response.cookies).replace('<RequestsCookieJar[<Cookie stok=', '').replace(' for 192.168.0.1/>]>', '')

cookies = {
    'stok': validCookie,
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
  'sms_time': smsTime,
  'MessageBody': message,
  'ID': '-1',
  'encode_type': 'GSM7_default',
}


# send SMS
print('sending sms...')
response = requests.post('http://vodafonemobile.wifi/goform/goform_set_cmd_process', headers=headers, cookies=cookies, data=data, verify=False)
print(response.content)
