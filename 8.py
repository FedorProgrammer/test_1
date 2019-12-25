EMPTY = '____'
data = [EMPTY] * 5

while True:
    user_input = input('Enter a command: ').split()
    command = user_input[0]
    if command == 'show':
        print(data)
    elif command == 'free':
        print(data.count(EMPTY))
    elif command == 'park':
        free_pos = data.index(EMPTY)
        data[free_pos] = user_input[1]
        print(data)
    elif command == 'leave':
            data[data.index(user_input[1])] = EMPTY
            print(data)
    else:
        break

