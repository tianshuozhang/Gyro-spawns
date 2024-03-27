from hhhex import *
from cirque import *
from  combine import h_combine
from write import ww
from round_table import *
from ball import *
from Concave_cone import *
import time


def compute(r1 = 2,r2 = 3,r3 = 2,h1 = 4,h2 = 30,h3 = 4,work="he"):
    if os.path.exists("datastore") == False:
        os.mkdir("datastore")
    # 获取当前时间戳
    timestamp = time.strftime("%Y%m%d_%H%M%S", time.localtime())
    # 构建文件夹路径
    folder_path = os.path.join(os.getcwd(), "datastore", timestamp)
    # 创建文件夹
    os.makedirs(folder_path)
    r4 = max(r1, r2, r3) * 2
    beishu = lcm(lcm(r4 - r1, r4 - r2), r4 - r3)
    beta = r4 * 2 * beishu
    print("beishu: {}, beta: {}".format(beishu, beta))
    hh1 = round_table(beishu, r1, int(r4 / 2), h1, beta, 0, 0, 0,"台",timestamp)

    alpha = float(r4 / 2 - r1) / h1
    hh2 = Concave_cone(int(beishu / (r4 - r1)), r1, r4, h1, alpha, beta, 0, 0, 0,"环凹",timestamp)
    alpha = float(r2 - r1) / h1
    hh3 = Concave_cone(int(beishu / (r4 - r1)), r1, r4, -1 * h1, alpha, beta, 0, 0, -1 * h1,"环凹",timestamp)
    hh4 = cirque(int(beishu / (r4 - r2)), r2, r4, h2, beta, 0, 0, -1 * (h1 + h2),"环",timestamp)
    alpha = float(r2 - r3) / h3
    hh5 = Concave_cone(int(beishu / (r4 - r3)), r3, r4, h3, alpha, beta, 0, 0, -1 * (h1 + h2 + h3),"环凹",timestamp)
    alpha = float(r4 / 2 - r3) / h3
    hh6 = Concave_cone(int(beishu / (r4 - r3)), r3, r4, -1 * h3, alpha, beta, 0, 0, -1 * (h1 + h2 + h3 + h3),"环凹",timestamp)
    hh7 = round_table(beishu, int(r4 / 2), r3, h3, beta, 0, 0, -1 * (h1 + h2 + h3 + h3),"台",timestamp)
    h_combine(hh3, hh4)
    ww(hh4, "1",timestamp)
    print(1)
    h_combine(hh2, hh4)
    ww(hh4, "2",timestamp)
    print(2)
    h_combine(hh1, hh4)
    ww(hh4, "3",timestamp)
    print(3)
    h_combine(hh5, hh4)
    ww(hh4, "4",timestamp)
    print(4)
    h_combine(hh6, hh4)
    ww(hh4, "5",timestamp)
    print(5)
    h_combine(hh7, hh4)
    ww(hh4, work,timestamp)



def lcm(x, y):
    #  获取最大的数
    if x > y:
        greater = x
    else:
        greater = y

    while (True):
        if ((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
    return lcm