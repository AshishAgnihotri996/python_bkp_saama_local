# class Solution:
#     def peak(self,ls):
#         n = len(ls)
#         for i in range(1,n):
#             if ls[i] >= ls[i-1] and ls[i] >= ls[i+1]:
#                 return i
# s = Solution()
# ans = s.peak([1,3,20,4,1,0])
# print(ans)

#min and max
#
# def minandmax(ls):
#     mini = ls[0]
#     maxi = ls[0]
#     n  = len(ls)
#     for i in range(0,n):
#         if ls[i]<mini:
#             mini = ls[i]
#         if ls[i]>maxi:
#             maxi = ls[i]
#     print(mini)
#     print(maxi)
#
# ls=[10, 89, 9, 56, 4, 80, 8]
# minandmax(ls)
#
# reverse the array
# def reverseList(ls):
#     newlist =[]
#     n = len(ls)
#     for i in range(0,n):
#         newlist.append(ls[n-1])
#         n-=1
#     print(newlist)
# ls=[1,2,3,4,5,6,7,8,9]
# reverseList(ls)

#sort the array

# def sortArray(ls):
#    n = len(ls)-1
#    for i in range(0,n):
#        for j in range(i+1,n):
#            if ls[i]>ls[j]:
#                temp = ls[i]
#                ls[i] = ls[j]
#                ls[j] = temp
#    for i in range(0,n):
#        print(ls[i])
# ls = [2,3,1,4,6,7,5,4]
# sortArray(ls)

#
# def occurance(ls,x):
#     count = 0
#     for i in ls:
#         if (i==x):
#             count+=1
#     print(count)
# ls=[1,6,2,2,3,4,5,6,6,7]
# x = 6
# occurance(ls,x)

#sum of array
#
# def subsum(arr,n,sum):
#     for i in range(n):
#         currsum=arr[i]
#         j=i+1
#         while j<=n:
#             if currsum==sum:
#                 print ("Sum found between")
#                 print("indexes %d and %d"%( i, j-1))
#                 return 1
#             if currsum>sum or j==n:
#                 break
#             currsum=currsum+arr[j]
#             j+=1
#     print ("No subarray found")
#     return 0
#
# # Driver program
# print("Enter the array")
# arr=list(map(int,input().split(" ")))
# n=len(arr)
# sum=int(input("Enter the sum to find in the array\n"))
# subsum(arr,n,sum)

#sort the negative element

# def negativeel(arr):
#     j = 0
#     n = len(arr)-1
#     for i in range(0,n):
#         if (arr[i] <0):
#             temp = arr[i]
#             arr[i] = arr[j]
#             arr[j] = temp
#             j = j+1
#     print(arr)
#
# arr =[-1,-3,5,-1,-5,-3,-7,5,6,7,-8]
# negativeel(arr)


#0 1 2
# class Solution:
#     def zeroonestwos(self,arr):
#         low =0
#         high = len(arr)-1
#         mid = 0
#         while (mid<=high):
#             if arr[mid]==0:
#                 arr[mid],arr[low] = arr[low],arr[mid]
#                 low+=1
#                 mid+=1
#             elif arr[mid]==1:
#                 mid+=1
#             else:
#                 arr[mid],arr[mid] = arr[mid],arr[high]
#         return mid
#
#
# s = Solution()
# ans = s.zeroonestwos([0,1,2,0,0,0,1,1,2,1,2,0])
# print(ans)


#cyclic rotate
#
# def rotate(a):
#    n = len(a)-1
#    for i in range(n,0,-1):
#        a[i]=a[i-1]
#    a[0] = len(a)
#    print(a)
# a =[1,2,3,4,5,6,7]
# rotate(a)

#missing

# def missingnumber(arr):
#     n = set(arr)
#     x = len(n)
#     o = []
#     for i in range(1,x):
#         if i not in n:
#             o.append(i)
#     print(o)
#
# arr =[1,2,3,4,5,6,9,10]
# missingnumber(arr)

#count pairs

# def countsum(arr):
#     target = 10
#     n = len(arr)
#     for i in range(0,n):
#         for j in range(i+1,n):
#             if arr[i]+arr[j] == target:
#                 print(i,j)
# arr =[1,2,3,4,5,6,7,8,9]
# countsum(arr)


#find duplicates in array

# def duplicates(arr):
#     count = 0
#     m =[]
#     n = len(arr)-1
#     for i in range(0,n):
#         for j in range(i+1,n):
#             if arr[i]==arr[j]:
#                 m.append(arr[i])
#     print(m)
#
# arr=[112,43,11,43,112,4,5,6,7,8]
# duplicates(arr)


