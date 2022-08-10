MORSE_CODE = { 'A':'.-', 'B':'-...',
                'C':'-.-.', 'D':'-..', 'E':'.',
                'F':'..-.', 'G':'--.', 'H':'....',
                'I':'..', 'J':'.---', 'K':'-.-',
                'L':'.-..', 'M':'--', 'N':'-.',
                'O':'---', 'P':'.--.', 'Q':'--.-',
                'R':'.-.', 'S':'...', 'T':'-',
                'U':'..-', 'V':'...-', 'W':'.--',
                'X':'-..-', 'Y':'-.--', 'Z':'--..',
                '1':'.----', '2':'..---', '3':'...--',
                '4':'....-', '5':'.....', '6':'-....',
                '7':'--...', '8':'---..', '9':'----.',
                '0':'-----', ', ':'--..--', '.':'.-.-.-',
                '?':'..--..', '/':'-..-.', '-':'-....-',
                '(':'-.--.', ')':'-.--.-'}

def decode_bits(bits):
    bits = bits.strip('0')
    if '0' not in bits:
        return '.'
    time = 0
    if bits[0] == '0':
        time = bits.find('1')
        aux = bits[bits.find('1'):]
        flag = False
    elif bits[0] == '1':
        time = bits.find('0')
        aux = bits[bits.find('0'):]
        flag = True
    while aux != '':
        if flag:
            if aux.find('1') != -1 and aux.find('1')+1 < time:
                time = aux.find('1')
            if aux.find('1') != -1:
                aux = aux[aux.find('1'):]
            else:
                if len(aux) < time:
                    time = len(aux)
                aux = ''
            flag = False
        else:
            if aux.find('0') != -1 and aux.find('0')+1 < time:
                time = aux.find('0')
            if aux.find('0') != -1:
                aux = aux[aux.find('0'):]
            else:
                if len(aux) < time:
                    time = len(aux)
                aux = ''
            flag = True
    return bits.replace('111'*time, '-').replace('000'*time, ' ').replace('1'*time, '.').replace('0'*time, '').replace('0', ' ')


def decode_morse(morse_code):
    ans = ''
    while morse_code != '':
        if morse_code[0] == ' ':
            ans += ' '
        while morse_code != '' and morse_code[0] == ' ':
            morse_code = morse_code[1:]
        current = morse_code[:morse_code.find(' ')]
        if morse_code.find(' ') != -1:
            ans += MORSE_CODE[current]
            morse_code = morse_code[morse_code.find(' ')+1:]
        elif morse_code != '':
            ans += MORSE_CODE[morse_code]
            morse_code = ''

    return ans.strip()


bits = '1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011'
print(decode_bits('11100011100011100000001'))
