result_task1 = 9 ** 0.5 * 5
print(result_task1)

result_task2 = (9.99 > 9.98) and (1000 != 1000.1)
print(result_task2)


result_task3_1 = 2 * 2 + 2
result_task3_2 = 2 * (2 + 2)
print(result_task3_1)
print(result_task3_2)
print(result_task3_1 == result_task3_2)



number_string = '123.456'

number_float = float(number_string)

number_float *= 10

first_digit_after_decimal = int(number_float) % 10

print(first_digit_after_decimal)  