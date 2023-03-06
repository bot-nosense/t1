
from components.visualization.draw.customer import * 
from dash.dependencies import Input, Output, State
from app import app


def customer_callback_item( constraint_name):
    
    value_constraint = get_value_in_constraint(constraint_name)
    return [ 
        dcc.Dropdown(
            options=[ {'label': x, 'value': x } for x in value_constraint  ], 
            value= value_constraint[0], 
            id='customer_dropdown',
        ),
        html.Br(),
        dcc.Graph(id='unload_time_for_customer', figure={}),
        html.Br(),
        dcc.Graph(id='wroking_time_of_customer', figure={}),
        html.Br(),
    ]


def customer_type_callback():

    @app.callback(
        Output(component_id='unload_time_for_customer', component_property='figure'),
        Output(component_id='wroking_time_of_customer', component_property='figure'),
        [Input(component_id='customer_dropdown', component_property='value')],
    )
    def update_my_graph(input_value):

        def customer_types_list(list, type):
            result = {}
            result[type] = []
            for customer in list:
                # chuyen sang switch case
                if customer['cType']['typeOfCustomerByLimitedHour'] == type: 
                    result[ type ].append(customer)
                elif customer['cType']['typeOfCustomerByTimeSync'] == type:
                    result[ type ].append(customer)
            return result
        
        seed = customer_types_list(customers, input_value)
        return unload_time_for_customer(seed[input_value]), wroking_time_of_customer(seed[input_value])


def customer_type_selector():
    element_selector = list(set( [ type_index for cus in customers for type_index in list( cus['cType'].keys() ) ] ))
    return [
        dcc.Dropdown(
            options=[ {'label': x, 'value': x } for x in element_selector ], 
            value= element_selector[0], 
            id='customer_type_selector',
        ),
        html.Br(),
        html.Div(id='callback_customer_type')
    ]

def customer_callback_type_selector():

    @app.callback(
        Output(component_id='callback_customer_type', component_property='children'),
        [Input(component_id='customer_type_selector', component_property='value')],
    )
    def update_output(input_value):
        return customer_callback_item(input_value)
    
    customer_type_callback()


#--------------------

customer_callback_type_selector()