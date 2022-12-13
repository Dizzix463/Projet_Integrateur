### THIS PROGRAM TEND TO CLEAN DATA SET ###

import pandas as pd
import os

# Indicate the path to save clean csv
directory = "../data/input/"


# Drop non-usable columns of the dataset
def drop_non_usable(df):
    df.drop(df.filter(regex="Unname"), axis=1, inplace=True)
    df.drop(['Date/Time'], axis=1, inplace=True)
    df.drop(['Recipe.RecipeName'], axis=1, inplace=True)


# Drop nulls rows of the dataset
def null_rows(df):
    df = df.drop(df[df.isin([0, 0.0]).all(axis=1)].index, axis=0)
    return df


# Return list of unique and non unique columns for a dataframe
def unique_cols(df):
    a = df.to_numpy()
    return (a[0] == a).all(0)


def clean_dataset(df):
    df_copy = df.copy()
    df_columns = df_copy.columns.values.tolist()
    u_columns = unique_cols(df)
    for i in range(0, len(u_columns)):
        if u_columns[i]:
            del df[df_columns[i]]
    return df


def save_csv(df, name: str):
    df.to_csv(directory + name, index=False)


for file in os.listdir(directory):
    print("***** INITIALISATION DU DATAFRAME *****")
    df = pd.read_csv("../data/input/"+file, sep=";", skiprows=1)
    drop_non_usable(df)
    print("Nombre de colonne(s) du dataframe:", len(df.columns.values.tolist()))

    print("***** ETUDE DES LIGNES NULLES  *****")
    df = null_rows(df)

    print("***** ETUDE DES COLONNES UNIQUES  *****")
    u_columns = unique_cols(df)
    print("Nombre de colonne(s) non unique:", sum(1 for x in u_columns if x))

    print("***** NETTOYAGE DU DATASET *****")
    clean_df = clean_dataset(df)
    print("Nombre de colonne(s) du dataframe après nettoyage:", len(clean_df.columns.values.tolist()))

    print("***** ENREGISTREMENT DU DATASET NETTOYÉ *****")
    save_csv(clean_df, f'../output/clean_{file}.csv')
    print("***** FIN *****")
