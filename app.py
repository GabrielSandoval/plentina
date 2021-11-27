from lib.utils import *
from lib.transaction import Transaction

import pandas as pd
from fastapi import FastAPI

app = FastAPI()
transactions = pd.read_csv("data/transactions_train.csv")
type_encoder, model, scaler = load_artifacts("artifacts/artifacts.pkl")

@app.get("/")
async def root():
    return {"message": "Hello World! :)"}

@app.post("/is-fraud")
async def is_fraud(transaction: Transaction):
    global transactions
    transactions = transactions.append(dict(transaction), ignore_index=True)

    prev_transactions = lookup(transactions, transaction)
    if len(prev_transactions) >= 5: return { "isFraud": True }

    transaction = transform(transaction, type_encoder)
    features = to_dataframe(transaction)
    features = normalize(features, scaler)
    prediction = model.predict(features)[0]

    return { "isFraud": bool(prediction) }
