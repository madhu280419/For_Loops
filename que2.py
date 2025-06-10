print('Q1) Do you like Dawn or Dusk?')
print('  1) Dawn')
print('  2) Dusk')
answer = int(input('Enter answer (1-2): '))
gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0
if answer == 1:
  gryffindor += 1
  ravenclaw += 1
elif answer == 2:
  hufflepuff += 1
  slytherin +=1
else: