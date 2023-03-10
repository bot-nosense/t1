from components.visualization.import_charts import *
from components.seed.input.get_seed_input import *
from utils.functions import *
from utils.constants import *
# from dash import dcc





# bar scatter combine charts
def time_per_cbm(vehicles):

    def data_preprocessing(vehicles, model):
        for veh in range( len(vehicles) ):
            model['load_time'].append( vehicles[veh]['loadTimePerCbm'])
            model['unload_time'].append( vehicles[veh]['unloadTimePerCbm'] )
            model['vehicle_name'].append( vehicles[veh]['vehicleCode'])
        return model


    def create_data_model(vehicles, model):
        model= data_preprocessing(vehicles, model)
        model['title']= "Time per cbm"
        return model


    def add_traces(fig, model):
        fig.add_trace( go.Scatter( x= model['vehicle_name'], y= model['load_time'], name= 'Load time per cbm' ) )
        fig.add_trace( go.Bar( x= model['vehicle_name'], y= model['unload_time'], name= 'Unload time per cbm' ) )


    def draw_model():
        model = { 'load_time': [], 'unload_time': [], 'vehicle_name': [], "title": []  }
        data_model = create_data_model(vehicles, model)
        fig = go.Figure()
        add_traces(fig, data_model)
        fig.update_layout( title= model['title'] )
        return fig

    return draw_model()


# bar scatter combine charts
def time_per_ton(vehicles):

    def data_preprocessing(vehicles, model):
        for veh in range( len(vehicles) ):
            model['Load Time'].append( vehicles[veh]['loadTimePerTon'])
            model['Unload Time'].append( vehicles[veh]['unloadTimePerTon'] )
            model['Vehicle Name'].append( vehicles[veh]['vehicleCode'])
        return model


    def create_data_model(vehicles, model):
        model= data_preprocessing(vehicles, model)
        model['title']= "Time per ton"
        return model


    def add_traces(fig, model):
        fig.add_trace( go.Scatter( x= model['Vehicle Name'], y= model['Load Time'], name= 'Load Time' ) )
        fig.add_trace( go.Bar( x= model['Vehicle Name'], y= model['Unload Time'], name= 'Unload Time' ) )


    def draw_model():
        model = { 'Load Time': [], 'Unload Time': [], 'Vehicle Name': [], "title": [] }
        data_model = create_data_model(vehicles, model)
        fig = go.Figure()
        add_traces(fig, data_model)
        fig.update_layout( title= model['title'] )
        return fig
        
    return draw_model()


def end_location_type_of_vehicles(vehicles):

    def data_preprocessing(vehicles, model): 
        number_of_customer, number_of_depot, number_of_station, number_of_hub, number_of_satellife = 0, 0, 0, 0, 0
        for veh in range( len(vehicles) ):
            end_location = vehicles[veh]['endLocationType']
            if end_location == 'DEPOT': number_of_depot +=1
            elif end_location == 'HUB': number_of_hub +=1
            elif end_location == "STATION": number_of_station += 1
            elif end_location == "CUSTOMER": number_of_customer += 1
            elif end_location == "SATELLITE": number_of_satellife += 1
        location_type =  { 'Customer': number_of_customer, 'Depot': number_of_depot, 'Station': number_of_station, 'Hub': number_of_hub, 'Satellite': number_of_satellife } 

        A = model[list(model.keys())[0]]
        B = model[list(model.keys())[1]]
        for a, b in location_type.items():
            A.append(str(a))
            B.append(str(b))
        return model


    def create_data_model(vehicles, model):
        model = data_preprocessing(vehicles, model)
        model['title'] = "End location type of vehicles"
        return model


    def add_traces(fig, model):
        fig.add_trace( go.Pie(labels=  model['name'] , values=  model['quantity']   ) )                         
        return fig


    def draw_model():
        fig = go.Figure()                                           
        model = { 'name': [], 'quantity': [], "title": [] }                          
        data_model = create_data_model(vehicles, model)          
        add_traces(fig, data_model)    
        fig.update_layout( title= model['title'] )                            
        return fig                  

    return draw_model()


def start_location_type_of_vehicles(vehicles):

    def data_preprocessing(vehicles, model): 
        number_of_customer, number_of_depot, number_of_station, number_of_hub, number_of_satellife = 0, 0, 0, 0, 0
        for veh in range( len(vehicles) ):
            end_location = vehicles[veh]['startLocationType']
            if end_location == 'DEPOT': number_of_depot +=1
            elif end_location == 'HUB': number_of_hub +=1
            elif end_location == "STATION": number_of_station += 1
            elif end_location == "CUSTOMER": number_of_customer += 1
            elif end_location == "SATELLITE": number_of_satellife += 1
        location_type =  { 'Customer': number_of_customer, 'Depot': number_of_depot, 'Station': number_of_station, 'Hub': number_of_hub, 'Satellite': number_of_satellife } 

        A = model[list(model.keys())[0]]
        B = model[list(model.keys())[1]]
        for a, b in location_type.items():
            A.append(str(a))
            B.append(str(b))

        return model


    def create_data_model(vehicles, model):
        model = data_preprocessing(vehicles, model)
        model['title'] = "Start location type of vehicles"
        return model


    def add_traces(fig, model):
        fig.add_trace( go.Pie(labels=  model['name'] , values=  model['quantity']   ) )                         
        return fig


    def draw_model():
        fig = go.Figure()                                           
        model = { 'name': [], 'quantity': [], "title": [] }                          
        data_model = create_data_model(vehicles, model)          
        add_traces(fig, data_model)    
        fig.update_layout( title= model['title'] ) 
        return fig                      

    return draw_model()




