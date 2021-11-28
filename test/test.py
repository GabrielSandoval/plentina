import requests

# Fraud
data = {
    "step": 699,
    "type": "TRANSFER",
    "amount": 162326.52,
    "nameOrig": "C1557504343",
    "oldbalanceOrig": 162326.52,
    "newbalanceOrig": 0.00,
    "nameDest": "C404511346",
    "oldbalanceDest": 0.0,
    "newbalanceDest": 0.0
}

# Not fraud
# data = {
#     "step":1,
#     "type":"PAYMENT",
#     "amount":9839.64,
#     "nameOrig":"C1231006815",
#     "oldbalanceOrig":170136.0,
#     "newbalanceOrig":160296.36,
#     "nameDest":"M1979787155",
#     "oldbalanceDest":0.0,
#     "newbalanceDest":0.0
# }

response = requests.post("http://ec2-44-198-192-99.compute-1.amazonaws.com/is-fraud", json=data)
print(response.json())
