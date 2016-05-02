def swap( A, x, y ):
 bt=[]
 process_queue = []
 wt=[]
 tat=[]
 total=0
 avg_wt
 avg_tat
 n = int(raw_input('Enter the total no of processes: '))

 for i in xrange(n):
    process_queue.append([])#append a list object to the list
    process_queue[i].append(raw_input('Enter p_name: '))
    process_queue[i].append(int(raw_input('Enter p_arrival: ')))
    total_wtime += process_queue[i][1]
    process_queue[i].append(int(raw_input('Enter p_bust: ')))
    print ''
    print 'ProcessName\tArrivalTime\tBurstTime'

for i in xrange(n):
    print process_queue[i][0],'\t\t',process_queue[i][1],'\t\t',process_queue[i][2]
     min=i
     for j in xrange(i+1 ,n):
         if arr[j] < arr[min]:
          min = j

         temp=bt[i]
         bt[i]=bt[min]
         bt[min]=temp

         temp=process_queue[i]
		          process_queue[i]=process_queue[min]
         process_queue[min]=temp

         wt[0]=0

for i in xrange (1,n):
        wt[i]=0
for j in xrange(i):
        wt[i]+=bt[j]
        total+=wt[i]
        avg_wt=total/n
        total=0

        print'Process\t    Burst Time    \t Waiting Time\t Turnaround Time'
for i in xrange(n):
 tat[i]=bt[i]+wt[i]
     total+=tat[i]
     print process_queue[i], bt[i],wt[i],tat[i]

     avg_tat=total/n
     print 'Average Waiting Time=',avg_wt
     print 'Average Turnaround Time=',avg_tat



