from dash import html
from components.visualization.draw.matrix_config import * 

layout = html.Div( [
    component_config(),
    vv_constraint(),
])




