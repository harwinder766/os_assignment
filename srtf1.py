class Process:
    def __init__(self,pid,at, bt, index):
        self.at = at
        self.pid = pid
        self.bt = bt
        self.rt= bt
        self.index = index
        self.ct = 0
        self.tat = 0
        self.wt =0

class SRTF:
    def __init__(self,processes):
        self.processes = processes
    
    def schedule(self):
        n = len(self.processes)
        
        time = 0
        completed = 0

        while completed<n:
            idx = -1
            min_rt =float('inf')

            for i in range(n):
                p = self.processes[i]
                if (p.at <= time and p.rt>0 and p.rt<min_rt):
                    min_rt= p.rt
                    idx = i
                
            if idx == -1:
                time += 1
                continue
            
            p = self.processes[idx]
            p.rt -= 1
            time +=1
            if p.rt == 0:
                p.ct = time
                p.tat = p.ct- p.at
                p.wt = p.tat - p.bt
                completed+=1

    def display(self):
        print(f'\nPID\tAT\tBT\tCT\tTAT\tWT')
        print('-'*45)
        avg_tat = 0
        avg_wt = 0
        for p in self.processes:
            print(f'\n{p.pid}\t{p.at}\t{p.bt}\t{p.ct}\t{p.tat}\t{p.wt}')
            avg_tat += p.tat
            avg_wt += p.wt
        avg_tat = avg_tat/len(self.processes)
        avg_wt = avg_wt/len(self.processes)
        print('-'*45)
        print(f"Average TAT: {avg_tat:.2f}")
        print(f"Average WT: {avg_wt:.2f}")
    
try:
    n = input('Enter no of processes: ')
    processes =[]
    for i in range(1, int(n)+ 1):
        at = input(f"Enter the arrival time of P{i}: ")
        bt = input(f"Enter the burst time of P{i}: ")
        processes.append(Process(f'P{i}', int(at), int(bt), i))
    
    a = SRTF(processes)
    a.schedule()
    a.display()

except ValueError:
    print("Please enter valid integers for no of processes, arrival time and burst time")


