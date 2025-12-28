import random
import string

def generate_plate_number():
    def generate_letters():
        rand_letter = random.choices(string.ascii_uppercase, k=3)
        appended_letter = "".join(rand_letter)
        return appended_letter

    def generate_numbers():
        rand_num = random.choices(string.digits, k=4)
        appended_num = "".join(rand_num)
        return appended_num

    print(f'\n{generate_letters()}-{generate_numbers()}')



generate_plate_number()