for i in range(0,21):
    if i % 2 ==0:
        print(i)
        
for i in range (1,51):
    if i % 5 == 0:
        print(i)
        
for i in range(1, 101):
    if i % 3 != 0:
        print(i)


for num in range(0, 11):
    if num % 2 != 0:
        num = num ** 2
        print(num)
        
for i in range(0,101):
    if i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz)")
    elif i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    else:
        print(i)
        
for i in range(1, 6):
  for j in range(1, 6):
    print(i * j)