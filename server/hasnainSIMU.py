import pandas as pd
import math
from utils import (
    is_server_idle,
    find_server_index_with_min_time_left,
)

NUM_OF_RECORDS = 12

def calculate_averages(df_simulation_table, num_of_servers):
    return [
        {
            "name": "Average Service Time",
            "value": df_simulation_table.service_time.mean(),
        },
        {
            "name": "Average Turn Around Time (Ws)",
            "value": df_simulation_table.turn_around_time.mean(),
        },
        {
            "name": "Average Wait Time (Wq)",
            "value": df_simulation_table.wait_time.mean(),
        },
        {
            "name": "Length of system (Ls)",
            "value": math.ceil(
                df_simulation_table.turn_around_time.sum()
                / df_simulation_table.iloc[-1].end_time
            ),
        },
        {
            "name": "Length of queue (Lq)",
            "value": math.ceil(
                df_simulation_table.wait_time.sum()
                / df_simulation_table.iloc[-1].start_time
            ),
        }

    ]

def construct_simulation_table(arrival_data, service_data, num_of_servers):
    servers = [[] for _ in range(num_of_servers)]
    df_simulation_table = pd.DataFrame(
        columns=[
            "arrival_time",
            "service_time",
            "start_time",
            "end_time",
            "turn_around_time",
            "wait_time"
        ]
    )


    for row_index in range(NUM_OF_RECORDS):
        arrival_time = arrival_data[row_index]
        service_time = service_data[row_index]

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
            

        df_simulation_table.loc[row_index, "arrival_time"] = arrival_time
        df_simulation_table.loc[row_index, "service_time"] = service_time
        df_simulation_table.loc[row_index, "start_time"] = start_time
        df_simulation_table.loc[row_index, "end_time"] = end_time
        df_simulation_table.loc[row_index, "turn_around_time"] = end_time - arrival_time
        df_simulation_table.loc[row_index, "wait_time"] = start_time - arrival_time

    averages = calculate_averages(df_simulation_table, num_of_servers)

    return df_simulation_table, servers , averages


if __name__ == "__main__":
    print("#################################################################")
    print("##############  M/ M/ S Queuing Model Simulation  ###############")
    print("#################################################################")

    num_of_servers = int(input("Enter number of servers: "))

    servers = [[] for _ in range(num_of_servers)]

    # Read arrival and service times from Excel file
    df_data = pd.read_excel("data.xlsx")
    arrival_data = df_data["arrival_time"].values[:NUM_OF_RECORDS]
    service_data = df_data["service_time"].values[:NUM_OF_RECORDS]

    # Construct the simulation table
    df_simulation_table, servers , averages = construct_simulation_table(
        arrival_data, service_data, num_of_servers
    )

    print("=================================================================")
    print("Step 01 => Construction of complete Simulation Table :")
    print(df_simulation_table)

    print("=================================================================")
    print("Step 02 => Finding averages and utilization factor :")
    for item in averages:
        print(item["name"], item["value"])


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
        print(f'Rho Value of Server {i+1} = {rho}')

    # Calculate and print the sum of total rho values
    sum_rho = round(sum(total_service_time_of_server) / total_service_time, 3)
    print(f'Total Utilization factor of servers = {sum_rho}')