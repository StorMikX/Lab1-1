calculator = True
while calculator:
    try:
        val_1 = float(input("Введите число: "))
    except ValueError:
        print("Некорректный ввод числа")
        continue
    try:    
        val_2 = float(input("Введите число: "))
    except ValueError:
        print("Некорректный ввод числа")
        continue
    operator = input("Введите операцию: ")
    if operator == "+":
        result = val_1 + val_2
        print(result)
    elif operator == "-":    
        result = val_1 - val_2        
        print(result)
    elif operator == "*":  
        result = val_1 * val_2
        print(result)
    elif operator == "/":
        if val_2 != 0:    
            result = val_1 / val_2
            print(result)
        else:
            print("Деления на ноль не существует!!!!")     
    else:
        print("Неподдерживаемая операция!!!")
    


    count = 1
    while True:
        command = (input("Продолжить? (Y/N): "))
        if count == 3:
            exit()
        elif command == "Y":
            break
        elif command == "N":
            calculator = False
            break 
        else:
            count = count + 1 
            
    
        
    
            
