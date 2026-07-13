from art_file import ceasar_art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceaser_cipher(text, shift, action):
    text_list = list(text)
    original_index_list = []

    for i in text_list:
        original_index = alphabet.index(i)
        original_index_list.append(original_index)
    shifted_index_list = []

    for i in original_index_list:
        if action == 'encrypt':
            j = (i + shift) % len(alphabet)
        elif action == 'decrypt':
            j = (i - shift) % len(alphabet)
        else:
            print('Invalid action!')
        shifted_index_list.append(j)
    shifted_text_list = []

    for k in shifted_index_list:
        shifted_text_list.append(alphabet[k])
    shifted_text = ''.join(shifted_text_list)
    print(f'This is the {action}ed output : {shifted_text}')



to_continue = True

while to_continue:
    your_task = input('Enter your task: encrypt or decrypt : ')
    your_text = input('Enter your text : ')
    your_shift = int(input('Enter your shift : '))
    ceaser_cipher(text=your_text, shift=your_shift, action=your_task)

    to_restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if to_restart == 'no':
        to_continue = False
        print('Goodbye!')