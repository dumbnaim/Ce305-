import datetime
def HamEncoding(msg):
    m = len(msg)
    x = 0
    while 2 ** x < m + x + 1:
        x += 1
    print(f"X = {x}")

    encoded = [''] * (m + x)
    j = 0
    for i in range(1, m + x + 1):
        if i & (i - 1) == 0:
            encoded[i - 1] = 'P'
        else:
            encoded[i - 1] = msg[j]
            j += 1
    for i in range(x):
        pos = 2 ** i
        parity = 0
        for j in range(1, len(encoded) + 1):
            if j & pos:
                if encoded[j - 1] == '1':
                    parity ^= 1
        encoded[pos - 1] = str(parity)

    return ''.join(encoded)

def HamDecoding(rcv, x):
    n = len(rcv)
    error_bin = ['0'] * x
    for i in range(x):
        pos = 2 ** i
        parity = 0
        for j in range(1, n + 1):
            if j & pos:
                if rcv[j - 1] == '1':
                    parity ^= 1
        error_bin[x - i - 1] = str(parity)

    error_pos = int(''.join(error_bin), 2)
    if error_pos == 0:
        return 'No error'
    else:
        corrected = list(rcv)
        corrected[error_pos - 1] = '1' if rcv[error_pos - 1] == '0' else '0'
        return f"Error at Position {error_pos}, and correct data: {''.join(corrected)}"

#printimg date:
print("Date: ", datetime.datetime.today())
# User inputs for original 
org_sig1 = input("Enter the bits for encoding: ")
encoded_sig1 = HamEncoding(org_sig1)
print(encoded_sig1)
#received messages
received_sig4 = input("Enter your received number: ")
print(HamDecoding(received_sig4, 4))