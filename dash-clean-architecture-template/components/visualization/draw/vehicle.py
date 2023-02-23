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

    def draw_model():
        struct_input = { 'Name': [], 'Quantity': [] }
        model = create_model( matrix_config, struct_input )
        data = go.Pie(labels=model.Name, values=model.Quantity)
        pie_chart = Pie_Charts(data)
        return pie_chart.render_go()
    
    return draw_model()


# bar scatter combine charts
def time_per_cbm():

    def create_data_model(vehicles, model):
        for veh in range( len(vehicles) ):
            model['Load Time'].append( vehicles[veh]['loadTimePerCbm'])
            model['Unload Time'].append( vehicles[veh]['unloadTimePerCbm'] )
            model['Vehicle Name'].append( vehicles[veh]['vehicleCode'])
        return model

    def add_traces(fig, model):
        fig.add_trace( go.Scatter( x= model['Vehicle Name'], y= model['Load Time'], name= 'Load Time' ) )
        fig.add_trace( go.Bar( x= model['Vehicle Name'], y= model['Unload Time'], name= 'Unload Time' ) )

    def draw_model():
        model = { 'Load Time': [], 'Unload Time': [], 'Vehicle Name': [] }
        data_model = create_data_model(vehicles, model)
        fig = go.Figure()
        add_traces(fig, data_model)
        combine_chart = BarScatterCombine(fig = fig)
        return combine_chart.render_go_trace()

    return draw_model()


# bar scatter combine charts
def time_per_ton():

    def create_data_model(vehicles, model):
        for veh in range( len(vehicles) ):
            model['Load Time'].append( vehicles[veh]['loadTimePerTon'])
            model['Unload Time'].append( vehicles[veh]['unloadTimePerTon'] )
            model['Vehicle Name'].append( vehicles[veh]['vehicleCode'])
        return model

    def add_traces(fig, model):
        fig.add_trace( go.Scatter( x= model['Vehicle Name'], y= model['Load Time'], name= 'Load Time' ) )
        fig.add_trace( go.Bar( x= model['Vehicle Name'], y= model['Unload Time'], name= 'Unload Time' ) )

    def draw_model():
        model = { 'Load Time': [], 'Unload Time': [], 'Vehicle Name': [] }
        data_model = create_data_model(vehicles, model)
        fig = go.Figure()
        add_traces(fig, data_model)
        combine_chart = BarScatterCombine(fig = fig)
        return combine_chart.render_go_trace()

    return draw_model()

    # bar scatter combine charts
def end_location_type_of_vehicles():

    def get_data(vehicles):
        number_of_customer, number_of_depot, number_of_station, number_of_hub, number_of_satellife = 0, 0, 0, 0, 0
        for veh in range( len(vehicles) ):
            end_location = vehicles[veh]['endLocationType']
            if end_location == 'DEPOT': number_of_depot +=1
            elif end_location == 'HUB': number_of_hub +=1
            elif end_location == "STATION": number_of_station += 1
            elif end_location == "CUSTOMER": number_of_customer += 1
            elif end_location == "SATELLITE": number_of_satellife += 1
        return { 'Customer': number_of_customer, 'Depot': number_of_depot, 'Station': number_of_station, 'Hub': number_of_hub, 'Satellite': number_of_satellife } 

    def create_model(vehicles, struct_input):
        location_type_list = get_data(vehicles)
        create_data_model(location_type_list, struct_input)
        df = pd.DataFrame(struct_input)
        return df

    def draw_model():
        struct_input = { 'Name': [], 'Quantity': [] }
        model = create_model( vehicles, struct_input )
        data = go.Pie(labels=model.Name, values=model.Quantity)
        pie_chart = Pie_Charts(data)
        return pie_chart.render_go()

    return draw_model()


def start_location_type_of_vehicles():

    def get_data(vehicles):
        number_of_customer, number_of_depot, number_of_station, number_of_hub, number_of_satellife = 0, 0, 0, 0, 0
        for veh in range( len(vehicles) ):
            end_location = vehicles[veh]['startLocationType']
            if end_location == 'DEPOT': number_of_depot +=1
            elif end_location == 'HUB': number_of_hub +=1
            elif end_location == "STATION": number_of_station += 1
            elif end_location == "CUSTOMER": number_of_customer += 1
            elif end_location == "SATELLITE": number_of_satellife += 1
        return { 'Customer': number_of_customer, 'Depot': number_of_depot, 'Station': number_of_station, 'Hub': number_of_hub, 'Satellite': number_of_satellife } 

    def create_model(vehicles, struct_input):
        location_type_list = get_data(vehicles)
        create_data_model(location_type_list, struct_input)
        df = pd.DataFrame(struct_input)
        return df

    def draw_model():
        struct_input = { 'Name': [], 'Quantity': [] }
        model = create_model( vehicles, struct_input )
        data = go.Pie(labels=model.Name, values=model.Quantity)
        pie_chart = Pie_Charts(data)
        return pie_chart.render_go()

    return draw_model()






# def start_location_type_of_vehicles(vehicles):
    
#     number_of_customer, number_of_depot, number_of_station, number_of_hub, number_of_satellife = 0, 0, 0, 0, 0
#     for veh in range( len( vehicles)):
#         start_location = vehicles[veh]['startLocationType']
#         if start_location == 'DEPOT': number_of_depot +=1
#         elif start_location == 'HUB': number_of_hub +=1
#         elif start_location == "STATION": number_of_station += 1
#         elif start_location == "CUSTOMER": number_of_customer += 1
#         elif start_location == "SATELLITE": number_of_satellife += 1

#     return { 'Customer': number_of_customer, 'Depot': number_of_depot, 'Station': number_of_station, 'Hub': number_of_hub, 'Satellite': number_of_satellife } 
