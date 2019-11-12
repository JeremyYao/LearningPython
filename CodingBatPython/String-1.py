# Jeremy Yao's (terrible) solutions to CodingBat's Python problem sets
def hello_name(name):
  return 'Hello ' + name + '!'

def make_abba(a, b):
  return a + b + b + a

def make_tags(tag, word):
  return "<" + tag + ">" + word + "</" + tag + ">"

def make_out_word(out, word):
  return out[:2] + word + out[2:]

def extra_end(str):
  return str[-2:] +  str[-2:] +  str[-2:]

def first_two(str):
  result = str 
  if len(str) > 2:
    result = str[:2]
  return result 
