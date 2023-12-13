if __name__ == '__main__':
    N = int(input())
    
result_list = []    

def translate_cmd(aux_str):
    aux_cmd = aux_str.split(' ')
    return aux_cmd
    
def operations(commands):
    if commands[0] == 'insert':
        result_list.insert(int(commands[1]), int(commands[2]))
    elif commands[0] == 'print':
        print(result_list)
    elif commands[0] == 'remove':
        result_list.remove(int(commands[1]))
    elif commands[0] == 'append':
        result_list.append(int(commands[1]))
    elif commands[0] == 'sort':
        result_list.sort()
    elif commands[0] == 'pop':
        result_list.pop()
    elif commands[0] == 'reverse':
        result_list.reverse()
    
iterations = 0

while iterations < N:
    # print(f"iteration: {iterations}")
    string = input()
    cmd = translate_cmd(string)
    operations(cmd)
    iterations += 1
    # print(f"input: {string}")
    