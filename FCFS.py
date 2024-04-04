import pandas as pd

color = {'Process 1':'#CAC1E8',
'Process 2':'#EACCEA',
'Process 3':"#ABCDEF",
'Process 4':'#FBCB9C',
'Process 5':'#CDEBCC',
'Process 6':'#DFC0E0',
'Process 7':'#9EDF96',
'Process 8':'#B6E6BD',
'Process 9':'#F59A8E',
'Process 10':'#FFC48C'}

def FCFS(df):
    # Sort the DataFrame by arrival time to simulate FCFS scheduling
    df = df.sort_values(by=['arrival_time'])

    # Initialize variables to keep track of metrics
    start_times = []
    end_times = []
    wait_times = []
    turnaround_times = []
    utilization_times = []

    current_time = 0  # Current time initialized to 0

    process_info_list = []  # Initialize list to store process information as dictionaries
    
    for index, row in df.iterrows():
        arrival_time = row['arrival_time']
        execution_time = row['execution_time']
        process_name = row['process_name']  # Added to get the process name

        # Calculate start time (maximum of arrival time and current time)
        start_time = max(arrival_time, current_time)
        start_times.append(start_time)

        # Calculate end time
        end_time = start_time + execution_time
        end_times.append(end_time)

        # Calculate wait time
        wait_time = start_time - arrival_time
        wait_times.append(wait_time)

        # Calculate turnaround time
        turnaround_time = end_time - arrival_time
        turnaround_times.append(turnaround_time)

        # Calculate utilization (execution time - turnaround time)
        utilization = round((execution_time / turnaround_time)*100,2)
        utilization_times.append(utilization)

        # Update the current time to the end time of the current process
        current_time = end_time

        # Create a dictionary for process information
        process_info = {
            'process_name': process_name,
            'start_time': start_time,
            'end_time': end_time
        }
        
        # Append the process information dictionary to the list
        process_info_list.append(process_info)

    # Add the calculated metrics to the DataFrame
    df['start_time'] = start_times
    df['end_time'] = end_times
    df['wait_time'] = wait_times
    df['turnaround_time'] = turnaround_times
    df['utilization'] = utilization_times

    for i in process_info_list:
        process_no = i['process_name'] 
        color_code = color[process_no]
        i['color'] = color_code
    
    wt_fc = df['wait_time'].mean()
    tt_fc = df['turnaround_time'].mean()
    ut_fc = df['utilization'].mean()


    # Return both the modified DataFrame and the list of process information
    return df, process_info_list, wt_fc, tt_fc, ut_fc

# Example usage:
data = {'process_name': ['Process 1','Process 2','Process 3','Process 4','Process 5', ],
        'arrival_time': [0, 1, 2, 3, 4],
        'execution_time': [10, 1, 2, 1, 5]}

df = pd.DataFrame(data)
result_df, process_info_list, wt, tt , ut = FCFS(df)
print("Modified DataFrame:")
print(result_df)
print("\nList of Process Information:")
print(process_info_list)

