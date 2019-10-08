import requests

cookies = {
    'stok': 'C18CE7B3031057A387E84736',
}

headers = {
    'Origin': 'http://vodafonemobile.wifi',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Referer': 'http://vodafonemobile.wifi/home.htm',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
}

data = {
  'goformId': 'SEND_SMS',
  'Number': '0000',
  'sms_time': '19;10;08;12;48;51;+2',
  'MessageBody': '0074006500730074002000740065007300740020007400650073007400740065007300740020007400650073007400200074006500730074',
  'ID': '-1',
  'encode_type': 'GSM7_default',
  '_': '1570531731114'
}

response = requests.post('http://vodafonemobile.wifi/goform/goform_set_cmd_process', headers=headers, cookies=cookies, data=data, verify=False)



print(response.content)
