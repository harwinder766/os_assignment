class Process:
    def __init__(self, pid, at, bt, pr):
        self.pid = pid
        self.at = at
        self.bt = bt
        self.pr = pr        # Priority (lower = higher priority)
        self.rt = bt        # Remaining Time
        self.ct = 0
        self.tat = 0
        self.wt = 0


class PriorityPreemptive:
    def __init__(self, processes):
        self.processes = processes
    
    def schedule(self):
        n = len(self.processes)
        completed = 0
        time = 0

        while completed <n:
            idx = -1
            best_pr = float('inf')

            for i,p in enumerate(self.processes):
                if (p.at <= time and p.rt>0):
                    if (p.pr  < best_pr ) or (p.pr == best_pr and p.at < self.processes[idx].at):
                        idx = i
                        best_pr = p.pr
                
            if idx ==-1:
                time+=1
                continue

            p= self.processes[idx]
            p.rt-=1
            time +=1

            if p.rt==0:
                p.ct = time
                p.tat = p.ct-p.at
                p.wt =p.tat -p.bt
                completed+=1
                                
    def display(self):
        print("\nPID\tAT\tBT\tPR\tCT\tTAT\tWT")
        print("-" * 52)

        avg_tat = 0
        avg_wt = 0

        for p in self.processes:
            print(f"{p.pid}\t{p.at}\t{p.bt}\t{p.pr}\t{p.ct}\t{p.tat}\t{p.wt}")
            avg_tat += p.tat
            avg_wt += p.wt

        avg_tat /= len(self.processes)
        avg_wt /= len(self.processes)

        print("-" * 52)
        print(f"\nAverage TAT: {avg_tat:.2f}")
        print(f"Average WT: {avg_wt:.2f}")



n = int(input("Enter number of processes: "))
processes = []
for i in range(1, n + 1):
    at = int(input(f"Enter AT of P{i}: "))
    bt = int(input(f"Enter BT of P{i}: "))
    pr = int(input(f"Enter Priority of P{i} (lower = higher): "))
    processes.append(Process(f"P{i}", at, bt, pr))
scheduler = PriorityPreemptive(processes)
scheduler.schedule()
scheduler.display()