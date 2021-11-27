from pydantic import BaseModel

class Transaction(BaseModel):
    step: int
    type: str
    amount: float
    nameOrig: str
    oldbalanceOrig: float
    newbalanceOrig: float
    nameDest: str
    oldbalanceDest: float
    newbalanceDest: float
