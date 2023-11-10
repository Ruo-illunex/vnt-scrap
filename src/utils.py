import time


def get_current_time():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))


def save_to_file(filename, result_text):
    with open(filename, 'w') as f:
        f.write(result_text)
