from encrypt_and_decrypt import encrypt, decrypt
from break_vg import guess_len_key, crack_key
import re


def pretreatment(input_string):
    pattern = re.compile('[\n]|\d|\W')
    plain_1 = re.sub(pattern, '', input_string).lower()
    return plain_1


if __name__ == '__main__':
    plain_text = """I’ve seen the hopeful faces of young graduates and our newest military officers.  I’ve mourned with grieving families searching for answers, and found grace in a Charleston church.  I’ve seen our scientists help a paralyzed man regain his sense of touch, and our wounded warriors walk again.  I’ve seen our doctors and volunteers rebuild after earthquakes and stop pandemics in their tracks.  I’ve learned from students who are building robots and curing diseases and who will change the world in ways we can’t even imagine.  I’ve seen the youngest of children remind us of our obligations to care for our refugees, to work in peace, and above all to look out for each other.Over the course of these eight years, I have seen the goodness, the resilience, and the hope of the American people.  I’ve seen neighbors looking out for each other as we rescued our economy from the worst crisis of our lifetimes.  I’ve hugged cancer survivors who finally know the security of affordable health care.  I’ve seen communities like Joplin rebuild from disaster, and cities like Boston show the world that no terrorist will ever break the American spirit."""
    real_plain_text = pretreatment(plain_text)
    print(real_plain_text)
    en_key = "watermelon"
    cipher_text = encrypt(real_plain_text, en_key)
    print(cipher_text)
    origin_text = decrypt(cipher_text, en_key)
    print(origin_text)

    l, guess_string = guess_len_key(cipher_text)
    print(l)
    print(guess_string)

    final_key = crack_key(l, guess_string)
    print("Finally: ", final_key)
