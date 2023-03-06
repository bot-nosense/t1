import collections

from components.visualization.import_charts import *
from components.seed.input.get_seed_input import *
from utils.functions import *
from utils.constants import *



# tỷ lệ loại hàng trong mỗi item, được dùng khi có callback
# def get_item_type_by_vehicle():

#     def create_data_model(requests, model):
        
#         temp_data = []
#         for index in range( len(requests)):
#             request_index = requests[index]['items']
#             for item in range( len(request_index) ):
#                 temp_data.append(request_index[item]['iType']['typeOfItemByVehicle'])
#         data = collections.Counter(temp_data)

#         A = model[list(model.keys())[0]]
#         B = model[list(model.keys())[1]]
#         for a, b in data.items():
#             A.append(str(a))
#             B.append(str(b))

#         return model        

#     def draw_model():
#         model = {  'Name': [], 'Quantity': []  }
#         data_model = create_data_model(requests, model)
#         data = go.Pie(labels=data_model['Name'], values=data_model['Quantity'])
#         pie_chart = Pie_Charts(data)
#         return pie_chart.render_go()

#     return draw_model()


def get_item_type_by_vehicle():


    def data_preprocessing(requests, model): 
        temp_data = []
        for index in range( len(requests)):
            request_index = requests[index]['items']
            for item in range( len(request_index) ):
                temp_data.append(request_index[item]['iType']['typeOfItemByVehicle'])
        data = collections.Counter(temp_data)

        A = model[list(model.keys())[0]]
        B = model[list(model.keys())[1]]
        for a, b in data.items():
            A.append(str(a))
            B.append(str(b))

        return model


    def create_data_model(requests, model):
        model = data_preprocessing(requests, model)
        model['title'] = "Get item type by vehicle"
        return model


    def add_traces(fig, model):
        fig.add_trace( go.Pie(labels=  model['name']  , values=  model['quantity']   ) )   
        return fig


    def draw_model():
        fig = go.Figure()                                           
        model = { 'name': [], 'quantity': [], "title": []  }                          
        data_model = create_data_model(requests, model)          
        add_traces(fig, data_model)
        fig.update_layout( title= model['title'] )
        pie_chart = Pie_Charts(fig= fig)                
        return pie_chart.render_go_trace() 

    return draw_model()



# đơn hàng và lượng hàng trong đơn đó
def count_items_by_request():


    def data_preprocessing(object_svrp, model):
        model['x'].append([ object_svrp[index]['orderCode'] for index in range( len(object_svrp) ) ])
        model['y'].append( [ len( object_svrp[index]['items'] ) for index in range( len( object_svrp ) ) ])
        return model
    

    def create_data_model(object_svrp, model):
        model = data_preprocessing(object_svrp, model)
        model['title'] = 'Count items by request'
        return model


    def add_traces(fig, model):
        for x_index in range( len(model['x'][0]) ):
            fig.add_trace(go.Bar(x= [ model['x'][0][x_index] ], y= [ model['y'][0][x_index] ]))
        return fig


    def draw_model():
        fig = go.Figure()
        model = { 'title': [], 'x': [], 'y': [], 'width': [], 'marker_color': [], 'name': []}
        data_model = create_data_model(requests, model)
        add_traces(fig, data_model)
        fig.update_layout( title= model['title'] )
        bar_chart = Bar_Charts(fig= fig)
        return bar_chart.render_go_trace()
    return draw_model()


