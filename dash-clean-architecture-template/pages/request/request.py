# import collections

from dash import html
from components.visualization.draw.request import * 

layout = html.Div( [
    get_item_type_by_vehicle(),
    count_items_by_request(),
    pickup_location_for_request(),
    delivery_location_for_request(),
    capacity_for_request()

])
