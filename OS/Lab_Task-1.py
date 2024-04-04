import random
from collections import deque

quantum_time = int(input("Enter quantum time: "))

num_processes = int(input("Enter the number of processes: "))
processes = {}
for i in range(1, num_processes + 1):
    process_name = f"process_{i}"
    process_to_be_executed = [random.randint(1, 8) for _ in range(random.randint(3, 5))]
    execution_time = len(process_to_be_executed)
    
    processes[process_name] = {
        'process_to_be_executed': process_to_be_executed,
        'execution_time': execution_time,
        'arrival_time': i,  # Automatically set the arrival time
        'resource_needed': False,
        'resource_timer': 0,
        'status': 'ready'
    }

print(f"\n=========== Sheduling Algorithm ======================")
print(f'\nAlgo : Round Robin')
print(f"\n=========== Process Details ======================")

for process_name, process_details in processes.items():
    print(f"Process Identification: {process_name}")
    print(f"Execution Time: {process_details['execution_time']}")
    print(f"Arrival Time: {process_details['arrival_time']}")
    print(f"Process to be executed: {process_details['process_to_be_executed']}\n")
print(f"===============================================")

status = 0

IR = 0
PC = 0

ready_queue = deque(processes.keys())
   
block_queue = deque()

elements_needing_resources = {}

while ready_queue or block_queue:
    if ready_queue:
        current_process_name = ready_queue.popleft()
        current_process = processes[current_process_name]
        status = current_process_name

        IR = current_process['process_to_be_executed'][:min(current_process['execution_time'], quantum_time)]
        PC = min(current_process['execution_time'], quantum_time)

        needs_resource = random.choice([False,True, False])
        if needs_resource:
            block_queue.append(current_process_name)
            current_process['status'] = 'waiting'
            current_process['resource_needed'] = True
            current_process['resource_timer'] = random.randint(2, 3)
            elements_needing_resources[current_process_name] = current_process['process_to_be_executed'][0]
            element_needing_resource = elements_needing_resources[current_process_name]
            if len(IR) == 2:
                if IR[0]==element_needing_resource:
                    del IR[1]

            current_process['process_to_be_executed'] = current_process['process_to_be_executed'][len(IR):]
            current_process['execution_time'] -= len(IR)
        else:
            current_process['process_to_be_executed'] = current_process['process_to_be_executed'][PC:]
            current_process['execution_time'] -= PC

            if current_process['execution_time'] > 0:
                ready_queue.append(current_process_name)

        print(f"\n===== Executing {current_process_name} =====")
        if current_process['resource_needed']==True :
            print(f"Status : Blocked ")
        else:
            print(f"Status : Running ")
        
        print(f"Elements Executed : {' , '.join(map(str, IR))}")
        if len(IR) == 2 :
            print(f"Instruction Register : {IR[1]}")
        else :
            print(f"Instruction Register : {IR[0]}")
        if ready_queue:
            next_process_name = ready_queue[0]
            print(f"Program Counter: {next_process_name}")

        if current_process['resource_needed']:
            if current_process['process_to_be_executed'] == 0 :
                pass
            else :
                print(f"{current_process_name} needs a resource for element {element_needing_resource}.")
            print(f"Resumed From : {current_process['process_to_be_executed'][0]}")

    if block_queue:

        blocked_process_name = block_queue[0]
        blocked_process = processes[blocked_process_name]
        
        blocked_process['resource_timer'] -= 1

        if blocked_process['resource_timer'] <= 0:
            if blocked_process['resource_needed']:
                print(f"{blocked_process_name} gets the resource successfully.")
                blocked_process['resource_needed'] = False
                block_queue.popleft()
                if blocked_process['execution_time'] > 0 :
                    ready_queue.append(blocked_process_name)
                    
                blocked_process['status'] = 'ready'
    
print(f"\nAll processes executed.")
