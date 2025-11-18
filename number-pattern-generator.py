def number_pattern(n):
    if not isinstance(n, int):
        return 'Argument must be an integer value.'
    if n < 1:
        return 'Argument must be an integer greater than 0.'
    number_pattern_to_return = ''
    for number in range(1,n+1):
        number_pattern_to_return += str(number) + ' '
    return number_pattern_to_return.strip()

print(number_pattern(8))