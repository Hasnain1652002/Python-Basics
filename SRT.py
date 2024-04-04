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

def SRT(df):
    x = len(df)
    p = [{'process_name': f'Process {i + 1}', 'arrival_time': df['arrival_time'][i], 'burst_time': df['execution_time'][i],
        'start_time': 0, 'completion_time': 0, 'turnaround_time': 0, 'waiting_time': 0, 'utilization': 0}
        for i in range(x)]

    burst_remaining = df['execution_time'].tolist()
    is_completed = [0] * x

    current_time = 0
    completed = 0
    prev = 0
    gantt_chart = []

    while completed != x:
        idx = -1
        mn = 10000000
        for i in range(x):
            if p[i]['arrival_time'] <= current_time and is_completed[i] == 0:
                if burst_remaining[i] < mn:
                    mn = burst_remaining[i]
                    idx = i
                if burst_remaining[i] == mn:
                    if p[i]['arrival_time'] < p[idx]['arrival_time']:
                        mn = burst_remaining[i]
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
                p[idx]['waiting_time'] = p[idx]['start_time'] - p[idx]['arrival_time']

                is_completed[idx] = 1
                completed += 1
        else:
            current_time += 1

    for process in p:
        if process['turnaround_time'] != 0:
            process['utilization'] = round((process['burst_time'] / process['turnaround_time']) * 100, 2)

    final_gantt = []

    # Handle sequences of the same process
    current_process = None
    for step in gantt_chart:
        if step['id'] != current_process:
            if current_process is not None:
                final_gantt.append({'id': current_process, 'start_time': min_start_time, 'end_time': max_end_time})
            current_process = step['id']
            min_start_time = step['start_time']
            max_end_time = step['end_time']
        else:
            max_end_time = step['end_time']

    # Add the last process
    if current_process is not None:
        final_gantt.append({'id': current_process, 'start_time': min_start_time, 'end_time': max_end_time})

    # Add color information to Gantt chart entries
    for i in final_gantt:
        process_no = i['id']
        color_code = color[process_no]
        i['color'] = color_code

    result_df = pd.DataFrame(p)
    result_df = result_df[['process_name', 'arrival_time', 'burst_time', 'start_time', 'completion_time', 'turnaround_time', 'waiting_time', 'utilization']]

    ut_srt = result_df['utilization'].mean()
    tt_srt = result_df['turnaround_time'].mean()
    wt_srt = result_df['waiting_time'].mean()

    return result_df, final_gantt, wt_srt, tt_srt, ut_srt
