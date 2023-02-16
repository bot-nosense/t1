from ..import_library import *

@dataclass
class Charts():
    
    data_model : list 
    layouts: dict 
    fig: go.Figure()

    def __init__(self, data = None, layout = None, fig = None): 
        self.data_model = data
        self.layouts = layout
        self.fig = fig

    # def update_layout(self):
    #     pass

    # def update_traces(self):
    #     pass

        # render with graph object
    def render_go(self):
        pass

        # render with plotly express
    def render_px(self):
        pass

        # render with graph object but add traces
    def render_go_trace(self):
        pass
        






