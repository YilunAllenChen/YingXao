import seeed_si114x
import time
import signal

SI1145 = seeed_si114x.grove_si114x()

def handler(signalnum, handler):
    print("Please use Ctrl C to quit")

def get_visible():
    return round(SI1145.ReadVisible, 0)

def get_uv():
    return round(SI1145.ReadUV/100, 1)

def get_ir():
    return round(SI1145.ReadIR, 0)


if __name__ == "__main__":
    print("Please use Ctrl C to quit")
    signal.signal(signal.SIGTSTP, handler) # Ctrl-z
    signal.signal(signal.SIGQUIT, handler) # Ctrl-\
    while True:
        print('Visible %03d UV %.2f IR %03d' % (get_visible() , get_uv() , get_ir()))
        # print('\r', end='')
        time.sleep(0.5)
