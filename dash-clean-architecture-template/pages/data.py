'''
    step 1: lấy data từ file json
    step 2: install package create seed data input SVRP v3
'''

import json

with open("pages\seed.json", "r") as f:
    seed_data_input_svrp_v3 = json.load(f)

locations = seed_data_input_svrp_v3["locations"]
vehicles = seed_data_input_svrp_v3["vehicles"]
customers = seed_data_input_svrp_v3["customers"]
matrixConfig = seed_data_input_svrp_v3["matrixConfig"]
depots = seed_data_input_svrp_v3["depots"]
distances = seed_data_input_svrp_v3["distances"]
requests = seed_data_input_svrp_v3["requests"]


