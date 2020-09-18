def digit_sum(n):
  if n == 0:
    return 0
  else:
    l = n % 10 #last digit
    n = l + digit_sum(n//10)  
    return n

def run():
 Uin = int(input(""))
 print(digit_sum(Uin))

if __name__ == "__main__":
  run()