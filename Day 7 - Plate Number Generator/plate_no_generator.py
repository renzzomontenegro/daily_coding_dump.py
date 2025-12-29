import random
import string

"""Store Previously Generated Plate Number"""
already_generated = set()

"""Main Function for Generating Plate Number"""
def generate_plate_number():
    def generate_letters():
        """Generates a list of random letters"""
        rand_letter = random.choices(string.ascii_uppercase, k=3)

        """Constraint: No Repeating Letters (ex. AAA)"""
        if rand_letter[0] == rand_letter[1]:
            rand_letter.remove(rand_letter[1])
            new_letter = random.choices(string.ascii_uppercase)
            rand_letter.insert(1, new_letter[0])

        elif rand_letter[1] == rand_letter[2]:
            rand_letter.remove(rand_letter[2])
            new_letter = random.choices(string.ascii_uppercase)
            rand_letter.insert(2, new_letter[0])

        """Combine Letters"""
        appended_letters = "".join(rand_letter)

        return appended_letters

    def generate_numbers():
        """Generates a list of random numbers"""
        rand_num = random.choices(string.digits, k=4)

        """Constraint: No Repeating Numbers (ex. 111)"""
        if rand_num[0] == rand_num[1]:
            rand_num.remove(rand_num[1])
            new_num = random.choices(string.digits)
            rand_num.insert(1, new_num[0])

        elif rand_num[1] == rand_num[2]:
            rand_num.remove(rand_num[2])
            new_num = random.choices(string.digits)
            rand_num.insert(2, new_num[0])

        """Combine Numbers"""
        appended_num = "".join(rand_num)

        return appended_num
    
    """Display Formatted Plate Number"""
    plate_number = (f'{generate_letters()}-{generate_numbers()}')
    return plate_number

"""Simulate Plate Number Generation"""
for i in range(10):
    plate_number = generate_plate_number()
    already_generated.add(plate_number)
    print(f'\nNewly Generated Plate Number: {plate_number}')
    print(f'\nUpdated Plate Number List: {already_generated}')