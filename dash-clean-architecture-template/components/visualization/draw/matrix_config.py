import copy 

from components.visualization.import_charts import *
from components.seed.input.get_seed_input import *
from utils.functions import *
from utils.constants import *


# thông tin chung của matrix config
def component_config():

    def data_preprocessing(matrix_config, model): 

        # tối ưu lại đoạn code này
        # replace alias constraint name
        def replace_alias_constraints(alias_list, model): 
            model['constraint_name'] = copy.deepcopy(alias_list) 
            for index in range( len(model['constraint_name']) ):
                if model['constraint_name'][index] == 'VD': model['constraint_name'][index] = 'Vehicle Depot'
                if model['constraint_name'][index] == 'VC': model['constraint_name'][index] = 'Vehicle Customer'
                if model['constraint_name'][index] == 'VV': model['constraint_name'][index] = 'Vehicle Vehicle'
                if model['constraint_name'][index] == 'DD': model['constraint_name'][index] = 'Depot Depot'
                if model['constraint_name'][index] == 'DC': model['constraint_name'][index] = 'Depot Customer'
                if model['constraint_name'][index] == 'DV': model['constraint_name'][index] = 'Depot Vehicle'
                if model['constraint_name'][index] == 'CV': model['constraint_name'][index] = 'Customer Vehicle'
                if model['constraint_name'][index] == 'CD': model['constraint_name'][index] = 'Customer Depot'
                if model['constraint_name'][index] == 'CC': model['constraint_name'][index] = 'Customer Customer'
            return model

        model['alias_constraint_name'] = [ i for i in matrix_config ]
        model['quantity_constraint'] = [ len(matrix_config[i]) for i in matrix_config ]
        replace_alias_constraints(model['alias_constraint_name'], model)
        return model

    def create_data_model(matrix_config, model):
        model = data_preprocessing(matrix_config, model)
        model['title'] = "Contraints và số lượng contraint"
        return model

    def add_traces(fig, model):
        fig.add_trace( go.Pie(labels=  model['constraint_name']  , values=  model['quantity_constraint']   ) )                                            
        return fig

    def draw_model():                                       
        fig = go.Figure()                                           
        model = { 'alias_constraint_name': [], 'quantity_constraint': [], 'constraint_name': [], "title": [] }                          
        data_model = create_data_model(matrix_config, model)          
        add_traces(fig, data_model)      
        fig.update_layout( title= model['title'] )                     
        pie_chart = Pie_Charts(fig = fig)                
        return pie_chart.render_go_trace()                      

    return draw_model()


def vv_constraint():

    def data_preprocessing(matrix_config, model): 

        def get_vehicle_type():
            # tìm cách cho đoạn này không bị hard code
            return {
            'Multiple Trips': len(matrix_config['VV']['multipleTrips']['matrix']), 
            'Maximum Distance Per Route': len(matrix_config['VV']['maximumDistancePerRoute']['matrix']),
            'Maximum Distance Per Day': len(matrix_config['VV']['maximumDistancePerDay']['matrix']), 
            'Maximum Customer Per Route': len(matrix_config['VV']['maximumCustomerPerRoute']['matrix']),
            'Maximum Customer Per Day': len(matrix_config['VV']['maximumCustomerPerDay']['matrix']), 
            'Cost To Deploy': len(matrix_config['VV']['costToDeploy']['matrix']), 
            'Price Per Km': len(matrix_config['VV']['pricePerKm']['matrix'])
        }

        type_list = get_vehicle_type()
        A = model[list(model.keys())[0]]
        B = model[list(model.keys())[1]]
        for a, b in type_list.items():
            A.append(str(a))
            B.append(str(b))
        return model


    def create_data_model(matrix_config, model):
        model = data_preprocessing(matrix_config, model)
        model['title'] = "Vehicle - Vehicle Contraint"    
        return model


    def add_traces(fig, model):
        fig.add_trace( go.Pie( labels=  model['name'], values=  model['quantity'], hole = 0.3 ) )     
        return fig


    def draw_model():
        fig = go.Figure()                                           
        model = { 'name': [], 'quantity': [], "title": []  }                          
        data_model = create_data_model(matrix_config, model)          
        add_traces(fig, data_model)
        fig.update_layout( title= model['title'] )                                   
        pie_chart = Pie_Charts(fig = fig)                
        return pie_chart.render_go_trace()                      

    return draw_model()


def matrix_cc_test():

    def data_preprocessing(matrix_config, model): 
        temp_a = list( dict.fromkeys ( [ matrix_config['CV']['itemToVehicleRule']['matrix'][index]['typeOfItem'] for index in range( len( matrix_config['CV']['itemToVehicleRule']['matrix'] ) ) ] ) )
        temp_b = list( dict.fromkeys ( [ matrix_config['CV']['itemToVehicleRule']['matrix'][index]['typeOfVehicle'] for index in range( len( matrix_config['CV']['itemToVehicleRule']['matrix'] ) ) ] ) )

        item_b_0 = [ matrix_config['CV']['itemToVehicleRule']['matrix'][index]['value'] for index in range( len( matrix_config['CV']['itemToVehicleRule']['matrix'] ) ) if matrix_config['CV']['itemToVehicleRule']['matrix'][index]['typeOfItem'] == temp_a[0] ]
        item_b_1 = [ matrix_config['CV']['itemToVehicleRule']['matrix'][index]['value'] for index in range( len( matrix_config['CV']['itemToVehicleRule']['matrix'] ) ) if matrix_config['CV']['itemToVehicleRule']['matrix'][index]['typeOfItem'] == temp_a[1] ]

        model['header'].extend([''])
        model['header'].extend(temp_a)
        model['col_value'] = [
            temp_b,
            item_b_0,
            item_b_1,
        ]
        return model


    def create_data_model(matrix_config, model):
        model = data_preprocessing(matrix_config, model)
        model['title'] = "Vehicle - Customer Contraint"    
        return model


    def draw_model():                                          
        model = { 'col_value': [], 'header': [], "title": []  }                          
        data_model = create_data_model(matrix_config, model)    
        datas = [go.Table(
            columnorder = [1,2],
            columnwidth = [80,400],
            header = dict(
                values = model['header'],
                line_color='darkslategray',
                fill_color='royalblue',
                align=['left','center'],
                font=dict(color='white', size=12),
                height=40
            ),
            cells=dict(
                values= model['col_value'],
                line_color='darkslategray',
                fill=dict(color=['paleturquoise', 'white']),
                align=['left', 'center'],
                font_size=12,
                height=30
            )
        )] 
        fig = go.Figure()      
        fig.update_layout( title= model['title'] )                                   
        table = Tables(data= datas)                
        return table.render_go()
    
    return draw_model()


def cv_constraint():
    return 1