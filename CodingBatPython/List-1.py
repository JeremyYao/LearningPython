#Jeremy Yao's solution to CodingBat's Python problems

def first_last6(nums):
  return nums[-1] == 6 or nums[0] == 6

def same_first_last(nums):
  return len(nums) >= 1 and nums[-1] == nums[0]

def make_pi():
  return [3,1,4]

def common_end(a, b):
  return a[0] == b[0] or a[-1] == b[-1]

def sum3(nums):
  sum = 0
  for i in nums:
    sum = sum + i
    
  return sum

def rotate_left3(nums):
  return nums[1:] + nums[0:1]

def reverse3(nums):
  temp = []
  for i in nums:
    temp.insert(0,i)
    
  return temp

def max_end3(nums):
  length = len(nums)
  copy = nums[0]
  if (copy < nums[-1]):
    copy = nums[-1]
    
  return [copy] * 3

def sum2(nums):
  counter = 0
  sum = 0
  upperB = 2
  if len(nums) < upperB:
    upperB = len(nums) 
  
  while counter < upperB:
    sum = sum + nums[counter]
    counter = counter + 1
    
    
  return sum

def middle_way(a, b):
  return [a[int(len(a)/2)], b[int(len(b)/2)]]
# Future refernce int(float) it rounds, doesn't truncate

def make_ends(nums):
  listNum = [nums[0], nums[0]]
  if len(nums) >= 2: 
    listNum = [nums[0],nums[-1]]
    
  return listNum

def has23(nums):
  return 2 in nums or 3 in nums
