# 🐶 Smart Dog Assistant

print("Welcome to the Smart Dog Assistant!")

# 1️⃣ Collect info from the user
name = input("What's your dog's name? ")
weight = float(input(f"How much does {name} weigh (in lbs)? "))
is_hungry = input("Is your dog hungry? (yes/no) ").lower() == "yes"
is_sleepy = input("Is your dog sleepy? (yes/no) ").lower() == "yes"

# 2️⃣ Analyze and respond
print(f"\nChecking {name}'s condition...")

if weight > 60:
    print(f"{name} is a big, strong pup! 💪")
else:
    print(f"{name} is a smaller, agile dog. 🐾")

if is_hungry and not is_sleepy:
    print("🍖 Time for dinner!")
elif is_sleepy:
    print("💤 Time for a nap!")
else:
    print("🎾 Time to play!")

# 3️⃣ Wrap-up message
print("\nDone! Thanks for using the Smart Dog Assistant 🐕")
