import copy

class Process():
    def __init__(self, name, cpuBurst, arrivalTime, priority ):
        self.name = name
        self.cpuBurst = cpuBurst
        self.arrivalTime = arrivalTime
        self.priority = priority
        self.turnaroundTime = 0
        self.waittingTime = 0

def readFile():
    while True:
        try:
            filename = input("Input file name:")
            f = open( filename + ".txt", 'r' )
            break
        except:
            print("No such file please try again!")
    
    line = f.readline()
    method = line.split()[0]
    time_slice = line.split()[1]
    #print( "Method = " + method + "   TimeSlice = " + time_slice)
    line = f.readline()
    #print(line)
    line = f.read()
    lines = line.split('\n')
    process_list = list()
    for l in lines:
        data = l.split() # data[0] = ID, data[1] = Burst, data[2] = arr Time, data[3] = priority
        if len(data) >= 4:
            process_list.append(Process(int(data[0]), int(data[1]), int(data[2]), int(data[3])))
        
    return filename, method, time_slice, process_list
    
def FCFS(filename, process_list, time_slice):
    gantter = str()
    process_list = sorted(process_list, key = lambda s: (s.arrivalTime, s.name))
    end_condition = len(process_list)
    print( 'ID\tCPU Burst\tArrival Time\tPriority' )
    for process in process_list:
        print(process.name,'\t',process.cpuBurst,'\t',process.arrivalTime,'\t',process.priority)
    
    waitting_queue = list()
    remove_list = list()
    done_list = list()
    time = 0
    done = 0
    while True:
        for process in process_list:
            if process.arrivalTime <= time:
                waitting_queue.append(process) #將已到達的process放入waitting_queue
                print('time =',time ,'\tpush\t',process.name,'\t',process.cpuBurst,'\t',process.arrivalTime,'\t',process.priority)
                remove_list.append(process)
        for process in remove_list:
            process_list.remove(process)
        remove_list.clear()   
        
        if len(waitting_queue) > 0:
            print( 'ID\tCPU Burst\tArrival Time\tPriority' )
        for process in waitting_queue:
            print(process.name,'\t',process.cpuBurst,'\t',process.arrivalTime,'\t',process.priority)
            
        if len(waitting_queue) > 0:
            process.waittingTime = time - process.arrivalTime
            process = waitting_queue[0]
            while process.cpuBurst > 0:
                if process.name >= 10:
                    gantter += chr(process.name+55)
                else:
                    gantter += str(process.name)
            
                process.cpuBurst -= 1
                time += 1
            process = waitting_queue.pop(0)
            print( time, ' - ', process.arrivalTime )
            process.turnaroundTime = time - process.arrivalTime
            done_list.append(process)
            done += 1
            print('pop\t',process.name,'\t',process.cpuBurst,'\t',process.arrivalTime,'\t',process.priority)
            if done == end_condition:
                break
            continue
        else:
            gantter += '-'
        time += 1
        
    print(gantter)
    return gantter, done_list
    
