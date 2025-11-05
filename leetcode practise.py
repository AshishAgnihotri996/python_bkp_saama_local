# # sum of array
# arr = [1,2,3,4,5,6]
# sum = 0
# n = len(arr)
# for i in range(0,n):
#     sum+=arr[i]
# print(sum)
#
# print(n*(n+1)//2)

#binary search
# n = int(input('enter thr number'))
# def binarySearch(arr,value):
#     left = 0
#     right = len(arr)-1
#     while (left <= right):
#         mid = (left + right) // 2
#         if (arr[mid]==value):
#             print(mid)
#             break
#         elif (arr[mid] < value):
#             left = mid +1
#         elif (arr[mid] > value):
#             right = mid -1
#         else:
#             print('wrong number')
#     return -1
#
# arr = [1,2,3,4,5,6,7,98]
# binarySearch(arr,n)

# move zeros

# def moveZeros(ls):
#     j = 0
#     for num in ls:
#         if num != 0:
#             ls[j]=num
#             j += 1
#     for x in range(j,len(ls)):
#         ls[x] = 0
#     print(ls)
#
# ls = [1,0,3,0,40]
# moveZeros(ls)

#cross the river
# class Solution:
#     def boat(self,people,limit):
#         people.sort()
#         n = len(people)
#         left = 0
#         right = len(people)-1
#         boat_number= 0
#         while (left <= right):
#             if left == right:
#                 boat_number+=1
#                 break
#             if (people[left]+people[right]<= limit):
#                 left +=1
#             right-=1
#             boat_number +=1
#         return boat_number
#
# s = Solution()
# answer = s.boat([2,1,3,4,4],0)
# print(answer)

#mountain problem
# class Mountain:
#     def mount(self,A:list[int])->bool:
#         if (len(A)<3):
#             return False
#         i = 1
#         while (i<len(A) and A[i]>A[i-1]):
#             i+=1
#         if (i ==1 or i == len(A)):
#             return False
#         while (i<len(A) and A[i]<A[i-1]):
#             i+=1
#         return i==len(A)
#
# m = Mountain()
# p = m.mount([1,2,3,2,1])
# print(p)

#substring problem

# class Solution:
#     def lengthofLongestSubstring(self,s:str)->int:
#         m = {}
#         left = 0
#         right = 0
#         ans = 0
#         n = len(s)
#         while(left < n and right <n):
#             el = s[right]
#             if el in m:
#                 left = max(left,m[el]+1)
#             m[el] = right
#             ans = max(ans,right-left+1)
#             right+=1
#         return ans

# s = Solution()
# answer = s.lengthofLongestSubstring("ashish")
# print(answer)

#first and last position of sorted array
# class Solution:
#     def getLeftPosition(self,nums,target):
#         left = 0
#         right = len(nums)-1
#         while(left<= right):
#             mid = (left+right)//2
#             if(nums[mid] == target):
#                 if(mid-1 >= 0 and nums[mid-1] != target or mid == 0):
#                     return mid
#                 right = mid-1
#             elif(nums[mid]>target):
#                 right = mid-1
#             else:
#                 left = mid+1
#         return -1
#     def getRightPosition(self,nums,target):
#         left = 0
#         right = len(nums)-1
#         while(left<= right):
#             mid = (left+right)//2
#             if(nums[mid] == target):
#                 if(mid+1 < len(nums) and nums[mid+1] != target or mid==len(nums)-1):
#                     return mid
#                 left = mid + 1
#             elif(nums[mid]>target):
#                 right = mid-1
#             else:
#                 left = mid+1
#         return -1
#
#     def searchRange(self,nums,target):
#         left = self.getLeftPosition(nums,target)
#         right = self.getRightPosition(nums,target)

#         return [left,right]
# s = Solution()
# answer = s.searchRange([1,2,3,4,4,4,4],4)
# print(answer)

#first bad version

#missing element
# class Solution:
#     def missingNumber(self,num):
#         numberSum = sum(num)
#         n = len(num)
#         intendent = n*(n+1)//2
#         return (intendent-numberSum)
#
# s = Solution()
# answer = s.missingNumber([1,2,4,6,5])
# print(answer)

