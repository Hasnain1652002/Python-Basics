import random
from collections import deque

# Step 1: Take input of quantum time
quantum_time = int(input("Enter quantum time: "))

# Step 2: Take input of the number of processes and create process dictionaries
num_processes = int(input("Enter the number of processes: "))
processes = {}
for i in range(1, num_processes + 1):
    process_name = f"process_{i}"
    process_to_be_executed = [random.randint(1, 8) for _ in range(random.randint(3, 7))]
    execution_time = len(process_to_be_executed)
    arrival_time = int(input(f"Enter arrival time for {process_name}: "))
    
    processes[process_name] = {
        'process_to_be_executed': process_to_be_executed,
        'execution_time': execution_time,
        'arrival_time': arrival_time
    }

# Print details of each process
print("=========== Process Details ======================")
for process_name, process_details in processes.items():
    print(f"Process Identification: {process_name}")
    print(f"Execution Time: {process_details['execution_time']}")
    print(f"Arrival Time: {process_details['arrival_time']}")
    print(f"Process to be executed: {process_details['process_to_be_executed']}\n")
print("===============================================")

# Step 3: Create a variable "status" and initialize it with 0
status = 0

# Step 4: Initialize IR and PC with 0
IR = 0
PC = 0

# Step 5: Create a ready queue and add each process in it sequence wise
ready_queue = deque(processes.keys())


# Step 6: Start a while loop until all processes are executed
while ready_queue:
    current_process_name = ready_queue.popleft()
    current_process = processes[current_process_name]
    # Update status to the process name
    status = current_process_name
    # Update IR and PC with the current process details
    IR = current_process['process_to_be_executed'][:min(current_process['execution_time'], quantum_time)]
    PC = min(current_process['execution_time'], quantum_time)
    
    print(f"\nStatus : Executing {current_process_name}")
    print(f"Elements Executed: {IR}")
    if ready_queue:
        next_process_name = ready_queue[0]
        print(f"Next Process: {next_process_name}")
    
    # Simulate the execution of the process for PC time
    current_process['process_to_be_executed'] = current_process['process_to_be_executed'][PC:]
    current_process['execution_time'] -= PC
    
    # Check if the process is completed
    if current_process['execution_time'] > 0:
        ready_queue.append(current_process_name)
    
    # # Check for other processes with arrival time <= status
    # for process_name in ready_queue.copy():
    #     if processes[process_name]['arrival_time'] <= processes[status]['arrival_time']:
    #         ready_queue.append(process_name)
    #         ready_queue.remove(process_name)

print("All processes executed.")
