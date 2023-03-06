
from dash import html
from components.visualization.draw.customer import * 
from pages.customer.customer_callbacks import *

layout = html.Div( [
    # unload_time_for_customer(),
    # wroking_time_of_customer(),



    html.Div(id='vehicle_type', children= customer_type_selector()),
], id= 'layout_vehicle')