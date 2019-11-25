#Jeremy Yao's solution to CodingBat's Python problems

def cigar_party(cigars, is_weekend):
    if not is_weekend:
      return (cigars >= 40 and cigars <= 60)
    else: 
      return cigars >= 40

def date_fashion(you, date):
  result = 1
  if (you <= 2 or date <= 2):
    result = 0
  elif (you >= 8 or date >= 8):
    result = 2
  
  
  return result

def squirrel_play(temp, is_summer):
  upperLim = 90
  if is_summer:
    upperLim = 100
    
  return temp >= 60 and temp <= upperLim

def caught_speeding(speed, is_birthday):

  modifier = 0
  if (is_birthday):
    modifier = 5
  
  ticket = 1
  
  if (speed <= 60 + modifier):
    ticket = 0
  elif (speed >= 81 + modifier):
    ticket = 2
    
  return ticket

def sorta_sum(a, b):
  result = a + b
  if (result >= 10 and result <= 19):
    result = 20
  
  return result

def alarm_clock(day, vacation):
  time = 'off'
  isWeekday = not( day == 6 or day == 0)
  
  if isWeekday and not vacation:
    time = '7:00'
  elif isWeekday and vacation or not isWeekday and not vacation: 
    time = '10:00'
  
  return time

def love6(a, b):
  return a == 6 or b == 6 or abs(a-b) == 6 or a  + b == 6

def in1to10(n, outside_mode):
  result = n >= 1 and n<= 10 
  if outside_mode: 
    result = n<= 1 or n>=10
  
  return result

def near_ten(num):
  return num % 10 <= 2 or (num - 8) % 10 <= 2
 