gap_number = 0
N_number = 0
gap_is_open = False
with open("Poil_scaffold.fa", 'r') as f:
    file = f.read()
    for i in file:
        if i == "N" and gap_is_open == True:
            N_number += 1
        else:
            if i == "N":
                gap_number += 1
                N_number += 1
                gap_is_open = True
            else:
                gap_is_open = False
print(gap_number)
print(N_number)