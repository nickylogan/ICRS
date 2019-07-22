import os
import pickle
from math import sqrt

import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_squared_error as MSE
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.preprocessing import normalize
from sklearn.svm import SVR

root_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_dir = os.path.join(root_dir, 'data')

general_courses = [
    "INF0131",  # calculus1
    "INF0221",  # discrete_math
    "INF0381",  # intro_to_it
    "INF0011",  # prolog
    "INF0141",  # calculus2
    "INF0621",  # data_structure
    "INF0301",  # java
    "INF0531",  # mis
    "INF0601",  # stats
    "INF0031",  # algo_analysis
    "INF0271",  # computer_arch
    "INF0521",  # database
    "INF0021",  # linear_algebra
    "INF0291",  # oop
]

print("Loading data...")
data_imdd = pd.read_csv(os.path.join(data_dir, 'imdd.csv'))
data_mi = pd.read_csv(os.path.join(data_dir, 'mi.csv'))
data_se = pd.read_csv(os.path.join(data_dir, 'se.csv'))

options = [
    {
        'name': 'imdd',
        'data': data_imdd,
        'file': 'imdd.sav',
        'seed': 260,
    },
    {
        'name': 'se',
        'data': data_se,
        'file': 'se.sav',
        'seed': 820,
    },
    {
        'name': 'mi',
        'data': data_mi,
        'file': 'mi.sav',
        'seed': 903,
    },
]

# Train all prediction models

for opt in options:
    name: str = opt['name']
    data: pd.DataFrame = opt['data']
    save_path: str = opt['file']
    seed: int = opt.get('seed', 0)
    print("######", name.upper(), "######")

    # Set feature and target
    target: pd.DataFrame = data.GPA
    feature: pd.DataFrame = data.filter(items=general_courses)

    # Impute missing data
    print("Imputing missing data...", end="\r")
    imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
    imputer.fit(feature)
    feature_array = imputer.transform(feature)
    feature = pd.DataFrame(feature_array, columns=feature.columns)

    # Split data into train and test
    print("Splitting data into train and test...", end="\r")
    X_train, X_test, y_train, y_test = train_test_split(
        feature, target, test_size=0.3, random_state=seed)

    tuned_parameters = [{
        'kernel': ['rbf', 'poly', 'sigmoid', 'linear'],
        'gamma': [1, 0.1, 0.01, 1e-3, 1e-4, 'auto', 'scale'],
        'C': [1, 10, 100, 1000],
        'degree': [3, 4, 5],
    }]

    # Building predictor model
    print("Training model...                     ", end="\r")
    clf = GridSearchCV(SVR(), tuned_parameters,
                       cv=2, iid=True,
                       refit='r2',
                       scoring=['r2', 'neg_mean_squared_error'],
                       )
    clf.fit(X_train, y_train)

    # Dumping model
    print("Dumping model...   ", end="\r")
    pickle.dump(clf, open(save_path, 'wb'))

    # Test data
    print()
    y_true, y_pred = y_test, clf.predict(X_test)
    print("Best parameters   :", clf.best_params_)
    print("Score             :", clf.score(X_test, y_test))
    print("Mean squared error:", MSE(y_true, y_pred))
    print()
