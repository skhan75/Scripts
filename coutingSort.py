
# coding: utf-8

# In[38]:

def countingSort(A):
    
    minimum = A[0]
    maximum = A[0]
    
    #Find mimimum and maximum for range of index
    for i in A:
        if(i < minimum):
            minimum = i
        if(i > maximum):
            maximum = i
    
    print ('Minimum Element: ', minimum)
    print ('Maximum Element: ', maximum)  
    
    index = []
    count = [0] * (maximum + 1)
    
    #First make all the elements 0 in count array
    for i in range(minimum, maximum):
        count[i] = 0 
        
    #Count occurences of each no in array 
    for i in A:
        count[A[i]] += 1
        
    
    
    
    
    count_array = [minimum, maximum]
    j = minimum
    
    for i in range(minimum, maximum):
        if(i == ):
            count_array[i] = count[A[j]] 
    
        
    

        
    


# In[39]:

countingSort([2,45,1,5,2,4,7,8])


# In[ ]:



