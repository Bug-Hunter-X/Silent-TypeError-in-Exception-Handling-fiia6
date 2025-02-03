def function_with_uncommon_error_solution(data):
    try:
        if not isinstance(data, dict):
            raise TypeError("Input data must be a dictionary.")
        result = data['key'] + 1
        return result
    except KeyError as e:
        print(f"KeyError: {e}. Input data: {data}")
        return 0 # or raise a more descriptive exception
    except TypeError as e:
        print(f"TypeError: {e}")
        return None #or raise a more descriptive exception
    except Exception as e:
        print(f"An unexpected error occurred: {e}. Input data: {data}")
        return -1

data = {'key':10}
print(function_with_uncommon_error_solution(data))
data = {'key':'abc'}
print(function_with_uncommon_error_solution(data))
data = 10
print(function_with_uncommon_error_solution(data))