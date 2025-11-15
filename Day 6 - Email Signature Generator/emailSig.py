
def generate_signature(name, title, company):
    name = f"{prefix}\t{name} \n\t{title} \n\t{company}"
    return name

while True:
    try:
        info = input(f"\nEnter Name, Title, Company (Separated by ', '): ")
        name, title, company = info.split(', ')

        prefix = ''
        first_letter = name[0].upper()
        
        a_i = tuple(chr(i) for i in range(ord('A'), ord('I') + 1))
        j_r = tuple(chr(i) for i in range(ord('J'), ord('R') + 1))
        s_z = tuple(chr(i) for i in range(ord('S'), ord('Z') + 1))

        if first_letter.startswith(a_i):
            prefix = '>>'
        elif first_letter.startswith(j_r):
            prefix = '--'
        elif first_letter.startswith(s_z):
            prefix = '::' 

        print(f"\n{generate_signature(name, title, company)}")

    except ValueError:
        print(f"\nInvalid Input. Please try again.")
        continue