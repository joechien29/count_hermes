import time
from hermes_buy.step.download_page import get_item_count
from hermes_buy.step.send_email import send_email
from hermes_buy.step.send_sns import send_sns


def main():
    item_count = 0
    while item_count <= 13:
        t = time.localtime()
        time_now = time.strftime('%Y/%m/%d %H:%M:%S', t)
        print(time_now)
        item_count = get_item_count()
        if item_count > 13:
            send_email()
            send_sns()
        time.sleep(600)


if __name__ == '__main__':
    main()
