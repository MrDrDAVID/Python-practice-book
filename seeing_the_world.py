places = ['gotham', 'metropolis', 'watch tower', 'fire nation', 'kanto region']

print("Here is the original list: ")
print(places)

print("\nHere is the sorted list: ")
print(sorted(places))

print("\nOnce again here is the original list: ")
print(places)

print("\nHere is the list in reverse alphabetical order: ")
print(sorted(places, reverse = True))

print("\nAgain, here is the original list: ")
print(places)

places.reverse()
print("\nHere is the list in reverse order: ")
print(places)

places.reverse()
print("\nHere is the list reversed back to original order: ")
print(places)

places.sort()
print("\nHere is the list sorted using sort(): ")
print(places)

places.sort(reverse = True)
print("\nHere is the list sorted in reverse alpabetical using sort(): ")
print(places)