
from dash import html
from components.visualization.draw.vehicle import * 
from pages.vehicle.vehicle_callbacks import *


layout = html.Div( [

    html.Div(id='test_dropdown_chart', children= test_dropdown_chart())

])
