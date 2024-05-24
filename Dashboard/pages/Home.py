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
from components.maps.mapsample_home import mapsample_3
mapa_contratos = mapsample_3('Mapa de Contratos', 'id_mapa_contratos')

#Import dataframe graphs

df_edad_sexo = pd.read_csv("data/Edad_sexo.csv", delimiter =";", encoding ='utf-8')
df_TIPACCID_count = pd.read_csv("data/TIPACCID_count.csv", delimiter =",", encoding ='utf-8') 
diasemana_count = pd.read_csv("data/DIASEMANA_count.csv", delimiter =",", encoding ='utf-8') 
temp_df2 = pd.read_csv("data/GeneroEdad.csv")

fig_pie = px.pie(pd.read_csv("data/SEXO_count.csv"), values='y', names='x',
             labels={'y':'Porcentaje accidentes',
             'x':'Sexo'}
             #, title="Sexo del conductor"
             )

fig_pie.update_traces(hole=.3, textposition='inside', textinfo='percent')
fig_pie.update_layout(font=dict(
        size=10
      ))

fig_pie.layout.plot_bgcolor = 'rgba(0,0,0,0)'
fig_pie.layout.paper_bgcolor = 'rgba(0,0,0,0)'


#Funtion for the tipo de accidente 
def act_contract(data, tipo_contrato):
    fig_act_contract = px.bar(data, x="x", y="y", height=450,
            labels={
                "x":"Tipo de accidente",
                "y":"Número de fallecidos o heridos"
            }).update_xaxes(tickangle=290)
    fig_act_contract.update_layout(xaxis={"tickfont":{"size":8}})
    fig_act_contract.update_layout(yaxis={"tickfont":{"size":10}})
    fig_act_contract.layout.plot_bgcolor = 'rgba(0,0,0,0)'
    fig_act_contract.layout.paper_bgcolor = 'rgba(0,0,0,0)'

    return fig_act_contract

# Grafico de dia de la semana
fig_sem = px.bar(diasemana_count, x="x", y="y", 
             #color="z", 
             color = "z",
             title="Personas heridas y fallecidas por dia de la semana en accidente",
             labels={"x":"Dia semana", "y":"Conteo" }) 
fig_sem.layout.plot_bgcolor = 'rgba(0,0,0,0)'
fig_sem.layout.paper_bgcolor = 'rgba(0,0,0,0)'


# Convertir la columna 'fecha' a tipo datetime si aún no lo está



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




#Grafico sexo
fig_gen2 = go.Figure()
fig_gen2.add_trace(go.Bar(x=-temp_df2["Mujer"].values,
                    y=temp_df2["RangoEdad"],
                    orientation='h',
                    name="Mujer",
                    customdata=temp_df2['Mujer'],
                    hovertemplate="Edad: %{y}<br>Accidentes:%{customdata}<br>Sexo:Mujer<extra></extra>",
                    marker_color="#F2B950"))
fig_gen2.add_trace(go.Bar(x=temp_df2["Hombre"].values,
                    y=temp_df2['RangoEdad'],
                    orientation='h',
                    name='Hombre',
                    hovertemplate="Edad: %{y}<br>Accidentes:%{x}<br>Sexo:Hombre<extra></extra>",
                    marker_color="#011C40"))

fig_gen2.update_layout(barmode='relative', 
                 height=500, 
                 width=400, 
                 yaxis_autorange='reversed',
                 bargap=0.01,
                 legend_orientation='h',
                 legend_x=0.07, legend_y=1.1)
                     #,"z":"Tipo de Accidente"})
fig_gen2.layout.plot_bgcolor = 'rgba(0,0,0,0)'
fig_gen2.layout.paper_bgcolor = 'rgba(0,0,0,0)'                     
                     
fig_sem.update_layout(font=dict(size = 11), height = 500)
fig_sem.update_traces(marker_color=1)
#Buttoms
Tipo_acc = [
    {"label":'Heridos', "value":"ACT"},
    {"label":'Fallecidos', "value":"OBSE"}
]


# specific layout for this page
layout = dbc.Container(
    [
        dbc.Row([
            dbc.Col([
                 html.H2(["Frubana infromación de precios"],className="title"),
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

@callback(
    Output("Accidentes", "figure"),
    Input("accidentes", "value")
)
def filter_contrato(select_contrato):
    if not select_contrato:
        filtered_data = df_TIPACCID_count
    elif select_contrato == 'ACT':
        filtered_data = df_TIPACCID_count[df_TIPACCID_count['z'] == 'No fatal']
    else:
        filtered_data = df_TIPACCID_count[df_TIPACCID_count['z'] == 'Fatal']

    fig_act_contract = act_contract(filtered_data, ['ACT', 'OBSE'])
    return fig_act_contract