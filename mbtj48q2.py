

def count_ephemeral(n1,n2,k):
    result = 0
    
    #store x^k values, so it doesn't recalculate each time 
    global storeKPower
    storeKPower = []
    for i in range (0,10):
        storeKPower.append(i**k)

    #numbers dictionary which stores whether a number is ephemeral or not
    global nums
    
    nums = {1:True}
    
    for i in range (n1,n2):

        boo = isEphemeralDict(i)
        
        if boo == True:
            result+=1
        
    return result


def isEphemeralDict(n1):
    original=n1
    currTable=[]


    while n1 !=1:

        tot=0
        for i in str(n1):
            tot += storeKPower[int(i)]

        # if the dictionary has a value for the number - then it is a repeated value and hence able to determine
        #whether it is ephemeral or eternal
        try:
            #n1 is ephemeral
            if nums[tot] == True:
                for cur in currTable:
                    nums[cur] = True     
                return True
            else:
                for cur in currTable:
                    nums[cur] = False     
                return False
            
        # if the dictionary doesnt have a value for the number then it has to
        #check whether the number is repeated in the list
        
        except KeyError:
            
            #I tried to use hashing to make this section quicker
            #however the inbuilt in function was a quicker lookup
            #for a large enough hash that didn't result in failure
            
            if tot in currTable:
                for cur in currTable:
                    nums[cur] = False
                return False
            else:

                currTable.append(tot)

        n1 = tot
        
        

    return True



#q2test.py
"""test function for question 2 of the ADS assignment, 2018-19"""

def q2test():
    
    """tests for the function count_ephemeral"""
    correct = True
    result = count_ephemeral(1, 10, 2)
    if result != 2:
        correct = False
        print("test failed for n1=1, n2=10, k=2; correct result is 2, result obtained was ", result)
    result = count_ephemeral(1000, 10000, 3)
    if result != 91:
        correct = False
        print("test failed for n1=1000, n2=10000, k=3; correct result is 91, result obtained was ", result)
    result = count_ephemeral(123456, 654321, 4)
    if result != 376:
        correct = False
        print("test failed for n1=123456, n2=654321, k=4; correct result is 376, result obtained was ", result)
    if correct:
        #print("all tests passed")
        return True




def largestTest():
    count_ephemeral(1, 10000000, 4)
    
#print(timeit.timeit(q2test,number=100)/100)
#print(timeit.timeit(largestTest, number=1))