# def missingNumber(ls):
#     number = set(ls)
#     length = len(ls)
#     output =[]
#     for i in range(1,ls[-1]):
#         if i not in ls:
#             output.append(i)
#     print(output)
# ls = [1,2,3,4,6]
# missingNumber(ls)
# import math
#
# class Solution:
#     def countPrime(self,n):
#         if (n < 2):
#             return 0
#         isPrime = [True] * n
#         for i in range(2,int(math.ceil(math.sqrt(n)))):
#             if (isPrime[i]):
#                 for m in range(i*i,n,i):
#                     isPrime[m] = False
#         return int(isPrime)
# s = Solution()
# a = s.countPrime(12)
# print(a)

#single numnber
# class Solution:
#     def singleNumber(self,n):
#         return 2*sum(set(n))-sum(n)
#
# s = Solution()
# ans = s.singleNumber([4,2,2,1,1])
# print(ans)

#
# class Solution:
#     def movesRobot(self,moves):
#         x = 0
#         y = 0
#         for move in moves:
#             if move=='u':
#                 y+=1
#             elif move == 'r':
#                 x+=1
#             elif move == 'l':
#                 x-=1
#             elif move =='d':
#                 y-=1
#         return x==0 and y==0
# s = Solution()
# ans = s.movesRobot('urrdll')
# print(ans)

#sum of 2 number
# class Solution:
#     def sumOfDigit(self,ls,target):
#         m={}
#         n = len(ls)
#         for i in range(0,n):
#             goal = target - ls[i]
#             if(goal in m):
#                 return [m[goal],i]
#             m[ls[i]] = i
# s = Solution()
# ans = s.sumOfDigit([1,2,3,4,5],7 )
# print(ans)


# DUPLICATE element
# class Solution:
#     def duplicate(self,ls)->bool:
#         m = {}
#         for num in ls:
#             if (m[num] in m):
#                 return True
#             m[num]+=1
#         return False
# ans = Solution()
# answer = ans.duplicate([1,2,3,4,5])
# print(answer)

#method 2
# def duplicate(ls):
#     n = len(ls)
#     for i in range(0,n):
#         for j in range(i+1,n):
#             if ls[i]==ls[j]:
#                 return True
#             else:
#                 return False
# ls=[1,2,3,4,4,1]
# duplicate(ls)

#majority element

# def majorityElement(ls):
#     m ={}
#     for i in ls:
#         m[i]=m.get(i,0)+1
#     for i in ls:
#         if(m[i]>len(ls)//2):
#             print(i)
# ls = [1,2,3,1,1]
# majorityElement(ls)

# class Solution:
#     def fourSumCount(self,l1,l2,l3,l4)->int:
#         ans = 0
#         m ={}
#         A = len(l1)
#         B = len(l2)
#         C = len(l3)
#         D = len(l4)
#
#         for i in range(0,A):
#             x = l1[i]
#             for j in range(0,B):
#                 y = l2[j]
#                 if (x+y not in m):
#                     m[x+y]=0
#                 m[x+y]+=1
#         for i in range(0,C):
#             x = l3[i]
#             for j in range(0,D):
#                 y = l4[j]
#                 target=-(x+y)
#                 if(target in m):
#                     ans+=m[target]
#         return ans
# s = Solution()
# answer = s.fourSumCount([-1,1],[1,-1],[-2,2],[2,-2])
# print(answer)

# from collections import deque
# class LRUCache:
#     def __init__(self,capacity):
#         self.c = capacity
#         self.m = dict()
#         self.deq = deque
#
#     def get(self,key):
#         if key in self.m:
#             value =self.m[key]
#             self.deq.remove(key)
#             self.deq.append(key)
#         else:
#             return -1
#     def put(self,key,value):
#         if key not in self.m:
#             if len(self.deq)==self.c:
#                 oldest = self.deq.popleft()
#                 del self.m[oldest]
#             else:
#                 self.deq.remove(key)
#         self.m[key]= value
#         self.deq.append(key)
#
# s = LRUCache(3)
# s.put(1,1000)
# s.put(2,2000)
# s.put(3,3000)
# print(s.get(1))
# s.put(4,4000)

