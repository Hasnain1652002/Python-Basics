import pandas as pd

def HRRN(df):
    x = len(df)
    p = [{'process_name': f'P{i + 1}', 'arrival_time': df['arrival_time'][i], 'burst_time': df['execution_time'][i],
        'start_time': 0, 'completion_time': 0, 'turnaround_time': 0, 'waiting_time': 0, 'utilization': 0, 'response_ratio': 0}
        for i in range(x)]

    burst_remaining = df['execution_time'].tolist()
    is_completed = [0] * x

    current_time = 0
    completed = 0
    gantt_chart = []

    while completed != x:
        max_response_ratio = -1
        idx = -1
        for i in range(x):
            if p[i]['arrival_time'] <= current_time and is_completed[i] == 0:
                waiting_time = current_time - p[i]['arrival_time']
                response_ratio = (waiting_time + p[i]['burst_time']) / p[i]['burst_time']
                if response_ratio > max_response_ratio:
                    max_response_ratio = response_ratio
                    idx = i

        if idx != -1:
            if burst_remaining[idx] == p[idx]['burst_time']:
                p[idx]['start_time'] = current_time
            burst_remaining[idx] -= 1
            current_time += 1
            p[idx]['utilization'] += 1

            # Save the execution time of the previous iteration
            prev_execution_time = current_time - 1

            gantt_chart.append({'id': p[idx]['process_name'], 'start_time': prev_execution_time, 'end_time': current_time})

            if burst_remaining[idx] == 0:
                p[idx]['completion_time'] = current_time
                p[idx]['turnaround_time'] = p[idx]['completion_time'] - p[idx]['arrival_time']
                p[idx]['waiting_time'] = p[idx]['turnaround_time'] - p[idx]['burst_time']

                is_completed[idx] = 1
                completed += 1
        else:
            current_time += 1

    for process in p:
        if process['turnaround_time'] != 0:
            process['utilization'] = f"{round((process['burst_time'] / process['turnaround_time']) * 100, 2)} %"

    # Create a list of dictionaries with minimum execution times and their indexes
    min_execution_times = [{'index': i, 'execution_time': p[i]['burst_time']} for i in range(x) if is_completed[i] == 0]
    min_execution_times.sort(key=lambda x: x['execution_time'])
    
    # Update start times in the Gantt chart list with values from result_df
    for entry in min_execution_times:
        process_idx = entry['index']
        process_name = p[process_idx]['process_name']
        start_time = result_df.loc[result_df['process_name'] == process_name, 'start_time'].values[0]
        
        # Update start time in the Gantt chart list
        for step in gantt_chart:
            if step['id'] == process_name:
                step['start_time'] = start_time
        
    result_df = pd.DataFrame(p)
    result_df = result_df[['process_name', 'arrival_time', 'burst_time', 'start_time', 'completion_time', 'turnaround_time', 'waiting_time', 'utilization']]

    return result_df, gantt_chart

# Example data
data = {'process_name': ['P1', 'P2'],
        'arrival_time': [0, 9],
        'execution_time': [1, 10]}

df = pd.DataFrame(data)

# Call the scheduling algorithm
result_df, gantt_chart = HRRN(df)

# Print the result DataFrame
print(result_df)

# Print the Gantt chart data
for step in gantt_chart:
    print(step)
