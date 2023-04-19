import numpy as np
import pandas as pd


def load_and_process(path_to_csv_file):
    df_1 = pd.read_csv('../data/raw/data.csv').drop(
        ['id', 'Unnamed: 32'], axis=1).dropna().reset_index(drop=True)

    df_2 = df_1.rename(
        columns={
            "concave points_mean": "concave_points_mean",
            "concave points_se": "concave_points_se",
            "concave points_worst": "concave_points_worst"
        }).assign(diagnosis=lambda x: x['diagnosis'].map({
            'M': 1,
            'B': 0
        })).sort_values(by='area_mean').reset_index(drop=True)
    # sorting by size of tumour

    return df_2
