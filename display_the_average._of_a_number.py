number_list = []
while True:
    ask_number = int(input("Enter a number: "))
    number_list.append(ask_number)
    
    for number in number_list:
        average = sum(number_list) / len(number_list)
        print(average)