names = ["Randy", "Lewis", "Shawn", "Senpai", "Diego"]

print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])

message = "Waddup ma boi " + names[0].capitalize()

print(message)

print(names)

names.append("Carlos")

print(names)

del names[0]

print(names)

names.insert(0, "Randy")
print(names)