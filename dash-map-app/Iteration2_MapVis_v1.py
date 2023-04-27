from dash import Dash, dash_table, html, dcc, Input, Output
import pandas as pd
import geopandas as gpd
import plotly.express as px
import dash_bootstrap_components as dbc

forecast_path = 'https://raw.githubusercontent.com/howh18170422/FIT5120-RentWithHeart-HWH/main/dash-map-app/df_forecast_cleaned.csv'
localities_path= 'https://raw.githubusercontent.com/howh18170422/FIT5120-RentWithHeart-HWH/main/dash-map-app/vic_localities_cleaned.geojson'


app = Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])
server = app.server

app.layout = html.Div([

    html.Div([
        dcc.Markdown(
            '# Forecasted Change in Median Rental Prices (%)'
            )
        ]),
    
    html.Div([
        
        html.Label(html.B("Select Housing Type"),
                   htmlFor="housing_type_dropdown",
                   style={'marginTop': '20px',
                          'marginBottom': '20px',
                          'marginLeft': '10px',
                          'fontSize': 16
                         }
                  ),
        
        dcc.Dropdown(
        
        id='housing_type_dropdown',
        options=[
            {'label': '1 bedroom flats', 'value': '1 bedroom flats'},
            {'label': '2 bedroom flats', 'value': '2 bedroom flats'},
            {'label': '2 bedroom houses', 'value': '2 bedroom houses'},
            {'label': '3 bedroom flats', 'value': '3 bedroom flats'},
            {'label': '3 bedroom houses', 'value': '3 bedroom houses'},
            {'label': '4 bedroom houses', 'value': '4 bedroom houses'},
            {'label': 'All properties', 'value': 'All properties'}
        ],
        value='All properties',
        multi=False,
        clearable=False)
             ],
        style={'width': '49%', 
               'display': 'inline-block',
               'marginTop': '20px',
               'marginBottom': '20px'}
    ),
    
    html.Div([dcc.Graph(id="map",
             style={'width': '90vw', 'height': '90vh'})
             ]) 

])

@app.callback(
    Output("map", "figure"),
    Input("housing_type_dropdown", "value"))

def update_choropleth(housing_type):
    df_forecast = pd.read_csv(forecast_path, index_col=0)
    localities_df = gpd.read_file(localities_path, encoding='utf-8')
    
    geo_df = localities_df.merge(df_forecast[df_forecast['Housing_Type'] == housing_type], on='Suburb').set_index('Suburb')
    
    fig = px.choropleth_mapbox(geo_df,
                           geojson=geo_df.geometry,
                           locations=geo_df.index,
                           color="Difference",
                           center={"lat": -37.81493464931014, "lon": 144.95950225995674},
                           mapbox_style="carto-positron",
                           zoom=8.5)
    
    return fig

app.run_server(debug=True,use_reloader=False)