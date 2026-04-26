class Process:
    def __init__(self, pid, at, bt, index):
        self.pid = pid
        self.at = at
        self.index = index
        self.bt = bt
        self.ct = 0
        self.tat = 0
        self.wt = 0

class FCFS:
    def __init__(self, processes):
        self.processes = processes

    def schedule(self):
        # Sort by Arrival Time, then by input index for tie-breaking
        self.processes.sort(key=lambda x: (x.at, x.index))
        time = 0
        for p in self.processes:
            if time < p.at:
                time = p.at
            
            p.ct = time + p.bt
            p.tat = p.ct - p.at
            p.wt = p.tat - p.bt
            time = p.ct

    def display(self):
                
        print(f'\nPID\tAT\tBT\tCT\tTAT\tWT')
        print("-" * 45)
        
        avg_tat = 0
        avg_wt = 0
        for p in self.processes:
            print(f'{p.pid}\t{p.at}\t{p.bt}\t{p.ct}\t{p.tat}\t{p.wt}')
            avg_tat += p.tat
            avg_wt += p.wt
        
        avg_tat /= len(self.processes)
        avg_wt /= len(self.processes)

        print("-" * 45)
        print(f'Average TAT: {avg_tat:.2f}')
        print(f'Average WT: {avg_wt:.2f}')

# Input Handling
try:
    n = int(input('Enter no of processes: '))
    processes = []
    for i in range(1, n + 1):
        at = int(input(f'Enter Arrival Time of P{i}: '))
        bt = int(input(f'Enter Burst Time of P{i}: '))
        processes.append(Process(f'P{i}', at, bt, i))

    b = FCFS(processes)
    b.schedule()
    b.display()
except ValueError:
    print("Please enter valid integers for process counts and times.")