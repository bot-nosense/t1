
# from .common import *
from .import_charts import *
# from .import_charts import *
from components.seed.input.get_seed_input import *
from utils.functions import *
from utils.constants import *


# pie chart
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
    data = go.Pie(labels=model.Name, values=model.Quantity)
    pie_chart = Pie_Charts(data)

    return pie_chart.render_go()


def random_color():
    return "#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])


# map chart
def point_on_the_map():

    def set_color_scheme(location_type):
        match location_type:
            case "HUB": return 'green'
            case "DEPOT": return'red'
            case "STATION": return 'blue'
            case "CUSTOMER": return 'orange'
            case "SATELLITE": return 'purple'

    # # def get_color_scheme(lat, long):
    # #     return 1


    model = {
        'Name': [], # loaction type
        'Latitude': [],
        'Longitude': [],
        'Color': []
    }

    def create_data_model(locations, model):
        for i in range(len(locations)):
            model['Name'].append(locations[i]['lTypes'][0])
            model['Latitude'].append(locations[i]['lat'])
            model['Longitude'].append(locations[i]['lng'])
            model['Color'].append(set_color_scheme(locations[i]['lTypes'][0]))

        df = pd.DataFrame(model)
        return df

    data_model = create_data_model( locations, model )

    # data = go.Scattermapbox(
    #     lat = list(data_model['Latitude']),
    #     lon = list(data_model['Longitude']),
    #     mode='markers+text',
    #     marker=go.scattermapbox.Marker(
    #         color=list(data_model['Color']),
    #         size=9
    #     ),
    #     textposition='top right',
    #     textfont= dict(size=12, color='black'),
    #     text=[data_model['Name'][i] for i in range(data_model.shape[0])]                                                                       
    # )

    # layout = dict(
    #     margin=margin_default,
    #     mapbox=dict(
    #         accesstoken=mapbox_access_token,
    #         center=locations_default['Ha Noi'],
    #         style='light',
    #         zoom = 7 )
    # )

    

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


