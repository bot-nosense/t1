import json
from dash import html
from ..data import locations

json_string = json.dumps(locations)

layout = html.Div(html.P(json_string))