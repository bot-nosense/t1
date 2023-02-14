
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

