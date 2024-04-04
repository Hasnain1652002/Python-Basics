import pandas as pd

def SJF(df):
    # Sort the DataFrame by arrival time and execution time (SJF)
    df = df.sort_values(by=['arrival_time', 'execution_time'])

    # Initialize variables to keep track of metrics
    start_times = []
    end_times = []
    wait_times = []
    turnaround_times = []
    utilization_times = []
    executed_processes = []  # To keep track of the executed processes

    current_time = 0  # Current time initialized to 0
    remaining_processes = df.copy()  # Create a copy of the DataFrame

    process_info_list = []  # Initialize list to store process information as dictionaries

    while not remaining_processes.empty:
        eligible_processes = remaining_processes[remaining_processes['arrival_time'] <= current_time]
        
        if not eligible_processes.empty:
            # Find the process with the shortest execution time
            shortest_process = eligible_processes.sort_values(by='execution_time').iloc[0]
            start_time = max(current_time, shortest_process['arrival_time'])
            
            start_times.append(start_time)
            execution_time = shortest_process['execution_time']
            
            # Update current time and remove the completed process
            current_time = start_time + execution_time
            end_times.append(current_time)
            wait_times.append(start_time - shortest_process['arrival_time'])
            turnaround_times.append(current_time - shortest_process['arrival_time'])
            utilization_times.append((round(execution_time / (current_time - shortest_process['arrival_time'])*100,2)))
            
            executed_processes.append(shortest_process['process_name'])
            remaining_processes = remaining_processes.drop(shortest_process.name)
            
            # Create a dictionary for process information
            process_info = {
                'id': shortest_process['process_name'],
                'start_time': start_time,
                'end_time': current_time
            }
            
            # Append the process information dictionary to the list
            process_info_list.append(process_info)
        else:
            # No eligible process available, move time forward to the next arrival
            next_arrival = remaining_processes['arrival_time'].min()
            current_time = next_arrival

    # Add the executed_processes list as a new column in the DataFrame
    df['executed_process'] = executed_processes
    df['start_time'] = start_times
    df['end_time'] = end_times
    df['wait_time'] = wait_times
    df['turnaround_time'] = turnaround_times
    df['utilization'] = utilization_times

    ut_sjf = df['utilization'].mean()
    wt_sjf = df['wait_time'].mean()
    tt_sjf = df['turnaround_time'].mean()

    # Return both the modified DataFrame and the list of process information
    return df, process_info_list, wt_sjf, tt_sjf , ut_sjf

# # Example usage:
# data = {'process_name': ['P1', 'P2', 'P3', 'P4', 'P5'],
#         'arrival_time': [0, 1, 2, 3, 4],
#         'execution_time': [10, 1, 2, 1, 5]}

# df = pd.DataFrame(data)
# result_df, process_info_list = SJF(df)
# print("Modified DataFrame:")
# print(result_df)
# print("\nList of Process Information:")
# print(process_info_list)
