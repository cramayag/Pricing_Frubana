# Libraries for the data
import pandas as pd
import dash
from dash import html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page
from datetime import datetime as dt

# Read the CSV file into a DataFrame
df = pd.read_csv('data/resultados.csv', 
                 #encoding='ISO-8859-1',
                 sep=",")

# dash-labs plugin call, menu name and route
register_page(__name__, path='/Recomendacion')

# Define the layout with just the table
layout = dbc.Container( [ 
    html.Div([
    dbc.Row([
        html.H6("En esta página podrás realizar ver la recomendación de los precios para los prodcutos en la plaza de Barranquilla"),
        html.Label('Recomendaciones:'),
    ]),
    html.Div(
        dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True),
        style={'overflowX': 'scroll'}  # Permite desplazar horizontalmente si es necesario
    )
])
])
