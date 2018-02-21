
#user input , Keep asking input until user gives right input

input_query=[]


while True:
    user_input = int(input('Input first no '))
    user_input2 = int(input('Input second no '))
    if 1 < user_input < user_input2 < 676:
        input_query.extend([user_input,user_input2])
        break
    else:
        print 'please input valid no'




#main cipher program


def cipher_values(user_in):
    cipher = {}
    values = map(chr, range(65, 91))

    _chr_update = 1
    _chunks = 27

    update_list = values[:]
    cipher_value = values[:]
    for i in range(27):
        cipher.update({value: update_list[value - _chr_update] for value in range(_chr_update, _chunks)})
        if cipher_value:
            update_list = [cipher_value[0] + value for value in values]

        _chr_update = _chunks

        _chunks += 26

        cipher_value = cipher_value[1:]

    return list(map(lambda x:cipher[x],list(range(user_in[0],user_in[1]+1))))

for i in cipher_values(input_query):
    print i
    
    
#sample input:

#Input first no 25
#Input second no 29
#Y
#Z
#AA
#AB
#AC
