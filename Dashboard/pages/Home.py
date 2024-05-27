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
register_page(__name__, path='/')

#Definition of map the contract

df =  pd.read_csv("data/base_consolidada.csv")
df['fecha'] = pd.to_datetime(df['fecha'])

# Calcular la cantidad total vendida para cada producto
ventas_por_producto = df.groupby('producto')['cantidad'].sum().reset_index()

# Seleccionar los 5 productos más vendidos
top_5_productos = ventas_por_producto.nlargest(5, 'cantidad')

# Filtrar el DataFrame original para obtener solo las ventas de los productos más vendidos
ventas_top_5 = df[df['producto'].isin(top_5_productos['producto'])]

# Calcular el precio promedio por producto a lo largo del tiempo
precio_promedio_por_producto = ventas_top_5.groupby(['producto', 'fecha'])['precio'].mean().reset_index()

# Crear el gráfico de líneas por producto
fig_pro_fru = go.Figure()

fig_pro_fru.layout.plot_bgcolor = 'rgba(0,0,0,0)'
fig_pro_fru.layout.paper_bgcolor = 'rgba(0,0,0,0)'

# Iterar sobre cada producto y agregar una línea al gráfico
for producto in top_5_productos['producto']:
    datos_producto = precio_promedio_por_producto[precio_promedio_por_producto['producto'] == producto]
    fig_pro_fru.add_trace(go.Scatter(x=datos_producto['fecha'], y=datos_producto['precio'],
                             mode='lines',
                             name=producto))

# Personalizar el diseño del gráfico
fig_pro_fru.update_layout(title='Precio Promedio por Producto a lo largo del tiempo',
                  xaxis_title='Fecha',
                  yaxis_title='Precio Promedio')


df['fecha'] = pd.to_datetime(df['fecha'])

# Filtrar el DataFrame original para obtener solo las ventas de los productos especificados
productos_especificos = ['Ajo Estandar Caja', 'Cebolla Cabezona Blanca Sin Pelar Mixta Desde 1Kg',
                        'Ñame Estándar Kg', 'Plátano Verde Estándar Mediano Estandar Verde',
                        'Tomate Chonto Maduración Mixta Estándar (Grande) Kg (Tamaño 🏠)']
ventas_productos_especificos = df[df['producto'].isin(productos_especificos)]

# Calcular la cantidad promedio vendida por producto a lo largo del tiempo
cantidad_promedio_por_producto = ventas_productos_especificos.groupby(['producto', 'fecha'])['cantidad'].mean().reset_index()

# Crear el gráfico de líneas por producto
fig_cant = go.Figure()

# Iterar sobre cada producto y agregar una línea al gráfico
for producto in productos_especificos:
    datos_producto = cantidad_promedio_por_producto[cantidad_promedio_por_producto['producto'] == producto]
    fig_cant.add_trace(go.Scatter(x=datos_producto['fecha'], y=datos_producto['cantidad'],
                             mode='lines',
                             name=producto))

# Personalizar el diseño del gráfico
fig_cant.update_layout(title='Cantidad Promedio Vendida por Producto a lo largo del tiempo',
                  xaxis_title='Fecha',
                  yaxis_title='Cantidad Promedio Vendida')



fig_cant.layout.plot_bgcolor = 'rgba(0,0,0,0)'
fig_cant.layout.paper_bgcolor = 'rgba(0,0,0,0)'

# Mostrar el gráfico

ventas_productos_especificos = df[df['producto'].isin(productos_especificos)]

# Calcular el precio promedio por producto a lo largo del tiempo
precio_promedio_por_producto = ventas_productos_especificos.groupby(['producto', 'fecha'])['precio'].mean().reset_index()

# Crear el gráfico de líneas por producto
fig_price2 = go.Figure()

# Iterar sobre cada producto y agregar una línea al gráfico
for producto in productos_especificos:
    datos_producto = precio_promedio_por_producto[precio_promedio_por_producto['producto'] == producto]
    fig_price2.add_trace(go.Scatter(x=datos_producto['fecha'], y=datos_producto['precio'],
                             mode='lines',
                             name=producto))

# Personalizar el diseño del gráfico
fig_price2.update_layout(title='Precio Promedio por Producto a lo largo del tiempo',
                  xaxis_title='Fecha',
                  yaxis_title='Precio Promedio')

fig_price2.layout.plot_bgcolor = 'rgba(0,0,0,0)'
fig_price2.layout.paper_bgcolor = 'rgba(0,0,0,0)'

# specific layout for this page
layout = dbc.Container(
    [
        dbc.Row([
            dbc.Col([
                 html.H2(["Frubana información de precios"],className="title"),
            ], md=12)           
        ]),
        dbc.Row([
            dbc.Col([
                 html.H6(["En este Tablero podrar observar el comportamiento de nuestros Productos, adicional explorar el comportamiento dinámico de los precios en el mercado de productos agrícolas en Colombia, con el fin de determinar el precio óptimo para los productos con la recomendación del modelo"],className="parrafo"),
            ], md=12)           
        ]),
        dbc.Row([
            dbc.Col([
                html.I(['  Precio Promedio por Producto'],className="fas fa-location-crosshairs me-2"),
                html.Br(),
                html.H6(className="subtitle"),
                html.Div([
                    dcc.Graph(figure=fig_price2)])          
            ], md=12, className="border_columna"),
        ]),        
        dbc.Row([
            dbc.Col([
                html.I([" Distribucion semana"],className="fas fa-file-lines me-2"),
                dcc.Graph(id="Semana", figure=fig_cant) 
                ], md=12, className="border_columna")
        ])
        ]
)