#quick sort algorithm

# def quicksort(arr,left,right):
#     if left < right:
#         partition_pos = partition(arr,left,right)
#         quicksort(arr,left, partition_pos-1)
#         quicksort(arr,partition_pos+1, right)

# 22 11 88 55 77 33 44
#
# def partition(arr,left,right):
#     i = left
#     j = right -1
#     pivot = arr[right]
#     while i < j :
#         while i < right and arr[i] < pivot:
#             i+=1
#         while j > left and arr[j] >= pivot:
#             j-+1
#         if i < j:
#             arr[i],arr[j] = arr[j],arr[i]
#     if arr[i] > pivot:
#         arr[i],arr[right],arr[right],arr[i]
#     return i
# arr= [22,11,88,66,77,33,44]
# quicksort(arr,0,len(arr)-1)
# print(arr)

#find the common elements in an array

# def commonelemet(x,y,z):
#     i = 0
#     n1 = len(x)-1
#     n2 = len(y)-1
#     n3 = len(z)-1
#     j=0
#     k=0
#     while(i<n1 and j < n2 and k<n3):
#         if(x[i]==y[j] and y[j]==z[k]):
#             print(x[i])
#             i+=1
#             j+=1
#             k+=1
#         elif x[i]<y[j]:
#             i+=1
#         elif y[j] < z[k]:
#             j+=1
#         else:
#             k+=1
# x = [1,2,3,4,5]
# x = sorted(x)
# y=[2,3,4,5,7]
# y = sorted(y)
# z= [4,3,2,6,7]
# z = sorted(z)
# commonelemet(x,y,z)

# to find tbe first repeating elements

# def printfirstrep(arr):
#     n = len(arr)
#     m = {}
#     min = -1
#     for i in range(n-1,-1,-1):
#         if arr[i] in m.keys():
#             min=i
#         else:
#             m[arr[i]]= 1
#     if(min != -1):
#         print(arr[min])
#     else:
#         print('no elements found')
#
# arr = [10,5,3,4,3,5,6]
# printfirstrep(arr)


#non repeating elemets

# def nonrepeatingele(arr):
#    m =dict()
#    n = len(arr)-1
#    for i in range(0,n):
#        if arr[i] in m.keys():
#            m[arr[i]]+=1
#        else:
#            m[arr[i]]= 1
#    for x in m:
#         if m[x]==1:
#             print(x)
#
# arr=[1,1,2,3,3,4,5,6,7,8]
# nonrepeatingele(arr)

#alternative postive and negative number

#Find if there is any subarray with a sum equal to zero
# def demo(arr):
#     sublist =[]
#     result =0
#     n = len(arr)-1
#     for i in range(0,n):
#         for j in range(i+1,n):
#             sublist.append(arr[i:j])
#     for i in sublist:
#         if sum(i)==0:
#             print('yes')
#             print(i)
#             result+=1
#     if result==0:
#         print('no')
# arr=[4,-3,1,6]
# demo(arr)

#Find Largest sum of contiguous Subarray in Python
# def find(arr):
#    max_sum = 0
#    n = len(arr)
#    ans =[]
#    for i in range(0,n):
#        for j in range(i+1,n):
#            a=sum(arr[i:j+1])
#            if a > max_sum:
#                max_sum=a
#                ans = arr[i:j+1]
#    print(max_sum)
#    print(ans)
#
# arr =[19,81,2,41,61,59,28,69,76,88]
# find(arr)

#Maximum Product Subarray

#rainwater
# def rainwater(arr):
#     res = 0
#     n = len(arr)-1
#     for i in range(0,n):
#         left = arr[i]
#         for j in range(i):
#             left = max(left,arr[j])
#         right = arr[i]
#
#         for j in range(i+1,n):
#             right = max(right,arr[j])
#
#         res = res + min(left,right)- arr[i]
#     print(res)
# arr =[0, 1, 0, 2, 1, 0,1, 3, 2, 1, 2, 1]
# rainwater(arr)



#wave array

# def wavearray(arr):
#     n = len(arr)
#     for i in range(0,n,2):
#         if (arr[i]>0 and arr[i-1]>arr[i]):
#             arr[i-1],arr[i] = arr[i],arr[i-1]
#         if (i<n-1 and arr[i]<arr[i+1]):
#             arr[i],arr[i+1] = arr[i+1],arr[i]
#     print(arr)
#
# arr= [3,5,12,2,6,10,7,9,8]
# wavearray(arr)

