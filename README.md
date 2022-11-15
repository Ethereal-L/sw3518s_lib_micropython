# sw3518s_lib_micropython
智融的sw3518s芯片的micropython函数库
只有简单的读取功能，i2c控制函数还没写。
如果想使用其中某一函数示例代码：


import sw3518lib
from machine import Pin, I2C

i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400_000)


sw = sw3518lib.sw3518(i2c)
v = sw.qcled()
print(v)
