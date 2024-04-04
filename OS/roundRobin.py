from pydantic import BaseModel
from collections import deque
from typing import List

"""
Process class and its attributes
"""
class Process(BaseModel):
        name           : str
        arrivalTime    : int 
        burstTime      : int
        completionTime : int
        remainingTime  : int 
        turnaroundTime : int 
        waitingTime    : int 
        responseTime   : int 

        def __repr__(self) -> str:
            return f"<{self.name}>"

"""
calculating Turnaround Time
"""
def calculateTurnaroundTime(process:Process)-> None:
    process.turnaroundTime = process.completionTime - process.arrivalTime

"""
calculating Waiting Time
"""
def calculateWaitingTime(process:Process)-> None:
    process.waitingTime = process.turnaroundTime - process.burstTime

"""
calculating Response Time
"""
def calculateResponseTime(process:Process, totalTime:int)-> None:
    process.responseTime = totalTime - process.arrivalTime


"""
calculating Completion Time and printing queue states
"""
def roundRobin(processes:List[Process], timeQuantum:int)-> None:
    queue = deque(processes)
    print("------------------------------------------------------------------------------------------------------")
    print("|                                          Queue States                                              |")
    print("------------------------------------------------------------------------------------------------------")

    print(f"Queue Current State : {queue}")
    
    totalTime = 0

    while queue:
        currentProcess = queue.popleft()

        if currentProcess.responseTime == -1:
            calculateResponseTime(currentProcess, totalTime)

        if currentProcess.remainingTime > timeQuantum:
            totalTime += timeQuantum
            currentProcess.remainingTime -= timeQuantum
            queue.append(currentProcess)
            print(f"Queue Current State : {queue}")
        else:
            totalTime += currentProcess.remainingTime
            currentProcess.completionTime = totalTime
            calculateTurnaroundTime(currentProcess)
            calculateWaitingTime(currentProcess)
            print(f"Queue Current State : {queue}")
        
        
        
    print("------------------------------------------------------------------------------------------------------\n")

"""
displaying the result
"""
def showResult(processes : List[Process]) -> None:
    print("------------------------------------------------------------------------------------------------------")
    print("|                                       Round Robin Result                                           |")
    print("------------------------------------------------------------------------------------------------------\n")

    print("------------------------------------------------------------------------------------------------------")
    print("|   Name   | ArrivalTime | BurstTime | CompletionTime | TurnArroundTime | WaitingTime | ResponseTime |")
    print("------------------------------------------------------------------------------------------------------")
    for process in processes:
        print(f"|{process.name.center(10)}|{str(process.arrivalTime).center(13)}|{str(process.burstTime).center(11)}|{str(process.completionTime).center(16)}|{str(process.turnaroundTime).center(17)}|{str(process.waitingTime).center(13)}|{str(process.responseTime).center(14)}|")
    print("------------------------------------------------------------------------------------------------------")



if __name__ == "__main__":
    """
    taking input : no Of Processes
    """
    noOfProcesses : int           = int(input("Enter no of Processes : ")) 
    
    """
    taking input : time Quantum
    """
    timeQuantum   : int           = int(input("Enter Time Quantum    : "))
    
    """
    List for storing all the processes
    """
    processes     : List[Process] = []

    """
    appending all the processes to the list
    """
    for process in range(noOfProcesses):
        
        print(f"Process # {process+1} :")
        
        arrivalTime : int = int(input("\tEnter Arrival Time : "))
        burstTime   : int = int(input("\tEnter Burst   Time : "))
        
        newProcess : Process = Process(
                                       name=f"Process#{process+1}",
                                       arrivalTime=arrivalTime,
                                       burstTime=burstTime,
                                       completionTime=0,
                                       remainingTime=burstTime,
                                       turnaroundTime=0,
                                       waitingTime=0,
                                       responseTime=-1
                                      )


        processes.append(newProcess)


    roundRobin(processes, timeQuantum)
    showResult(processes)