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
|   ├── constants.py.example               <- Template for constants file storing values
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
├── app.py                                 <- FastApi application
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
#### Cross-validation
<img src="https://raw.githubusercontent.com/GabrielSandoval/plentina/master/docs/KFoldCV.png" width=400>

#### CV F1Score and Accuracy
<img src="https://raw.githubusercontent.com/GabrielSandoval/plentina/master/docs/Metrics.png" width=400>

#### AUC
<img src="https://raw.githubusercontent.com/GabrielSandoval/plentina/master/docs/AUC.png" width=400>

#### Test F1Score and Accuracy

```
F1Score: 0.8028
Accuracy: 0.9995
```

### Run API locally

```
uvicorn app:app --host 0.0.0.0 --port 8080
```

### Deployed API endpoint:

```
POST http://ec2-44-198-192-99.compute-1.amazonaws.com/is-fraud
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
