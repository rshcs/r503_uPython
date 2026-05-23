from r503u import R503
from time import sleep


if __name__ == "__main__":
    print("Running.")
    fp = R503()
    # fp.manual_enroll(3)
    x = fp.wu_pin.value()
    print(f'x {x}')
    while True:
        y = fp.wu_pin.value()
        if y != x:
            print(y)
            sleep(2)
            y = 1
