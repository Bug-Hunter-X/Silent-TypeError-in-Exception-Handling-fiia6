def function_with_uncommon_error(data):
    try:
        # Simulate some data processing that might raise an exception
        result = data['key'] + 1 
        return result
    except KeyError:
        # Handle KeyError, but also add a hidden bug!
        return 0
    except TypeError:
        return None
    except Exception as e:
        # Handle other exception
        return -1

data = {'key':10}
print(function_with_uncommon_error(data))
data = {'key':'abc'}
print(function_with_uncommon_error(data))
data = 10
print(function_with_uncommon_error(data))