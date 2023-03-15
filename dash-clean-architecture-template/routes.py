import dash_bootstrap_components as dbc
from dash import html
from dash.dependencies import Input, Output

from app import app

from utils.constants import home_page_location, location_page_location, depot_page_location, vehicle_page_location, request_page_location, customer_page_location, mtr_config_page_location


from pages.home import home
from pages.request import request
from pages.location import location
from pages.depot import depot
from pages.vehicle import vehicle
from pages.customer import customer
from pages.matrix_config import matrix_config




@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == home_page_location:
        return home.layout
    elif pathname == customer_page_location:
        return customer.layout
    elif pathname == request_page_location:
        return request.layout
    elif pathname == location_page_location:
        return location.layout
    elif pathname == depot_page_location:
        return depot.layout
    elif pathname == vehicle_page_location:
        return vehicle.layout
    elif pathname == mtr_config_page_location:
        return matrix_config.layout
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )