import pickle
import numpy as np
import pandas as pd
import sklearn.model_selection as ms
import random

def load_imdd(X_test):
    f = open(r'../data/imdd.sav', 'rb')
    loaded_model = pickle.load(f)
    return loaded_model.predict(X_test)


def load_se(X_test):
    f = open(r'../data/se.sav', 'rb')
    loaded_model = pickle.load(f)
    return loaded_model.predict(X_test)


def load_mi(X_test):
    f = open(r'../data/mi.sav', 'rb')
    loaded_model = pickle.load(f)
    return loaded_model.predict(X_test)


def predict(score_dict):
    # print(score_dict)
    data = pd.DataFrame(score_dict)
    result = {
        "iim": "%.2f" % (load_imdd(data)[0]/4*100),
        "mi": "%.2f" % (load_mi(data)[0]/4*100),
        "se": "%.2f" % (load_se(data)[0]/4*100),
    }
    return result
