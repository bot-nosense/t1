from components.visualization.import_charts import *
from components.seed.input.get_seed_input import *
from utils.functions import *
from utils.constants import *


# pie chart
def composition_of_depot():

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


    def create_model(depots, struct_input):
        depot_type_list = get_depot_type_list(depots)
        create_data_model(depot_type_list, struct_input)
        df = pd.DataFrame(struct_input)
        return df


    struct_input = { 'Name': [], 'Quantity': [] }
    model = create_model( depots, struct_input )
    data = [go.Pie(labels=model['Name'], values=model['Quantity'])]
    pie_chart = Pie_Charts(data = data)

    return pie_chart.render_go()



# bar chart
def wroking_time_of_depot(): # depot này chỉ hoạt động trong ngày

    def create_model(depots, model):

        def create_time_default(working_time): # input: '2019-01-01 00:00'
            get_day = working_time.split()[0]
            return [get_day + ' 00:00:00', get_day + ' 24:00:00'] # start and end time of 1 days


        def get_seed_time(depots):
            result = []
            time_default = create_time_default(depots[0]['workingTime']['start'])

            for index in range( len(depots) ):
                working_time = depots[index]['workingTime']
                break_time = depots[index]['breakTimes'][0]
                result.append([time_default[0], working_time['start'], break_time['start'], break_time['end'], working_time['end'], time_default[1]])
            return result


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


        # lấy danh sách tên kho
        def get_depot_code(depots):
            return [depots[veh]['depotCode'] for veh in range(0, len(depots)) ]

        data = convert_struct_seed(get_seed_time(depots))
        model['Name']= get_depot_code(depots)
        model['Time']= create_timeline(data)
        model['Time Name']= ['Time 1','Time 2','Time 3','Time 4', 'Time 5']
        model['Color']= ['#FFD700', '#00EE00', '#FFD700', '#00EE00', '#FFD700']

        return model

    def add_traces(fig, model):
        for i in range( len(model['Time'])):
            fig.add_trace( go.Bar( name = model['Time Name'][i], x = model['Name'], y = model['Time'][i], marker_color = model['Color'][i] ) ) 
        return fig 

    def draw_model():
        model = { 'Name': [], 'Time': [], 'Time Name': [], 'Color': [] }
        data_model = create_model(depots, model)
        fig = go.Figure()
        add_traces(fig, data_model)
        fig.update_layout(barmode='stack') 
        bar_chart = Bar_Charts(fig = fig)
        return bar_chart.render_go_trace()

    return draw_model()