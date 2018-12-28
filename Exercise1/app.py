my_file = open('people.txt', 'r')
people_list = my_file.read()
my_file.close()
print(people_list)

my_file = open('people.txt', 'r')
lines = [line.strip() for line in my_file.readlines()]

print(lines)
print(lines)

your_friends_list = input(f'enter the names of your friends: ').split(',')
print(your_friends_list)

common_set = {}

people_set = set(lines)
your_friends_set = set(your_friends_list)
print(people_set)
print(your_friends_set)

common_set = people_set.intersection(your_friends_set)
print(common_set)

fo = open('in_town', 'w')
for string in common_set:
    fo.write(f'{string}\n')
fo.close()
"""
for i in range(0,len(lines)):
    print (lines[i])
    for j in range(0,len(your_friends_list)):
        print (your_friends_list[j])
        if lines[i] == your_friends_list[j]:
            common_list.append(your_friends_list[j])
            print(common_list)
"""
