# https://plotly.com/python/pie-charts/

from ..charts import * 


class Pie_Charts(Charts):
        

    def render_go(self):
        if self.data_model:
            fig = go.Figure( data = self.data_model)
            return dcc.Graph(figure = fig)
        else:
            return 'Pie_Charts: data model'




