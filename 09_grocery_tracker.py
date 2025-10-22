#Grocery Loop Tracker

groceries = ["milk", "bread" , "eggs", "apples" ]

print("grocery list:")
for item in groceries:
      print("-", item) 
#add new items dynamically
while True:
    new_item = input("Add another item (or 'done' to finsh): ")
    if new_item.lower() == "done":
        break
    groceries.append(new_item)

print("Final Grocery List:")
for i, item in enumerate(groceries, start=1):
    print(f"{i}. {item}")
