# https://plotly.com/python/line-charts/

# from turtle import title
from ..charts import * 


class Line_Charts(Charts):

    def render_go(self):
        if self.data_model:
            fig = go.Figure( data = self.data_model)
            self.update_traces(fig)
            self.update_layout(fig)
            return dcc.Graph(figure = fig)
        else:
            return 'Line_Charts: data model'


    def render_px(self):
        if self.data_model:
            fig = px.line(self.data_model, x = self.data_model['x'], y = self.data_model['y'], title = self.data_model['title'])
            self.update_traces(fig)
            self.update_layout(fig)
            return dcc.Graph(figure = fig)
        else:
            return 'Line_Charts: data model'
        

