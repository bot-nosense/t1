
def formatter_2_decimals(x):
	return "{:.2f}".format(x)


# -------------------

def create_data_model(model_name, value_list):
	for key, value in value_list.items():
		for k, v in model_name.items():

			model_name[k].append(key)
			model_name[k].append(value)

	return model_name

# def get_data_model(data_table):

# 	location_type_list = get_location_type_list(locations)
# 	for key, value in location_type_list.items():
# 		for k, v in data_table.items():

# 			data_table[k].append(key)
# 			data_table[k].append(value)
