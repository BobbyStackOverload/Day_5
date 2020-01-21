# caeser_code = input("ibh zhfg hayrnea jung lbh unir yrnearq")
caeser_code = "ibh zhfg hayrnea jung lbh unir yrnearq"
letters = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz" 
number = 13
solve = ""

for index in range(len(caeser_code)):
    add_to = ""
    for innderindex in range(len(letters)):
        if caeser_code[index] == letters[innderindex]:
            rotated_index = innderindex + number
            add_to = str(letters[rotated_index])
            break
        else:
            add_to = caeser_code[index]

    solve = solve + add_to

print(solve)