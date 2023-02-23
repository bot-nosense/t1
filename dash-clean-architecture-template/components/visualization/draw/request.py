import collections

from components.visualization.import_charts import *
from components.seed.input.get_seed_input import *
from utils.functions import *
from utils.constants import *

def get_item_type_by_vehicle():

    def create_data_model(requests, model):
        
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

    def draw_model():
        model = {  'Name': [], 'Quantity': []  }
        data_model = create_data_model(requests, model)
        data = go.Pie(labels=data_model['Name'], values=data_model['Quantity'])
        pie_chart = Pie_Charts(data)
        return pie_chart.render_go()

    return draw_model()