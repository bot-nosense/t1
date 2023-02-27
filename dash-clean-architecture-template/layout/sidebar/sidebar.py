import dash_bootstrap_components as dbc
# import dash_html_components as html
from dash import html

from utils.constants import home_page_location, location_page_location, depot_page_location, vehicle_page_location, request_page_location, customer_page_location, mtr_config_page_location


# we use the Row and Col components to construct the sidebar header
# it consists of a title, and a toggle, the latter is hidden on large screens
sidebar_header = dbc.Row(
    [
        dbc.Col(html.H2("Sidebar", className="display-4")),
        dbc.Col(
            [
                html.Button(
                    # use the Bootstrap navbar-toggler classes to style
                    html.Span(className="navbar-toggler-icon"),
                    className="navbar-toggler",
                    # the navbar-toggler classes don't set color
                    style={
                        "color": "rgba(0,0,0,.5)",
                        "border-color": "rgba(0,0,0,.1)",
                    },
                    id="navbar-toggle",
                ),
                html.Button(
                    # use the Bootstrap navbar-toggler classes to style
                    html.Span(className="navbar-toggler-icon"),
                    className="navbar-toggler",
                    # the navbar-toggler classes don't set color
                    style={
                        "color": "rgba(0,0,0,.5)",
                        "border-color": "rgba(0,0,0,.1)",
                    },
                    id="sidebar-toggle",
                ),
            ],
            # the column containing the toggle will be only as wide as the
            # toggle, resulting in the toggle being right aligned
            width="auto",
            # vertically align the toggle in the center
            align="center",
        ),
    ]
)

sidebar = html.Div(
    [
        sidebar_header,
        # we wrap the horizontal rule and short blurb in a div that can be
        # hidden on a small screen
        html.Div(
            [
                html.Hr(),
                html.P(
                    "A responsive sidebar layout with collapsible navigation "
                    "links.",
                    className="lead",
                ),
            ],
            id="blurb",
        ),
        # use the Collapse component to animate hiding / revealing links
        dbc.Collapse(
            dbc.Nav(
                [
                    dbc.NavLink("Home", href=home_page_location, active="exact"),
                    dbc.NavLink("Location", href=location_page_location, active="exact"),
                    dbc.NavLink("Depot", href=depot_page_location, active="exact"),
                    dbc.NavLink("Vehicle", href=vehicle_page_location, active="exact"),
                    dbc.NavLink("Request", href=request_page_location, active="exact"),
                    dbc.NavLink("Customer", href=customer_page_location, active="exact"),
                    dbc.NavLink("Matrix Config", href=mtr_config_page_location, active="exact"),
                ],
                vertical=True,
                pills=True,
            ),
            id="collapse",
        ),
    ],
    id="sidebar",
)