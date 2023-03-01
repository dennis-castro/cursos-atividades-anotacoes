import json
from urllib import request


cota = request.get("http://economia.awesomeapi.com.br/json/last/USD-BRL")
cota = cota.json()
print(cota)

