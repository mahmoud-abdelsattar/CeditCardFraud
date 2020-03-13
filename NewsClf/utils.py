import os
import re
import pandas as pd

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "creditcard.csv")


def load_data():
    df = pd.read_csv(DATA_DIR)
    # Determine number of fraud cases in dataset
    fraud = df[df['Class'] == 1]
    valid = df[df['Class'] == 0]
    outlierFraction = len(fraud) / float(len(valid))
    print(outlierFraction)
    print('Fraud Cases: {}'.format(len(df[df['Class'] == 1])))
    print('Valid Transactions: {}'.format(len(df[df['Class'] == 0])))

    # dividing the X and the Y from the dataset
    X = df.drop(['Class'], axis=1)
    Y = df["Class"]
    print(X.shape)
    print(Y.shape)
    # getting just the values for the sake of processing
    # (its a numpy array with no columns)
    xData = X.values
    yData = Y.values

    return xData, yData


