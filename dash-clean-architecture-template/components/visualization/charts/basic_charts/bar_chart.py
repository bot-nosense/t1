# https://plotly.com/python/bar-charts/

from ..charts import * 


class Bar_Charts(Charts):

    def render_go(self):
        if self.data_model:
            fig = go.Figure( data = self.data_model, layout= self.layouts)
            return dcc.Graph(figure = fig)
        else:
            return 'Bar_Charts: data model'

    def render_go_trace(self):
        if self.fig:
            return dcc.Graph(figure = self.fig)
        else:
            return 'Bar_Charts: data model'
