def toNumber(input: str) -> int:
    try:
        result = 0
        arabNumbers = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7, "VIII": 8, "IХ": 9, "Х": 10}
        if arabNumbers.get(input) is not None:
            result = arabNumbers[input]
        elif int(input) in range(1, 11):
            result = int(input)    
        else:
            raise ValueError()
    except ValueError:
        exit("throws Exception")
    else:
        return result

def toOperation(input: str) -> str:
    if input in ["+", "-", "*", "/"]:
        return input
    else:
        exit("throws Exception")

def main(input: str) -> str:
    try:
        result    = 0
        numberA   = 0
        numberB   = 0
        operation = ""

        inputList = input.split(" ")
        if len(inputList) != 3:
            exit("throws Exception")

        numberA     = toNumber(inputList[0])
        numberB     = toNumber(inputList[2])
        operation   = toOperation(inputList[1])

        if   operation == "+": result = numberA + numberB
        elif operation == "-": result = numberA - numberB
        elif operation == "*": result = numberA * numberB
        elif operation == "/": result = numberA / numberB

        return str(int(result))
    
    except ValueError:
        exit("throws Exception")        

while True:
    print(main(input()))