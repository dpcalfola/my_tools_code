# Type checker and caster
# If input value is not integer return (False, -1)
def non_integer_filter(s: str) -> (bool, int):
    try:
        casted = int(s)
        return True, casted
    except ValueError:
        print('\nError: Input value should be integer')
        return False, -1
