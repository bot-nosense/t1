# https://plotly.com/python/filled-area-plots/

from ..charts import * 

class Filled_Area_Plots(Charts):

    def render_go(self):

        if self.data_model:

            fig = go.Figure()

            for i in range(len(self.data_model['x'])):
                fig.add_trace(go.Scatter(x=self.data_model['x'][i], y=self.data_model['y'][i], 
                                fill=self.data_model[str(i)]['fill'],                    
                                mode=self.data_model[str(i)]['mode'],                    
                                line_color=self.data_model[str(i)]['line_color'],                    
            ))

            self.update_traces(fig)
            self.update_layout(fig)
            return dcc.Graph(figure = fig)
            
        else:
            return 'Filled_Area_Plots: data model'


    def render_px(self):
        if self.data_model:
            fig = px.area(  self.data_model, x = self.data_model['x'], y = self.data_model['y'], line_group = self.data_model['line_group'], color = self.data_model['color'], )
            self.update_traces(fig)
            self.update_layout(fig)
            return dcc.Graph(figure = fig)
        else:
            return 'Filled_Area_Plots: data model'