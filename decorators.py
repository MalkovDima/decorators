import datetime
from functools import wraps


def write_file(file_name, str_text):
    with open(file_name, 'a') as file:
        file.write(str_text + '\n')


#1 задание
def logger_decorator(old_function):
    @wraps(old_function)
    def new_function(*args, **kwargs):
        write_str = ''
        start_time = datetime.datetime.now().strftime('DATE: %m.%d.%Y TIME: %H:%M:%S:%f')
        str_name_function = 'NAME: ' + old_function.__name__
        str_args = 'Args: ' + str(args)
        str_kwargs = 'Kwargs: ' + str(kwargs)
        result = old_function(*args, **kwargs)
        str_result = 'RESULT: ' + str(result)
        write_str = start_time + ' ' + str_name_function + ' PARAMETRS: ' + str_args + ' ' + str_kwargs + ' ' + str_result
        write_file('file.txt', write_str)
        return result
    return new_function

#2 задание
def logger_decorator_param(param_adress):
    def logger_decorator(old_function):
        @wraps(old_function)
        def new_function(*args, **kwargs):
            write_str = ''
            start_time = datetime.datetime.now().strftime('DATE: %m.%d.%Y TIME: %H:%M:%S:%f')
            str_name_function = 'NAME: ' + old_function.__name__
            str_args = 'Args: ' + str(args)
            str_kwargs = 'Kwargs: ' + str(kwargs)
            result = old_function(*args, **kwargs)
            str_result = 'RESULT: ' + str(result)
            write_str = start_time + ' ' + str_name_function + ' PARAMETRS: ' + str_args + ' ' + str_kwargs + ' ' + str_result
            write_file(param_adress, write_str)
            return result

        return new_function
    return logger_decorator