def NSJF(filename, process_list, time_slice):
    gantter = str()
    process_list = sorted(process_list, key = lambda s: (s.arrivalTime, s.name))
    print( 'ID\tCPU Burst\tArrival Time\tPriority' )
    for process in process_list:
        print(process.name,'\t',process.cpuBurst,'\t',process.arrivalTime,'\t',process.priority)
    waitting_queue = list()
    remove_list = list()
    done_list = list()
    time = 0
    done = 0
    end_condition = len(process_list)
    while True:
        for process in process_list:
            if process.arrivalTime <= time:
                waitting_queue.append(process) #將已到達的process放入waitting_queue
                print('time =',time ,'\tpush\t',process.name,'\t',process.cpuBurst,'\t',process.arrivalTime,'\t',process.priority)
                remove_list.append(process)
                waitting_queue = sorted(waitting_queue, key = lambda s: (s.cpuBurst, s.arrivalTime, s.name)) #依照cpuBurst排序
        for process in remove_list:
            process_list.remove(process)
        remove_list.clear()
        
        if len(waitting_queue) > 0:
            print( 'ID\tCPU Burst\tArrival Time\tPriority' )
        for process in waitting_queue:
            print(process.name,'\t',process.cpuBurst,'\t',process.arrivalTime,'\t',process.priority)
        if len(waitting_queue) > 0:
            process = waitting_queue[0]
            while process.cpuBurst > 0:
                if process.name >= 10:
                    gantter += chr(process.name+55)
                else:
                    gantter += str(process.name)
            
                process.cpuBurst -= 1
                time += 1
            process = waitting_queue.pop(0)
            print( time, ' - ', process.arrivalTime )
            process.turnaroundTime = time - process.arrivalTime
            done_list.append(process)
            done += 1
            print('pop\t',process.name,'\t',process.cpuBurst,'\t',process.arrivalTime,'\t',process.priority)
            if done == end_condition:
                break
            continue
        else:
            gantter += '-'
        time += 1
        
    print(gantter)
    return gantter, done_list
    
def PSJF(filename, process_list, time_slice):
    gantter = str()
    process_list = sorted(process_list, key = lambda s: (s.arrivalTime, s.name))
    print( 'ID\tCPU Burst\tArrival Time\tPriority' )
    for process in process_list:
        print(process.name,'\t',process.cpuBurst,'\t',process.arrivalTime,'\t',process.priority)
    waitting_queue = list()
    remove_list = list()
    done_list = list()
    time = 0
    done = 0
    end_condition = len(process_list)
    while True:
        for process in process_list:
            if process.arrivalTime <= time:
                waitting_queue.append(process) #將已到達的process放入waitting_queue
                print('time =',time ,'\tpush\t',process.name,'\t',process.cpuBurst,'\t',process.arrivalTime,'\t',process.priority)
                remove_list.append(process)
                waitting_queue = sorted(waitting_queue, key = lambda s: (s.cpuBurst, s.arrivalTime, s.name)) #依照cpuBurst排序
        for process in remove_list:
            process_list.remove(process)
        remove_list.clear()
            
        if len(waitting_queue) > 0:
            print( 'ID\tCPU Burst\tArrival Time\tPriority' )
        for process in waitting_queue:
            print(process.name,'\t',process.cpuBurst,'\t',process.arrivalTime,'\t',process.priority)
        if len(waitting_queue) > 0:
            ####TODO: 在這加以下條件==>如果cpuBurst全都一樣就先拿還沒跑過的
            process = waitting_queue.pop(0)
            if process.name >= 10:
                gantter += chr(process.name+55)
            else:
                gantter += str(process.name)
            print('pop\t',process.name,'\t',process.cpuBurst,'\t',process.arrivalTime,'\t',process.priority)
            process.cpuBurst -= 1
            if process.cpuBurst <= 0: #如果此process執行完了，就不放回waitting_queue
                print( time, ' - ', process.arrivalTime )
                process.turnaroundTime = time - process.arrivalTime + 1
                done_list.append(process)
                done += 1
                pass
            else:
                waitting_queue.append(process)
                waitting_queue = sorted(waitting_queue, key = lambda s: (s.cpuBurst, s.arrivalTime, s.name)) #依照cpuBurst排序
        else:
            gantter += '-'
        time += 1
        if done == end_condition:
            break
    print(gantter)
    return gantter, done_list
    
