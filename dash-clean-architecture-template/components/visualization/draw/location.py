
from components.visualization.import_charts import *
from components.seed.input.get_seed_input import *
from utils.functions import *
from utils.constants import *


def composition_of_locations():

    def data_preprocessing(locations, model): 

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
        A = model[list(model.keys())[0]]
        B = model[list(model.keys())[1]]
        for a, b in location_type_list.items():
            A.append(str(a))
            B.append(str(b))
        # print('model', model)
        return model

    def create_data_model(locations, model):
        model = data_preprocessing(locations, model)
        model['title'] = "Composition of location"
        return model

    def add_traces(fig, model):
        fig.add_trace( go.Pie(labels=  model['location_type']  , values=  model['quantity'] ) )                                                    
        return fig

    def draw_model():
        fig = go.Figure()                                           
        model = { 'location_type': [], 'quantity': [], "title": [], 'color':[] }                          
        data_model = create_data_model(locations, model)          
        add_traces(fig, data_model)
        fig.update_layout( title= model['title'] )
        pie_chart = Pie_Charts(fig = fig)
        return pie_chart.render_go_trace()                      

    return draw_model()



def point_on_the_map():

    def data_preprocessing(locations, model): 
        for i in range(len(locations)):
            model['location_type'].append(locations[i]['lTypes'][0])
            model['latitude'].append(locations[i]['lat'])
            model['longitude'].append(locations[i]['lng'])
            model['color'].append(set_color_scheme_location_type(locations[i]['lTypes'][0]))
        return model

    def create_data_model(locations, model):
        model = data_preprocessing(locations, model)
        model['title'] = "Composition of location with mapbox"
        return model

    def add_traces(fig, model):
        for i in range(len(model['location_type'])):
            fig.add_trace(go.Scattermapbox( lat=[model['latitude'][i]], lon=[model['longitude'][i]], mode='markers+text',
                marker=dict( size=10, color = model['color'][i] ), text=model['location_type'][i],
                textposition='top right', textfont= dict(size=12, color='black')
            ))                                           
        return fig 

    def draw_model():
        fig = go.Figure()                                           
        model = { 'location_type': [], 'latitude': [], 'longitude': [], 'color': [], "title": []  }                          
        data_model = create_data_model(locations, model)          
        add_traces(fig, data_model)
        fig.update_layout( 
            title= model['title'],  # add title nhưng không chạy 
            autosize=True,
            hovermode='closest',
            margin=margin_default,
            mapbox=dict( accesstoken=mapbox_access_token, center=locations_default['Ha Noi'], zoom=7, style='light' ), )                                      
        combine_chart = BarScatterCombine(fig = fig)                
        return combine_chart.render_go_trace()                      

    return draw_model()