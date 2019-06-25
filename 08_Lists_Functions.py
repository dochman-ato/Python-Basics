#1
lucky_numbers = [4, 8, 9, 18, 42, 56]
friends = ["Kevin", "Jack", "Jane", "Oscar", "Toby"]
print(friends)
print(lucky_numbers)

#2
friends.extend(lucky_numbers)
print(friends)

#3
lucky_numbers = [4, 8, 9, 18, 42, 56]
friends = ["Kevin", "Jack", "Jane", "Oscar", "Toby"]

#4
friends.append("Olek")
print(friends)

#5
friends.insert(1, "Aleksander")
print(friends)

#6
friends.remove("Olek")
print(friends)

#7
friends.clear()
print(friends)

#8
lucky_numbers = [4, 8, 9, 18, 42, 56]
friends = ["Kevin", "Jack", "Jane", "Oscar", "Toby"]

#9
tmp = friends.pop()
print(friends, tmp)

#10
print(friends.index("Jane"))

#11
print(friends.count("Jim"))

#12
friends.sort()
lucky_numbers.sort()
print(friends, lucky_numbers)

#13
friends.reverse()
lucky_numbers.reverse()
print(friends, lucky_numbers)

#14
friends2 = friends.copy()
print(friends2)

#15
print(len(friends2))
