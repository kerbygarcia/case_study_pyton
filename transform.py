def letter_grade(avg):
    if avg >= 96:
        return 'A'
    elif avg >= 90:
        return 'B'
    elif avg >= 84:
        return 'C'
    elif avg >= 75:
        return 'D'
    else: return 'F'

avg = int(input("Enter Num: "))

letter_grade(avg)

print(letter_grade(avg))

#wait 'di pa yan final
#-kerbs
