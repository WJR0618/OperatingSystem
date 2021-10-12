# -*- coding: utf-8 -*-
"""
Created on Mon May  4 17:34:27 2020

@author: 王俊儒
"""

'''
假設有一個檔案內有若干個(N個)數目字(至少多於1萬,最多不超過100萬),
請寫一個java thread的程式,能夠將該些數目字切成k份(k由使用者自訂),
並由K個threads分別進行Bubble Sort之後,再由k-1個threads作Merge Sort,
以完成這些數目字之排序.同時顯示CPU執行之時間.本程式需完成下列事項:

1. 將N個數目字直接作Bubble Sort,並顯示CPU執行之時間.
2. 將N個數目字切成k份,並由K個threads分別進行Bubble Sort之後,再由k-1個threads作Merge Sort,同時顯示CPU執行之時間.
3. 將N個數目字切成k份,並由K個Processes分別進行Bubble Sort之後,再由k-1個Processes作Merge Sort,同時顯示CPU執行之時間.
4. 將N個數目字切成k份,在一個Process內對K份資料進行Bubble Sort之後,再用同一個Process作Merge Sort,同時顯示CPU執行之時間.
'''

import threading
import time
import queue
import multiprocessing 


def read_into_list(fileName, f):
    num_str = f.read()
    num_list = num_str.split()
    num_list = list(map(int, num_list)) 
    return num_list

def read_into_sep_list(fileName, sepNum, f):
    int_con_ls = read_into_list(fileName, f)
    lenOfcont = len(int_con_ls)
    n = len(int_con_ls) // sepNum

    sep_ls = [int_con_ls[i:i+n] for i in range(0, n*sepNum, n)] 
    sep_ls[sepNum-1].extend(int_con_ls[n*sepNum:lenOfcont]) 
    return sep_ls

def BubbleSort(numbers, unsorted_queue):
    lenOfList = len(numbers)
    for i in range(lenOfList):
        for j in range(lenOfList-1-i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    unsorted_queue.put(numbers)
    
def Merge(left, right, unsorted_queue):
    l, r = 0, 0
    length_of_left = len(left)
    length_of_right = len(right)
    items = []

    while l < length_of_left and r < length_of_right:
        if left[l] < right[r]:
            items.append(left[l])
            l += 1
        else :
            items.append(right[r])
            r += 1

   
    if l == length_of_left:
        items.extend(right[r:length_of_right])
    else:
        items.extend(left[l:length_of_left])

    unsorted_queue.put(items)
    

def PrintFile(fileName, _list, perf_time):
    fileName = fileName[0:len(fileName) - 4]
    file = open(fileName + '_output.txt', "w")
    
    file.write('排序後:\n')
    for index in _list:
        file.write(str(index) + ' ')
    file.write('\n執行時間 : {:.5f} seconds'.format(perf_time))
    file.close()

def mission1(fileName, f):
    '''1. 將N個數目字直接作Bubble Sort,並顯示CPU執行之時間.'''
    num_list = read_into_list(fileName, f)
    q = queue.Queue(len(num_list))
    start_time = time.perf_counter()
    BubbleSort(num_list, q)
    end_time = time.perf_counter()
    print('執行時間 : ' + str(end_time-start_time))
    PrintFile(fileName, q.get(), end_time-start_time)
    
def mission2(fileName, f):
    threads = []
    m_threads = []
    num_of_seperated_list = ''

    while not num_of_seperated_list.isdigit():
         num_of_seperated_list = input('K : ')
    num_of_seperated_list = int(num_of_seperated_list)
    sep_list = read_into_sep_list(fileName, num_of_seperated_list, f) 
    q = queue.Queue(num_of_seperated_list) 

    for i in range(num_of_seperated_list):
        thread = threading.Thread(target=BubbleSort, args=(sep_list[i], q))
        threads.append(thread)

    start_time = time.perf_counter()

    counter,i = 0,0
    while i < num_of_seperated_list or counter < num_of_seperated_list - 1:
        if i < num_of_seperated_list:
            threads[i].start()
            i += 1
        if q.qsize() >= 2:
            left = q.get()
            right = q.get()
            multiprocess = threading.Thread(target=Merge, args=(left, right, q))
            multiprocess.start()
            m_threads.append(multiprocess)
            counter += 1

    for m in m_threads:
        m.join()
    
    end_time = time.perf_counter()

    print('執行時間 : ' + str(end_time-start_time))
    PrintFile(fileName, q.get(), end_time-start_time)
    
def Process_bubble_merge(numbers, unsorted_queue):
    for item in numbers:
        BubbleSort(item, unsorted_queue)

    while unsorted_queue.qsize() != 1:
        left = unsorted_queue.get()
        right = unsorted_queue.get()
        Merge(left, right, unsorted_queue)

def mission3(fileName, file):
    processes = []
    m_processes = []
    num_of_seperated_list = ''

    while not num_of_seperated_list.isdigit():
         num_of_seperated_list = input('K : ')
    num_of_seperated_list = int(num_of_seperated_list)
    sep_list = read_into_sep_list(fileName, num_of_seperated_list, file)
    manager = multiprocessing.Manager()
    unsorted_queue = manager.Queue(num_of_seperated_list) 

    for i in range(num_of_seperated_list):
        p = multiprocessing.Process(target=BubbleSort, args=(sep_list[i], unsorted_queue))
        processes.append(p)

    start_time = time.perf_counter()
    counter, i = 0,0
    while i < num_of_seperated_list or counter < num_of_seperated_list - 1:
        if i < num_of_seperated_list:
            processes[i].start()
            i += 1
        if unsorted_queue.qsize() >= 2:
            left = unsorted_queue.get()
            right = unsorted_queue.get()
            multiprocess = multiprocessing.Process(target=Merge, args=(left, right, unsorted_queue))
            multiprocess.start()
            m_processes.append(multiprocess)
            counter += 1

    for mp in m_processes:
        mp.join()

    end_time = time.perf_counter()

    print('執行時間 : ' + str(end_time-start_time))
    PrintFile(fileName, unsorted_queue.get(), end_time-start_time)


def mission4(fileName, file):
    num_of_seperated_list = ''
    while not num_of_seperated_list.isdigit():
        num_of_seperated_list = input('K : ')
    num_of_seperated_list = int(num_of_seperated_list)
    sep_list = read_into_sep_list(fileName, num_of_seperated_list, file)
    manager = multiprocessing.Manager()
    q = manager.Queue(num_of_seperated_list)

    start_time = time.perf_counter()


    multiprocess = multiprocessing.Process(target = Process_bubble_merge, args = (sep_list, q))
    multiprocess.start()
    multiprocess.join()

    end_time = time.perf_counter()

    print('執行時間 : ' + str(end_time-start_time))
    PrintFile(fileName, q.get(), end_time-start_time)
    
if __name__ == '__main__':
    fileName = input( 'Testing File : ' )
    fileName += '.txt'
    while True:
        try:
            file = open(fileName , "r")
            break
        except:
            print( 'No such file plrase try again !' )
            fileName = input( 'Testing File : ' )
            fileName += '.txt'
    
    testNumber = file.read(1)
    print(testNumber)
    
    if testNumber == '1':
        print('Start only bubble sort version...')
        mission1(fileName, file)
    if testNumber == '2':
        print('Start K thread Bubble sort and K-1 thread Merge version...')
        mission2(fileName, file)
    if testNumber == '3':
        print('Start K process Bubble sort and K-1 process Merge version...')
        mission3(fileName, file)
    if testNumber == '4':
        print('Start One process to K Bubble sort and same process Merge version...') 
        mission4(fileName, file)
    
