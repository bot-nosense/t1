# https://plotly.com/python/line-and-scatter/

from ..charts import * 


class Scatter_Plots(Charts):

    def render_go(self):
        if self.data_model:
            fig = go.Figure( data = self.data_model)
            self.update_traces(fig)
            self.update_layout(fig)
            return dcc.Graph(figure = fig)
        else:
            return 'Scatter_Plots: data model'


    def render_px(self):
        if self.data_model:
            fig = px.scatter(self.data_model, x=self.data_model['x'], y=self.data_model['y'])
            self.update_traces(fig)
            self.update_layout(fig)
            return dcc.Graph(figure = fig)
        else:
            return 'Scatter_Plots: data model'
