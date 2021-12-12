
def mergeSort(A):

    #if slection sort is applied when length <= 4, as base case, all of the list sizes
    #will be length 4 or less so when the list is split there may be two lists one of length three, the other of two
    #and will sort these and merge them back together

    if len(A)<=4:

        #apply selection sort when length is 4 or less
        for i in range (0,len(A)-1):
            elem = A[i]
            pos = i
            for j in range (i+1,len(A)):
                if A[j] > elem:
                    elem = A[j]
                    pos = j

            A[i], A[pos] = A[pos], A[i]
        return A
    else:

        #find integer middle
        m = len(A)//2

        return merge(mergeSort(A[m:]),mergeSort(A[:m]))
        #return merge(left,right)


#merge the two lists together
def merge(A,B):
    final = []
    while len(A)>0 or len(B)>0:
        if len(A)>0 and len(B)>0:
            if A[0]>B[0]:
                final.append(A.pop(0))
            else:
                final.append(B.pop(0))
                
        elif len(A)>0:
            final.append(A.pop(0))

        elif len(B)>0:
            final.append(B.pop(0))
            
    return final
                
            

list1 = [5,7,8,6,4,3,32,76]
list2 = [32,54,76,38,34]
list3 = [32,54,76,38,34,78,90,99]
list4 = [32,54,76,38,34,78,90,99,4545,43,567,23414325,123,54,2,45,4135,123,5476,745]


#print (mergeSort(list1))
#print (mergeSort(list2))
#print (mergeSort(list3))
#print (mergeSort(list4))

x=mergeSort(list(range(1000)))
#print(x)
