from flask import Flask, render_template, request
import pandas as pd
from FCFS import FCFS  # Import your FCFS function
from HRRN import HRRN  # Import your HRRN function
from SJF import SJF  # Import your SJF function
from SRT import SRT  # Import your SRT function

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    num_processes = int(request.form['numProcesses'])
    process_name = []
    arrival = []
    execution = []

    for i in range(1, num_processes + 1):
        arrival_time = request.form.get(f'arrivalTime{i}')
        execution_time = request.form.get(f'executionTime{i}')

        if arrival_time and execution_time:
            process_name.append(f'Process {i}')
            arrival.append(int(arrival_time))
            execution.append(int(execution_time))

    data = {
        'process_name': process_name,
        'arrival_time': arrival,
        'execution_time': execution
    }

    if not data:
        return "No data entered. Please go back and enter process details."

    df = pd.DataFrame(data)  # Creating the original DataFrame

    # Calling scheduling algorithms and getting results
    fc_data, fc_chart, wt_fc, tt_fc , ut_fc = FCFS(df)
    srt_data, srt_chart, wt_srt, tt_srt , ut_srt = SRT(df)
    sjf_data, sjf_chart,wt_sjf, tt_sjf , ut_sjf = SJF(df)
    hrrn_data, hrrn_chart, wt_hrrn, tt_hrrn , ut_hrrn = HRRN(df)

    # Converting DataFrames to HTML tables
    original_table = df.to_html(classes='table table-bordered table-striped', index=False)
    first_come_table = fc_data.to_html(index=False)
    hrrn_table = hrrn_data.to_html(index=False)
    srt_table = srt_data.to_html(index=False)
    sjf_table = sjf_data.to_html(index=False)

    return render_template('result.html', original_table=original_table, first_come_table=first_come_table,
                           fc_chart=fc_chart, srt_table=srt_table, srt_chart=srt_chart, sjf_table=sjf_table,
                           hrrn_table=hrrn_table, wt_fc=wt_fc, tt_fc=tt_fc, ut_srt=ut_srt, tt_srt=tt_srt,
                           wt_srt=wt_srt, ut_hrrn=ut_hrrn, tt_hrrn=tt_hrrn, wt_hrrn=wt_hrrn)

if __name__ == '__main__':
    app.run(debug=True)
