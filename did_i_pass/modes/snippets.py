# Type checker and caster
# If input value is not integer return (False, -1)
def non_integer_filter(s: str) -> (bool, int):
    try:
        casted = int(s)
        return True, casted
    except ValueError:
        print('\nError: Input value should be integer')
        return False, -1


# Get_ordinal
def get_ordinal(n: int) -> (bool, str):
    # return (is_success, 'ordinal' or 'error message')
    if n <= 0:
        return False, 'Error: Input should be positive number'
    elif n > 100:
        return False, 'Error: Too large number (available number are 1~99)'
    elif n % 10 == 1 and n != 11:
        return True, f'{n}st'
    elif n % 10 == 2 and n != 12:
        return True, f'{n}nd'
    elif n % 10 == 3 and n != 13:
        return True, f'{n}rd'
    else:
        return True, f'{n}th'


# # testcode
# num_arr = [i for i in range(101)]
#
# for i in num_arr:
#     print(get_ordinal(i))
