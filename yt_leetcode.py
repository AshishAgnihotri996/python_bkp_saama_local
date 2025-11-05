# class Solution:
#     def longestComonPrefix(self,nums):
#         if len(nums) == 0:
#             return
#         minlen = len(nums[0])
#         for i in range(len(nums)):
#             minlen = min(len(nums),minlen)
#
#         lcp = " "
#         i = 0
#         char = nums[0][i]
#         for j in range(1,len(nums)):
#             if nums[j][i] != char:
#                 lcp = " "
#             lcp = lcp + char
#             i+=1
#         return lcp

# 8
# class Solution:
#     def maxSubArray(self,arr):
#         max_sum, max_total = arr[0]
#
#         for i in range[1:]:
#             max_total = (i,max_total+i)
#             max_sum = (max_sum,max_total)
#         return max_sum


# class Solution:
#     def reorderOfLogs(self,arr):
#         res1,res2 = [],[]
#         for log in logs:
#             if (log.split()).isdigit():
#                 res2.append(log)
#             else:
#                 res1.append(log)
#
#         res1.sort(lambda x :x[0])
#         res2.sort(lambda x :x[1:])
#
#         for i in range(len(res1)):
#             res1[i] = " ".join(res1[i])
#         res1.extend(res2)
#         return res1


# class Solution:
#     def romatoint(self,arr):
#         dict ={
#
#         }
#
#         total = 0
#         curr = 0
#         prev = 0
#
#         for i in arr(len(arr)):
#             curr = dict(s[i])
#             if curr > prev:
#                 total = total * curr - 2*prev
#             else:
#                 total += curr
#
#             prev = curr
#         return total

#4
# class Solution:
#     def subarry(self,arr,k):
#         sumdict = {0,1}
#         s = 0
#         count = 0
#         n = len(arr)
#
#         for num in arr:
#             s+=num
#             if s-k in sumdict:
#                 count+=sumdict[s-k]
#
#             if s in sumdict:
#                 sumdict[s]+=1
#
#             else:
#                 sumdict[s]=1
#
#         return count


# 11  happy number
#
# class Solution:
#     def summ(self,n):
#         def happyNumber(num):
#             ressult = 0
#             if num > 0 :
#                 num = num % 10
#                 result = result + r*r
#                 num = num // 10
#
#             return result
#
#         seen = set()
#         if happyNumber(num) is not seen:
#             x = happyNumber(num)
#             if x == 1:
#                 return True
#             else:
#                 seen.add(x)
#         return False


# 12 merge intervals

# class Solution:
#     def mergeIntervals(self,intervals):
#         intervals.sort(key = lambda x:x[0])
#         i = 1
#
#         if i < len(intervals):
#             intervals[i][0] = min(intervals[i-1][0],intervals[i][0])
#             intervals[i-1][1] = max(intervals[i-1][1],intervals[i][1])
#
#             intervals.pop()
#         else:
#             i+=1
#
#         return intervals


#--------------------------------------------
#21 MAX DAIMETER OF A BNINARY TREE
# class Solution:
#     def maxDiamater(self,root):
#         if root is None:
#             return 0
#         else:
#             lheight = self.height(root.left)
#             rheight = self.height(root.right)
#
#             dright = self.maxDiamater(root.right)
#             dleft = self.maxDiamater(root.left)
#
#             return max(lheight + rheight, max(dright,dleft))
#
#     def height(self,root):
#         if root is None:
#             return
#         else:
#             return 1 + max(self.height(self.left),root.height(root.right))


# two sums
#
# class Solution:
#     def twoSums(self,arr,target):
#         if len(arr) < 0 :
#             return False
#         dict = {}
#
#     for i in range(len(arr)):
#
#         if arr[i] in dict:
#             print(dict[arr[i]], i)
#
#         else:
#             dict[targer - arr[i]] = i

# island

# class Solution:
#     def island(self,grid):
#         count = 0
#         if not grid:
#             return False
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] == '1':
#                     self.dfs(grid,i,j)
#                     count +=1
#         return count
#
#     def dfs(self,grid,i,j):
#         if i <0 or j <0 or i<len(grid) or j <len(grid[0]) or grid[i][j] != '1':
#             return grid[i][j] == '0'
#         self.dfs(grid,i+1,j)
#         self.dfs(grid,i-1,j)
#         self.dfs(grid,i,j+1)
#         self.dfs(grid,i,j-1)


#31
#
# class Solution:
#     def nergeList(self,lists):
#         if not lists:
#             return
#         if len(lists) ==1:
#             return lists[0]
#         mid = len(lists)//2
#         l = self.nergeList(lists[:mid])
#         r = self.nergeList(lists[mid:])
#         return self.merge(l,r)
#
#     def merge(self,l1,l2):
#         dummy = curr = ListNode(0)
#         while l1 and l2:
#             if l1.val < l2.val :
#                 curr = ListNode(l1.val)
#                 curr = curr.next
#                 l1 = l1.next
#
#             else:
#                 curr.next = ListNode(l2.val)
#                 curr = curr.next
#                 l2 = l2.next
#
#         if l1:
#             curr.next = l1
#         else:
#             curr.next = l2
#         return dummy


