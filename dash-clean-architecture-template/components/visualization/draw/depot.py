from components.visualization.import_charts import *
from components.seed.input.get_seed_input import *
from utils.functions import *
from utils.constants import *




def composition_of_depot():

    def data_preprocessing(depots, model): 

        # hiện tại depot type đang không có, mặc định sẽ là depot vô danh, khi nào depot được phân loại sẽ đặt tên sau
        def get_depot_type_list(depots):
            number_of_nonsense_depot = 0
            for i in range( len(depots) ):
                depot_type = ( depots[i]['dType'] )
                if list(depot_type.values()) == []: number_of_nonsense_depot += 1
                else:
                    match depot_type:
                        case 'None': number_of_nonsense_depot += 1
            return { 'Nonsense Depot': number_of_nonsense_depot}
        
        depot_type_list = get_depot_type_list(depots)

        # tối ưu lại đoạn này
        A = model[list(model.keys())[0]]
        B = model[list(model.keys())[1]]
        for a, b in depot_type_list.items():
            A.append(str(a))
            B.append(str(b))
        
        return model

    def create_data_model(depots, model):
        model = data_preprocessing(depots, model)
        model['title'] = "Composition of depot"
        return model

    def add_traces(fig, model):
        fig.add_trace( go.Pie(labels=  model['depot_name']  , values=  model['quantity']   ) )                                                    
        return fig

    def draw_model():
        fig = go.Figure()                                           
        model = { 'depot_name': [], 'quantity': [], "title": [] }                          
        data_model = create_data_model(depots, model)          
        add_traces(fig, data_model)
        pie_chart = Pie_Charts(fig= fig)
        fig.update_layout( title={ 'text': model['title'], 'y':0.9, 'x':0.5, 'xanchor': 'right', 'yanchor': 'top'} )
        return pie_chart.render_go_trace()                    

    return draw_model()



def wroking_time_of_depot():

    def data_preprocessing(depots, model): 

        # convert data to struct input model
        def convert_struct_seed(seed):
            return [ ( [ (seed[i][j]) for i in range( len(seed) ) ] ) for j in range( len(seed[0]) ) ]


        # data input cho chart, list time dạng phút 
        def create_timeline(seed_convert):
            result = []
            nb_of_depot = len(seed_convert[0])
            nb_of_timeline = len(seed_convert) - 1

            for time_index in range( nb_of_timeline ):
                timeline = []
                for depot_index in range( nb_of_depot ):   
                    temp = get_minute( seed_convert[time_index + 1][depot_index] ) - get_minute( seed_convert[time_index][depot_index] )
                    timeline.append(temp)
                result.append(timeline)
            return result


        data = convert_struct_seed(object_operating_time(depots))
        model['timeline']= create_timeline(data)
        
        return model


    def create_data_model(depots, model):

        # lấy danh sách tên kho
        def get_depot_code(depots):
            return [depots[veh]['depotCode'] for veh in range(0, len(depots)) ]
        
        model = data_preprocessing(depots, model)
        model['depot_code']= get_depot_code(depots)
        model['time_name']= ['Time 1','Time 2','Time 3','Time 4', 'Time 5'] # đặt lại tên
        model['color']= ['#FFD700', '#00EE00', '#FFD700', '#00EE00', '#FFD700'] # set lại màu
        model['title'] = "wroking time of depot"
        return model


    def add_traces(fig, model):
        for i in range( len(model['timeline'])):
            fig.add_trace( go.Bar( name = model['time_name'][i], x = model['depot_code'], y = model['timeline'][i], marker_color = model['color'][i], width = [0.3] ) ) 
        return fig 


    def draw_model():
        fig = go.Figure()                                           
        model = { 'depot_code': [], 'timeline': [], 'time_name': [], 'color': [], "title": []  }                        
        data_model = create_data_model(depots, model)          
        add_traces(fig, data_model)
        fig.update_layout(barmode='stack', title={ 'text': model['title'], 'y':0.9, 'x':0.5, 'xanchor': 'right', 'yanchor': 'top'})
        bar_chart = Bar_Charts(fig = fig)
        return bar_chart.render_go_trace()              

    return draw_model()