#majority elements
# def majoritysol(arr):
#     m ={}
#     for i in arr:
#         if i not in m:
#             m[i] = 1
#         if m[i] > len(arr)//2:
#             return i
#         else:
#             m[i]+=1
#     print(i)
# arr=[1,2,1,2,1,3,4,5,1,2,2,3,4,1,4,4,4,4,4,4,4]
# majoritysol(arr)

#subarray
# Python 3 program to find whether an array
# is subset of another array

# Return 1 if arr2[] is a subset of
# arr1[]


# def isSubset(arr1, arr2, m, n):
# 	i = 0
# 	j = 0
# 	for i in range(n):
# 		for j in range(m):
# 			if(arr2[i] == arr1[j]):
# 				break
#
#
# 		if (j == m):
# 			return 0
#
#
# 	return 1
#
#
# # Driver code
# if __name__ == "__main__":
#
# 	arr1 = [11, 1, 13, 21, 3, 7]
# 	arr2 = [11, 3, 7, 1]
#
# 	m = len(arr1)
# 	n = len(arr2)
#
# 	if(isSubset(arr1, arr2, m, n)):
# 		print("arr2[] is subset of arr1[] ")
# 	else:
# 		print("arr2[] is not a subset of arr1[]")

#matrix

# m = int(input('enter the row'))
# n = int(input('enter the col'))
#
# a =[]
# for i in range(m):
#     b = []
#     for j in range(n):
#         j = input("enter the elemensts["+str(i)+"]["+str(j)+"]")
#         b.append(j)
#     a.append(b)
# for i in range(m):
#     for j in range(n):
#         print(a[i][j],end=" ")
#     print()
#
# row = 0
# col = 0
#
# while row < n and col < m:
#     for i in range(col,n):
#         print(a[row][i],end=" ")
#     row+=1
#     for i in range(row,m):
#         print(a[i][n-1],end=" ")
#     n-=1
#     if row < m:
#         for i in range(n-1,(col-1),-1):
#             print(a[m-1][i],end=" ")
#         m-=1
#     if col < n:
#         for i in range(m-1,row-1,-1):
#             print(a[i][col],end=" ")
#         col+=1
#
# r,c = 4,4
#
# def first(arr,l,h):
#     if (h>=l):
#         mid = l+(h-l)//2
#         if((mid ==0 and arr[mid-1]==0 ) and arr[mid] ==1):
#             return mid
#         elif(arr[mid]==0):
#             return first(arr,(mid+1),h)
#         else:
#             return first(arr,l,(mid-1))
#     return -1
#
# def rowwithmax(mat):
#     max = -1
#     row_with_index = 0
#
#     for i in range(r):
#         index=first(mat[i],0,c-1)
#         if(index != -1 and c-index > max):
#             max=c-index
#             row_with_index=i
#     return row_with_index
#
# mat = [[0, 0, 0, 1],
#        [0, 1, 1, 1],
#        [1, 1, 1, 1],
#        [0, 0, 0, 0]]
# print("Index of row with maximum 1s is " + str(rowwithmax(mat)))
# Python implementation of the approach
# R, C = 4, 4
#
#
# # Function to find the index of first index
# # of 1 in a boolean array arr
# def first(arr, low, high):
#     if (high >= low):
#
#         # Get the middle index
#         mid = low + (high - low) // 2
#
#         # Check if the element at middle index is first 1
#         if ((mid == 0 or arr[mid - 1] == 0) and arr[mid] == 1):
#             return mid
#
#         # If the element is 0, recur for right side
#         elif (arr[mid] == 0):
#             return first(arr, (mid + 1), high);
#
#         # If element is not first 1, recur for left side
#         else:
#             return first(arr, low, (mid - 1));
#
#     return -1
#
#
# # Function that returns index of row
# # with maximum number of 1s.
# def rowWithMax1s(mat):
#     # Initialize max values
#     max_row_index, Max = 0, -1
#
#     # Traverse for each row and count number of 1s
#     # by finding the index of first 1
#     for i in range(R):
#
#         index = first(mat[i], 0, C - 1)
#         if (index != -1 and C - index > Max):
#             Max = C - index;
#             max_row_index = i
#
#     return max_row_index
#
#
# # Driver Code
# mat = [[0, 0, 0, 1],
#        [0, 1, 1, 1],
#        [1, 1, 1, 1],
#        [0, 0, 0, 0]]
# print("Index of row with maximum 1s is " + str(rowWithMax1s(mat)))
#
# # This code is contributed by shinjanpatra

#max diff

