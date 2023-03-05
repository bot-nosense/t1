from components.visualization.draw.vehicle import * 
from dash.dependencies import Input, Output, State
from app import app


def test_dropdown_chart():
    
    def get_vehicle_to_item_rule(): # lấy ra loại xe khô lạnh đông
        return list( set ([ matrix_config['CV']['itemToVehicleRule']['matrix'][matrix_index]['typeOfVehicle'] for matrix_index in range( len( matrix_config['CV']['itemToVehicleRule']['matrix'] ) ) ] ) )

    return [ 
        dcc.Dropdown(
            options=[ {'label': x, 'value': x } for x in get_vehicle_to_item_rule()  ], 
            value=get_vehicle_to_item_rule()[0], 
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


def test_callback():

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
                if vehicle['vType']['typeOfVehicleToItemRule'] == vehicle_type: 
                    result[ vehicle_type ].append(vehicle)
            return result
        
        seed = vehicle_types_list(vehicles, input_value)
        return time_per_cbm(seed[input_value]), time_per_ton(seed[input_value]), start_location_type_of_vehicles(seed[input_value]), end_location_type_of_vehicles(seed[input_value])


test_callback()