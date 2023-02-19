from components.visualization.import_charts import *
from components.seed.input.get_seed_input import *
from utils.functions import *
from utils.constants import *

# pie chart
def vehicle_types():

    def get_data(seed):
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

        seed = get_data(matrix_config)
        create_data_model(seed, struct_input)
        df = pd.DataFrame(struct_input)

        return df

    struct_input = { 'Name': [], 'Quantity': [] }
    model = create_model( matrix_config, struct_input )
    data = go.Pie(labels=model.Name, values=model.Quantity)
    pie_chart = Pie_Charts(data)

    return pie_chart.render_go()