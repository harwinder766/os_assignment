from collections import deque

class Process:
    def __init__(self, pid, at, bt):
        self.pid = pid
        self.at = at
        self.bt = bt
        self.rt = bt   # Remaining Time
        self.ct = 0
        self.tat = 0
        self.wt = 0


class RoundRobin:
    def __init__(self, processes, tq):
        self.processes = processes
        self.tq = tq

    def schedule(self):
        n = len(self.processes)
        time = 0
        completed = 0

        # Sort by arrival time
        self.processes.sort(key=lambda x: x.at)

        ready_queue = deque()
        i = 0  # pointer for processes

        while completed < n:

            # Add all processes that have arrived
            while i < n and self.processes[i].at <= time:
                ready_queue.append(self.processes[i])
                i += 1

            # If no process is ready → CPU idle
            if not ready_queue:
                time = self.processes[i].at
                continue

            # Get next process
            p = ready_queue.popleft()

            # Execute for time quantum or remaining time
            exec_time = min(self.tq, p.rt)
            p.rt -= exec_time
            time += exec_time

            # Add newly arrived processes during execution
            while i < n and self.processes[i].at <= time:
                ready_queue.append(self.processes[i])
                i += 1

            # If process not finished → requeue
            if p.rt > 0:
                ready_queue.append(p)
            else:
                # Process completed
                p.ct = time
                p.tat = p.ct - p.at
                p.wt = p.tat - p.bt
                completed += 1



            

    def display(self):
        print("\nPID\tAT\tBT\tCT\tTAT\tWT")
        print("-" * 44)

        avg_tat = 0
        avg_wt = 0

        for p in self.processes:
            print(f"{p.pid}\t{p.at}\t{p.bt}\t{p.ct}\t{p.tat}\t{p.wt}")
            avg_tat += p.tat
            avg_wt += p.wt

        avg_tat /= len(self.processes)
        avg_wt /= len(self.processes)

        print("-" * 44)
        print(f"\nAverage TAT: {avg_tat:.2f}")
        print(f"Average WT: {avg_wt:.2f}")



n = int(input("Enter number of processes: "))
tq = int(input("Enter Time Quantum: "))
processes = []
for i in range(1, n + 1):
    at = int(input(f"Enter AT of P{i}: "))
    bt = int(input(f"Enter BT of P{i}: "))
    processes.append(Process(f"P{i}", at, bt))
rr = RoundRobin(processes, tq)
rr.schedule()
rr.display()

