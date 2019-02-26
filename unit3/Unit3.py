input_strings = []


def user_input():
    new_string = ''
    while new_string != 'quit':
        new_string = input("Input a string, or type 'quit' to exit: ")
        if new_string != 'quit':
            input_strings.append(new_string)


user_input()


def stupid_case(string):
    ret = ""
    i = True
    for char in string:
        if i:
            ret += char.upper()
        else:
            ret += char.lower()

        i = not i

    return ret


def stupid_case_for_list(input_strings):
    result = []
    for i in input_strings:
        result.append(stupid_case(i))
    return result


print(stupid_case_for_list(input_strings))
