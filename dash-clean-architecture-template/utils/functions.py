import random


def formatter_2_decimals(x):
	return "{:.2f}".format(x)


# -------------------


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
