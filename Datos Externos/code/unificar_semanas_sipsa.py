## Unificación de información del SIPSA 
### Obtener la lista de archivos Excel en la carpeta "datos"

import pandas as pd
import pickle
import glob

def sipsa():
    archivos_excel = glob.glob('../input/SIPSA Semanal/*.xlsx')  # La ruta puede variar según la ubicación de la carpeta

    # Lista para almacenar los DataFrames de cada archivo
    dfs = []

    # Iterar sobre cada archivo Excel
    for archivo in archivos_excel:
        nombre_archivo = archivo.split('../input/SIPSA Semanal\\anex-SIPSA')[-1]
        # Leer el archivo Excel y seleccionar la hoja "hoja2", comenzando desde la fila 12
        df_temp = pd.read_excel(archivo, sheet_name='1.1', skiprows=11)  # Comienza desde la fila 12 (índice 11)

        # Renombrar las primeras seis columnas basándose en su contenido
        df_temp = df_temp.rename(columns={
            df_temp.columns[0]: 'Producto',
            df_temp.columns[1]: 'Mercado mayorista',
            df_temp.columns[2]: 'Precio mínimo',
            df_temp.columns[3]: 'Precio máximo',
            df_temp.columns[4]: 'Precio medio',
            df_temp.columns[5]: 'Tendencia'
        })

        # Agregar una columna con el nombre del archivo
        df_temp['Archivo'] = nombre_archivo
        # Agregar el DataFrame a la lista
        dfs.append(df_temp)

    # Concatenar todos los DataFrames en uno solo
    df_final = pd.concat(dfs, ignore_index=True)

    # Mostrar el DataFrame final
    df_final.head(2)

    fechas_periodo = pd.read_excel("../input/fechas.xlsx")
    fechas_periodo.head(2)
    print('finalizado concatenado de la base 1')
    print('Guadando información')
    df_merged = pd.merge(df_final, fechas_periodo, on='Archivo', how='inner')  # 'how' puede ser 'inner', 'outer', 'left' o 'right'
    df_merged.to_excel('../interim/data1.xlsx')
    print('finalizado 1 de 3')

    ######----------------- Inicio segundo archivo

    # Obtener la lista de archivos Excel en la carpeta "datos"
    archivos_excel = glob.glob('../input/SIPSA Semanal/*.xlsx')  # La ruta puede variar según la ubicación de la carpeta

    # Lista para almacenar los DataFrames de cada archivo
    dfs = []

    # Iterar sobre cada archivo Excel
    for archivo in archivos_excel:
        nombre_archivo = archivo.split('../input/SIPSA Semanal\\anex-SIPSA')[-1]
        # Leer el archivo Excel y seleccionar la hoja "hoja2", comenzando desde la fila 12
        df_temp = pd.read_excel(archivo, sheet_name='1.2', skiprows=11)  # Comienza desde la fila 12 (índice 11)

        # Renombrar las primeras seis columnas basándose en su contenido
        df_temp = df_temp.rename(columns={
            df_temp.columns[0]: 'Producto',
            df_temp.columns[1]: 'Mercado mayorista',
            df_temp.columns[2]: 'Precio mínimo',
            df_temp.columns[3]: 'Precio máximo',
            df_temp.columns[4]: 'Precio medio',
            df_temp.columns[5]: 'Tendencia'
        })

        # Agregar una columna con el nombre del archivo
        df_temp['Archivo'] = nombre_archivo
        # Agregar el DataFrame a la lista
        dfs.append(df_temp)

    # Concatenar todos los DataFrames en uno solo
    df_final = pd.concat(dfs, ignore_index=True)

    # Mostrar el DataFrame final
    df_final.head(2)

    fechas_periodo = pd.read_excel("../input/fechas.xlsx")
    fechas_periodo.head(2)
    print('finalizado concatenado de la base 2')
    print('Guadando información')
    df_merged = pd.merge(df_final, fechas_periodo, on='Archivo', how='inner')  # 'how' puede ser 'inner', 'outer', 'left' o 'right'
    df_merged.to_excel('../interim/data2.xlsx')
    print('finalizado 2 de 3')


    ######----------------- Inicio tercer archivo

    # Obtener la lista de archivos Excel en la carpeta "datos"
    archivos_excel = glob.glob('../input/SIPSA Semanal/*.xlsx')  # La ruta puede variar según la ubicación de la carpeta

    # Lista para almacenar los DataFrames de cada archivo
    dfs = []

    # Iterar sobre cada archivo Excel
    for archivo in archivos_excel:
        nombre_archivo = archivo.split('../input/SIPSA Semanal\\anex-SIPSA')[-1]
        # Leer el archivo Excel y seleccionar la hoja "hoja2", comenzando desde la fila 12
        df_temp = pd.read_excel(archivo, sheet_name='1.3', skiprows=11)  # Comienza desde la fila 12 (índice 11)

        # Renombrar las primeras seis columnas basándose en su contenido
        df_temp = df_temp.rename(columns={
            df_temp.columns[0]: 'Producto',
            df_temp.columns[1]: 'Mercado mayorista',
            df_temp.columns[2]: 'Precio mínimo',
            df_temp.columns[3]: 'Precio máximo',
            df_temp.columns[4]: 'Precio medio',
            df_temp.columns[5]: 'Tendencia'
        })

        # Agregar una columna con el nombre del archivo
        df_temp['Archivo'] = nombre_archivo
        # Agregar el DataFrame a la lista
        dfs.append(df_temp)

    # Concatenar todos los DataFrames en uno solo
    df_final = pd.concat(dfs, ignore_index=True)

    # Mostrar el DataFrame final
    df_final.head(2)

    fechas_periodo = pd.read_excel("../input/fechas.xlsx")
    fechas_periodo.head(2)
    print('finalizado concatenado de la base 3')
    print('Guadando información')
    df_merged = pd.merge(df_final, fechas_periodo, on='Archivo', how='inner')  # 'how' puede ser 'inner', 'outer', 'left' o 'right'
    df_merged.to_excel('../interim/data3.xlsx')
    print('finalizado 3 de 3') 