# tỷ lệ điểm bắt đầu của các đơn hàng
def pickup_location_for_request():


    def data_preprocessing(requests, model):

        def get_location_type(locations, location_code):
            return [ locations[location_index]['lTypes'][0] for location_index in range( len(locations) ) if locations[location_index]['locationCode'] == location_code ]

        def create_temp_model():
            return [ get_location_type( locations, requests[rq_index]['pickupLocationCode'][0] )[0] for rq_index in range( len(requests) ) ]

        temp_model = collections.Counter(create_temp_model())
        model['labels'].append(temp_model.most_common(1)[0][0])
        model['values'].append(temp_model.most_common(1)[0][1])
        return model
    

    def create_data_model(object_svrp, model):
        model = data_preprocessing(object_svrp, model)
        model['title'] = "Pickup location for request"
        return model
    

    def add_traces(fig, model):
        fig.add_trace( go.Pie(labels= model['labels'], values= model['values']) )
        return fig


    def draw_model():
        fig = go.Figure()
        model = { 'title': [], 'labels': [], 'values': [], 'width': [], 'name': []}
        data_model = create_data_model(requests, model)
        add_traces(fig, data_model)
        fig.update_layout( title= model['title'] )
        pie_chart = Pie_Charts(fig= fig)
        return pie_chart.render_go_trace()

    return draw_model()


# tỷ lệ điểm kết thúc của các đơn hàng
def delivery_location_for_request():

    def data_preprocessing(requests, model):

        def get_location_type(locations, location_code):
            return [ locations[location_index]['lTypes'][0] for location_index in range( len(locations) ) if locations[location_index]['locationCode'] == location_code ]

        def create_temp_model():
            return [ get_location_type( locations, requests[rq_index]['deliveryLocationCode'][0] )[0] for rq_index in range( len(requests) ) ]

        temp_model = collections.Counter(create_temp_model())
        model['labels'].append(temp_model.most_common(1)[0][0])
        model['values'].append(temp_model.most_common(1)[0][1])
        return model
    

    def create_data_model(object_svrp, model):
        model = data_preprocessing(object_svrp, model)
        model['title'] = "Delivery location for request"
        return model


    def add_traces(fig, model):
        fig.add_trace( go.Pie(labels= model['labels'], values= model['values']) )
        return fig


    def draw_model():
        fig = go.Figure()
        model = { 'title': [], 'labels': [], 'values': [], 'width': [], 'name': []}
        data_model = create_data_model(requests, model)
        add_traces(fig, data_model)
        fig.update_layout( title= model['title'] )
        pie_chart = Pie_Charts(fig= fig)
        return pie_chart.render_go_trace()
        
    return draw_model()


# weight của từng item và weight của đơn hàng, dùng callback, yêu cầu chọn đơn hàng trước
def capacity_for_request():

    # đoạn này cần tối ưu truy vấn vòng lặp
    def data_preprocessing(requests, model, request_index):
        model['item_name'].append( [ requests[request_index]['items'][item_index]['itemCode'] for item_index in range( len( requests[request_index]['items'] ) ) ] )
        model['cbm_item'].append( [ requests[request_index]['items'][item_index]['cbm'] for item_index in range( len( requests[request_index]['items'] ) ) ] )
        model['weight_item'].append( [ requests[request_index]['items'][item_index]['weight'] for item_index in range( len( requests[request_index]['items'] ) ) ] )
        model['quantity_item'].append( [ requests[request_index]['items'][item_index]['quantity'] for item_index in range( len( requests[request_index]['items'] ) ) ] )
        return model


    def create_data_model(requests, model, request_index):
        model = data_preprocessing(requests, model, request_index)
        model['title'] = "Capacity for request"
        return model


    def add_traces(fig, model):
        fig.add_trace( go.Scatter( x= model['item_name'][0], y= model['quantity_item'][0], name= 'quantity' ) )
        fig.add_trace( go.Bar( x= model['item_name'][0], y= model['weight_item'][0], name= 'weight' ) )
        fig.add_trace( go.Bar( x= model['item_name'][0], y= model['cbm_item'][0], name= 'cbm' ) )
        return fig


    def draw_model():
        fig = go.Figure()
        model = { 'title': [], 'item_name': [], 'cbm_item': [], 'weight_item': [], 'quantity_item': [], 'width': [], 'name': [] }
        request_index = 0
        data_model = create_data_model(requests, model, request_index)
        add_traces(fig, data_model)
        fig.update_layout( title= model['title'] )
        combine_chart = BarScatterCombine(fig = fig)
        return combine_chart.render_go_trace()

    return draw_model()
    