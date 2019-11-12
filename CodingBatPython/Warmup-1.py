# Jeremy Yao's (terrible) solutions to CodingBat's Python problem sets
def sleep_in(weekday, vacation):
  return not weekday or vacation

def monkey_trouble(a_smile, b_smile):
  return a_smile == b_smile

def sum_double(a, b):
  sum = a + b
  if a == b:
    sum = sum * 2
  return sum

def diff21(n):
  n1 = 21 - n
  
  if n1 < 0:
    n1 = -n1
    
  if n>= 21:
    n1 = 2*n1

  return n1

def parrot_trouble(talking, hour):
  return talking and (hour < 7 or hour > 20)

def makes10(a, b):
  return a == 10 or b == 10 or a + b == 10

def near_hundred(n):
  return abs(n - 100) <= 10 or abs(n-200) <= 10

def pos_neg(a, b, negative):
  if negative:
    return a < 0 and b < 0
  else: 
    return a * b < 0

def not_string(str):

  if not(len(str) >= 3 and str[:3] == 'not'):
    str = "not " + str
  
  return str

def missing_char(str, n):
  return str[:n] + str[n+1:]

def front_back(str):
  
  length = len(str)
  if (length >= 2):
    str = str[-1] + str[1:length-1] + str[0]
  return str

def front3(str):
  strCopy = str[:3]
  str = ""
  for i in range(0,3):
    str = strCopy + str
  
  return str
