import numpy as np
import pandas as pd
import pickle

def load_artifacts(artifact_path):
    with open(artifact_path, 'rb') as handle:
        artifacts = pickle.load(handle)
        return (
            artifacts["type_encoder"],
            artifacts["model"],
            artifacts["scaler"],
        )

def transform(transaction, type_encoder):
    transaction.type = transaction.type if transaction.type in type_encoder.classes_ else "<unknown>"
    transaction.type = np.where(type_encoder.classes_ == transaction.type)[0]

    return transaction

def normalize(features, scaler):
    features = scaler.transform(features)
    return features

def to_dataframe(transaction):
    x = pd.DataFrame.from_dict(dict(transaction), orient="index").T
    return x.drop(['step', "nameOrig", "nameDest"], axis=1)