#linked list - single linked list

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#         self.head = None
# class LinkedList:
#     def printLinkedList(self):
#         temp=self.head
#         Linked_list = ""
#         while(temp):
#             Linked_list+=(str(temp.data)+ " ")
#             temp = temp.next
#         print(Linked_list)
#
# linked_list = LinkedList()
# linked_list.head = Node(5)
# second_node = Node(1)
# third_node = Node(3)
# fourth_node = Node(7)
#
# linked_list.head.next = second_node
# second_node.next = third_node
# third_node.next = fourth_node
#
# linked_list.printLinkedList()

#
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#         self.head = None
#
# class LinkedList:
#     def printedLinkedList(self):
#         temp = self.head
#         linkedlist = ""
#         while(temp):
#             linkedlist+=(str(temp.data)+" ")
#             temp = temp.next
#         print(linkedlist)
#
#
#     def insertNode(self,val,pos):
#         target = self.head
#         if(pos == 0):
#            target.next = self.head
#            self.head = target
#            return
#         def getPrev(pos):
#             temp = self.head
#             count= 1
#             if(count<pos):
#                 temp = temp.next
#                 count+=1
#             return temp
#
#         prev = getPrev(pos)
#         nextNode=prev.next
#
#         prev.next = target
#         target.next = nextNode
#
#
# ll = LinkedList()
# ll.head = Node(5)
# l2 = Node(1)
# l3= Node(3)
# l4 = Node(7)
#
# ll.head.next = l2
# l2.next = l3
# l3.next  = l4
# ll.printedLinkedList()
#
# ll.insertNode(2,4)
# ll.printedLinkedList()



#stones prbm


# class Solution:
#     def stonesprbm(self,arr):
#         while len(arr) >1:
#             arr.sort()
#             if arr[-1] == arr[-2]:
#                 arr = arr[-2]
#             else:
#                 arr[-2] = arr[-1]-arr[-2]
#                 arr = arr[:1]
#         if len(arr)==1:
#             return arr[0]
#         else:
#             return 0
# arr =[2,4,7,4,9,1]
#
# s = Solution()
# ans =s.stonesprbm(arr)
# print(ans)

#by heapify method
import heapq


# class Solution:
#     def laststoneweight(self,stones):
#         stones = [-i for i in stones]
#         heapq.heapify(stines)
#         while len(stones)>1:
#             firststone = abs(heapq.heappop(stones))
#             secondstone = abs(heapq.heappop(stones))
#             if firststone != secondstone:
#                 heapq.heappush(stones, -abs(firststone-secondstone))
#
#             if len(stones):
#                 return abs(stones[0])
#             else:
#                 return 0
#
# s = Solution()
# ans = s.laststoneweight([2,4,1,7,8,1])
# print(ans)
#
# class Solution:
#     def getallelement(self,roo1:TreeNode, root2:TreeNode):
#         res= []
#         if root is None:
#             return 0
#         inorder(root.left=
#         res.append(root.val)
#         inorder(root.right)
#
#         inorder(root1)
#         inorder(root2)
#         return sorted(res)

#sum combination
#
# class Solution:
#     def dfs(self,digit,start_num,cur,cur_sum):
#         ans =[]
#         if cur_sum == n and  digit ==k:
#             ans.append(cur[:])
#
#         elif cur_sum  > n and digit >k :
#             return
#
#         else:
#             for i in range(start_num+1,10):
#                 cur.append(i)
#
#                 dfs(digit+1,cur,cur_sum+i)
#                 cur.pop()
#
#     return ans




#stock sell and buy
#
# class Solution:
#     def stocksellbuy(self,arr):
#         profit = 0
#         for i in range(0,len(arr)):
#             if arr[i-1]<arr[i]:
#                 profit+=arr[i]-arr[i-1]
#         return
#
# s = Solution()
# ans = s.stocksellbuy([10,22,343,22,66,33])
# print(ans)
#
# def swapzero(arr):
#     i = 0
#     for j in range(len(arr)):
#         if arr[j] != 0:
#             arr[i],arr[j] = ar[j],arr[i]
#             i+=1
#

# arr =[0,3,0,5,0,6]
# swapzero(arr)

