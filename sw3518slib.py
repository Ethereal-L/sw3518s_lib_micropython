#sw3518s芯片库
from math import log


class sw3518:
    
    def __init__(self, i2c):
        self.i2c = i2c
        
    def qcled(self):
        i = self.i2c.readfrom_mem(60, 0x06, 1,addrsize=8)  #获取对应寄存器数据
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
        
        return reg_list[0]                        #如果7bit为0则快充led关闭，为1则为打开

        
    def pd_xieyi(self):
        i = self.i2c.readfrom_mem(60, 0x06, 1,addrsize=8)  #获取对应寄存器数据
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
        #print(reg_list_new)
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
        return reg
    
    
    
    def ac_state(self):
        ac = self.i2c.readfrom_mem(60, 0x08, 1,addrsize=8)  #获取对应寄存器数据
        ten = ord(ac)                                  #将Ascii码转换为十进制数
        two = bin(ten)                                #十进制转二进制
        #a = str(two)                                 #int转换str
        reg_list = list(two)                          #将二进制数转换为列表方便后面读取比特位
        #print(reg_list)
        del reg_list[0: 2]                            #删除转换二进制自带的“0”和“b”
        if len(reg_list) < 8:                         #自动转二进制不会往前补0
            reg_list.insert(0, 0)
        elif len(reg_list) < 8:
            reg_list.insert(0, 0)
        else:
            pass
        reg_list_new = list(map(int, reg_list))       #元素全部转换成int
        #print(reg_list_new)
        ac = reg_list_new[0:4]
        #print(pd)
        #reg = None
        #将列表的数转换为十进制数
        c = len(ac)-1
        regac = 0
        #print(c)
        for r in ac:
            t = r * 2**c
            c -= 1
            regac += t
            #print(reg)
        return regac
    
    
        
    def read_vin(self):
        self.i2c.writeto_mem(60, 0x13, b'\x02')                   #写0x13寄存器使能adcvin
        ascvin = self.i2c.readfrom_mem(60, 0x30, 1,addrsize=8)    #读取adcvin数据
        tenvin = ord(ascvin)                                 #转换数据
        vin = tenvin * 0.16
        hvin = round(vin, 3)
        return hvin
        
    def adc_vout(self):
        ascvout = self.i2c.readfrom_mem(60, 0x31, 1,addrsize=8)
        tenvout = ord(ascvout)                                 #转换数据
        vout    = tenvout * 0.096
        hvout = round(vout, 3)
        return hvout
        
    def adc_c_iout(self):
        asciout = self.i2c.readfrom_mem(60, 0x33, 1,addrsize=8)
        teniout = ord(asciout)
        c_iout  = teniout * 0.04
        hc_iout = round(c_iout, 3)
        return hc_iout
      
    def adc_a_iout(self):
        asciout = self.i2c.readfrom_mem(60, 0x34, 1,addrsize=8)
        teniout = ord(asciout)
        a_iout  = teniout * 0.04
        ha_iout = round(a_iout, 3)
        return ha_iout

    def temp(self):
        ascntc = self.i2c.readfrom_mem(60, 0x37, 1,addrsize=8)
        ntc = ord(ascntc)
        rntc= ntc * 0.008/0.00008
        B = 3380                                                                           #取决于模块热敏B值
        temp = (1.0 / ((1.0 / B) * log( rntc / 10000) + (1.0 / (25 + 273.15))) - 273.15)   #此计算公式中默认是用的10k热敏电阻所以是rntc/10k
        htemp = round(temp, 1)                                                             #温度保留一位小数
        return htemp
