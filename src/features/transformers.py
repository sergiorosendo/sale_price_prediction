import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

def num_pipe():

    pipe = Pipeline([
        ('imputer', SimpleImputer(strategy='mean')),
        ('standard_scaler', StandardScaler())
    ])

    return pipe

def cat_pipe():

    pipe = Pipeline([
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('one_hot_encoder', OneHotEncoder(handle_unknown='ignore', sparse=False))
    ])

    return pipe

def preprocessor(num_feat, cat_feat, num_pipe=num_pipe(), cat_pipe=cat_pipe()):

    pp = ColumnTransformer([
        ('numeric_transformer', num_pipe, num_feat),
        ('categorical_transformer', cat_pipe, cat_feat)
    ])

    return pp

def preprocess(df, num_feat, cat_feat, target, num_pipe=num_pipe(), cat_pipe=cat_pipe()):
    
    pp = preprocessor(num_feat, cat_feat, num_pipe, cat_pipe)
    x = pp.fit_transform(df)
    
    cols = get_column_names_from_ColumnTransformer(pp, cat_feat)

    x = pd.DataFrame(x, columns=cols)
    y = df[[target]]
    
    return pd.concat([x, y], axis=1)


def get_column_names_from_ColumnTransformer(column_transformer, cat_feat_names):
    # source: https://github.com/scikit-learn/scikit-learn/issues/12525

    col_name = []
    for transformer_in_columns in column_transformer.transformers_[:-1]: # the last transformer is ColumnTransformer's 'remainder'
        raw_col_name = transformer_in_columns[2]
        if isinstance(transformer_in_columns[1], Pipeline):
            transformer = transformer_in_columns[1].steps[-1][1]
        else:
            transformer = transformer_in_columns[1]
        try:
            names = transformer.get_feature_names(cat_feat_names)
        except AttributeError: # if no 'get_feature_names' function, use raw column name
            names = raw_col_name
        if isinstance(names, np.ndarray): # eg.
            col_name += names.tolist()
        elif isinstance(names, list):
            col_name += names
        elif isinstance(names, str):
            col_name.append(names)
    return col_name

