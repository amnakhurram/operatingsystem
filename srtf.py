 process_queue = []
 at=[]
 bt=[]
 rt=[]
 endTime
 smallest
 remain=0
 time
 sum_wait=0
sum_turnaround=0
   
   n = int(raw_input('Enter the total no of processes: '))
	
    for i in xrange(n):
	
    process_queue.append([])
	process_queue[i].append(raw_input('Enter p_name: '))
    process_queue[i].append(int(raw_input('Enter p_arrival: ')))
	 process_queue[i].append(int(raw_input('Enter p_bust: ')))
     
        rt[i]=bt[i]
    
    print 'Process\t |Turnaround Time| Waiting Time'
    rt[small]
    for time in xrange(remain!=n):
    
        smallest=small
        for i in xrange(n):
        
            if at[i]<=time && rt[i]<rt[smallest] && rt[i]>0:
            
                smallest=i
            
        
        rt[smallest]--
        if rt[smallest]==0:
        
            remain++
            endTime=time+1
            print 'smallest+1,endTime-at[smallest],endTime-bt[smallest]-at[smallest])'
            sum_wait+=endTime-bt[smallest]-at[smallest]
            sum_turnaround+=endTime-at[smallest]
        
    
    print 'Average waiting time = ',sum_wait*1.0/n
    print 'Average Turnaround time =',sum_turnaround*1.0/5