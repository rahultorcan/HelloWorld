numbers = [1,2,3,4,5,6]
numbers.append(7)
print(numbers)
numbers.insert(2,9)  # use control p over insert to see type of arguments
print(numbers)
numbers.remove(2)
print(numbers)
#numbers.clear()
#print(numbers)

print(1 in numbers) # to check if 1 is in the list, gives boolean value

print(len(numbers))

for item in numbers:
    print(item)

i = 0
while i < len(numbers):
    print(numbers [i])
    i=i+1

