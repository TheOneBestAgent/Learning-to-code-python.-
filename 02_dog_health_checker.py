#Dog health checker
name = "Roscoe"
weight = 120
is_hungry = True
is_tired = True
previous_weight =120
current_weight = 110

print(f"Checking {name}'s Condition")
if weight > 70:
    print("thats a heavy dog")
else:
    print("thats a light dog")

    if is_hungry and not is_tired:
        print (f"{name} Sounds like you want some food")
    elif is_tired:
        print (f"{name} Sounds like you want to nap")
    else:
        print (f"{name} Lets play a game!!!")
if is_hungry and is_tired:
    print (f"{name} sounds like it's time for you to eat and go rest")

if current_weight < previous_weight:
    print(f"{name} Good job on losing {previous_weight-current_weight} pounds!")