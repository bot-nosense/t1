from components.visualization.draw.vehicle import * 
from dash.dependencies import Input, Output, State
from app import app


def vehicle_callback_item( constraint_name):

    def get_options():
        if value_constraint: return [ {'label': x, 'value': x } for x in value_constraint  ]
        return [ ['could not load data'] ]
    
    value_constraint = get_value_in_constraint(constraint_name)
    return [ 
        dcc.Dropdown(
            options= get_options(), 
            value= value_constraint[0], 
            id='vehicle_to_item_rule_dropdown',
        ),
        html.Br(),
        dcc.Graph(id='time_per_cbm', figure={}),
        html.Br(),
        dcc.Graph(id='time_per_ton', figure={}),
        html.Br(),
        dcc.Graph(id='start_location_type_of_vehicles', figure={}),
        html.Br(),
        dcc.Graph(id='end_location_type_of_vehicles', figure={}),
    ]


def vehicle_type_callback():

    @app.callback(
        Output(component_id='time_per_cbm', component_property='figure'),
        Output(component_id='time_per_ton', component_property='figure'),
        Output(component_id='start_location_type_of_vehicles', component_property='figure'),
        Output(component_id='end_location_type_of_vehicles', component_property='figure'),
        [Input(component_id='vehicle_to_item_rule_dropdown', component_property='value')],
    )
    def update_my_graph(input_value):

        # truyền vào loại xe, trả ra seed vehicle chứa loại xe đó 
        def vehicle_types_list(vehicle_list, vehicle_type):
            result = {}
            result[vehicle_type] = []
            for vehicle in vehicle_list:
                # chuyen sang switch case
                if vehicle['vType']['typeOfVehicleToItemRule'] == vehicle_type: 
                    result[ vehicle_type ].append(vehicle)
                elif vehicle['vType']['typeOfVehicleByMultipleTrips'] == vehicle_type:
                    result[ vehicle_type ].append(vehicle)
                elif vehicle['vType']['typeOfVehicleByLimitedHour'] == vehicle_type:
                    result[ vehicle_type ].append(vehicle)
                elif vehicle['vType']['typeOfVehicleByLimits'] == vehicle_type:
                    result[ vehicle_type ].append(vehicle)
                elif vehicle['vType']['typeOfVehicleByCostToDeploy'] == vehicle_type:
                    result[ vehicle_type ].append(vehicle)
                elif vehicle['vType']['typeOfVehicleByPricePerKm'] == vehicle_type:
                    result[ vehicle_type ].append(vehicle)
            return result
        
        seed = vehicle_types_list(vehicles, input_value)
        return time_per_cbm(seed[input_value]), time_per_ton(seed[input_value]), start_location_type_of_vehicles(seed[input_value]), end_location_type_of_vehicles(seed[input_value])


def vehicle_type_selector():
    element_selector = list(set( [ type_index for vehicle in vehicles for type_index in list( vehicle['vType'].keys() ) ] ))
    return [
        dcc.Dropdown(
            options=[ {'label': x, 'value': x } for x in element_selector ], 
            value= element_selector[0], 
            id='vehicle_type_selector',
        ),
        html.Br(),
        html.Div(id='callback_vehicle_type')
    ]

def vehicle_callback_type_selector():

    @app.callback(
        Output(component_id='callback_vehicle_type', component_property='children'),
        [Input(component_id='vehicle_type_selector', component_property='value')],
    )
    def update_output(input_value):
        return vehicle_callback_item(input_value)
    
    vehicle_type_callback()


#--------------------

vehicle_callback_type_selector()