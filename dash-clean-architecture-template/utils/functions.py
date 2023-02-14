
def formatter_2_decimals(x):
	return "{:.2f}".format(x)


# -------------------

def create_data_model(model, value_list):
	for key, value in value_list.items():
		for k, v in model.items():

			model[k].append(key)
			model[k].append(value)

	return model

