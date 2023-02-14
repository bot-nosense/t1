import json

from dash import html
# from ..data import locations
# from components.visualization.common import *
from components.visualization.draw import * 

# json_string = json.dumps(locations)


layout = html.Div( [
    composition_of_locations(), # Pie chart

])