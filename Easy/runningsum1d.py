# class Solution:

#  def runningSum():
      
#         # Take the input of the size of the list
#         # n = int (input ("Enter number of elements: ")) 

#         # Take input of all the elements as a string 
#         s = input("\nEnter the elements: ")

#         # Use map function to wrap-up them and converting to desired data type.
#         nums = list (int(num) for num in s.split())
#         print(nums)
#         result=[]
#         sum=0
    
#         for i in nums:
#             sum=sum+i
#             result.append(sum)
#         return result
        
# print(Solution.runningSum())
from typing import List
class Solution:

    def runningSum(self,nums):
        result = []
        sum = 0
        for i in nums:
            sum +=i
            result.append(sum)
        return result
