import requests

Baseurl="https://datahunter.store/api/"
headers={"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiYzViMTZmYmYxOTk4Yzk3ODU3YzNjY2JkZWI5OTYxYWUxYTExOGZjNGRiMzM1Mjc1ZDhiMjQ0YjE4YTk2M2ViZTVlMTkwOTJiNTE1NmFhMDQiLCJpYXQiOjE2MjIwMTMxMzQuNjQ1Mzg5LCJuYmYiOjE2MjIwMTMxMzQuNjQ1MzkzLCJleHAiOjE2NTM1NDkxMzQuMzEzMjI2LCJzdWIiOiIxMjEiLCJzY29wZXMiOltdfQ.XQIfceINWR7bQS12drmv0z06xdb8tavomR8HfkuVPf540cCZQTbMNFzkwyoroSkg1-lRNj2YrcbWDO7FAKUoG9EUumv1v34c79yb6KsGWrQsD4ksVu94O1L4jw1a-LsPkM1gGkq8wqUa8miJ8j_eqWlrrs2X2AjhxvGVrvP0SJ6f8G8xtizGAOzYc--QkwA8cNwvDwGuFSAj6iSqYF08DLd_YIRxBLUR2xLUmvejy6EInoee7dbLenR4IdIWwuQSrAnpFO1gI54AMuqu07NQb6-CESUjHO_f8y6QgXSzsbaASi_cGfjaRS9zyCPOQw9Q92XgGMCrNMP7R-gdh0BCr_TwJPsIgDpyiisWBQFPoqxTjoxaFHAtHikZnCIUvGup8L5TtkMTKhSLNx5pf2uDE3Pefqk_3Fd6QolX5F-Qnh2NmVtbKAR3RyXpjzY0XgkjHOI9ZMrs23RWsvvXfFMpIwc2hDN4xZ9whxBy-d-JhiiBUOx1wu7lTxqAxi5ASZZ8qrSXkpxR2E_4PUrwSR4VDbJggY7Sr0fno5Mt-QT1C2bsIwLx-TjJZlfUvzW1MkbJ5gt90SfsW21iXHkdwRxmlSEr2CJDGp_87CtPGAspmneaibEey4C44ZFeARA_5Mkmw7qhpFNHwkHwV5ua4ouV7MRcHVZ20oAybSaOb-w0w44"}

endpoint = Baseurl+"v1/source/directory/country/all/ru"
data = {} #{"ip": "1.1.2.3"}

count=0
limit=10
while (count < limit):
    count = count + 1
    print(count)
    res=requests.get(endpoint, data=data, headers=headers).json()

print(res)
count=0

endpoint = Baseurl+"v1/currency/exchange/conversion?pair=BTCUSD&amount=12"
data = {"pair": "BTCUSD", "amount": "10878"}

while (count < limit):
    count = count + 1
    print(count)
    res=requests.get(endpoint, data=data, headers=headers).json()

print(res)