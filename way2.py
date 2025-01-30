import time
from decimal import Decimal, getcontext

# 设置初始精度
initial_precision = 10

def gauss_legendre(iterations):
    # 初始值
    a = Decimal(1)
    b = Decimal(1) / Decimal(2).sqrt()
    t = Decimal(0.25)
    p = Decimal(1)
    
    for _ in range(iterations):
        a_next = (a + b) / 2
        b = (a * b).sqrt()
        t -= p * (a - a_next) ** 2
        a = a_next
        p *= 2
    
    # 最终结果
    pi = (a + b) ** 2 / (4 * t)
    return pi

def continuous_pi():
    iterations = 1
    precision = initial_precision
    
    with open("pi_estimate.txt", "w") as file:  # 打开文件以追加模式写入
        while True:
            # 设置当前的精度
            getcontext().prec = precision
            pi_value = gauss_legendre(iterations)
            
            # 打印到控制台
            print(f"\rpi: {pi_value}", end="", flush=True)
            
            # 写入文件
            file.write(f"\npi: {pi_value}")
            file.flush()  # 强制刷新文件缓冲区

            # 增加精度和迭代次数
            time.sleep(0.01)  # 每秒输出一次
            iterations += 1
            precision += 1  # 每次增加精度

# 启动持续计算圆周率
continuous_pi()
