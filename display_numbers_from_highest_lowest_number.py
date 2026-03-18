number_list = []
while True:
    ask_number = int(input("Enter a number: "))
    number_list.append(ask_number)
    number_list.sort(reverse=True)
    print(number_list)