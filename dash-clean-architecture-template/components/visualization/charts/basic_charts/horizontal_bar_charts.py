# https://plotly.com/python/horizontal-bar-charts/


from ..charts import * 

class Horizontal_Bar_Charts(Charts):

    def update_layout(self, figure):
        figure.update_layout(
            paper_bgcolor = self.data_model['paper_bgcolor'],
            plot_bgcolor = self.data_model['plot_bgcolor'],
            showlegend=False,
            height = self.data_model['height']
        )

    def render_go(self):

        if self.data_model:

            fig = go.Figure()
            len_data = len(self.data_model['x_data'][0])
            x_data = self.data_model['x_data']
            y_data = self.data_model['y_data']
            colors = self.data_model['colors']

            for i in range(0, len_data):
                for xd, yd in zip(x_data, y_data):
                    fig.add_trace(go.Bar( x=[xd[i]], y=[yd], orientation='h',
                        marker=dict( color= colors[i], line=dict(color='rgb(248, 248, 249)', width=1)
                    )
                ))

            fig.update_layout( barmode='stack')
            self.update_traces(fig)
            self.update_layout(fig)
        
            return dcc.Graph(figure = fig)
            
        else:
            return 'Horizontal_Bar_Charts: data model'


    def render_px(self):
        if self.data_model:
            fig = px.bar(  self.data_model, orientation='h', x = self.data_model['x'], y = self.data_model['y'], title = self.data_model['title'] )
            self.update_traces(fig)
            self.update_layout(fig)
            return dcc.Graph(figure = fig)
        else:
            return 'Horizontal_Bar_Charts: data model'