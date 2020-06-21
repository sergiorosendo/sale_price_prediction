import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.pipeline import Pipeline
from matplotlib.pyplot import figure

def plot_price_dist(df):

    figure(figsize=(12, 4))
    ax = sns.distplot(df['price'])
    ax.set(title='Price Distribution', xlabel='Price', ylabel='Frequency')


def plot_correlation(df):

    figure(figsize=(12, 4))
    corr = df.corr()['price'].sort_values()
    ax = sns.scatterplot(x=corr.index.values.tolist(), y=corr.values)
    ax.set(title='Correlation: Feature x Price', xlabel='Feature',  ylabel='Correlation')
    ax = plt.xticks(rotation=90)


def plot_location(df):

    figure(figsize=(12, 7.2))
    plt.scatter(df['longitude'], df['latitude'], cmap='Reds', c=df['price'], s=10)
    plt.colorbar().set_label('Price')
    plt.clim(vmin=0, vmax=1500000)
    plt.title('Location x Price')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')


def plot_waterfront(df):

    ax = sns.boxplot(x='is_waterfront', y='price', data=df, showfliers=False)
    ax.set(title='Waterfront x House price', xlabel='Waterfront', ylabel='Price')
    ax = plt.xticks(rotation=90)


def plot_zip_codes(df):

    figure(figsize=(16, 6))
    ax = sns.boxplot(x='zip', y='price', data=df, showfliers=False)
    ax.set(title='Zip Code x House price', xlabel='zip', ylabel='Price')
    ax = plt.xticks(rotation=90)


def plot_size(df):

    figure(figsize=(8, 5))
    plt.scatter(df['size_house'], df['price'], s=10)
    plt.xlim(0, 6000)
    plt.title('House size x Price')
    plt.xlabel('Size')
    plt.ylabel('Price')


def plot_avg_size_neigh(df):

    figure(figsize=(8, 5))
    plt.scatter(df['avg_size_neighbor_houses'], df['price'], s=10)
    plt.title('Average size of neighbor houses x Price')
    plt.xlim(0, 6000)
    plt.xlabel('Average size')
    plt.ylabel('Price')


def plot_lot_size(df):

    figure(figsize=(8, 5))
    plt.scatter(df['avg_size_neighbor_houses'], df['price'], s=10)
    plt.title('Average size of neighbor houses x Price')
    plt.xlim(0, 6000)
    plt.xlabel('Average size')
    plt.ylabel('Price')


def plot_avg_lot_size_neigh(df):

    figure(figsize=(8, 5))
    plt.scatter(df['avg_size_neighbor_lot'], df['price'], s=10)
    plt.title('Average size of neighbor Lots x Price')
    plt.xlim(0, 6000)
    plt.xlabel('Average lot size')
    plt.ylabel('Price')


def plot_bathrooms(df):

    figure(figsize=(8, 4))
    ax = sns.boxplot(x='num_bath', y='price', data=df, showfliers=False)
    ax.set(title='Bathrooms x House price', xlabel='Number of bathrooms', ylabel='Price')
    ax = plt.xticks(rotation=90)


def plot_floors(df):

    figure(figsize=(8, 4))
    ax = sns.boxplot(x='num_floors', y='price', data=df, showfliers=False)
    ax.set(title='Bathrooms x House price', xlabel='Number of floors', ylabel='Price')
    ax = plt.xticks(rotation=90)


def plot_condition(df):

    figure(num=None, figsize=(8, 4), dpi=80, facecolor='w', edgecolor='k')
    ax = sns.boxplot(x='condition', y='price', data=df, showfliers=False)
    ax.set(title='Condition x House price', xlabel='Condition', ylabel='Price')
    ax = plt.xticks(rotation=90)


def plot_bedrooms(df):

    figure(num=None, figsize=(8, 4), dpi=80, facecolor='w', edgecolor='k')
    ax = sns.boxplot(x='num_bed', y='price', data=df, showfliers=False)
    ax.set(title='Bedrooms x House price', xlabel='Number of bedrooms', ylabel='Price')
    ax = plt.xticks(rotation=90)


def plot_basement_size(df):

    figure(figsize=(8, 5))
    ax = plt.scatter(df['size_basement'], df['price'], s=10)
    #plt.ylim(0, 600000)
    plt.title('Basement size x Price')
    plt.xlabel('Basement Size')
    plt.ylabel('Price')
    plt.show()


def plot_year_built(df):

    figure(figsize=(16, 6))
    ax = sns.boxplot(x='year_built', y='price', data=df, showfliers=False)
    ax.set(title='Year Built x Price', xlabel='Year Built', ylabel='Price')
    ax.get_xaxis().set_ticks([])
    ax = plt.xticks(rotation=90)


def plot_renovation_date(df):

    figure(figsize=(16, 6))
    ddf = df[df['renovation_date'] != 0]
    ax = sns.boxplot(x='renovation_date', y='price', data=ddf, showfliers=False)
    ax.set(title='Renovation Date x Price', xlabel='Renovation Year', ylabel='Price')
    ax = plt.xticks(rotation=90)


from ..features.transformers import get_column_names_from_ColumnTransformer

def lr_coeff(cols, clf):

    reg_coeff = pd.concat([
        pd.DataFrame(cols, columns=['Feature']), 
        pd.DataFrame(np.transpose(clf.coef_), columns=['Coefficient'])
        ], axis = 1)
    reg_coeff.set_index(keys='Feature', inplace=True)
    reg_coeff.sort_values(by='Coefficient', ascending=False, inplace=True)
    return reg_coeff
