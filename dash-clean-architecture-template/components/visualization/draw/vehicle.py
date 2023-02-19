from components.visualization.import_charts import *
from components.seed.input.get_seed_input import *
from utils.functions import *
from utils.constants import *

# pie chart
def vehicle_types():

    def get_data_model(seed):
        return {
            'Multiple Trips': len(seed['VV']['multipleTrips']['matrix']), 
            'Maximum Distance Per Route': len(seed['VV']['maximumDistancePerRoute']['matrix']),
            'Maximum Distance Per Day': len(seed['VV']['maximumDistancePerDay']['matrix']), 
            'Maximum Customer Per Route': len(seed['VV']['maximumCustomerPerRoute']['matrix']),
            'Maximum Customer Per Day': len(seed['VV']['maximumCustomerPerDay']['matrix']), 
            'Cost To Deploy': len(seed['VV']['costToDeploy']['matrix']), 
            'Price Per Km': len(seed['VV']['pricePerKm']['matrix'])
        }

    def create_model(matrix_config, struct_input):

        seed = get_data_model(matrix_config)
        create_data_model(seed, struct_input)
        df = pd.DataFrame(struct_input)

        return df

    struct_input = { 'Name': [], 'Quantity': [] }
    model = create_model( matrix_config, struct_input )
    data = go.Pie(labels=model.Name, values=model.Quantity)
    pie_chart = Pie_Charts(data)

    return pie_chart.render_go()


def time_per_cbm():

    struct_input = { 'Load Time': [], 'Unload Time': [], 'Vehicle Name': [] }

    def data_model():
        for veh in range( len(vehicles) ):
            struct_input['Load Time'].append( vehicles[veh]['loadTimePerCbm'])
            struct_input['Unload Time'].append( vehicles[veh]['unloadTimePerCbm'] )
            struct_input['Vehicle Name'].append( vehicles[veh]['vehicleCode'])
        return struct_input

    def add_traces(fig, model):
        fig.add_trace( go.Scatter( x= model['Vehicle Name'], y= model['Load Time'], name= 'Load Time' ) )
        fig.add_trace( go.Bar( x= model['Vehicle Name'], y= model['Unload Time'], name= 'Unload Time'  ) )

    def draw_model():
        model = data_model()
        fig = go.Figure()
        add_traces(fig, model)
        combine_chart = BarScatterCombine(fig = fig)
        return combine_chart.render_go_trace()

    return draw_model()