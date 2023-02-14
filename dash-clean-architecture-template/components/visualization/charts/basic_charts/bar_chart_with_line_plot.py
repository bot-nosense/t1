# https://plotly.com/python/horizontal-bar-charts/

from components.visualization.import_library import *
from ..charts import * 

class Bar_Chart_with_Line_Plot(Charts): 

    def update_layout(self, figure):
        if self.data:
            figure.update_layout(
                title= self.data['title'],
                yaxis= self.data['yaxis'],
                xaxis= self.data['xaxis'],
                xaxis2= self.data['xaxis2'],
                legend= self.data['legend'],
                margin= self.data['margin'],
                paper_bgcolor= self.data['paper_bgcolor'],
                plot_bgcolor= self.data['plot_bgcolor'],
            )

    def render_go(self):
        
        if self.data:

            fig = make_subplots(rows=1, cols=2, specs=[[{}, {}]], shared_xaxes=True, shared_yaxes=False, vertical_spacing=0.001)
            
            fig.append_trace(go.Bar( orientation='h',
                x=self.data['y_saving'],
                y=self.data['x'],
                marker=dict(
                    color=self.data['bar_chart_color'],
                    line=dict(
                        color=self.data['bar_chart_line_color'],
                        width=1),
                ),
                name= self.data['bar_chart_name'],
            ), 1, 1)

            fig.append_trace(go.Scatter(
                x=self.data['y_net_worth'], y=self.data['x'],
                mode=self.data['line_plot_mode'],
                line_color=self.data['line_plot_color'],
                name=self.data['line_plot_name'],
            ), 1, 2)

            self.update_layout(fig)
            return dcc.Graph(figure = fig)
        
        else:
            return 'Bar_Chart_with_Line_Plot: data model is none'