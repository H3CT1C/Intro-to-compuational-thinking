import ast

def input_meal(name):
    f1 = open(name, 'r')
    myd = ast.literal_eval(f1.read())
    return myd

def input_operate():
    dict_1 = open("operating_hour.txt", 'r')
    dict_list = []
    o_h = {}  # for the dictionary
    for words in dict_1:  # first we append to the list and remove the new line character
        dict_list.append(words.strip("\n"))

    # print(dict_list)
    dict_list = [i.split(",") for i in dict_list]  # to split the list via the commas

    # print(dict_list)
    for values in dict_list:  # to create the dictionary
        o_h[values[0]] = values[1:]

    for key, values in o_h.items():  # a little brute forcey, change the strings to integer for time
        values[0] = int(values[0])
        values[1] = int(values[1])
        values[4] = int(values[4])
        values[5] = int(values[5])

    return o_h