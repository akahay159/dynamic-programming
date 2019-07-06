'''maximum sum array problem'''
def findmax_sum(array,size):
    cur_max=0
    max_number=0
    index=0
    j=0
    summ=0
    for index in range(size):
        cur_max+=array[index]
        if cur_max<0:
            cur_max=0
        elif(cur_max>max_number):
            max_number=cur_max
            ind=index
    
    
    again=ind
    while summ!=max_number:
        summ=summ+array[ind]
        ind=ind-1
    return max_number,ind+1,again
array=[1,2,3]
sz=len(array)
print(findmax_sum(array,sz))
