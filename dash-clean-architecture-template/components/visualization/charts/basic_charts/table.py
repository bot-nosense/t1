
from ..charts import * 


class Tables(Charts):

    def render_go(self):
        if self.data_model:
            fig = go.Figure( data = self.data_model)
            return dcc.Graph(figure = fig)
        else:
            return 'Tables: data model'




