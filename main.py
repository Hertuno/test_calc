def main(input: str) -> int:
    try:
        result      = 0
        inputList   = input.split(" ", 2)
        numberA     = int(inputList[0])
        numberB     = int(inputList[2])
        operation   = str(inputList[1])
        
        if numberA in range(1, 11) and numberB in range(1, 11) and operation in ["+", "-", "*", "/"]:
            if   operation == "+": result = numberA + numberB
            elif operation == "-": result = numberA - numberB
            elif operation == "*": result = numberA * numberB
            elif operation == "/": result = numberA / numberB
        else:
            raise NameError('throws Exception')
    except (ValueError, ZeroDivisionError, NameError) as err:
        exit(err)
    else:
        return int(result)

while True:
    print(main(input("Введите выражение: ")))