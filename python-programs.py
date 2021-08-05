#Author: Chetan Dharmik
#Date: 05/08/2021
#Array Programs


# Find pair with given sum in the array
def Sum_array(arr,sum):
    flag=0
    x=[]
    for i in arr:
        for j in range (len(arr)):
            b= i+j
            x.append(b)
    for k in x:
        if (sum==k):
            flag=1
            break
        else:
            continue
    if flag==1:
        print("found")
    else:
        print("not found")


#program for array rotation in left
def left_rotation(arr,d,n):
    x=[]
    b=[]
    c=[]
    for i in range(d):
        x.append(arr[i])
    for j in range(d,n):
        c.append(arr[j])
    b=c+x
    print(b)
    # print(x)
    # print(arr)
    return x


#program for array rotation in right
def right_rotation(arr,d,n):
    x=[]
    b=[]
    c=[]
    for i in range(d,n):
        x.append(arr[i])
    for j in range(0,d):
        c.append(arr[j])
    b=x+c
    print(b)
    #print(x)
    #print(c)
    return x



#Search an element in a sorted and rotated list
def Search_key(arr,key):
    flag=0
    for i in arr:
        if i==key:
            flag=1
            position=arr.index(i)
            break
        else:
            flag=0
    print(position)
    return position

#Given a sorted and rotated array, find if there is a pair with a given sum
def Sum_pair(arr,x,n):
    flag=0
    arr1=[]
    i=0
    j=1
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            m=arr[i]+arr[j]
            arr1.append(m)
    #print(arr1)
    for k in arr1:
        if x==k:
            flag=1
        else:
            flag=0
    if flag:
        print("found")
    else:
        print("not found")
    return arr1



#Find maximum value of Sum( i*arr[i]) with only rotations on given array allowed    
def max_array_rotation(arr,rotation_freq,length_arr):
    x=[]
    b=[]
    c=[]
    z=[]
    for i in range(rotation_freq):
        x.append(arr[i])
    for j in range(rotation_freq,length_arr):
        c.append(arr[j])
    b=c+x
    for k in range(len(b)):
        f=k*b[k]
        z.append(f)
    print(b)
    print(sum(z))
    return z

#Find the Rotation Count in Rotated Sorted array
def no_of_rotation(arr,rotated_array,n,d)
    x=[]
    b=[]
    c=[]
    count=0
    for f in range(d):
        for i in range(f):
            x.append(arr[i])
        for j in range(f,n):
            c.append(arr[j])
        b=c+x
        if(b==rotated_array):
            count=count+1
            break
        else:
            count=count+1
    print(count)
    # print(b)
    # # print(x)
    # # print(arr)
    return x







            