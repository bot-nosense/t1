
from dash import html
from components.visualization.draw.depot import * 


layout = html.Div( [
    composition_of_depot(),
    wroking_time_of_depot()
])