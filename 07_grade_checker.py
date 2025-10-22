grade = input("whats your grade? ")
if grade >= 95 and grade <= 100:
    print("You got an A+")
elif grade >= 90 and grade < 95:
    print("You got an A")
elif grade >= 85 and grade <90:
    print("You got a B+")
elif grade >= 80 and grade <85:
    print("You got a B")
elif grade >=70 and grade <79:
    print("You got a C")
elif grade >=60 and grade <69:
    print("You got a D")
else: grade <=60
print("You failed")