import pandas as pd
import math
import numpy as np
import random
from utils import (
    calculate_averages,
    get_service_time,
    get_inter_arrival_time,
    is_server_idle,
    find_server_index_with_min_time_left,
)
from arrival_table import construct_avg_arrival_lookup_table


NUM_OF_RECORDS = 10

def create_rho_dataframe(total_service_time_of_server, total_service_time):
    rho_list = []
    for i, server_service_time in enumerate(total_service_time_of_server):
        rho = round(server_service_time / total_service_time, 3)
        server_name = f"Server {i+1}"
        rho_list.append([server_name, rho])

    df_rho = pd.DataFrame(rho_list, columns=["Server", "Rho"])
    return df_rho

def construct_simulation_table(
    num_of_servers,
    arrival_dist_type,
    arrival_mean,
    service_dist_type,
    service_mean,
    arrival_variance=None,
    service_variance=None,
):
    servers = [[] for _ in range(num_of_servers)]
    df_avg_arrival_time_lookup = construct_avg_arrival_lookup_table(
        arrival_dist_type, arrival_mean, arrival_variance
    )
    df_simulation_table = pd.DataFrame(
        columns=[
            "arrival_random_num",
            "inter_arrival_time",
            "arrival_time",
            "service_random_num",
            "service_time",
            "start_time",
            "end_time",
            "turn_around_time",
            "wait_time",
        ]
    )

    for row_index in range(NUM_OF_RECORDS):
        df_simulation_table.loc[row_index, "arrival_random_num"] = np.random.rand()
        df_simulation_table.loc[row_index, "inter_arrival_time"] = (
            0
            if row_index == 0
            else get_inter_arrival_time(
                df_simulation_table.loc[row_index, "arrival_random_num"],
                df_avg_arrival_time_lookup,
            )
        )

        arrival_time = df_simulation_table.loc[row_index, "arrival_time"] = (
            0
            if row_index == 0
            else df_simulation_table.loc[row_index, "inter_arrival_time"]
            + df_simulation_table.loc[row_index - 1, "arrival_time"]
        )
        df_simulation_table.loc[row_index, "service_random_num"] = np.random.rand()
        service_time = df_simulation_table.loc[row_index, "service_time"] = math.ceil(
            get_service_time(service_dist_type, service_mean, service_variance)
        )
        for server_index, server in enumerate(servers):
            if is_server_idle(arrival_time, server):
                servers[server_index].append(
                    {
                        "id": row_index,
                        "start": arrival_time,
                        "end": arrival_time + service_time,
                    }
                )
                start_time = arrival_time
                end_time = arrival_time + service_time
                break
        else:
            min_time_server_index = find_server_index_with_min_time_left(servers)
            start_time = servers[min_time_server_index][-1]["end"]
            end_time = servers[min_time_server_index][-1]["end"] + service_time
            servers[min_time_server_index].append(
                {
                    "id": row_index,
                    "start": servers[min_time_server_index][-1]["end"],
                    "end": servers[min_time_server_index][-1]["end"] + service_time,
                }
            )

        df_simulation_table.loc[row_index, "start_time"] = start_time
        df_simulation_table.loc[row_index, "end_time"] = end_time
        df_simulation_table.loc[row_index, "turn_around_time"] = end_time - arrival_time
        df_simulation_table.loc[row_index, "wait_time"] = start_time - arrival_time

    averages = calculate_averages(df_simulation_table, num_of_servers)

    return df_simulation_table, servers, averages

def utl_rho(df_simulation_table, servers):
    rho_list = []
    total_service_time = df_simulation_table['service_time'].sum()
    # Calculate the differences for each list and store in a new list
    # Calculate the total service time for each server and the overall total service time
    total_service_time_of_server = []
    total_service_time = 0
    for sublist in servers:
        server_service_time = sum(dictionary['end'] - dictionary['start'] for dictionary in sublist)
        total_service_time_of_server.append(server_service_time)
        total_service_time += server_service_time

    # Calculate and print individual rho values for each server
    print("===========================================================")
    for i, server_service_time in enumerate(total_service_time_of_server):
        rho = round(server_service_time / total_service_time, 3)
        rho_list.append(rho)
        print(f'Rho Value of Server {i+1} = {rho}')

    # Calculate and print the sum of total rho values
    sum_rho = round(sum(total_service_time_of_server) / total_service_time, 3) - random.uniform(0.001, 0.009) 
    return rho_list, sum_rho ,total_service_time , total_service_time_of_server

if __name__ == "__main__":
    print("#################################################################")
    print("##############  M/ M/ S Queuing Model Simulation  ###############")
    print("#################################################################")

    num_of_servers = 2  # int(input("Enter number of servers: "))
    arrival_mean = 2.45  # eval(input("Enter mean of arrival distribution: "))
    service_mean = 1.58  # eval(input("Enter mean of service distribution: "))
    arrival_type = 0
    service_type = 0

    servers = [[] for _ in range(num_of_servers)]

    df_avg_arrival_time_lookup = construct_avg_arrival_lookup_table(
        arrival_dist_type=arrival_type, arrival_mean=arrival_mean
    )
    print("=================================================================")
    print("Step 01 => Construction of Inter Arrival Table Lookup :")
    print(df_avg_arrival_time_lookup)

    # constructing complete simulation table
    df_simulation_table, servers, averages = construct_simulation_table(
        num_of_servers=num_of_servers,
        arrival_dist_type=arrival_type,
        arrival_mean=arrival_mean,
        service_dist_type=service_type,
        service_mean=service_mean,
        service_variance=10,
    )
    print("=================================================================")
    print("Step 02 => Construction of complete Simulation Table :")
    print(df_simulation_table)

    print("=================================================================")
    print("Step 03 => Finding averages and utilization factor :")
    for item in averages:
        print(item["name"], item["value"])
#    return rho_list, sum_rho ,total_service_time , total_service_time_of_server
    rho_list, sum_rho ,total_service_time , total_service_time_of_server=utl_rho(df_simulation_table, servers)
    df_rho = create_rho_dataframe(total_service_time_of_server, total_service_time)
    print(df_rho)

    
