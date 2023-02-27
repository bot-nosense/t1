
from components.visualization.import_charts import *
from components.seed.input.get_seed_input import *
from utils.functions import *
from utils.constants import *


# # pie chart
# def composition_of_locations():

#     def get_location_type_list(locations):

#         number_of_customer, number_of_depot, number_of_station, number_of_hub, number_of_satellife = 0, 0, 0, 0, 0

#         for i in range( len(locations) ):

#             location_type = ( locations[i]['lTypes'] )[0]
#             match location_type:
#                 case "HUB": number_of_hub += 1
#                 case "DEPOT": number_of_depot += 1
#                 case "STATION": number_of_station += 1
#                 case "CUSTOMER": number_of_customer += 1
#                 case "SATELLITE": number_of_satellife += 1
        
#         return { 'Customer': number_of_customer, 'Depot': number_of_depot, 'Station': number_of_station, 'Hub': number_of_hub, 'Satellite': number_of_satellife } 

#     def create_model(locations, struct_input):

#         location_type_list = get_location_type_list(locations)
#         create_data_model(location_type_list, struct_input)
#         df = pd.DataFrame(struct_input)

#         return df

#     struct_input = { 'Name': [], 'Quantity': [] }
#     model = create_model( locations, struct_input )
#     data = go.Pie(labels=model.Name, values=model.Quantity)
#     pie_chart = Pie_Charts(data)

#     return pie_chart.render_go()


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
        print('model', model)
        return model

    def create_data_model(locations, model):
        model = data_preprocessing(locations, model)
        model['title'] = "Composition of location"
        return model

    def add_traces(fig, model):
        fig.add_trace( go.Pie(labels=  model['location_type']  , values=  model['quantity']   ) )                                                    
        return fig

    def draw_model():
        fig = go.Figure()                                           
        model = { 'location_type': [], 'quantity': [], "title": [], 'color':[] }                          
        data_model = create_data_model(locations, model)          
        add_traces(fig, data_model)
        fig.update_layout( title={ 'text': model['title'], 'y':0.9, 'x':0.5, 'xanchor': 'right', 'yanchor': 'top'} )
        pie_chart = Pie_Charts(fig = fig)
        return pie_chart.render_go_trace()                      

    return draw_model()



# map chart
def point_on_the_map():

    model = { 'Name': [], # loaction type
        'Latitude': [],
        'Longitude': [],
        'Color': []
    }

    def create_data_model(locations, model):
        for i in range(len(locations)):
            model['Name'].append(locations[i]['lTypes'][0])
            model['Latitude'].append(locations[i]['lat'])
            model['Longitude'].append(locations[i]['lng'])
            model['Color'].append(set_color_scheme_location_type(locations[i]['lTypes'][0]))

        df = pd.DataFrame(model)
        return df

    data_model = create_data_model( locations, model )
    fig = go.Figure()

    for i in range(data_model.shape[0]):

        fig.add_trace(go.Scattermapbox(
            lat=[data_model['Latitude'][i]],
            lon=[data_model['Longitude'][i]],
            mode='markers+text',
            marker=dict(
                size=10,
                color = data_model['Color'][i]
            ),
            text=data_model['Name'][i],
            # hoverinfo='text',
            textposition='top right',
            textfont= dict(size=12, color='black'),
        ))

    fig.update_layout(
        # title='Nuclear Waste Sites on Campus',
        # autosize=True,
        # hovermode='closest',
        # showlegend=False,
        margin=margin_default,
        mapbox=dict(
            accesstoken=mapbox_access_token,
            # bearing=0,
            center=locations_default['Ha Noi'],
            # pitch=0,
            zoom=7,
            style='light'
        ),
    )

    map_chart = Scatter_Plots_on_Mapbox(fig= fig)
    return map_chart.render_go_trace()



def chart_name():

    def data_preprocessing(locations, model): 
        return model

    def create_data_model(locations, model):
        model = data_preprocessing(locations, model)
        return model

    def add_traces(fig, model):
        fig.add_trace()                                             
        return fig

    def draw_model():
        fig = go.Figure()                                           
        model = { 'location_type': [], 'latitude': [], 'longitude': [], 'color': []  }                          
        data_model = create_data_model(locations, model)          
        add_traces(fig, data_model)
        # fig.update_layout()
        # fig.update_traces()                                         
        combine_chart = BarScatterCombine(fig = fig)                
        return combine_chart.render_go_trace()                      

    return draw_model()