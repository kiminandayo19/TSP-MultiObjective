import numpy as np
import sympy as sym
import pandas as pd
import json
from IPython.display import display
from python_tsp.exact import solve_tsp_dynamic_programming

# All we need to do is:
# 1. Create func to generate the cost matrix
# 2. Create function to calculate time
# 3. Create function to do the main

# Required library to install : python-tsp, numpy, sympy, and pandas
# How to install : pip install python-tsp, pip install numpy, pip install sympy, pip install pandas
# Do the installation first then you can run this python file

def generate_cost_matrix(route_data, profit):
    """This function will generate the cost matrix
       for each of the iteration to solve the TSP-MPUT
       problem and returning the cost matrix and each 
       possible choice route"""
    # The idea of this function is
    # 1. We create some empty matrix shape n_city x n_city
    # 2. The matrix input which is route data is a matrix 
    #    with dictionary data type
    # 3. We take the key and value for each entry in the route_data
    #    then we count each P * t + S (1)-> find the index of the minimum
    #    entry and use the index to find the minimum val of (1) and the
    #    the corresponding dictionary key
    # 4. Return the cost matrix and the corresponding index
    row_cost_matrix = []
    for i in range(route_data.shape[0]):
        col_cost_matrix = []
        list_key_assoc = []
        for j in range(route_data.shape[1]):
            min_cost = []       # This is temporary list to find the minimum cost for each s and t
            assoc_key = []      # This is temporary list to find the minimum index correspond to each s and t
            for key, val in route_data[i, j].items():
                entri = ((profit * val[1]) + val[0])    # Here we count the (1)
                min_cost.append(entri)
                assoc_key.append(key)
            # Find the idx of the min val of min_cost
            min_idx = np.argmin(min_cost)               # Here we find the minimum index
            col_cost_matrix.append(min_cost[min_idx])   # And only choose the minimum of (1)
            list_key_assoc.append(assoc_key[min_idx])   # Also the corresonding choice of route
        row_cost_matrix.append(col_cost_matrix)
    row_cost_matrix = np.array(row_cost_matrix)
    list_key_assoc = list_key_assoc

    return row_cost_matrix, list_key_assoc

def calculate_total_time(route_data, route, assoc_key):
    """This function is used to calculate the total time needed
       to cross all the route. This function will return the
       total time needed"""
    # The idea of this function is to sum up all the time use
    # That correspondence to the route choosen
    total_time = 0
    for i in range(len(route) - 1):
        k = assoc_key[i]    # Here we choose the correspondence route which have the minimum cost
        total_time += route_data[route[i], route[i+1]][k][1]    # Here we sum all the choosen time
    
    return total_time

def main():
    """This function is the main function to do the task which
       is to solve the TSP-MPUT using the algorithm that we have 
       already"""
    # Here's the data input
    # Note that:
    # 1. "Ngaglik": [{i:(si, ti), j:(sj, tj)}]
    #    i and j means the route we need to choose so our travel cost is minimum
    #    si, ti means the corresponding cost and time with respect to i
    # Here's we have 5 city with 2 route that connected each city to another city
    route_data = {
    "ngaglik": [{1:(0, 0), 2:(0, 0)},
                {1:(178000, 45), 2:(271000, 38)},
                {1:(353000, 105), 2:(487000, 94)},
                {1:(323000, 88), 2:(451000, 83)},
                {1:(172000, 48), 2:(263000, 38)}
               ],
    "kasihan": [{1:(178000, 45), 2:(271000, 38)},
                {1:(0, 0), 2:(0, 0)},
                {1:(285000, 70), 2:(403000, 65)},
                {1:(307000, 100), 2:(430000, 80)},
                {1:(136000, 24), 2:(207000, 21)}
               ],
    "glagah": [{1:(353000, 105), 2:(487000, 94)},
               {1:(285000, 70), 2:(403000, 65)},
               {1:(0, 0), 2:(0, 0)},
               {1:(434000, 144), 2:(588000, 116)},
               {1:(324000, 91), 2:(451000, 80)}
              ],
    "wonosari": [{1:(323000, 88), 2:(451000, 83)},
                 {1:(307000, 100), 2:(430000, 80)},
                 {1:(434000, 144), 2:(588000, 116)},
                 {1:(0, 0), 2:(0, 0)},
                 {1:(263000, 70), 2:(375000, 64)}
                ],
    "kotagede": [{1:(172000, 48), 2:(263000, 38)},
                 {1:(136000, 24), 2:(207000, 21)},
                 {1:(324000, 91), 2:(451000, 80)},
                 {1:(263000, 70), 2:(375000, 64)},
                 {1:(0, 0), 2:(0, 0)}
                ]
    }
    route_data_matrix = pd.DataFrame(route_data).to_numpy()     # Here's we convert the dictionary to numpy array

    p_in = 0                # Here's the initial value of p_in
    list_assoc_key = []     # Here's the empty list to store each assoc choosen route
    list_pout = []          # .... to store each p_out in each iteration
    list_total_cost = []    # .... to store each total cost in each iteration
    list_total_time = []    # .... to cost the total time
    list_cost_matrix = []   # .... to store each cost matrix in each iteration
    list_tour = []          # .... to store each tour the traveller do
    rev = 2575000
    total_time = 0
    max_iter = 1000
    for i in range(max_iter):       # Here we began the loop till p_out <= p_in
        cost_matrix, assoc_key = generate_cost_matrix(route_data_matrix, p_in)  # Here we generate cost_matrix and associated min idx
        route, total_cost = solve_tsp_dynamic_programming(cost_matrix)          # Here we solve the tsp using dynamic programming and get the minimum route and the total cost
        route = route + [0]     # This make sure the traveller will back to the first city
        total_time = calculate_total_time(route_data_matrix, route, assoc_key)  # Here we get the total time of the travel

        p_out = ((rev - total_cost) / total_time)       # Here we count the p_out
        list_cost_matrix.append(cost_matrix)
        list_total_cost.append(total_cost)
        list_total_time.append(total_time)
        list_pout.append(p_out)
        list_tour.append(route)
        list_assoc_key.append(assoc_key)
        # If p_out > p_in then update the p_in
        if p_out > p_in:
            p_in = p_out
        # Else if the p_out <= p_in then stop the iteration
        elif p_out <= p_in:
            break

    for j in range(len(list_pout)):
        print(f"Iterasi ke-{j+1}")
        print(f"Diperoleh p_out: {list_pout[j]}")
        print("Cost matrix:")
        display(sym.Matrix(list_cost_matrix[j]))
        print(f"Dengan rute: {list_tour[j]}")
        print(f"Pilihan jalur yang dilalui : {list_assoc_key[j]}")
        print(f"Total cost: {list_total_cost[j]}")
        print(f"Total waktu: {list_total_time[j]}")
        print("<========================================>")

    # Save the path to json file
    data_jarak = {"list rute": list_tour[-1], "Jalur yang dipilih": list_assoc_key[-1], "Urutan Kota": {}}
    data_kota = {0:"Ngaglik", 1:"Kasihan", 2:"Glagah", 3:"Wonosari", 4:"Kotagede"}
    for i in list_tour[-1]:
        data_jarak["Urutan Kota"][data_kota[i]] = ""
        
    json_obj = json.dumps(data_jarak, indent = 4)
    # Writing to tsp.json
    with open("tsp.json", "w") as outfile:
        outfile.write(json_obj)


if __name__ == "__main__":
    main()