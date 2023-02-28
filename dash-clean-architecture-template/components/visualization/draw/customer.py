
import collections

from components.visualization.import_charts import *
from components.seed.input.get_seed_input import *
from utils.functions import *
from utils.constants import *



# unload time của cus
def unload_time_for_customer():

    def data_preprocessing(customers, model):
        model['cus_name'].append( [  customers[cus_index]['customerCode'] for cus_index in range( len( customers ) ) ] )
        model['fixed_unload_time'].append( [  customers[cus_index]['fixedUnloadTime'] for cus_index in range( len( customers ) ) ] )
        model['unload_time_per_ton'].append( [  customers[cus_index]['unloadTimePerTon'] for cus_index in range( len( customers ) ) ] )
        model['unload_time_per_cbm'].append( [  customers[cus_index]['unloadTimePerCbm'] for cus_index in range( len( customers ) ) ] )
        return model


    def create_data_model(customers, model):
        model = data_preprocessing(customers, model)
        model['title'] = "Unload time for customer"
        return model


    def add_traces(fig, model):
        fig.add_trace( go.Scatter( x= model['cus_name'][0], y= model['fixed_unload_time'][0], name= 'fixed unload time' ) )
        fig.add_trace( go.Bar( x= model['cus_name'][0], y= model['unload_time_per_ton'][0], name= 'unload time per ton', width = [ 0.3, 0.3 ] ) )
        fig.add_trace( go.Bar( x= model['cus_name'][0], y= model['unload_time_per_cbm'][0], name= 'unload time per cbm', width = [ 0.3, 0.3 ] ) )
        return fig


    def draw_model():
        fig = go.Figure()
        model = { 'title': [], 'cus_name': [], 'fixed_unload_time': [], 'unload_time_per_ton': [], 'unload_time_per_cbm': [], 'name': [] }
        data_model = create_data_model(customers, model)
        add_traces(fig, data_model)
        fig.update_layout( title={ 'text': model['title'], 'y':0.9, 'x':0.5, 'xanchor': 'right', 'yanchor': 'top'} )
        combine_chart = BarScatterCombine(fig = fig)
        return combine_chart.render_go_trace()

    return draw_model()



def wroking_time_of_customer(): # the customer is only open during the day

    def data_preprocessing(customers, model):
        
        # convert data to struct input model
        def convert_struct_time_layout(seed):
            return [ ( [ (seed[i][j]) for i in range( len(seed) ) ] ) for j in range( len(seed[0]) ) ]
        

        def create_timeline(seed_convert):
            result = []
            nb_of_customer = len(seed_convert[0])
            nb_of_timeline = len(seed_convert) - 1

            for time_index in range( nb_of_timeline ):
                timeline = []
                for cus_index in range( nb_of_customer ) :   
                    timeline.append( get_minute( seed_convert[time_index + 1][cus_index] ) - get_minute( seed_convert[time_index][cus_index] ) )
                result.append(timeline)
            return result
        
        time_layout = convert_struct_time_layout(object_operating_time(customers))
        model['timeline']= create_timeline(time_layout)
        return model
    

    def create_data_model(customers, model):
        model = data_preprocessing(customers, model)
        model['name_chart']= [customers[index]['customerCode'] for index in range( len(customers) ) ]
        model['name_of_timeline']= ['Time 1','wroking time','Time 3','wroking time', 'Time 5'] # đặt lại tên
        model['color']= ['#FFD700', '#00EE00', '#FFD700', '#00EE00', '#FFD700'] # đổi lại màu
        model['title'] = "Wroking time of customer"
        return model   
    

    def add_traces(fig, model):
        for i in range( len(model['timeline'])):
            fig.add_trace( go.Bar( name = model['name_of_timeline'][i], x = model['name_chart'], y = model['timeline'][i], marker_color = model['color'][i], width = [ 0.3, 0.3 ] ) ) 
        return fig 


    def draw_model():
        model = { 'name_chart': [], 'timeline': [], 'name_of_timeline': [], 'color': [], "title": []  }
        data_model = create_data_model(customers, model)
        fig = go.Figure()
        add_traces(fig, data_model)
        fig.update_layout(barmode='stack', title={ 'text': model['title'], 'y':0.9, 'x':0.5, 'xanchor': 'right', 'yanchor': 'top'})  
        bar_chart = Bar_Charts(fig = fig)
        return bar_chart.render_go_trace()

    return draw_model()


