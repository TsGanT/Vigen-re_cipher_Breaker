def encrypt(input_plain_text, key):
    plain_text_len = len(input_plain_text)
    key_len = len(key)

    en_time = plain_text_len // key_len
    reminder_time = plain_text_len % key_len

    out = ""
    for i in range(en_time):
        for j in range(0, key_len):
            c = int((ord(input_plain_text[i * key_len + j]) - ord('a') + ord(key[j]) - ord('a')) % 26 + ord('a'))
            out += chr(c)

    for i in range(reminder_time):
        c = int((ord(input_plain_text[i * key_len + i]) - ord('a') + ord(key[i]) - ord('a')) % 26 + ord('a'))
        out += chr(c)

    return out


def decrypt(input_cipher_text, key):
    cipher_text_len = len(input_cipher_text)
    key_len = len(key)

    en_time = cipher_text_len // key_len
    reminder_time = cipher_text_len % key_len

    out = ""
    for i in range(en_time):
        for j in range(0, key_len):
            c = int((ord(input_cipher_text[i * key_len + j]) - ord('a') - (ord(key[j]) - ord('a'))) % 26 + ord('a'))
            out += chr(c)

    for i in range(reminder_time):
        c = int((ord(input_cipher_text[i * key_len + i]) - ord('a') - (ord(key[i]) - ord('a'))) % 26 + ord('a'))
        out += chr(c)

    return out
