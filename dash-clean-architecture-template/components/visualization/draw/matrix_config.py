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
        model['title'] = "Contraints và số lượng contraint trong matrix config"
        return model

    def add_traces(fig, model):
        fig.add_trace( go.Pie(labels=  model['constraint_name']  , values=  model['quantity_constraint']   ) )                                            
        return fig

    def draw_model():                                       
        fig = go.Figure()                                           
        model = { 'alias_constraint_name': [], 'quantity_constraint': [], 'constraint_name': [], "title": [] }                          
        data_model = create_data_model(matrix_config, model)          
        add_traces(fig, data_model)      
        fig.update_layout( title={ 'text': model['title'], 'y':0.9, 'x':0.5, 'xanchor': 'right', 'yanchor': 'top'} )                     
        pie_chart = Pie_Charts(fig = fig)                
        return pie_chart.render_go_trace()                      

    return draw_model()