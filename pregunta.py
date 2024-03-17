"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";",header=0,index_col=0)

    #
    # Inserte su código aquí
    #

    # Se remueven las filas sin datos
    df.dropna(axis=0,inplace=True)
    df.drop_duplicates(inplace=True)

    # Se pasan las columnas de texto a minúscula y se cambian los guiones por espacios
    for col in ["sexo", "tipo_de_emprendimiento", "idea_negocio", "barrio", "línea_credito"]:
        df[col] = df[col].str.lower()
        df[col] = df[col].str.replace('-',' ')
        df[col] = df[col].str.replace('_',' ')

    # Se convierte la columna de comuna a dato entero
    df["comuna_ciudadano"] = df["comuna_ciudadano"].astype(int)

    # Revisión y estandarización de las fechas
    # Estandarización de las fechas
    def correccion(fecha):
        componentes = fecha.split('/')
        if len(componentes[0]) == 4:
            nueva_fecha = '/'.join(reversed(componentes))
        else:
            nueva_fecha = fecha
        return nueva_fecha
    
    df["fecha_de_beneficio"] = df["fecha_de_beneficio"].apply(correccion)

    # Estandarización de los montos de crédito
    df["monto_del_credito"] = df["monto_del_credito"].str.strip('$')
    df["monto_del_credito"] = df["monto_del_credito"].str.replace(',','')
    df["monto_del_credito"] = df["monto_del_credito"].str.replace(' ','')
    df["monto_del_credito"] = df["monto_del_credito"].astype(float)
    df["monto_del_credito"] = df["monto_del_credito"].astype(int)

    # Eliminación de nulos y duplicados nuevamente
    df.dropna(axis=0,inplace=True)
    df.drop_duplicates(subset=["sexo","tipo_de_emprendimiento","idea_negocio",
                                    "barrio", "estrato", "comuna_ciudadano",
                                    "fecha_de_beneficio", "monto_del_credito",
                                    "línea_credito"],
                                    inplace=True)

    return df
