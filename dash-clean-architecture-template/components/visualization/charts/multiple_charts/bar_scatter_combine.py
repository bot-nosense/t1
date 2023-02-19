# https://plotly.com/python/graphing-multiple-chart-types/

from components.visualization.import_library import *
from ..charts import * 

class BarScatterCombine(Charts): 

    def render_go_trace(self):
        if self.fig:
            return dcc.Graph(figure = self.fig)
        else:
            return 'Bar Scatter Combine Chart: data model'