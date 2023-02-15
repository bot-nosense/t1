# https://plotly.com/python/scattermapbox/

from ..charts import * 


class Scatter_Plots_on_Mapbox(Charts):

    def render_go(self):
        if self.data_model:
            fig = go.Figure( data = self.data_model, layout= self.layouts)
            return dcc.Graph(figure = fig)
        else:
            return 'Scatter_Plots_on_Mapbox: data model'

    def render_go_trace(self):
        if self.fig:
            return dcc.Graph(figure = self.fig)
        else:
            return 'Scatter_Plots_on_Mapbox: data model'


'''
        Example:
    import plotly.graph_objects as go
    import pandas as pd

    mapbox_access_token = 'pk.eyJ1IjoiYm90LW5vc2Vuc2UiLCJhIjoiY2xlNDRuODJmMDk0YTNuc2FucDMwZWZyciJ9.gmDfK4g6y8aptLWpQM9E4w'

    df = pd.DataFrame({'name': ['London', 'Oxford'],
                    'latitude': [51.509865, 51.7520],
                    'longitude': [-0.118092, -1.2577],
                    'forecast': ['Cloudy', 'Sunny']}) 

    data = go.Scattermapbox(lat=list(df['latitude']),
                            lon=list(df['longitude']),
                            mode='markers+text',
                            marker=dict(size=20, color='green'),
                            textposition='top right',
                            textfont=dict(size=16, color='black'),
                            text=[df['name'][i] + '<br>' + df['forecast'][i] for i in range(df.shape[0])])

    layout = dict(margin=dict(l=0, t=0, r=0, b=0, pad=0),
                mapbox=dict(accesstoken=mapbox_access_token,
                            center=dict(lat=51.6, lon=-0.2),
                            style='light',
                            zoom=8))

    fig = go.Figure(data=data, layout=layout)
    fig.show()

'''