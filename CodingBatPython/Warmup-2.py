# Jeremy Yao's (terrible) solutions to CodingBat's Python problem sets
def string_times(str, n):
  strCopy = ""
  for i in range(0,n):
    strCopy = strCopy + str
    
  return strCopy

def front_times(str, n):
  if (len(str) >= 3):
    str = str[0:3]
    
  longStr = ""
  for i in range(0,n):
    longStr = longStr + str
    
  return longStr

def string_bits(str):
  tempStr = ""
  for i in range(0,len(str),2):
    tempStr = tempStr + str[i]
    
  return tempStr

def string_splosion(str):
  tempStr = ""
  for i in range(0,len(str)):
    tempStr = tempStr + str[:i+1]
    
  return tempStr

def last2(str):
  count = 0
  
  if not(len(str) < 2):
    subStr = str[-2:]
    for i in range(0, len(str)-2):
      if subStr == str[i: i+2]:
        count = count + 1
  
  return count

def array_count9(nums):
  count = 0
  
  for i in nums:
    if i == 9:
      count = 1 + count
      
  return count 

def array_front9(nums):
  numsCopy = nums[:]
  if len(numsCopy) > 4:
    numsCopy = nums[:4]
    
  return 9 in numsCopy

def array123(nums):
  sequence = [1,2,3]
  found = (nums == sequence)
  if len(nums) > 3:
    count = 0
    while (not found) and count < len(nums)-2:
      found = nums[count:count+3] == sequence
      count = count + 1
  
  return found

