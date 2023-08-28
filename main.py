# write your code here
favorite_animals=["dog","cat","Monkey","rabbit"]
print(favorite_animals)
print(favorite_animals[1])
favorite_animals.remove("Monkey")


print(favorite_animals)
favorite_animals.append("dog")
for animal in favorite_animals:
    print(f"I love {animal}")

numbers=[1,2,3,4,5]
number_sum=0
for x in numbers:
    number_sum= x + number_sum
    print(number_sum)
