import os
while True :
    os.system("cls")
    try :
        input1 = int(input(" Bilangan - 1 : "))
        input2 = int(input(" Bilangan - 2 : "))
        if input1 == 0 or input2 == 0:
            print("Tolong masukin angka yang bener jangan nilai 0")
    except ValueError :
        print(">>> Error inputan harus bertipe INT ")
    except Exception as e :
        print(f">>> SALAH {e}")

    else:
        i = 1   
        while(i <= input1 and i <= input2):
            if(input1 % i == 0 and input2 % i == 0):
                abc = i
            i = i + 1
        print(f">>> FPB Dari Bilangan : {input1} dan {input2} adalah ", abc)

        while True :
            a = input("ngulang? (y/n) = ")
            os.system("cls")
            if a in ("y","n") :
                break
            else :
                continue

        if a == "y":
            continue
        elif a == "n":
            print("Selamat tinggal")
            break