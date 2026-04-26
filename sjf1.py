class Process:
    def __init__(self,pid,at,bt, index):
        self.pid = pid
        self.at = at
        self.bt =bt
        self.index = index
        self.tat = 0
        self.ct = 0
        self.wt = 0

class SJF:
    def __init__(self,processes:list):
        self.processes = processes
    
    def schedule(self):
        n = len(processes)
        completed= 0
        visited = [False]*n
        time = 0
        
        while completed<n:
            idx = -1
            min_bf = float('inf')

            for i in range(n):
                if (self.processes[i].at <= time and not visited[i] and self.processes[i].bt <= min_bf):
                    min_bf = self.processes[i].bt
                    idx = i
            
            if idx ==-1:
                time += 1
                continue

            p = self.processes[idx]
            p.ct =time+ p.bt
            p.tat = p.ct - p.at
            p.wt = p.tat - p.bt
            time = p.ct
            visited[idx] = True
            completed+=1
    
    def display(self):

        print("\nPID\tAT\tBT\tCT\tTAT\tWT")
        print("-" * 52)
        avg_tat = 0
        avg_wt = 0
        for p in self.processes:
            print(f"{p.pid}\t{p.at}\t{p.bt}\t{p.ct}\t{p.tat}\t{p.wt}")
            avg_tat += p.tat
            avg_wt += p.wt
        avg_tat /= len(self.processes)
        avg_wt /= len(self.processes)
        print("-" * 52)
        print(f"\nAverage TAT: {avg_tat:.2f}")
        print(f"Average WT: {avg_wt:.2f}")
   


try:
    n = input('Enter no of processes: ')
    processes =[]
    for i in range(1, int(n)+ 1):
        at = input(f"Enter the arrival time of P{i}: ")
        bt = input(f"Enter the burst time of P{i}: ")
        processes.append(Process(f'P{i}', int(at), int(bt), i))
    
    a = SJF(processes)
    a.schedule()
    a.display()

except ValueError:
    print("Please enter valid integers for no of processes, arrival time and burst time")


