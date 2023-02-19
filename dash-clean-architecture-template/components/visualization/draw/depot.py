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
def wroking_time_of_depot():
    return 1
    # đã commit model bên colab
