#if-else logic
isRainyDay=False
isBadMood=False

if isRainyDay:
    print("Bring Umbrella")
elif isBadMood:
    print("Bring friends")
else:
    print("Enjoy your time")

print("Exit Logic Statement")

# Loop
l=[5,3,4,7,8]
for i in range(3,10):
    print(i)

for i in l:
    print(i)
    print("next line with i = ", i)

i = 0

while i <= 8:
    print("i = ", i)
    i = i + 1

while True: # Infinite Loop
    print("Before Break")
    break
    print("After Break")

print("Exited from while loop")

j=9

while True:
    j=j-1
    if j>3:
        print("Value of j is ",j)
    else:
        break

import numpy

correct = 0
wrong = 0
for i in range(10):
    a = numpy.random.randint(100)
    b = numpy.random.randint(100)

    print("Find the value of ", a," + ", b)
    c = input("Write your answer: ")
    if a+b == int(c):
        correct = correct + 1
        print("Your Answer of ", c, " is correct!")
    else:
        wrong = wrong + 1
        print("Wrong Answer, The correct answer is:", a+b)

score = correct - wrong
print("Your Score is:", score)
print("Correct Answer: ", correct)
print("Wrong Answer: ", wrong)