#word pattern
#
# class Solution:
#     def wordpattern(self,lst):
#         words = str.split(" ")
#
#         if  not len(words)==len(patter):
#             return False
#         ch_to_wrd = {}
#         wrd_to_ch ={}
#
#         for ch, word in zip(word,patter):
#             if ch not in ch_to_wrd:
#                 if word in wrd_to_ch:
#                     return False
#                 else:
#                     ch_to_wrd = ch
#                     wrd_to_ch = word
#
#             else:
#                 if ch_to_wrd[ch] != word:
#                     return False
#     return False

#-----------------------------15-11-2022------------------------
#21 longest daimeter of a binary tre
#
# class Solution:
#     def diameterOfBinaryTree(self,root):
#         if tree is None:
#             return 0
#         lheight = self.height(root.left)
#         rheight = self.height(root.right)
#
#         ldaimeter = self.diameterOfBinaryTree(root.left)
#         rdaimeter = self.diameterOfBinaryTree(root.right)
#
#         maxdia = max(lheight+rheight,max([ldaimeter,rdaimeter]))
#
#     def height(self,root):
#         if tree is None:
#             return 0
#         else:
#             return 1+max(self.height(root.left),self.height(root.right))

#22 find the indices of the two number -> target
#
# class Solution:
#     def twoSum(self,arr,targer):
#         if len(arr)<0:
#             return False
#         dict1 = {}
#
#         for i in range(len(arr)):
#             if arr[i] in dict1:
#                 return dict1[arr[i]],i
#         else:
#             dict1[target - arr[i]] = i

# number of island
# class Solution:
#     def island(self,grid):
#         if grid is None:
#             return 0
#
#         count = 0
#
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j]=='1':
#                     self.dfs(grid,i,j)
#                     count+=1
#         return count
#
#     def dfs(self,grid,i,j):
#         if i<0 or j<0 or i<len(grid) or j<len(grid[0] or grid[i][j]!='1'):
#             return
#         grid[i][j]= '0'
#         self.dfs(grid,i+1,j)
#         self.dfs(grid,i-1,j)
#         self.dfs(grid,i,j+1)
#         self.dfs(grid,i,j+1)

# Swap Nodes in Pairs

# class Solution:
#     def swap_nodes(self,ListNode):
#         d1 = d = ListNode(0)
#         d.next = head
#
#         while d.next and d.next.next:
#             p = d.next
#             q = d.next.next
#             d.next,p.next,q.next = q,q.next,p
#             d = p
#         return d1.next


#add two linked list

# class Solution:
#     def addTwoNumbers(self,l1:ListNode,l2:ListNode):
#         result = curr = ListNode(0)
#         carry = 0
#
#         while l1 or l1 or carry:
#             if l1:
#                 carry += l1
#                 l1 = l1.next
#             if l2:
#                 carry+=l2
#                 l2 = l2.next
#
#             curr.next = ListNode(curr%10)
#             curr = curr.next
#             carry = carry //10
#         return resultlist

#valid parenthieses

# open_list = ["[","{","("]
# close_list = ["]","}",")"]
#
# def check(mystr):
#     stack = []
#
#     for i in mystr:
#         if i in open_list:
#             stack.append(i)
#         elif i in close_list:
#             pos = close_list.index(i)
#             if (len(stack)> 0) and (open_list[pos] == stack[len(stack-1)]):
#                 stack.pop()
#             else:
#                 return 'unbalalnced'
#
#     if len(stack == 0):
#         return 'balanced'
#     else:
#         return  'unbalanced'
#
#
# string = "{[]{()}}"
# print(string, "-", check(string))
#
# string = "[{}{})(]"
# print(string, "-", check(string))
#
# string = "((()"
# print(string, "-", check(string))


#rotate the matrix int 90^
#
# class Solution:
#     def rotatemat(self,matrix):
#         n = len(matrix[0])
#
#         for row in range(n):
#             for col in range(row,n):
#                 matrix[col][row],matrix[row][col] = matrix[row][col],matrix[col][row]
#
#         for i in range(n):
#             matrix[i].reverse()

#contiguous array

# class Solution:
#     def contiguous_array(self,nums):
#        n = len(nums)
#        subarray,count = 0,0
#
#        for i in range(n):
#            if nums[i]==1:
#                count+=1
#            else:
#                count+=-1
#
#            if nums[i]==0:
#                subarray = i-1
#
#            if count in dict:
#                subarray = max(subarray,i-dict[count])
#            else:
#                dict[count] = i
#
#        return count


