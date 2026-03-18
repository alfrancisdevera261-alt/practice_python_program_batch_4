number_list = []
for i in range(10):
    ask_number = int(input("Enter a number: "))
    number_list.append(ask_number)

result = []
for number_count in number_list:
    if number_list.count(number_count) != 1:
        if number_count not in result:
            result.append(number_count)
print(result)