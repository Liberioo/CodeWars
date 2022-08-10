def decode_bits(bits):
    bits = bits.strip('0') #handles extra zeros at star and beginning
    if '0' not in bits: return '.' #if only 1s in string returns '.'
    time = 0 
    if bits[0] == '0': #checks the length of the first sequence
        time = bits.find('1')
        aux = bits[bits.find('1'):]
        flag = False #flag to alternate between lookinh at 1s and 0s sequence
    elif bits[0] == '1':
        time = bits.find('0')
        aux = bits[bits.find('0'):]
        flag = True
    while aux != '':
        if flag:
            if aux.find('1') != -1 and aux.find('1')+1 < time: #checks if its not last sequence
                time = aux.find('1') #if sequence is shorter than any others before, time becomes its length
            if aux.find('1') != -1:
                aux = aux[aux.find('1'):] #gets the rest of unchecked sequences
            else:
                if len(aux) < time: time = len(aux) #if it was last sequence, checks length and ends loop
                aux = ''
            flag = False #changes flag value to alternate from looking at 0s to looking at 1s
        else:
            if aux.find('0') != -1 and aux.find('0')+1 < time:
                time = aux.find('0')
            if aux.find('0') != -1:
                aux = aux[aux.find('0'):]
            else:
                if len(aux) < time: time = len(aux)
                aux = ''
            flag = True
    return bits.replace('111'*time, '-').replace('000'*time, ' ').replace('1'*time, '.').replace('0'*time, '').replace('0', ' ')