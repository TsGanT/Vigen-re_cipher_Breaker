import numpy as np

s = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
     'x', 'y', 'z']
frequency = [0.082, 0.015, 0.028, 0.043, 0.127, 0.022, 0.02, 0.061, 0.07, 0.002, 0.008, 0.04, 0.024, 0.06, 0.075, 0.019,
             0.001, 0.06, 0.063, 0.091, 0.028, 0.01, 0.023, 0.001, 0.02, 0.001]


def coincidence_index(en_text):
    values = np.zeros([26])
    times_of_chara = 0.0
    times_value = 0

    for i in range(26):
        values[i] = 0
    for ch in en_text:
        ch_number = ord(ch) - 97
        values[ch_number] = values[ch_number] + 1
        times_of_chara = times_of_chara + 1
    for i in range(26):
        chara_total_time = values[i]
        times_value = times_value + chara_total_time * (chara_total_time - 1)
    ic_value = times_value/(times_of_chara*(times_of_chara-1))
    return ic_value


def simulate_coincidence_index(sub_string):
    len_sub_string = len(sub_string)
    r = []
    sum_simulate = 0
    for y in range(26):
        r.append(sub_string.count(chr(97 + y), 0, len_sub_string))
    for x in range(0, 26):
        f = (r[x] * frequency[x]) / len_sub_string
        sum_simulate = sum_simulate + f
    return sum_simulate


def guess_len_key(en_text):
    guess_key_len = 1
    d = {}
    while True:
        for i in range(len(en_text)):
            n = i % guess_key_len
            if n not in d:
                d[n] = ''
            d[n] = d[n] + en_text[i]
        sum_index = sum(coincidence_index(d[j]) for j in range(guess_key_len)) / guess_key_len
        if 0.064 <= sum_index <= 0.073:
            print("IoC value here: %s" % sum_index)
            break
        else:
            guess_key_len += 1
            d = {}
    return guess_key_len, d


def crack_key(key_len, dir_sub_string):
    key_value = ''
    for i in range(key_len):
        sub_string = dir_sub_string[i]
        for offset in range(26):
            out = ""
            for j in sub_string:
                c = int((ord(j) - ord('a') - offset) % 26 + ord('a'))
                out += chr(c)
            sum_index = simulate_coincidence_index(out)
            if 0.052 <= sum_index <= 0.074:
                key_value = key_value + s[offset]
                break
    return key_value