# def maxIndexDiff(arr):
#     n = len(arr)
#     maxdiff= 0
#     for i in range(0,n):
#         for j in range(i+1,n):
#             if arr[j]>arr[i] and maxdiff < (j-i):
#                 maxdiff = j-i
#             j-=1
#     print(maxdiff)
#
# arr = [9, 2, 3, 4, 5, 6, 7, 8, 18, 0]
# maxIndexDiff(arr)

#maxim sum of two array

# def maxsum(ar1,ar2):
#    i =0
#    j =0
#    m = len(ar1)
#    n = len(ar2)
#    sum1 = 0
#    sum2 = 0
#    result = 0
#    while (i< m and j < n):
#        if ar1[i]<ar2[j]:
#            sum1+=ar1[i]
#            i+=1
#        elif ar1[i]>ar2[j]:
#            sum2+=ar2[j]
#            j+=1
#        else:
#            result += max(sum1,sum2)+ar1[i]
#            sum1=0
#            sum2=0
#            i+=1
#            j+=1
#
#    while i<m:
#        sum1+=ar1[i]
#        i+=1
#    while j<n:
#        sum2 = ar2[j]
#        j+=1
#        result += max(sum1,sum2)
#    print(result)
#
# ar1 = [2, 3, 7, 10, 12, 15, 30, 34]
# ar2 = [1, 5, 7, 8, 10, 15, 16, 19]
#
# maxsum(ar1,ar2)

#repeating and missing element

# def demo(arr):
#     n = len(arr)
#     for i in range(n):
#         if arr[abs(arr[i])-1] > 0:
#             arr[abs(arr[i])-1] = -arr[abs(arr[i])-1]
#         else:
#             print('tthe repeating elemetn is ',abs(arr[i]))
#     m = []
#     for i in range(n):
#         if arr[i]>0:
#             m.append(arr[i])
#     print('the missing element is ',i)
# arr=[1,2,2,4,3,5,7]
# demo(arr)

#stock buy and sell

# def stockBuySell(arr):
#     n = len(arr)
#     if (n==1):
#         return
#     i=0
#     while(i<n):
#         while((i<n)and ((arr[i+1])<=arr[i])):
#             i+=1
#         if (i==n):
#          break
#
#         buy  = i
#         i+=1
#
#         while((i<n) and (arr[i-1]<=arr[i])):
#             i+=1
#
#         sell = i-1
#
#         print("Buy on day: ", buy, "\t",
#               "Sell on day: ", sell)
#
#
#
# arr = [100, 180, 260, 310, 40, 535, 695]
#
#
# # Function call
# stockBuySell(arr)
#
# #closest number
# max_num= 1000000
# def closestNum(arr,x):
#    n = len(arr)
#    l =0
#    r = n-1
#    diff =max_num
#    resl = 0
#    resr = 0
#
#    while(l<r):
#        if abs(arr[l]+arr[r]-x)<diff:
#            resl = l
#            resr = r
#            diff = abs(arr[l]+arr[r]-x)
#
#        if arr[l]+arr[r] > x:
#            r-=1
#        else:
#            l+=1
#    print('closest value are',arr[resl],arr[resr])
#
# arr= [10, 22, 28, 29, 30, 40]
# x =54
#
# closestNum(arr,x)
#
# def chocolate(arr,m):
#     n = len(arr)
#
#     if (n==0 and m==0):
#         return 0
#     if (n<m):
#         return -1
#     arr.sort()
#     diff = arr[n-1]-arr[0]
#
#     for i in range(n-m+1):
#         diff = min(diff,arr[i+m-1]-arr[i])
#     print(diff)
#
# arr = [12, 4, 7, 9, 2, 23, 25, 41,
#            30, 40, 28, 42, 30, 44, 48,
#            43, 50]
#
# m = 7
# chocolate(arr,m)

#subset problem
#
# def subsetprnm(arr,n,sum):
#     if sum==0:
#         return True
#     if n==0 and sum!=0:
#         return False
#
#     if arr[n-1] > sum:
#         return subsetprnm(arr,n-1,sum)
#
#     return subsetprnm(arr,n-1,sum) or subsetprnm(arr,n-1,sum-arr[n-1])
#
# def findpart(arr,n):
#     sum = 0
#     for i in range(0,n):
#         sum+=arr[i]
#
#     if sum%2!=0:
#         return  False
#     return subsetprnm(arr,n,sum//2)


# arr = [3, 1, 5, 9, 12]
# n = len(arr)
#
# if findpart(arr,n)==True:
#     print('can be divided ')
# else:
#     print('no')