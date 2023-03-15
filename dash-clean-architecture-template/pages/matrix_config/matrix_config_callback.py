
from components.visualization.draw.matrix_config import * 
from dash.dependencies import Input, Output, State
from app import app


def cc_constraint():
    return [
        html.Div(id= 'tbl_out')
    ]

# def cc_callback():

#     @app.callback(
#         Output(component_id='tbl_out', component_property='children'),
#         [Input(component_id='tbl', component_property='active_cell')], 
#     )

#     def update_output(input_value):
#         return matrix_cc_test()