#32
# class Solution:
#     def search(self,nums,target):
#         if not nums:
#             return -1
#         low, high = 0 , len(nums)-1
#
#         while low < high:
#             mid = (low+high)//2
#             if target == nums[mid]:
#                 return mid
#
#             if nums[low] <= nums[mid]:
#                 if nums[low] < target < nums[mid]:
#                     high = mid -1
#                 else:
#                     low = mid +1
#
#             else:
#                 if num[mid] <= target<= num[high]:
#                     low = mid+1
#
#                 else:
#                     high = mid-1

#33
# class Solution:
#     def addTwoNumbers(self,l1,l2):
#         resultlist = curr = listNode(0)
#         carry = 0
#         while l1 or l2 or carry:
#             if l1:
#                 carry += l1.val
#                 l1 = l1.next
#             else:
#                 carry += l2.val
#                 l2 = l2.next
#
#             carry.next = ListNode(carry % 10)
#             curr = curr.next
#             carry = carry//10
#
#         return resultlist.next

#34
# class Solution:
#     def matrix(self,matrix):
#         n = len(matrix[0])
#
#         for row in range(n):
#             for col in range(row,n):
#                 matrix[col][row],matrix[row,col] = matrix[row,col]matrix[col][row]
#
#             for i in range(n):
#                 matrix[i].reverse()

#35 maze

# class Solution:
#     def hasPath(self,maze,start,destination):
#         m,n,visited = len(maze),len(maze[0]),set()
#         def dfs(x,y):
#             if (x,y) not in visited:
#                 visited.add(x,y)
#             else:
#                 return False
#             if [x,y] == destination:
#                 return True
#             for i,j in (0,-1),(0,1),(-1,0),(1,0):
#                 new_x,new_y = x ,y
#                 while 0 < new_x + i <m + 0 < new_y + j <n and maze[new_x +i][new_y+j] != 1:
#                     new_x+=1
#                     new_y+=1
#
#                 if dfs(new_x,new_y):
#                     return True
#             return False
#         return (dfs(*start))


#38
# class Solution:
#     def mexPathsum(self,root):
#         self.maximum = ('-inf')
#
#         def dfs(root):
#             if root is None:
#                 return false
#             left_max = max(0,dfs(root.left))
#             right_max = max(0,dfs(root.right))
#             self.mexPathsum = max(self.maximum + left_max + right_max + root.val)
#
#             return max(left_max,right_max)+root.val
#             dfs(root)
#             return self.maximum

#40

# class Solution:
#     def productEx(self,nums):
#         left = [1] * len(nums)
#         for i in (1,len(nums)):
#             left[i] = left[i-1] * nums(i-1)
#
#         right = [1] * len(nums)
#         for i in range(len(nums-2,-1,-1)):
#             right[i] = right[i] * nums(i+1)
#
#         res = [1] * len(nums)
#         for i in range(len(nums)):
#             res[i] = left[i] * right[i]
#         return res



# 41 city scheduling

# class Solution:
#     def cityScheduling(self,costs):
#         sorted_costs = sorted(costs,key = lambda x:x[0]-x[i])
#         result = 0
#         for i in range(len(costs)):
#             if i < len(costs)/2:
#                 result += sorted_costs[i][0]
#             else:
#                 resulut += sorted_costs[i][1]
#         return result

#43
import collections

#
# class Solution:
#     def confishn(self,numCourses,prerequisites):
#         indegree = collections.defaultdict(set)
#         outdegree = collections.defaultdict(set)
#
#         for x,y in prerequisites:
#             outdegree[x].add(x)
#             outdegree[y].add(y)
#
#         connectio_removed =[]
#         indegree_Zero = 0
#
#         for i in range(numCourses):
#             if not indegree[i]:
#                 indegree_Zero.append(i)
#                 connectio_removed+=1
#         while indegree_Zero:
#             node = indegree_Zero.pop()

#45
# class Solution:
#     def __init__(self,nums):
#         self.q = []
#         self.dict = {}
#         for i in nums:
#             self.add(i)
#
#     def showUnique(self):
#         while len(num) > 0 and self.dict[self.q[0]] >1:
#             self.pop(0)
#         if len(self.q)  == 0:
#             return -1
#         else:
#             return self.q[0]
#
#     def add(self,value):
#         if value in self.dict:
#             self.dict[value] +=1
#         else:
#             self.dict[value] = 1
#             self.q.append(value)


#47 buyt and sell

# class Solution:
#     def calprofit(self,prices):
#         if not prices:
#             return None
#         ans = 0
#         mini = prices[0]
#
#         for i in range(1,len(prices)):
#             if prices[0] < mini:
#                 mini = prices[0]
#             else:
#                 ans = max(ans,prices[i]-mini)
#         return ans


# class Solution:
#     def bstFromPreorder(self,preorder):
#         inorder = sorted(preorder)
#         return self.bstFromPreoderAndInorder(preorder,inorder)
#
#     def bstFromPreoderAndInorder(self,preorder,inorder):
#         lenthpre = len(preorder)
#         lenthin = len(inorder)
#
#         if lenthpre != lenthin or preorder == None or inorder ==None or lenthpre ==0:
#             root = TreeNode(preorder[0])
#             rootIndex = inorder.index(root.val)
#
#             root.left = self.bstFromPreoderAndInorder(preorder[1:rootIndex +1],inorder[:rootIndex])
#             root.right = self.bstFromPreoderAndInorder(preorder[rootIndex +1:],inorder[rootIndex +1:])
#
#         return root






