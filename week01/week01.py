import datetime
from pathlib import Path
import logging
log_file_path_str = "/var/log/python-" + str(datetime.date.today()) + "/call.log"
log_file_path = Path(log_file_path_str)

logging.basicConfig(level=logging.DEBUG, filename="new.log", filemode='a',
                    format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',)


def log_call(func):
    def inner(*args, **kwargs):
        call_say_hi_time = datetime.datetime.now()
        logging.info("say_hi call time:{}".format(call_say_hi_time))
        return func(*args, **kwargs)
    return inner


@log_call
def say_hi():
    print("hi,little boy!")


if __name__ == '__main__':
    say_hi()
