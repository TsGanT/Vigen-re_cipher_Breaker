import numpy as np


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


if __name__ == '__main__':
    ic_v = coincidence_index("hdgokdxfcdcmrkqeqdqvfuekrbfzdmtqhgdmqudqdrdokcqhrrsgnndqqkzudqsznsrtzqszzszlhdqrkmqsmgdkfnmqczzgkzsnhxbdhhuddmsgqdcenfnndnddnjdzaznjezs")
    print(ic_v)
