import getpass
import time

input_signs = "abcdefghij"
input_signs1 = "!\"#$%&€\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz{|}~'"


sentence = """Herzlich Willkommen zum Passwort-Knacker!
Geben Sie Ihr Passwort ein um es hier ausgeben zu lassen.
Dies ist eine Übung und sie funktioniert.
Sie sollten keine echten Passwörter verwenden, sonst sind Sie selbst schuld :P!
"""
print(sentence)

pswd = getpass.getpass('Write your password here:')

list_input_signs = list(input_signs)
list_pw = list(pswd)
index = 0
figured_pw = ""

# print(list_input_signs[2])
for letter2 in list_pw:
    for letter in input_signs1:
        time.sleep(0.051)
        if list_pw[index+1] == letter:
            print(list_pw[index + 1])
            figured_pw = figured_pw + letter
            time.sleep(0.5)
            print(f"Das Passwort ist {letter}")
            time.sleep(1)
            index = index + 1
            break
    else:
        print(letter)


# while index < len(list_pw):
#    print(f"Das Passwort ist {figured_pw}")
# for letter in pswd:
#    print(letter)
#    time.sleep(.7)

# for letter in pswd:
#   if list_input_signs[index] != letter:
#      print(list_input_signs[index])
#     list_input_signs[index] = list_input_signs[index+1]
#    time.sleep(0.2)
#   elif list_input_signs[index] == letter
#      print(f"Wir haben einen Buchstaben {letter}")
#     break
# else:
#   print("Du Schlaumeier! Nimm bitte nur Zeichen die gültig sind!")
#  break
