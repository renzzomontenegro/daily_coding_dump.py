import random
import string

def generate_plate_number():
    rand_letter = random.choices(string.ascii_uppercase, k=3)
    appended_letter = "".join(rand_letter)

    rand_num = string.digits

    rand_num = random.choices(rand_num, k=4)
    appended_num = "".join(rand_num)

    print(f'\n{appended_letter}-{appended_num}')



generate_plate_number()