def encode():   # encoder
    password = input()
    result = ''
    for i in password:
        new_digit = str((int(i) + 3) % 10)
        result += new_digit
    return result

if __name__ == '__main__':  # main function
    menu = True
    while menu:
        print()
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        print('Please enter an option: ', end='')

menu_option = int(input())

        if menu_option == 1:    # Option 1: Encoder
            print('Please enter your password to encode: ', end='')
            encoded_password = encode()
            print('Your password has been encoded and stored!')
	if menu_option == 2:	# Option 2: Decoder
		pass
        if menu_option == 3:    # Option 3: Quit
            menu = False