def RR(filename, process_list, time_slice):
    gantter = str()
    process_list = sorted(process_list, key = lambda s: (s.arrivalTime, s.name))
    end_condition = len(process_list)
    print( 'ID\tCPU Burst\tArrival Time\tPriority' )
    for process in process_list:
        print(process.name,'\t',process.cpuBurst,'\t',process.arrivalTime,'\t',process.priority)
    
    waitting_queue = list()
    remove_list = list()
    done_list = list()
    time = 0
    done = 0
    process_which_need_to_append = None
    while True:
        for process in process_list:
            if process.arrivalTime <= time:
                waitting_queue.append(process) #將已到達的process放入waitting_queue
                print('time =',time ,'\tpush\t',process.name,'\t',process.cpuBurst,'\t',process.arrivalTime,'\t',process.priority)
                remove_list.append(process)
        for process in remove_list:
            process_list.remove(process)
        remove_list.clear() 
        
        if process_which_need_to_append != None:
            waitting_queue.append(process_which_need_to_append)
            process_which_need_to_append = None
        
        if len(waitting_queue) > 0:
            print( 'ID\tCPU Burst\tArrival Time\tPriority' )
        for process in waitting_queue:
            print(process.name,'\t',process.cpuBurst,'\t',process.arrivalTime,'\t',process.priority)

        if len(waitting_queue) > 0:
            for i in range(int(time_slice)):
                process = waitting_queue[0]
                if process.cpuBurst > 0:
                    if process.name >= 10:
                        gantter += chr(process.name+55)
                    else:
                        gantter += str(process.name)
                
                    process.cpuBurst -= 1
                    time += 1
                    if process.cpuBurst == 0:
                        print( time, ' - ', process.arrivalTime )
                        process.turnaroundTime = time - process.arrivalTime
                        done_list.append(process)
                        done += 1
                        process = waitting_queue.pop(0)
                        print('pop\t',process.name,'\t',process.cpuBurst,'\t',process.arrivalTime,'\t',process.priority)
                        if done == end_condition:
                            print(gantter)
                            return gantter, done_list
                        break
            if process.cpuBurst > 0:
                process_which_need_to_append = waitting_queue.pop(0)
        else:
            gantter += '-'
            time += 1
         
def PP(filename, process_list, time_slice):
    gantter = str()
    process_list = sorted(process_list, key = lambda s: (s.arrivalTime, s.name))
    print( 'ID\tCPU Burst\tArrival Time\tPriority' )
    for process in process_list:
        print(process.name,'\t',process.cpuBurst,'\t',process.arrivalTime,'\t',process.priority)
    waitting_queue = list()
    remove_list = list()
    have_been_run_list = list()
    done_list = list()
    time = 0
    done = 0
    move_to_front = False
    next_process = None
    end_condition = len(process_list)
    while True:
        for process in process_list:
            if process.arrivalTime <= time:
                waitting_queue.append(process) #將已到達的process放入waitting_queue
                print('time =',time ,'\tpush\t',process.name,'\t',process.cpuBurst,'\t',process.arrivalTime,'\t',process.priority)
                remove_list.append(process)
                waitting_queue = sorted(waitting_queue, key = lambda s: (s.priority, s.arrivalTime, s.name)) #依照priority排序
        for process in remove_list:
            process_list.remove(process)
        remove_list.clear()
        
        if len(waitting_queue) > 0:
            print( 'ID\tCPU Burst\tArrival Time\tPriority' )
        for process in waitting_queue:
            print(process.name,'\t',process.cpuBurst,'\t',process.arrivalTime,'\t',process.priority)
        if len(waitting_queue) > 0:
            ####TODO: 在這加以下條件==>如果priority一樣就先拿還沒跑過的
            sameList = same_list( waitting_queue, 'priority' )
            if len(sameList) > 1 and move_to_front != True:
                if len(have_been_run_list) > 0:
                    for process in sameList:
                        if process in have_been_run_list:
                            pass
                        else:
                            next_process = process
                            break
                    if next_process != None:
                        process = next_process
                        waitting_queue.remove(next_process)
                        next_process = None
                        move_to_front = True
                    else:
                        process = waitting_queue.pop(0) #依照arrive time 小的先
                else:
                    process = waitting_queue.pop(0) #依照arrive time 小的先
            else:
                process = waitting_queue.pop(0)
            have_been_run_list.append(process)
            if process.name >= 10:
                gantter += chr(process.name+55)
            else:
                gantter += str(process.name)
            print('pop\t',process.name,'\t',process.cpuBurst,'\t',process.arrivalTime,'\t',process.priority)
            process.cpuBurst -= 1
            if process.cpuBurst <= 0: #如果此process執行完了，就不放回waitting_queue
                print( time, ' - ', process.arrivalTime )
                process.turnaroundTime = time - process.arrivalTime + 1
                done_list.append(process)
                done += 1
                move_to_front = False
                pass
            else:
                if move_to_front != True:
                    waitting_queue.append(process)
                    waitting_queue = sorted(waitting_queue, key = lambda s: (s.priority, s.arrivalTime, s.name)) #依照priority排序
                else:
                    waitting_queue.insert(0, process)
        else:
            gantter += '-'
        time += 1
        if done == end_condition:
            break
    print(gantter)
    return gantter, done_list
    
