# https://plotly.com/python/gantt/

from ..charts import * 

class Gantt_Chart(Charts): 

    def render_go(self):
        if self.data_model:
            return super().render_go()
        else:
            return 'Gantt_Chart: data model'

    def render_px(self):
        if self.data_model:
            fig = px.timeline(self.data_model, x_start = self.data_model['x_start'], y = self.data_model['y'], title = self.data_model['title'], x_end = self.data_model['x_end'], color = self.data_model['color'])
            self.update_traces(fig)
            self.update_layout(fig)
            return dcc.Graph(figure = fig)
        else:
            return 'Gantt_Chart: data model'
            