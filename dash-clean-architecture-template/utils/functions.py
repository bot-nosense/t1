import random


'''
	model = { 'Customer': 4, 'Depot': 2, 'Station': 3, 'Hub': 44, 'Satellite': 4 } 
	struct_input = { 'Name': [], 'Quantity': [] }
'''
# suy tính tới trường hợp struct nhiều hơn 2 key 
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


def get_minute(time):       # time = '2019-01-01 10:40'
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



















