
from dash import html
from components.visualization.draw.location import * 



layout = html.Div( [
    composition_of_locations(),
    html.Div( html.P('Composition of location with mapbox')),
    point_on_the_map(), 



    
])