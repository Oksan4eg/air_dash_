from dash import Input, Output, html
from utils.data_loader import load_data
import plotly.graph_objects as go


def register_callbacks(app):
    @app.callback(
        Output('weather-output', 'children'),
        Output('co-graph', 'figure'),
        Output('no2-graph', 'figure'),
        Output('o3-graph', 'figure'),
        Output('so2-graph', 'figure'),
        Output('pm2_5-graph', 'figure'),
        Output('pm10-graph', 'figure'),
        Input('city-input', 'value')
    )
    def update_dashboard(city):
        data = load_data(city)
    
        weather_info = html.Div([
            html.H4(f"{data['city_name']}", className="card-title"),
            html.Img(src=f"https:{data['icon']}", style={"height": "64px"}),
            html.H5(f"{data['temp']}°C", className="card-subtitle mb-2 text-muted"),
            html.P(data['condition'], className="card-text")
        ])
        
        hours = data['hours']

        co_fig = go.Figure(
           data=[go.Scatter(x=data['hours'], y=data['co'], mode='lines+markers', name='Угарный газ')],
           layout=go.Layout(title='Угарный газ по часам', xaxis_title='Время', yaxis_title='СО (ppb)', template='plotly_dark') 
        )

        no2_fig = go.Figure(
           data=[go.Scatter(x=data['hours'], y=data['no2'], mode='lines+markers', name='Диоксид азота')],
           layout=go.Layout(title='Диоксид азота по часам', xaxis_title='Время', yaxis_title='NO2 (ppb)', template='plotly_dark') 
        )

        o3_fig = go.Figure(
           data=[go.Scatter(x=data['hours'], y=data['o3'], mode='lines+markers', name='Озон')],
           layout=go.Layout(title='Озон по часам', xaxis_title='Время', yaxis_title='NO2 (ppb)', template='plotly_dark') 
        )

        so2_fig = go.Figure(
           data=[go.Scatter(x=data['hours'], y=data['so2'], mode='lines+markers', name='Диоксид серы')],
           layout=go.Layout(title='Диоксид серы по часам', xaxis_title='Время', yaxis_title='SO2 (ppb)', template='plotly_dark') 
        )

        pm2_5_fig = go.Figure(
           data=[go.Scatter(x=data['hours'], y=data['pm2_5'], mode='lines+markers', name='Твердые частицы')],
           layout=go.Layout(title='Твердые частицы по часам', xaxis_title='Время', yaxis_title='PM2.5 (µg/m³)', template='plotly_dark') 
        )

        pm10_fig = go.Figure(
           data=[go.Scatter(x=data['hours'], y=data['pm10'], mode='lines+markers', name='Твердые частицы')],
           layout=go.Layout(title='Твердые частицы по часам', xaxis_title='Время', yaxis_title='PM10 (µg/m³)', template='plotly_dark') 
        )

                     

        return weather_info, co_fig, no2_fig, o3_fig, so2_fig, pm2_5_fig, pm10_fig