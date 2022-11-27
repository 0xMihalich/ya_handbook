def recursive_digit_sum(number):
    if number == 0:
        return 0
    else:
        return (number % 10) + recursive_digit_sum(number // 10)
