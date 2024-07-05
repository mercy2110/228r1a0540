def check_is_perfect_number(input_number):
    divisors_sum = 0
    for i in range(1, input_number):
        if input_number % i == 0:
            divisors_sum += i

    if divisors_sum == input_number:
        print(f"The number {input_number} is a perfect number.")
    else:
        print(f"The number {input_number} is not a perfect number.")

input_number = int(input("Enter a positive integer: "))
check_is_perfect_number(input_number)
