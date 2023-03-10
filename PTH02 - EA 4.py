import math

global grad_bogen
global result

run1 = True
while run1 == True:
    grad_bogen = input("Soll ein Gradmaß oder ein Bogenmaß eingelesen werden? Tippe 'g' oder 'b': ")
    if grad_bogen == "g":
        grad_bogen = "Gradmaß"
        run1 = False
    elif grad_bogen == "b":
        grad_bogen = "Bogenmaß"
        run1 = False
    else:
        print("'" + grad_bogen + "'" + " ist undefiniert, bitte erneut: ")


print(grad_bogen + " eingeben (bei Gleitkommazahl Punkt verwenden):")
number = input()
run2 = True
while run2 == True:
    if number.isdigit() == False:
        if number.count(".") != 1:
            number = input("undefiniert, bitte erneut " + grad_bogen + " eingeben: ")
        elif number.count(".") == 1:
            test_number = number
            test_number = test_number.replace(".", "")
            if test_number.isdigit() == False:
                number = input("undefiniert, bitte erneut " + grad_bogen + " eingeben: ")
            else:
                if grad_bogen == "Gradmaß":
                    number = math.radians(float(number))
                    run2 = False
                else:
                    number = float(number)
                    run2 = False

    else:
        if grad_bogen == "Gradmaß":
            number = math.radians(float(number))
            run2 = False
        else:
            number = float(number)
            run2 = False


sin_cos_tan = input("Gib 's' für Sinus, 'k' für Kosinus oder 't' für Tangens ein: ")
run3 = True
while run3 == True:
    if sin_cos_tan == "s":
        result = "{:.8f}".format(math.sin(number))
        run3 = False
    elif sin_cos_tan == "k":
        result = "{:.8f}".format(math.cos(number))
        run3 = False
    elif sin_cos_tan == "t":
        result = "{:.8f}".format(math.tan(number))
        run3 = False
    else:
        print("undefiniert, bitte erneut: ")
        sin_cos_tan = input("Gib 's' für Sinus, 'k' für Kosinus oder 't' für Tangens ein: ")
        continue

print(result)
