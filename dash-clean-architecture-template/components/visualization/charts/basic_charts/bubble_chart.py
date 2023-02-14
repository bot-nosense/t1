# https://plotly.com/python/bubble-charts/


from ..charts import * 

class Bubble_Charts(Charts):

    def render_go(self):
        if self.data_model:
            fig = go.Figure( data = self.data_model)
            self.update_traces(fig)
            self.update_layout(fig)
            return dcc.Graph(figure = fig)
        else:
            return 'Bubble_Charts: data model'


    def render_px(self):
        if self.data_model:
            fig = px.line(  self.data, x = self.data_model['x'], y = self.data_model['y'], size = self.data_model['size'], color = self.data_model['color'], 
                            hover_name = self.data_model['hover_name'], log_x = self.data_model['log_x'], size_max = self.data_model['size_max']
            )
            self.update_traces(fig)
            self.update_layout(fig)
            return dcc.Graph(figure = fig)
        else:
            return 'Bubble_Charts: data model'

