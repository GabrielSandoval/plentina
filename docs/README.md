### Directory structure:

```
└── artifacts
│   └── artifacts.pkl                      <- ML artifacts (encoder, model, scaler)
│
├── data                                   <- Put switrs.sqlite and transactions_train.csv here
│
├── docs
|   └─── README.md                         <- Contains top-level information of this project
│
├── lib
|   ├── transaction.py                     <- Basic Model for transaction reqquest
│   └── utils.py                           <- Utility functions
│
├── notebooks                              <- Jupyter notebooks
│   ├── Exploratory Data Analysis.ipynb    <- EDA for transactions_train.csv dataset
│   ├── Screening Test.ipynb               <- EDA to answer SWITRS questions
│   └── Train.ipynb                        <- Train model for Fraud detection
│
├── test
│   └── Train.ipynb                        <- Test fraud detection API
│
├── api.py                                 <- FastApi application
|
├── dockerfile                             <- Build docker image
│
└── requirements.txt                       <- Dependencies
```


### Install dependencies

```
pip install -r requirements.txt
```

### Model
```
Features:   [type amount oldbalanceOrig newbalanceOrig oldbalanceDest newbalanceDest]

Train Size: 80%
Test Size:  20%

Accuracy:   0.9996
F1-Score:   0.8202
```

### Run API locally

```
uvicorn app:app --host 0.0.0.0 --port 8080
```

### Deployed API endpoint:

```
POST http://ec2-3-82-148-48.compute-1.amazonaws.com/is-fraud
Params:
    "step": 699,
    "type": "TRANSFER",
    "amount": 162326.52,
    "nameOrig": "C1557504343",
    "oldbalanceOrig": 162326.52,
    "newbalanceOrig": 0.00,
    "nameDest": "C404511346",
    "oldbalanceDest": 0.0,
    "newbalanceDest": 0.0
```
