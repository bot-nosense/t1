from dash import html
from components.visualization.draw.matrix_config import * 
# from .matrix_config_callback import *

layout = html.Div( [
    component_config(),
    vv_constraint(),
    matrix_cc_test(),
    # cv_constraint(),

    # html.Div(id='cc_constraint', children= cc_constraint()),
])




