 count
 time
 remain
 flag=0
 time_quantum
 wait_time=0
 turnaround_time=0
 at=[]
 bt=[]
 rt=[] 
  
  remain=n
  for count in xrange(n): 
    process_queue.append([])
	process_queue[i].append(int(raw_input('Enter p_name: ') ,count+1))
    process_queue[i].append(int(raw_input('Enter p_arrival: '),count+1))
	process_queue[i].append(int(raw_input('Enter p_burst: '),count+1))
	
    
    rt[count]=bt[count] 
	
  
  time_quantum= int(raw_input ( 'Enter Time Quantum:'))
  print 'Process\t|Turnaround Time|Waiting Time'
  for time in xrange( count =0 , remain !=0):
  
    if rt[count]<=time_quantum && rt[count]>0
    
      time+=rt[count]
      rt[count]=0
      flag=1 
    
    else if rt[count]>0
     
      rt[count]-=time_quantum 
      time+=time_quantum
    
    if rt[count]==0 && flag==1)
    
      remain-- 
      print count+1,time-at[count],time-at[count]-bt[count] 
      wait_time+=time-at[count]-bt[count] 
      turnaround_time+=time-at[count]
      flag=0
	  
    if(count==n-1) 
      count=0; 
    else if at[count+1]<=time 
      count++
    else 
      count=0 
  
  print'average Waiting Time= ',wait_time*1.0/n
  print 'Avg Turnaround Time = ',turnaround_time*1.0/n