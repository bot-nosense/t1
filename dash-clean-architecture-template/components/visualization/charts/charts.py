from ..import_library import *

@dataclass
class Charts():
    
    data_model : list 
    layouts: dict 

    def __init__(self, data = None, layout = None): 
        self.data_model = data
        self.layouts = layout

    def update_layout(self):
        pass

    def update_traces(self):
        pass

    def render_go(self):
        pass

    def render_px(self):
        pass
        