def same_list( waitting_queue, key):
    key_list = list()
    if key == 'priority':
        for i in range(len(waitting_queue)):
            if waitting_queue[i].priority == waitting_queue[0].priority:
                key_list.append( waitting_queue[i] )
    elif key == 'cpuBurst':
        for i in len(waitting_queue):
            if waitting_queue[i].cpuBurst == waitting_queue[0].cpuBurst:
                key_list.append( waitting_queue[i] )
    
    return key_list

def writeFile( method, gantters, done_lists ):
    f = open( filename + "_output.txt", 'w' )
    if method == '1':
        f.write('==\tFCFS\t==\n')
        f.write(gantters[0])
    elif method == '2':
        f.write('==\tRR\t==\n')
        f.write(gantters[0])
    elif method == '3':
        f.write('==\tPSJF\t==\n')
        f.write(gantters[0])
    elif method == '4':
        f.write('==\tNon-PSJF\t==\n')
        f.write(gantters[0])
    elif method == '5':
        f.write('==\tPriority\t==\n')
        f.write(gantters[0])
    elif method == '6':
        f.write('==\tFCFS\t==\n')
        f.write(gantters[0])
        f.write('\n==\tRR\t==\n')
        f.write(gantters[1])
        f.write('\n==\tPSJF\t==\n')
        f.write(gantters[2])
        f.write('\n==\tNon-PSJF\t==\n')
        f.write(gantters[3])
        f.write('\n==\tPriority\t==\n')
        f.write(gantters[4])
    if method == '6':
        times = 5
    else:
        times = 1
    f.write('\n===========================================================\n')
    f.write('Waiting Time\nID      FCFS    RR      PSJF    NPSJF   Priority\n')
    isPrint = False
    for i in range(len(done_lists[0])):
        for j in range(times):
            if not isPrint:
                f.write( str(done_lists[j][i].name) + '\t' )
                isPrint = True
            f.write( str(done_lists[j][i].waittingTime) + '\t' )
        isPrint = False
        f.write('\n')
            
    f.write('\n===========================================================\n')
    
    f.write('\n===========================================================\n')
    f.write('Turnaround Time\nID      FCFS    RR      PSJF    NPSJF   Priority\n')
    isPrint = False
    for i in range(len(done_lists[0])):
        for j in range(times):
            if not isPrint:
                f.write( str(done_lists[j][i].name) + '\t' )
                isPrint = True
            f.write( str(done_lists[j][i].turnaroundTime) + '\t' )
        isPrint = False
        f.write('\n')
    f.write('\n===========================================================\n')

def setWaittingTime( done_list, original_list ):
    ori_list = copy.deepcopy(original_list)
    ori_list = sorted(ori_list, key = lambda s: (s.name))
    for i in range(len(done_list)):
        done_list[i].waittingTime = done_list[i].turnaroundTime - ori_list[i].cpuBurst
    return done_list
    
