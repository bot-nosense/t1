
from dash import html
from components.visualization.draw.vehicle import * 
from pages.vehicle.vehicle_callbacks import *


layout = html.Div( [
    html.Div(id='vehicle_type', children= vehicle_type_selector()),
], id= 'layout_vehicle')
