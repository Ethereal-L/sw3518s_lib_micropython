#sw3518s芯片库
from math import log




def qcled():
    i = i2c.readfrom_mem(60, 0x06, 1,addrsize=8)  #获取对应寄存器数据
    ten = ord(i)                                  #将Ascii码转换为十进制数
    two = bin(ten)                                #十进制转二进制
    a = str(two)                                  #int转换str
    reg_list = list(a)                            #将二进制数转换为列表方便后面读取比特位
    #print(reg_list)
    del reg_list[0: 2]                            #删除转换二进制自带的“0”和“b”
    if len(reg_list) < 8:                         #自动转二进制不会往前补0
        reg_list.insert(0, 0)
        reg_list.insert(0, 0)
    else:
        pass
    if reg_list[0] == 0:                          #如果7bit为0则快充led关闭，为1则为打开
        print("qcled close")
    else:
        print("qcled open")


def pd_xieyi():
    i = i2c.readfrom_mem(60, 0x06, 1,addrsize=8)  #获取对应寄存器数据
    ten = ord(i)                                  #将Ascii码转换为十进制数
    two = bin(ten)                                #十进制转二进制
    #a = str(two)                                 #int转换str
    reg_list = list(two)                          #将二进制数转换为列表方便后面读取比特位
    #print(reg_list)
    del reg_list[0: 2]                            #删除转换二进制自带的“0”和“b”
    if len(reg_list) < 8:                         #自动转二进制不会往前补0
        reg_list.insert(0, 0)
        reg_list.insert(0, 0)
    else:
        pass
    reg_list_new = list(map(int, reg_list))       #元素全部转换成int
    print(reg_list_new)
    pd = reg_list_new[2:4]
    #print(pd)
    #reg = None
    #将列表的数转换为十进制数
    c = len(pd)-1
    reg = 0
    #print(c)
    for r in pd:
        t = r * 2**c
        c -= 1
        reg += t
        #print(reg)
    if reg == 1:
        print("PD2.0")
        
    elif reg == 2:
        print("PD3.0")
        
    else:
        print("other")



def read_vin():
    i2c.writeto_mem(60, 0x13, b'\x02')                   #写0x13寄存器使能adcvin
    ascvin = i2c.readfrom_mem(60, 0x30, 1,addrsize=8)    #读取adcvin数据
    tenvin = ord(ascvin)                                 #转换数据
    vin = tenvin * 0.16
    return vin
    
def adc_vout():
    ascvout = i2c.readfrom_mem(60, 0x31, 1,addrsize=8)
    tenvout = ord(ascvout)                                 #转换数据
    vout    = tenvin * 0.096
    return vout

def adc_c_iout():
    asciout = i2c.readfrom_mem(60, 0x33, 1,addrsize=8)
    teniout = ord(asciout)
    c_iout  = teniout * 0.04
    return c_iout
    
def adc_a_iout():
    asciout = i2c.readfrom_mem(60, 0x34, 1,addrsize=8)
    teniout = ord(asciout)
    a_iout  = teniout * 0.04
    return a_iout

def temp():
    ascntc = i2c.readfrom_mem(60, 0x37, 1,addrsize=8)
    ntc = ord(ascntc)
    rntc= ntc * 0.008/0.00008
    B = 3380
    temp = (1.0 / ((1.0 / B) * log( rntc / 10000) + (1.0 / (25 + 273.15))) - 273.15)
    return temp
    
