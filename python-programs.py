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
def no_of_rotation(arr,rotated_array,n,d):
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



#Rearrange an array such that arr[i] = i
def Rearrange_array(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[j]==i:
                arr[i],arr[j]=arr[j],arr[i]
    for i in range(len(arr)):
        if arr[i]!=i:
            arr[i]=-1
   
    print(arr)
    return arr


#Write a program to reverse an array or string
def Reverse_array(arr):
    print(arr[::-1])
    return arr


#Rearrange array such that arr[i] >= arr[j] if i is even and arr[i]<=arr[j] if i is odd and j < i
def rearrangeArr(arr,len_arr):
    temp_arr=[]
    even_pos=len_arr/2
    odd_pos=len_arr - even_pos
    for i in range(0,len_arr):
        temp_arr=arr[i]
    temp_arr.sort()
    print(temp_arr)
    j=odd_pos-1
    for i in range(0,len_arr,2):
        arr[i]=temp_arr[j]
        j=j-1
    k=even_pos+1
    for i in range(1,len_arr,2):
        arr[i]=temp_arr[k]
        k=k+1
    print(arr)
    return arr

#Rearrange positive and negative numbers in O(n) time and O(1) extra space
def Positive_negative_rearrange(arr,Length_arr):
    positive_arr=[]
    negative_arr=[]
    for pos in arr:
        if pos>0:
            positive_arr.append(pos)
        else:
            negative_arr.append(pos) 
    sorted_arr=negative_arr+positive_arr
    print(sorted_arr)
    return sorted_arr

#move all zeros to the end
def move_zeros(arr,n):
    temp_arr=[]
    temp1_arr=[]
    for i in arr:
        if i==0:
            temp_arr.append(i)
        else:
            temp1_arr.append(i)
    print(temp1_arr+temp_arr)  
    return temp_arr

#K’th Smallest/Largest Element in Unsorted Array
def Kth_Smallest_largest(arr,n,ks,kl):
    arr.sort()
    print(arr[ks-1])
    print(arr[n-kl])
    return arr

#Program for Mean and median of an unsorted array
def Mean_and_Median(arr,n):
    sum=0
    mid=n//2
    for i in arr:
        sum=sum+i
    mean=float(sum/n)
    if(n%2==0):
        median=float(arr[mid]+arr[mid-1])/2
    else:
        median=arr[mid] 
    print(mean)
    print(median) 
    return mean


#K maximum sum combinations from two arrays
def max_sum_two_array(arr1,arr2,length_arr1,length_arr2,k):
    res_arr=[]
    p=[]
    unique_arr=[]
    for i in arr1:
        for j in arr2:
            x=i+j
            res_arr.append(x)
    m=len(res_arr)
    res_arr.sort()
    for i in res_arr:
        if i not in unique_arr:
            unique_arr.append(i)
    for i in range(k):
        print(unique_arr[len(unique_arr)-i-1])
    return res_arr






            