alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
your_task = input('Enter your task: encrypt or decrypt : ')
your_text = input('Enter your text : ')
your_shift = int(input('Enter your shift : '))

def encrypt(text, shift):
    text_list = list(text)
    original_index_list = []

    for i in text_list:
        original_index = alphabet.index(i)
        original_index_list.append(original_index)
    shifted_index_list = []

    for i in original_index_list:
        j = (i + shift) % len(alphabet)
        shifted_index_list.append(j)
    shifted_text_list = []

    for k in shifted_index_list:
        shifted_text_list.append(alphabet[k])
    shifted_text = ''.join(shifted_text_list)
    print(shifted_text)

def decrypt(text, shift):
    text_list = list(text)
    original_index_list = []

    for i in text_list:
        original_index = alphabet.index(i)
        original_index_list.append(original_index)

    shifted_index_list = []
    for i in original_index_list:
        j = (i - shift) % len(alphabet)
        shifted_index_list.append(j)

    shifted_text_list = []
    for k in shifted_index_list:
        shifted_text_list.append(alphabet[k])
    shifted_text = ''.join(shifted_text_list)
    print(shifted_text)
    
if your_task == 'encrypt':
    encrypt(your_text,your_shift)
elif your_task == 'decrypt':
    decrypt(your_text,your_shift)
else:
    print('Invalid task!')