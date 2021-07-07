#!/usr/bin/python3

def pressure(v, t, n):
        """以帕斯卡为单位计算理想气体的压力。

        应用理想气体定律：http://en.wikipedia.org/wiki/Ideal_gas_law

        v——体积气体，以立方米为单位
        t -- 绝对温度，单位为开尔文
        n -- 气体粒子
        """
        k = 1.38e-23 # 玻尔兹曼常数
        return n * k * t / v
        
def a():
    for i  in []:
        print(i)
    print(1)
