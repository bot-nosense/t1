
# from .common import *
from .import_charts import *
# from .import_charts import *
from components.seed.input.get_seed_input import *
from utils.functions import *



def composition_of_locations():

    def get_location_type_list(locations):

        number_of_customer, number_of_depot, number_of_station, number_of_hub, number_of_satellife = 0, 0, 0, 0, 0

        for i in range( len(locations) ):
            
            location_type = ( locations[i]['lTypes'] )[0]
            match location_type:
                case "HUB": number_of_hub += 1
                case "DEPOT": number_of_depot += 1
                case "STATION": number_of_station += 1
                case "CUSTOMER": number_of_customer += 1
                case "SATELLITE": number_of_satellife += 1
        
        return { 'Customer': number_of_customer, 'Depot': number_of_depot, 'Station': number_of_station, 'Hub': number_of_hub, 'Satellite': number_of_satellife } 

    def create_model(locations, struct_input):

        location_type_list = get_location_type_list(locations)
        create_data_model(location_type_list, struct_input)
        df = pd.DataFrame(struct_input)

        return df

    struct_input = { 'Name': [], 'Quantity': [] }
    model = create_model( locations, struct_input )
    data = [go.Pie(labels=model.Name, values=model.Quantity)]
    pie_chart = Pie_Charts(data)

    return pie_chart.render_go()



