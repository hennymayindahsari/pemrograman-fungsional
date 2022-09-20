#No.1
def square(x):
  return x**2

def sum_squares(*n):
  sum = 0
  for i in n:
    sum += square(i)
  return sum

print(sum_squares(1,2,3))


#No. 2
def triangular(n):
  if (n < 0):
    return print("Hanya Masukkan bilangan positif")
  elif (type(n) != int):
    return print("Hanya Masukkan bilangan bulat")

  return int(n * (n+1)/2)

print(triangular(5))
triangular(-5)
triangular(5.2)


#No .3
def pangkat(bilangan,pangkat):
  if (bilangan < 0):
    return print("Hanya Masukkan bilangan positif")
  elif (type(bilangan) != int):
    return print("Hanya Masukkan bilangan bulat")

  return bilangan**pangkat
  
pangkat(3,2)


#No. 4
def isPalindrome(s):
  s = s.lower()
  s = s.replace(" ","")
  return s == s[::-1]

#kata = (input("Input kata : "))
kata1 = "No lemon, no melon"
kata2 = "Madam, I’m Adam"
print (isPalindrome(kata1))
print (isPalindrome(kata2))