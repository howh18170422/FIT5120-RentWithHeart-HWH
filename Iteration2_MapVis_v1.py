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
        html.H1(
            'Suburb Recommender'
            )
        ],style={'width': '100%', 
                 'display': 'flex', 
                 'align-items':'center', 
                 'justify-content':'center'}
    ),
    
    html.Div([
        html.P('Finding it hard to identify a suitable suburb for your needs? Looking for somewhere that suits your budget and also the various needs of your family?')
    ],
        style={'width': '100%',
                          'display': 'flex',
                          'align-items':'left',
                          'justify-content':'left',
                          'marginTop': '5px',
                          'marginBottom': '5px',
                          'marginLeft': '20px',
                          'fontSize': 16
                         }
    
    ),
        
        
    html.Div([
        html.P('Use our suburb recommender tool to identify the suburb that is the most suitable for your requirements.')
    ],
         style={'width': '100%',
                          'display': 'flex',
                          'align-items':'left',
                          'justify-content':'left',
                          'marginTop': '5px',
                          'marginBottom': '5px',
                          'marginLeft': '20px',
                          'fontSize': 16
                         }
    ),
    
    html.Div([
        
        html.Label(html.B("Select Preferred Housing Type"),
                   htmlFor="preferred_housing_dropdown",
                   style={'width': '100%',
                          'display': 'flex',
                          'align-items':'left',
                          'justify-content':'left',
                          'marginTop': '20px',
                          'marginBottom': '5px',
                          'marginLeft': '20px',
                          'fontSize': 16
                         }
                  )
    ]),
    
    html.Div([
        
        dcc.Dropdown(
        
        id='preferred_housing_dropdown',
        options=[
            {'label': '1 bedroom flats', 'value': '1 bedroom flats'},
            {'label': '2 bedroom flats', 'value': '2 bedroom flats'},
            {'label': '2 bedroom houses', 'value': '2 bedroom houses'},
            {'label': '3 bedroom flats', 'value': '3 bedroom flats'},
            {'label': '3 bedroom houses', 'value': '3 bedroom houses'},
            {'label': '4 bedroom houses', 'value': '4 bedroom houses'}
        ],
        value='1 bedroom flats',
        multi=False,
        clearable=False)
    
    ],
        style={'width': '40vw',
               'display': 'inline-block',
               'align-items':'left',
               'justify-content':'left',
               'marginTop': '5px',
               'marginBottom': '20px',
               'marginLeft': '20px',
               'fontSize': 16}
    ),
    
    html.Div([
        
        html.Label(html.B("Select Weekly Budget"),
                   htmlFor="preferred_budget_dropdown",
                   style={'width': '100%',
                          'display': 'flex',
                          'align-items':'left',
                          'justify-content':'left',
                          'marginTop': '20px',
                          'marginBottom': '5px',
                          'marginLeft': '20px',
                          'fontSize': 16
                         }
                  )
    ]),
    
    html.Div([
        
        dcc.Dropdown(
        
        id='preferred_budget_dropdown',
        options=[
            {'label': 'Less than $100', 'value': 'Less than $100'},
            {'label': '$100 - $200', 'value': '$100 - $200'},
            {'label': '$200 - $300', 'value': '$200 - $300'},
            {'label': '$300 - $400', 'value': '$300 - $400'},
            {'label': '$400 - $500', 'value': '$400 - $500'},
            {'label': '$500 - $600', 'value': '$500 - $600'},
            {'label': 'More than $600', 'value': 'More than $600'}
        ],
        value='Less than $100',
        multi=False,
        clearable=False)
    
    ],
        style={'width': '40vw',
               'display': 'inline-block',
               'align-items':'left',
               'justify-content':'left',
               'marginTop': '5px',
               'marginBottom': '20px',
               'marginLeft': '20px',
               'fontSize': 16}
    ),
    
    html.Div([
        
        html.Label(html.B("Select Age of Children"),
                   htmlFor="children_checklist",
                   style={'width': '100%',
                          'display': 'flex',
                          'align-items':'left',
                          'justify-content':'left',
                          'marginTop': '20px',
                          'marginBottom': '5px',
                          'marginLeft': '20px',
                          'fontSize': 16
                         }
                  )
    ]),
    
    html.Div([
        
        dcc.Checklist(
        
        id='children_checklist',
        options=[
            {'label': 'No Children', 'value': 'No Children'},
            {'label': '0 - 2 Years', 'value': '0 - 3 Years'},
            {'label': '3 - 4 Years', 'value': '3 - 4 Years'},
            {'label': '5 - 12 Years', 'value': '5 - 12 Years'},
            {'label': '13 - 17 Years', 'value': '13 - 17 Years'},
            {'label': '18 Years and Above', 'value': '18 Years and Above'}
        ],
            value=['0 - 2 Years'],
            inputStyle={"margin-right": "10px",
                        "margin-left": "10px"}
        )
    
    ],
        style={'width': '40vw',
               'display': 'inline-block',
               'align-items':'left',
               'justify-content':'left',
               'marginTop': '5px',
               'marginBottom': '20px',
               'marginLeft': '20px',
               'fontSize': 16}
    ),
    
    html.Div([
        
        html.Label(html.B("Select Housing Type to Display"),
                   htmlFor="housing_type_dropdown",
                   style={'width': '100%',
                          'display': 'flex',
                          'align-items':'left',
                          'justify-content':'left',
                          'marginTop': '20px',
                          'marginBottom': '5px',
                          'marginLeft': '20px',
                          'fontSize': 16
                         }
                  )
    ]),
    
    html.Div([
        
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
        style={'width': '40vw',
               'display': 'inline-block',
               'align-items':'left',
               'justify-content':'left',
               'marginTop': '5px',
               'marginBottom': '20px',
               'marginLeft': '20px',
               'fontSize': 16}
    ),
    
    html.Div([
        html.H2(
            'Recommended Suburb & Forecasted Change in Median Rental Prices (%)'
            )
        ],style={'width': '100%', 
                 'display': 'flex', 
                 'align-items':'center', 
                 'justify-content':'center'}
    ),
    
    html.Div([dcc.Graph(id="map",
             style={'width': '90vw', 
                    'height': '90vh'})
             ]) 

])

@app.callback(
    Output("map", "figure"),
    Input("housing_type_dropdown", "value"))

def update_choropleth(housing_type):
    df_forecast = pd.read_csv(forecast_path, index_col=0)
    localities_df = gpd.read_file(localities_path, encoding='utf-8')
    
    geo_df = localities_df.merge(df_forecast[df_forecast['Housing_Type'] == housing_type], on='Suburb').set_index('Suburb')
    
    fig = px.choropleth_mapbox(
        geo_df,
        geojson=geo_df.geometry,
        locations=geo_df.index,
        color="Difference",
        color_continuous_scale = px.colors.sequential.Bluered,
        color_continuous_midpoint = 0,
        center={"lat": -37.81493464931014, "lon": 144.95950225995674},
        mapbox_style="carto-positron",
        zoom=8.5
    )
    
    fig.update_layout(
#         coloraxis_colorbar_x=-0.15,
        coloraxis_colorbar=dict(
            title=""
        ),
        coloraxis_colorbar_orientation='h'
    )
    
    return fig

app.run_server(debug=True,use_reloader=False)