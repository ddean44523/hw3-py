sumOfNumbs = 0

def digit_sum(n):
  global sumOfNumbs
  if len(str(n)) == 1:
    sumOfNumbs += n
  else:
    first_dig = firstDig(n)
    sumOfNumbs += first_dig
    digit_sum(restDig(n))
  return(sumOfNumbs)

def firstDig(n):
  ''''returns first dig of n'''
  return n // 10 ** (len(str(n)) - 1)
  #doesn't return 0 with 00n

def restDig(n):
  '''returns rest of digits'''
  return n % 10 ** (len(str(n))- 1)

def run():
  Uin = int(input("enter numb: "))
  print(digit_sum(Uin))
  # 0 is actually a big problem

if __name__ == "__main__":
  run()

