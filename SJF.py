#TAKE INPUT
process = []
old = []
arival = []
print("Enter The Number of Processes")
n = int(input())
print("Which tecnique to use \n1.Non-Preemptive\n2.Preemptive")
g = int(input())
print("Enter Arrival Time and Burst Time Of Each Process")
for i in range(1,n+1):
    print(f"For P{i}")
    k = list(map(int,input().split()))
    process.append([i-1,k[0],k[1]])
    old.append([i-1,k[0],k[1]])
    arival.append(k[0])

#Internal Processing
#print(process)
#print(old)
#print(arival)

que = []
comp = list(range(n))
con = 0
prev_comp = 0
arival.sort()
comp_time = 0

if g == 1:
    print("\n\nGnatt Chart is as follows:\n")
    while con != n:
        if len(que)==0:
            for i in range(arival.count(min(arival))):
                for g in process:
                    if g[1] == min(arival):
                        que.append(g)
                        #print(que)
                        comp_time = min(arival)
                        process.remove(g)
                arival.remove(min(arival))
        #print(que)
        min = 10000
        id = 0
        gh = que[0]
        prev_comp = comp_time
        for h in que:
            if h[2]<min:
                min = h[2]
                gh = h
                id = h[0]
        comp_time += min
        comp[id] = comp_time
        print(f"Time {prev_comp}-{comp_time} --> Process {id+1}")
        #print(id)
        #print(gh)
        #print(comp_time,comp)
        que.remove(gh)
        #print(que)
        con += 1

        buffer = []
        for i in process:
            if i[1] in range(prev_comp,comp_time):
                buffer.append(i)
        for g in buffer:
            process.remove(g)
            que.append(g)

    print("\n\nThe answer is:\n\n")
    print("-"*61)
    print("|Process    |Arrival    |Burst      |TurnAround |Waiting    |")
    print("-"*61)
    wait = []
    turn = []
    for x in old:
        print(f"|Process {x[0]+1}" + " "*(3-len(str(x[0]))),end = "|")
        print(f"{x[1]}" + " "*(11-len(str(x[1]))),end = "|")
        print(f"{x[2]}" + " "*(11-len(str(x[2]))),end = "|")
        llp = comp[x[0]]
        turn.append(llp - x[1])
        wait.append(llp - x[1] - x[2])
        print(f"{llp - x[1]}" + " "*(11-len(str(llp - x[1]))),end = "|")
        print(f"{llp - x[1] - x[2]}" + " "*(11-len(str(llp - x[1] - x[2]))),end = "|\n")
        print("-"*61)
                
    print(f"\nAverage TurnAround Time : {sum(turn)/n}")
    print(f"\nAverage Waiting Time : {sum(wait)/n}")

else:
    #print(f"Starting {arival}")
    print(f"Staring {process}")
    print("\n\nGnatt Chart is as follows:\n")
    while con<n:
        print(f"Time {comp_time}-->",end="")
        buffer = []
        for i in process:
            if i[1] in range(prev_comp,comp_time+1):
                buffer.append(i)
        for g in buffer:
            process.remove(g)
            que.append(g)

        #print(f"Time{comp_time}")
        #print(f"Queue {que}")

        if con == n:
            break
        min = 10000
        id = 0
        pid = 0
        prev_comp = comp_time
        if len(que)!=0:
            for h in que:
                if h[2]<min:
                    id = que.index(h)   
                    pid = h[0]
                    min = h[2]
            comp_time += 1
            que[id][2] -= 1
            print(f"Process {pid+1}")
            if que[id][2]==0:
                que.remove(que[id])
                comp[pid] = comp_time
                con += 1
        else:
            print("No process Available")
            comp_time += 1

    #print("Hello")
    #print(comp)
    print("\n\nThe answer is:\n\n")
    print("-"*61)
    print("|Process    |Arrival    |Burst      |TurnAround |Waiting    |")
    print("-"*61)
    wait = []
    turn = []
    for x in old:
        print(f"|Process {x[0]+1}" + " "*(3-len(str(x[0]))),end = "|")
        print(f"{x[1]}" + " "*(11-len(str(x[1]))),end = "|")
        print(f"{x[2]}" + " "*(11-len(str(x[2]))),end = "|")
        llp = comp[x[0]]
        turn.append(llp - x[1])
        wait.append(llp - x[1] - x[2])
        print(f"{llp - x[1]}" + " "*(11-len(str(llp - x[1]))),end = "|")
        print(f"{llp - x[1] - x[2]}" + " "*(11-len(str(llp - x[1] - x[2]))),end = "|\n")
        print("-"*61)
                
    print(f"\nAverage TurnAround Time : {sum(turn)/n}")
    print(f"\nAverage Waiting Time : {sum(wait)/n}")
        
        


