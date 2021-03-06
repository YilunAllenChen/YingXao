import seeed_si114x
import time
import signal
def handler(signalnum, handler):
    print("Please use Ctrl C to quit")

def get_visible(sensor):
    return round(sensor.ReadVisible, 0)

def get_uv(sensor):
    return round(sensor.ReadUV/100, 1)

def get_ir(sensor):
    return round(sensor.ReadIR, 0)

def main():
    SI1145 = seeed_si114x.grove_si114x()
    print("Please use Ctrl C to quit")
    signal.signal(signal.SIGTSTP, handler) # Ctrl-z
    signal.signal(signal.SIGQUIT, handler) # Ctrl-\
    while True:
        print('Visible %03d UV %.2f IR %03d' % (get_visible(SI1145) , get_uv(SI1145) , get_ir(SI1145)) , end=" ")
        print('\r', end='')
        time.sleep(0.5)
if __name__  == '__main__':
    main()
