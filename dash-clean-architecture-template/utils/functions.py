from components.seed.input.get_seed_input import *

import random
import dash_bootstrap_components as dbc



'''
	model = { 'Customer': 4, 'Depot': 2, 'Station': 3, 'Hub': 44, 'Satellite': 4 } 
	struct_input = { 'Name': [], 'Quantity': [] }
'''
# suy tính tới trường hợp struct nhiều hơn 2 key, lược bỏ trong lần tối ưu tới
def create_data_model(model, struct):
    A = struct[list(struct.keys())[0]]
    B = struct[list(struct.keys())[1]]
    for a, b in model.items():
        A.append(str(a))
        B.append(str(b))

    return model


def random_color():
    return "#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])


def set_color_scheme_location_type(location_type):
    match location_type:
        case "HUB": return 'green'
        case "DEPOT": return'red'
        case "STATION": return 'blue'
        case "CUSTOMER": return 'orange'
        case "SATELLITE": return 'purple'



'''     covert time to minutes
    - input: time in string format - HH:MM:SS
    - output: time in minutes - HH * 60 + MM
'''
def get_minute(time):       
    minute = time.split()[1]
    split_time = minute.split(':')
    result = int(split_time[0]) * 60 + int(split_time[1])
    return result



'''     start and end time of 1 day
    - input: '2019-01-01 40:00'
    - output: [ '2019-01-01 00:00', '2019-01-02 24:00' ]
'''
def create_limited_time(working_time):
    return [working_time.split()[0] + ' 00:00:00', working_time.split()[0] + ' 24:00:00']   



'''     object operating time
    - input: object_svrp
    - output: [ [ start_day_time, start_working_time, start_break_time, end_break_time, end_working_time, end_day_time ] ]
'''
def object_operating_time(object_svrp):
    result = []
    time_default = create_limited_time(object_svrp[0]['workingTime']['start'])

    for index in range( len(object_svrp) ):
        working_time = object_svrp[index]['workingTime']
        break_time = object_svrp[index]['breakTimes'][0]
        result.append([time_default[0], working_time['start'], break_time['start'], break_time['end'], working_time['end'], time_default[1]])
    return result



# create element of sidebar 
def render_sidebar(model):
    return [ dbc.NavLink(model[0][index], href= model[1][index], active=model[2][index]) for index in range(len(model[0])) ]



def get_object_type(constraint):
    if constraint == 'VV': return 'vehicleType'
    if constraint == 'CV': return 'itemType'
    if constraint == 'CC': return 'customerType'



'''    
    - input: constraint_name - 'typeOfVehicleToItemRule'
    - output: constraint_value - ['XE LANH', 'XE DONG']
'''
def get_value_in_constraint(type_value):

    for config_index in matrix_config: 

        if matrix_config[config_index]:

            contraints_list = list( matrix_config[config_index].keys() )
            for constraint_index in contraints_list :      
                
                if config_index == 'CV':
                    
                    obj_type_c = obj_type = matrix_config[config_index][constraint_index]['referenceType']['itemType']
                    obj_type_v = obj_type = matrix_config[config_index][constraint_index]['referenceType']['vehicleType']
                    value_list = matrix_config[config_index][constraint_index]['matrix']

                    if obj_type_c == type_value: return list( set( [ value['typeOfItem'] for value in value_list ] ) )
                    elif obj_type_v == type_value: return list( set( [ value['typeOfVehicle'] for value in value_list ] ) )

                elif config_index == 'CC':

                    obj_type = matrix_config[config_index][constraint_index]['referenceType'][ get_object_type(config_index) ]
                    value_list = matrix_config[config_index][constraint_index]['matrix']
                    if obj_type == type_value: return list( set( [ value['typeOfCustomer'] for value in value_list ] ) )

                else:

                    obj_type = matrix_config[config_index][constraint_index]['referenceType'][ get_object_type(config_index) ]
                    value_list = matrix_config[config_index][constraint_index]['matrix']
                    if obj_type == type_value: return list( set( [ value['typeOfVehicle'] for value in value_list ] ) )



# kiem tra xem vehicle do co constraint dang xet khon
# viet lai, hien tai chwa dung towi
# dung trong callback, kiem tra xem constraint_name co ton tai trong object_svrp khong 
'''
    - input: vehicle, vehicle_type
    - output: boolean
'''
def validate_vehicle_type(vehicle, type_list):
    if vehicle['vType'][type_list]: return True
    return False










