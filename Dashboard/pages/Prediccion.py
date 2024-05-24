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

#Definition of map the contract



#Import dataframe graphs

df_edad_sexo = pd.read_csv("data/Edad_sexo.csv", delimiter =";", encoding ='utf-8')
df_TIPACCID_count = pd.read_csv("data/TIPACCID_count.csv", delimiter =",", encoding ='utf-8') 
diasemana_count = pd.read_csv("data/DIASEMANA_count.csv", delimiter =",", encoding ='utf-8') 
temp_df2 = pd.read_csv("data/GeneroEdad.csv")


df_pct = pd.read_csv("data/df_pct.csv")
# Datos de ejemplo
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