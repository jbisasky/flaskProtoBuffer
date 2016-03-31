import requests
import calendar_pb2

customer = calendar_pb2.Customer()
customer.id = 32
serial = customer.SerializeToString()

url = 'http://localhost:5000'
headers = {
    'Content-type': 'binary/octet-stream',
    'Content-transfer-encoding': 'binary',
}
res = requests.post(url, data=serial, headers=headers)
print str(res)
