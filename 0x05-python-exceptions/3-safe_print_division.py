def safe_print_division(a, b):
    try:
        value = a / b
    except:
        value = None
    finally:
        print("Inside result: {}".format(value))
        return value
