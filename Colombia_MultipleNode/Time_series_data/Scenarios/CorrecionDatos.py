import pandas as pd


df = pd.read_csv('Wind2030.csv')  # Reemplaza 'nombre_archivo.csv' con tu propio archivo

# Reemplazar los valores nulos en las columnas 2 en adelante con 0 y los mayores a 1 con 1
for col in df.columns[1:]:  # Iterar sobre todas las columnas desde la segunda en adelante
    df[col] = df[col].fillna(0)  # Reemplazar los valores nulos con 0
    df[col] = df[col].apply(lambda x: 1 if x > 1 else x)  # Reemplazar los valores mayores a 1 con 1


print(df)
df.to_csv('Wind2030.csv')
