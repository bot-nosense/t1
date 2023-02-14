from ..import_library import *

@dataclass
class Charts():
    
    data_model : list

    def __init__(self, data): #, update_layout, update_traces
        self.data_model = data

    def update_layout(self):
        pass

    def update_traces(self):
        pass

    def renders(self, _data):
        fig = go.Figure( data = _data )
        fig.update_traces(hole = 0.3)
        return dcc.Graph(figure = fig)






