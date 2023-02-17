# https://plotly.com/python/pie-charts/

from ..charts import * 


class Pie_Charts(Charts):
        

    def render_go(self):
        if self.data_model:
            fig = go.Figure( data = self.data_model)
            return dcc.Graph(figure = fig)
        else:
            return 'Pie_Charts: data model'

    def render_go_trace(self):
        if self.fig:
            return dcc.Graph(figure = self.fig)
        else:
            return 'Pie_Charts: data model'




