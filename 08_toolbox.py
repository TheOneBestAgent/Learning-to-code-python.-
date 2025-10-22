tools = ["hammer", "screwdriver", "wrench"]

print(tools[0])  # hammer
tools.append("drill")  # add new item
print(len(tools))  # number of items

for tool in tools:
    print("Using:", tool)
