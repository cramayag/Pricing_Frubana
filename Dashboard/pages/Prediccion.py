#Libraries for the data
from operator import contains
from pydoc import classname
from matplotlib.axis import Tick
from matplotlib.pyplot import xlabel
import pandas as pd
import plotly.express as px
import numpy as np
import plotly.graph_objects as gp

#libraries
import dash
from dash import Dash, html , dcc, callback, Output, Input
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page
from xarray import align
import plotly.graph_objects as go

# dash-labs plugin call, menu name and route
register_page(__name__, path='/Prediccion')

#Import dataframe graphs

df_pct = pd.read_csv("data/df_pct.csv")

fechas = df_pct['fecha']
pct_dif = df_pct['pct_Dif']
fig_pct = go.Figure()
fig_pct.add_trace(go.Scatter(x=fechas, y=pct_dif, mode='markers+lines'))
# Personalizar el diseño del gráfico
fig_pct.update_layout(
    title='Diferencia Procentual Precio Frubana Vs Mercado',
    xaxis_title='Fecha',
    yaxis_title='Pct_Dif',
    xaxis_tickangle=-45,  # Rotar las fechas en el eje X,
    plot_bgcolor='rgba(0,0,0,0)'
)
fig_pct.layout.plot_bgcolor = 'rgba(0,0,0,0)'
fig_pct.layout.paper_bgcolor = 'rgba(0,0,0,0)'


base_s = pd.read_csv("data/base_total.csv")
base_s = base_s.dropna()
promedio_por_producto = base_s.groupby('producto')['pct_Dif'].mean().reset_index()

# Obtenemos los 10 productos con los mayores promedios de pct_Dif
top_10_productos = promedio_por_producto.nlargest(10, 'pct_Dif')

# Creamos el gráfico de barras
fig_top = go.Figure()

# Añadimos cada producto como una barra en el gráfico
for _, producto in top_10_productos.iterrows():
    fig_top.add_trace(go.Bar(x=[producto['producto']], y=[producto['pct_Dif']],
                         name=producto['producto'], showlegend=False))
# Personalizamos el diseño del gráfico
fig_top.update_layout(title='Top 10 Productos con Mayor Promedio de Diferencia',
                  xaxis_title='Producto',
                  yaxis_title='Promedio de Pct_Dif')

fig_top.layout.plot_bgcolor = 'rgba(0,0,0,0)'
fig_top.layout.paper_bgcolor = 'rgba(0,0,0,0)'

# specific layout for this page
layout = dbc.Container(
    [
        dbc.Row([
            dbc.Col([
                 html.H2(["Relación con el Mercado"],className="title"),
            ], md=12)           
        ]),
        dbc.Row([
            dbc.Col([
                 html.H6(["Comportamiento y comparación respecto a los datos del SIPSA ( Sistema de Información de Precios y Abastecimiento del Sector Agropecuario - DANE) "],className="parrafo"),
            ], md=12)           
        ]),
        dbc.Row([
            dbc.Col([
                html.I(['Diferencia Con preciso del mercado'],className="fas fa-location-crosshairs me-2"),
                html.Br(),
                html.H6(className="subtitle"),
                html.Div([
                    dcc.Graph(figure=fig_pct)])          
            ], md=12, className="border_columna")
        ]),        
        dbc.Row([
            dbc.Col([
                html.I([" Los 10 productos con mayor % de precio de venta vs el mercado"],className="fas fa-file-lines me-2"),
                dcc.Graph(id="Semana", figure=fig_top) 
                ], md=12, className="border_columna")
        ])
        ]
)