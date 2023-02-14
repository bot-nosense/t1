
# from .common import *
from .import_charts import *
# from .import_charts import *
from components.seed.input.get_seed_input import *
from utils.functions import *




# def composition_of_locations(locations):
#     location_types = { "Customer": 0, "Depot": 0, "Station": 0, "Hub": 0, "Satellite": 0 }
#     for location in locations:
#         location_types[location['lTypes'][0]] += 1

#     struct_input = { 'Name': list(location_types.keys()), 'Quantity': list(location_types.values()) }
#     df = pd.DataFrame(struct_input)

#     data = [go.Pie(labels=df.Name, values=df.Quantity)]
#     pie_chart = Pie_Charts(data)

#     return pie_chart.render_go()


# def create_data_model(model_name, value_list):
# 	for key, value in value_list.items():
# 		for k, v in model_name.items():

# 			model_name[k].append(key)
# 			model_name[k].append(value)

# 	return model_name

def composition_of_locations():
    
    def create_model(locations, struct_input):

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

        location_type_list = get_location_type_list(locations)
        create_data_model(struct_input, location_type_list)
        df = pd.DataFrame(struct_input)

        return df

    struct_input = { 'Name': [], 'Quantity': [] }
    model = create_model( locations, struct_input )
    data = [go.Pie(labels=model.Name, values=model.Quantity)]
    pie_chart = Pie_Charts(data)

    return pie_chart.render_go()



