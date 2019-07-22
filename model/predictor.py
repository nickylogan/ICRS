import os
import pickle
import random

import numpy as np
import pandas as pd
import sklearn.model_selection as ms


class Predictor:
    '''Predictor serves as a class for generating predictions'''

    def __init__(self):
        curr_dir = os.path.dirname(os.path.realpath(__file__))
        self.imdd_model = pickle.load(
            open(os.path.join(curr_dir, 'imdd-cv.sav'), 'rb'))
        self.se_model = pickle.load(
            open(os.path.join(curr_dir, 'se-cv.sav'), 'rb'))
        self.mi_model = pickle.load(
            open(os.path.join(curr_dir, 'mi-cv.sav'), 'rb'))

    def predict_imdd(self, data: pd.DataFrame):
        return self.imdd_model.predict(data)

    def predict_se(self, data: pd.DataFrame):
        return self.se_model.predict(data)

    def predict_mi(self, data: pd.DataFrame):
        return self.mi_model.predict(data)

    def predict(self, **kwargs):
        data = {
            "INF0131": [kwargs['calculus1']],
            "INF0221": [kwargs['discrete_math']],
            "INF0381": [kwargs['intro_to_it']],
            "INF0011": [kwargs['prolog']],
            "INF0141": [kwargs['calculus2']],
            "INF0621": [kwargs['data_structure']],
            "INF0301": [kwargs['java']],
            "INF0531": [kwargs['mis']],
            "INF0601": [kwargs['stats']],
            "INF0031": [kwargs['algo_analysis']],
            "INF0271": [kwargs['computer_arch']],
            "INF0521": [kwargs['database']],
            "INF0021": [kwargs['linear_algebra']],
            "INF0291": [kwargs['oop']],
        }
        data = pd.DataFrame(data)
        result = {
            "imdd": min(max(0, self.predict_imdd(data))[0], 4) / 4 * 100,
            "mi"  : min(max(0, self.predict_mi(data))[0], 4) / 4 * 100,
            "se"  : min(max(0, self.predict_se(data))[0], 4) / 4 * 100,
        }
        return result

    def predict_batch(self, data: pd.DataFrame) -> pd.DataFrame:
        data.rename(columns={
            'calculus1': "INF0131",
            'discrete_math': "INF0221",
            'intro_to_it': "INF0381",
            'prolog': "INF0011",
            'calculus2': "INF0141",
            'data_structure': "INF0621",
            'java': "INF0301",
            'mis': "INF0531",
            'stats': "INF0601",
            'algo_analysis': "INF0031",
            'computer_arch': "INF0271",
            'database': "INF0521",
            'linear_algebra': "INF0021",
            'oop': "INF0291",
        })
        result = data.copy()
        result["No"] = range(1, len(data) + 1)
        result["IMDD"] = [min(max(0, x), 4) / 4 * 100 for x in self.predict_imdd(data)]
        result["SE"] = [min(max(0, x), 4) / 4 * 100 for x in self.predict_mi(data)]
        result["MI"] = [min(max(0, x), 4) / 4 * 100 for x in self.predict_se(data)]
        result.set_index('No')
        result["Recommended"] = result[["IMDD", "SE", "MI"]].idxmax(axis=1)
        result = result[["No", "IMDD", "SE", "MI", "Recommended"]]
        return result