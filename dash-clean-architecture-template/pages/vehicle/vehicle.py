
from dash import html
from components.visualization.draw.vehicle import * 

layout = html.Div( [
    vehicle_types(), #  pie chart of vehicle types
    time_per_cbm(), #  bar scatter combine chart of time per cbm
    time_per_ton(), #  bar scatter combine chart of time per ton
    end_location_type_of_vehicles(),
    start_location_type_of_vehicles()


    
])