#Binary tree maximum path sum
#
# class Solution:
#     def maxPathSum(self,root):
#         self.maximun = float('-inf')
#
#         def dfs(root):
#             if root is None:
#                 return False
#             left = max(0,dfs(root.left))
#             right = max(0,dfs(root.right))
#             self.maximun = max(self.maximun,root.left+root.right,root.val)
#             return max(left,right)+root.val
#             dfs(root)
#         return self.maximun

#product of array except itself

# class Solution:
#     def prodarray(self,nums):
#         left = [i]* len(nums)
#         for i in range(1,len(nums)):
#             left[i] = left[i-1]*nums[i-1]
#
#         right = [i]*len(nums)
#         for i in range(1,len(nums)-2,-1,-1):
#             right[i] = right[i+1]*nums[i+1]
#
#         res = [i]*len(nums)
#         for i in range(len(nums)):
#             res[i] = left[i]*right[i]
#         return res

#two city scheduling

# class Solution:
#     def twocity(self,costs):
#         sorted_cost = sorted(costs,key = lambda x:x[0]-x[1])
#         result = 0
#         for i in range(len(costs)):
#             if i < len(costs)/2:
#                 result += sorted_cost[i][0]
#             else:
#                 result -= sorted_cost[i][1]
#         return result

# first unique number
# class Solution:
#     def firstuniquenum(self,nums):
#         self.q = []
#         self.dict ={}
#         for i in nums:
#             self.add(i)
#
#     def showunique(self):
#         while len(nums)>0 and self.dict[self.q[0]] >1:
#             self.q.pop(0)
#         if len(self.q)==0:
#             return -1
#         else:
#             return self.q[0]
#
#     def addfunc(self,value):
#         if value in self.dict:
#             self.dict[value]+=1
#         else:
#             self.dict[value]=1
#             self.q.append(value)


#reverse a linked list ?

#construt bin tree from preorder traversal

#remove n th node from the end of the list

# class SOlution:
#     def removenthele(self,head:ListNode,n):
#         fast = slow = head
#         for  i in range(n):
#             fast = fast.next
#
#         if fast in None:
#             return head.next
#
#         while fast.next:
#             fast = fast.next
#             slow = slow.next
#         slow.next = slow.next.next
#         return head

#first unique character
#
# class Solution:
#     def uniquechar(self,li):
#         s = len(li)
#         d = {}
#         for i in range(len(s)):
#             if i not in d:
#                 d[s[i]] =1
#             else:
#                 d[d[i]] +=1
#         for i in range(len(S)):
#             if d[s[i]] == 1:
#                 return i
#         return -1

#remove k digit
# class Solution:
#     def remokele(self,num,k):
#         stack =[]
#         number_to_remove = k
#         for currele in num:
#             if number_to_remove and stack and stack[-1] > currele:
#                 stack.pop()
#                 number_to_remove -=1
#             stack.append(currele)
#
#         ans = " ".join(stack[0:len(num)-k].lstrip("0"))
#         if len(ans):
#             return ans
#         else:
#             return 0

#Cousins in binary tree
class Solution:
    def isCousins(self,root,x,y):
        xinfo =[]
        yinfo =[]
        parent = None
        depth = 0
        if root is None:
            return False

    def dfs(self,root,x,y,depth,parent,xinfo,yinfo):
        if root is None:
            return None
        if root.val == x:
            xinfo.append((depth,parent))
        if root.val == y:
            yinfo.append((depth,parent))


#-------60-----------
# Counting elements leetcode
# class Solution:
#     def countingele(self,arr):
#         dict = {}
#         for i in arr:
#             dict[i] =1
#
#         result = 0
#         for x in arr:
#             if x+1 in dict:
#                 result+=1
#         return result

#------------------59-----------------
#verfiying an alien dict

class Solution:
    def aliendict(self,word,order):
        dict= {}
        for x,y in enumerate(order):
            dict[y]=x

        for i in range(leb(word)-1):
            word1 = word[i]
            word2 = wordi[i+1]

            for i in range(min(len(word1),len(word2))):
                if word1[i]!= word2[i]:
                    if dict[word1[i]] > dict[word2[i]]:
                        return False
                    break
            else:
                if len(word1) > len(word2):
                    return False
        return True
