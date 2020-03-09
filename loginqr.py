#get auth 👉 https://api.boteater.us/get_token
try:
    header = "ios_ipad"
    auth = "Z6vMBEnkp04n"
    result = json.loads(requests.get("https://api.boteater.us/line_qr_v2?header="+header+"&auth="+auth).text)
    print("Login IP: {}".format(result["result"]["login_ip"]))
    print("QR Link: {}".format(result["result"]["qr_link"]))
    result = json.loads(requests.get(result["result"]["callback"]+"&auth="+auth).text)
    if result["status"] != 200:
      raise Exception("Timeout!!!")
    print("Pincode: "+result["result"]["pin_code"])
    result = json.loads(requests.get(result["result"]["callback"]+"&auth="+auth).text)
    if result["status"] != 200:
      raise Exception("Timeout!!!")
    bardifamz = LINE(result["result"]["token"],appName="IOSIPAD\t9.18.1\tiPhone X\t12.4.1")
    print("Login Sukses")
except:pass