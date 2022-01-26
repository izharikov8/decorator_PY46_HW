import datetime
import csv
import os

def logger_path(directory, name):
    path = os.path.join(directory, name)
    def log_decorator(old_function):
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
            data = [datetime.datetime.now(), old_function.__name__,
                    args, kwargs, result]
            with open(path, "a", newline='', encoding='utf-8') as f:
                writer_object = csv.writer(f)
                writer_object.writerow(data)
                f.close()
            return result
        return new_function
    return log_decorator