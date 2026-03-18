number_list = []
while True:
    ask_number = int(input("Enter number: "))
    number_list.append(ask_number)
    
    most_duplicate = None
    max_count = 0
    for numbers in number_list:
        number_count = number_list.count(numbers)
        if number_count > max_count:
            max_count = number_count
            most_duplicate = numbers
    print(f"Most duplicate so far: {most_duplicate} (appears {max_count} times)")
    
