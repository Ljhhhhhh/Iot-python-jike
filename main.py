
import machine
import time

# 指明 GPIO2 管脚
pin = machine.Pin(2, machine.Pin.OUT)

# 循环执行
while True:
    time.sleep(0.1)   # 等待 2 秒
    pin.on()        # 控制 LED 状态
    time.sleep(0.1)   # 等待 2 秒
    pin.off()       # 切换 LED 状
