import datetime
import time


def generate_hunam_time(pretime) -> str:
    print_pre_midnight = time.localtime(pretime)
    human_time = time.strftime("%Y-%m-%d %H:%M:%S", print_pre_midnight)
    return human_time


def transfer_time(timestamp):
    """
    转换时间，从timestamp > 方便阅读时间
    """
    dateArray = datetime.datetime.fromtimestamp(timestamp)
    otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S")
    return otherStyleTime


if __name__ == '__main__':
    pass
