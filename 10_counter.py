numbers = [2,4,6,8,10,12,14,16,18,20]
for number in numbers:
    print ("Number is", number)

while True:
        task = input("Enter a task (or type 'stop' to finsh)")
        if task.lower() == 'stop':
            break
        print("You added: ", task)
print("Tasklist")
for i, task in enumerate(numbers, start=1):
     print(f" {task}")


     numbers = [3, 6, 9, 12]
total = 0
i = 0

while i < len(numbers):
    print("Adding:", numbers[i])
    total += numbers[i]
    i += 1

print("Total sum:", total)
