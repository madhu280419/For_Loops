ques = input("write a question")
ans = int(input("enter answer"))
gryggindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0
if ans == 1:
    gryggindor += 1
    ravenclaw += 1
    print("1.Dawn")
elif ans == 2:
    hufflepuff += 1 
    slytherin += 1
    print("2.Dusk")
else:
    print("Wrong input")