if __name__ == "__main__":
    filename, method, time_slice, process_list = readFile()
    process_list_copy = copy.deepcopy(process_list)
    gantter_list = list()
    done_list = list()
    done_lists = list()
    print('method : ' + method)
    if method == '1':
        gantter, done_list = FCFS(filename, process_list, time_slice )
        done_list = sorted(done_list, key = lambda s: (s.name))
        done_list = setWaittingTime( done_list, process_list_copy )
        gantter_list.append(gantter)
        done_lists.append(done_list)
        writeFile( method, gantter_list, done_lists )
        print(gantter)
    elif method == '2':
        gantter, done_list = NSJF(filename, process_list, time_slice )
        done_list = sorted(done_list, key = lambda s: (s.name))
        done_list = setWaittingTime( done_list, process_list_copy )
        gantter_list.append(gantter)
        done_lists.append(done_list)
        writeFile( method, gantter_list, done_lists )
        print(gantter)
    elif method == '3':
        gantter, done_list = PSJF(filename, process_list, time_slice )
        done_list = sorted(done_list, key = lambda s: (s.name))
        done_list = setWaittingTime( done_list, process_list_copy )
        gantter_list.append(gantter)
        done_lists.append(done_list)
        writeFile( method, gantter_list, done_lists )
        print(gantter)
    elif method == '4':
        gantter, done_list = RR(filename, process_list, time_slice)
        done_list = sorted(done_list, key = lambda s: (s.name))
        done_list = setWaittingTime( done_list, process_list_copy )
        gantter_list.append(gantter)
        done_lists.append(done_list)
        writeFile( method, gantter_list, done_lists )
        print(gantter)
    elif method == '5':
        gantter, done_list = PP(filename, process_list, time_slice)
        done_list = sorted(done_list, key = lambda s: (s.name))
        done_list = setWaittingTime( done_list, process_list_copy )
        gantter_list.append(gantter)
        done_lists.append(done_list)
        writeFile( method, gantter_list, done_lists )
        print(gantter)
    elif method == '6':
        gantter, done_list = FCFS(filename, process_list, time_slice )
        done_list = sorted(done_list, key = lambda s: (s.name))
        done_list = setWaittingTime( done_list, process_list_copy )
        gantter_list.append(gantter)
        done_lists.append(done_list)
        
        process_list = copy.deepcopy(process_list_copy)
        gantter, done_list = RR(filename, process_list, time_slice)
        done_list = sorted(done_list, key = lambda s: (s.name))
        done_list = setWaittingTime( done_list, process_list_copy )
        gantter_list.append(gantter)
        done_lists.append(done_list)
        
        process_list = copy.deepcopy(process_list_copy)
        gantter,done_list = PSJF(filename, process_list, time_slice )
        done_list = sorted(done_list, key = lambda s: (s.name))
        done_list = setWaittingTime( done_list, process_list_copy )
        done_lists.append(done_list)
        gantter_list.append(gantter)
        
        process_list = copy.deepcopy(process_list_copy)
        gantter, done_list = NSJF(filename, process_list, time_slice )
        done_list = sorted(done_list, key = lambda s: (s.name))
        done_list = setWaittingTime( done_list, process_list_copy )
        gantter_list.append(gantter)
        done_lists.append(done_list)
        
        process_list = copy.deepcopy(process_list_copy)
        gantter, done_list = PP(filename, process_list, time_slice )
        done_list = sorted(done_list, key = lambda s: (s.name))
        done_list = setWaittingTime( done_list, process_list_copy )
        gantter_list.append(gantter)
        done_lists.append(done_list)
        
        writeFile( method, gantter_list, done_lists )
        for gantter in gantter_list:
            print(gantter)
        for done in done_list:
            print(done.name,done.waittingTime, done.turnaroundTime)
    
    
        
    
    
    
    
    
    
    
