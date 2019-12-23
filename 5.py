l = []
while True:
    user_input = input('Enter command: ').split()
    user_command = user_input[0]
    if user_command == 'append':
        l += [int(x) for x in user_input[1:]]
        print(l)
    elif user_command == 'max':
        print(max(l))
    elif user_command == 'min':
        print(min(l))
    elif user_command == 'reverse':
        l.reverse()
        print(l)
    elif user_command == 'second_max':
        sorted_l = sorted(l)
        print(sorted_l[-2])
    elif user_command == 'sort':
        l.sort()
        print(l)
    elif user_command == "sum":
        print(sum([int(x) for x in l]))