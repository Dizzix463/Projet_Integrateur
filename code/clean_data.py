### THIS PROGRAM TEND TO CLEAN DATA SET ###

import pandas as pd

# Indicate the path to save clean csv
path = "data/clean/"

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

def save_csv(df,name : str):
    df.to_csv(path+name, index=False)

df = pd.read_csv("data/A1417-20221205T084035Z-001/A1417/2021-09-24_04-00-50_Bx-P1-C0-Growth-A1417 SL calib.csv",
                 sep=";", skiprows=1)

print("***** INITIALISATION DU DATAFRAME *****")
print("Nombre de colonne(s) du dataframe:", len(df.columns.values.tolist()))

print("***** ETUDE DES COLONNES UNIQUES  *****")
u_columns = unique_cols(df)
print("Nombre de colonne(s) non unique:", sum(1 for x in u_columns if x))

print("***** NETTOYAGE DU DATASET *****")
clean_df = clean_dataset(df)
print("Nombre de colonne(s) du dataframe après nettoyage:", len(clean_df.columns.values.tolist()))

print("***** ENREGISTREMENT DU DATASET NETTOYÉ *****")
save_csv(clean_df,'test.csv')
print("***** FIN *****")
