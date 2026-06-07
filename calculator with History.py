#making a calculator that also show a history

HISTORY_FILE="history.txt"

def show_history():
    file = open(HISTORY_FILE, 'r')
    lines=file.readlines()
    if len(lines)==0:
        print("No history found.")
    else:
        for line in reversed(lines):
            print(line.strip())
    
    file.close()
    
def clear_history():
    file = open(HISTORY_FILE, 'w')
    file.close()
    print("History cleared.")
    
def save_to_history(equation, result):
    file = open(HISTORY_FILE, 'a')
    file.write(equation + "=" + str(result) + "\n")
    file.close()
    
def calculate(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print("Invalid input, use format: number operator number (e.g 8+8=16).")
        

    num1=float(parts[0])
    op = parts[1]
    num2=float(parts[2])

    if op == "+":
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print("Cannot divide by zero.")
            return
        result = num1/num2
    else:
        print("Invalid operator. Use Only + - * /.")
        return
    
    if int(result) == result:
        result = int(result)
    print("Result: ", result)
    save_to_history(user_input, result)
    
def main():
    print('=====SIMPLE CALCULATOR (type history, clear or exit.)')
    while True:
        User_input= input("Enter Calculation (+ - * /) or command (history, clear and exit): ").lower()
        if User_input =='exit':
            print("Good Bye")
            break
        elif User_input=='history':
            show_history()
        elif User_input == 'clear':
            clear_history()
        else:
            calculate(User_input)
            
main()