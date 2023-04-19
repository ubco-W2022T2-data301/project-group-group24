import pandas as pd
import numpy as np

def load_and_process(filename):
    df1 = (
        pd.read_csv(filename)
        .drop(['id', 'Unnamed: 32'], axis=1)
        .dropna()
        .reset_index(drop = True)
        .rename(columns={'diagnosis': 'Diagnosis', 'radius_mean': 'Mean Radius', 'texture_mean': 'Mean Texture', 'perimeter_mean': 'Mean Perimeter', 
                        'area_mean': 'Mean Area', 'smoothness_mean': 'Mean Smoothness', 'compactness_mean': 'Mean Compactness',
                        'concavity_mean': 'Mean Concavity', 'concave points_mean': 'Mean Concave Points', 'symmetry_mean': 'Mean Symmetry', 
                        'fractal_dimension_mean': 'Mean Fractal Dimension',
                        'radius_se': 'Radius standard error', 'texture_se': 'Texture standard error', 'perimeter_se': 'Perimeter standard error', 
                        'area_se': 'Area standard error', 'smoothness_se': 'Smoothness standard error', 
                        'compactness_se': 'Compactness standard error', 'concavity_se': 'Concavity standard error', 
                        'concave points_se': 'Concave points standard error', 'symmetry_se': 'Symmetry standard error', 
                        'fractal_dimension_se': 'Fractal Dimension standard error', 'radius_worst': 'Worst Radius', 
                        'texture_worst': 'Worst Texture', 'perimeter_worst': 'Worst Perimeter', 'area_worst': 'Worst Area', 
                        'smoothness_worst': 'Worst Smoothness', 'compactness_worst': 'Worst Compactness',
                        'concavity_worst': 'Worst Concavity', 'concave points_worst': 'Worst Concave Points', 
                        'symmetry_worst': 'Worst Symmetry', 'fractal_dimension_worst': 'Worst Fractal Dimension'})
         .sort_values(by = 'Diagnosis', ascending = False)
         #['Diagnosis'].replace({'M':'Malignant','B':'Benign'}, inplace=True)
       # .apply(lambda x: x.map({'M': 'Malignant', 'B': 'Benign'})
    )
    )
    df2={
        df1.assign(Diagnosis = lambda x: x['Diagnosis'].replace(['M', 'B'], ['Malignant', 'Benign']))
    }
    return df2