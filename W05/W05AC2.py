friend_list = []
friend = None

while friend != 'end':
    friend = input("Type the name of a friend:")
    friend_list.append(friend)

friend_list.pop()
print("Your friends are:")

for i in range(len(friend_list)):
    print(friend_list[i])