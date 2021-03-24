import time
import SI1145.SI1145 as light_sensor
import datetime as dt


if __name__ == '__main__':
    now = dt.datetime.now()
    current_time = now.strftime('%H:%M:%S')
    print("Current time = ", current_time)
    total_visible = 0
    total_uv = 0.0
    total_ir = 0
    total_measurement = 0
    while int(dt.datetime.now().strftime('%M')) < 32:
        try:
            print(int(now.strftime('%M')))
            visible_light = light_sensor.get_visible()
            total_visible += int(visible_light)
            uv_light = light_sensor.get_uv()
            total_uv += float(uv_light)
            ir_light = light_sensor.get_ir()
            total_ir += int(ir_light)
            total_measurement += 1
            print(total_visible)
            print(total_uv)
            print(total_ir)
        except:
            print('Failed to read sunlight information, check SI1145')
        time.sleep(2)
    print('total visible = ',total_visible)
    print('total uv = ', total_uv)
    print('total ir = ', total_ir)
    print('total measurement = ', total_measurement)
    print('average visible = ', total_visible/total_measurement)
    print('average uv = ', total_uv/total_measurement)
    print('average ir = ', total_ir/total_measurement)

