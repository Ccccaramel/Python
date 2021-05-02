""" 解数独
Step 1
  录入待解数独
Step 2   new
  初始化数独,复杂度,坐标,以及相关标记值
Step 3   ergodic
  重置复杂度,查看数独,同时获取坐标并计算复杂度
  打印复杂度,打印坐标
  进入 Step 4
Step 4   update_completion_degree
  寻找最大复杂度,寻找最小复杂度并获取其范围
  【若最小复杂度为 1 ,则进入 Step 5】
Step 5   only_one
  通过传入的参数
  打印复杂度为 1 的空格的相对具体位置
  向数独填入正确值，进入 Step 6
  进入 Step 3
Step 6   update_coordinate
  更新坐标

Step 3
  把每行/每列/每个小九宫格仅剩1个空格的优先填上---此步每填补1个空格就检查数独，判断是否执行1次
Step 4
  逐个分析待填空格(复杂度由低到高)，从其所在的横列、竖列、小九宫格所存在的数字进行分析填补
"""

# def get_number(horizontal, vertical, hor, ver):
#     while 1:
#         # 从键盘输入的是 str 类型
#         num = input("大九宫格第{}行第{}列,小九宫格第{}行第{}列,请输入数字:".format(horizontal + 1, vertical + 1, hor + 1, ver + 1))
#         if num.isdigit() and 0 <= int(num) <= 9:
#             return int(num)
#         else:
#             print("! 请输入有效数字(0-9,0:待解空格)")
#             get_number(horizontal, vertical, hor, ver)
import copy


# 逐行获取待解数独数据
def get_a_set_of_data(line):
    s = input("请输入待解数独的第{}行数字:".format(line))
    if s.isdigit() and len(s) == 9:
        return s
    else:
        print("! 请输入有效数字 0-9 , 0 为待解数字, 例如: 048503611")
        return get_a_set_of_data(line)


class square:

    def __init__(self):
        # 0 意为待填数字
        # self.unit = [
        #     [[[0, 0, 0], [0, 0, 0], [0, 0, 0]],  [[0, 0, 0], [0, 0, 0], [0, 0, 0]],  [[0, 0, 0], [0, 0, 0], [0, 0, 0]]],
        #     [[[0, 0, 0], [0, 0, 0], [0, 0, 0]],  [[0, 0, 0], [0, 0, 0], [0, 0, 0]],  [[0, 0, 0], [0, 0, 0], [0, 0, 0]]],
        #     [[[0, 0, 0], [0, 0, 0], [0, 0, 0]],  [[0, 0, 0], [0, 0, 0], [0, 0, 0]],  [[0, 0, 0], [0, 0, 0], [0, 0, 0]]]
        # ]

        self.unit = [
            [[[0, 7, 0], [0, 9, 8], [6, 3, 0]], [[3, 9, 4], [1, 0, 0], [8, 0, 7]], [[1, 6, 8], [0, 5, 0], [0, 0, 0]]],
            [[[3, 0, 6], [0, 8, 9], [2, 4, 7]], [[2, 4, 8], [6, 0, 3], [0, 1, 0]], [[9, 1, 7], [2, 4, 0], [8, 0, 6]]],
            [[[7, 0, 0], [9, 2, 3], [0, 0, 0]], [[5, 8, 0], [7, 6, 1], [4, 3, 2]], [[0, 2, 0], [5, 0, 4], [6, 7, 9]]]
        ]

        # 对应行或对应列或对应小九宫格的复杂度越低,在其内的未解格立即解出的可能性越大,通过参照复杂度来有选择性地解出未解格
        self.completion_degree_initial = [  # 初始值样本，不可改变
            [9, 9, 9, 9, 9, 9, 9, 9, 9],  # 第1,2,3...,9行复杂度
            [9, 9, 9, 9, 9, 9, 9, 9, 9],  # 第1,2,3...,9列复杂度
            [9, 9, 9, 9, 9, 9, 9, 9, 9]  # 第1,2,3...,9个小九宫格复杂度
        ]

        # 坐标,当前元素准确位置会被存入对应列表中
        self.coordinate = [
            [],  # 0
            [],  # 1
            [],  # 2
            [],  # 3
            [],  # 4
            [],  # 5
            [],  # 6
            [],  # 7
            [],  # 8
            []  # 9
        ]
        # 记号,读取数独时会添加所有元素坐标,而此过程只需一次即可
        self.tag = 0

        self.completion_degree = 0

        self.min_completion_degree = 9  # 最小复杂度,最小复杂度用于快速定位易解待填空格
        self.max_completion_degree = 0  # 最大复杂度,最大复杂度用于快速检测数独是否完成
        self.min_completion_degree_trait = 0  # 0:行 1:列 2:小九宫格
        self.min_completion_degree_place = 0  # 0-9:第0-9行/列/小九宫格

    # 查看数独副本,同时计算获取副本复杂度
    def ergodic(self):
        self.completion_degree = copy.deepcopy(
            self.completion_degree_initial)  # 将复制数独初始复杂度列表,得到一个副本,因为每次都会重新计算复杂度,故不能在原有列表中
        # 继续操作
        horizontal = 0  # 大九宫格<橫>
        vertical = 0  # 大九宫格<竖>
        hor = 0
        ver = 0
        print("***************************数独副本如下***************************\n")
        while horizontal < 3:
            while hor < 3:

                while vertical < 3:
                    while ver < 3:
                        print(self.unit[horizontal][vertical][hor][ver], end="     ")
                        if self.tag == 0:
                            self.coordinate[self.unit[horizontal][vertical][hor][ver]].append(
                                [horizontal, vertical, hor, ver])
                        if self.unit[horizontal][vertical][hor][ver] != 0:
                            self.completion_degree[0][horizontal * 3 + hor] -= 1  # 横列复杂度减 1
                            self.completion_degree[1][vertical * 3 + ver] -= 1  # 竖列复杂度减 1
                            self.completion_degree[2][horizontal * 3 + vertical] -= 1  # 小九宫格复杂度减 1
                        ver += 1
                    if vertical < 2:
                        print("   |   ", end=" ")
                    ver = 0
                    vertical += 1
                vertical = 0
                hor += 1
                print("\n")

            print("--------------------------------------------------------------------\n")
            horizontal += 1
            hor = 0

        print("***************************数独复杂度如下***************************\n")
        sign = 0  # 0 : 所有横列复杂度    1 : 所有竖列复杂度    2 : 所有小九宫格复杂度
        for lis in self.completion_degree:
            if sign == 0:
                print("各横列复杂度:\n----1----2----3----4----5----6----7----8----9----(横列)")
            if sign == 1:
                print("各竖列复杂度:\n----1----2----3----4----5----6----7----8----9----(竖列)")
            if sign == 2:
                print("各小九宫格复杂度:\n----1----2----3----4----5----6----7----8----9----(九宫格)")
            for data in lis:
                print("   ", data, end="")
            sign += 1
            print("")

        print("\n***************************数独各值所在位置(H,V,h,v)如下***************************")
        sign = 0
        sign1 = 1
        for list1 in self.coordinate:
            print("\n值为 {} 的坐标:".format(sign))
            for list2 in list1:
                print("   ", end="")
                for list3 in list2:
                    if sign1 == 1:
                        print("[", end="")
                    print("{}".format(list3 + 1), end="")
                    sign1 += 1
                    if sign1 == 5:
                        print("]", end="")
                    else:
                        print(",", end="")
                sign1 = 1
            print("")
            sign += 1
        print("")

        self.tag = 1

        self.update_completion_degree()  # 更新数独复杂度最值,若有更新则会再次打印数独

    # 录入待解数独样本,逐行录入,录入的待解数独请确保可解有效
    def input_sud(self):
        horizontal = 0  # 大九宫格<橫>
        vertical = 0  # 大九宫格<竖>
        hor = 0
        ver = 0
        while horizontal < 3:
            while hor < 3:
                line = horizontal * 3 + hor + 1
                arr = get_a_set_of_data(line)
                sign = 0
                while vertical < 3:
                    while ver < 3:
                        # data = get_number(horizontal, vertical, hor, ver)  # 用户逐行输入数独  --弃用,逐个输入检查太慢,改为逐行录入
                        data = arr[sign]
                        self.unit[horizontal][vertical][hor][ver] = int(data)  # 将数独录入副本中
                        ver += 1
                        sign += 1
                    ver = 0
                    vertical += 1
                vertical = 0
                hor += 1

            horizontal += 1
            hor = 0

    # 更新最大复杂度、最小复杂度以及其位置
    """
    trait:
     0 --- 横列 
     1 --- 竖列
     2 --- 小九宫格
    """

    def update_completion_degree(self):
        self.min_completion_degree = 9  # 最小复杂度置 0
        self.max_completion_degree = 0  # 最大复杂度置 0
        for n1 in range(3):
            for n2 in range(9):
                if self.max_completion_degree <= self.completion_degree[n1][n2]:
                    self.max_completion_degree = self.completion_degree[n1][n2]  # 获取最大复杂度
                if self.min_completion_degree >= self.completion_degree[n1][n2] != 0:
                    self.min_completion_degree = self.completion_degree[n1][n2]  # 获取最小复杂度
                    self.min_completion_degree_trait = n1  # 最小复杂度所在位置的类型
                    self.min_completion_degree_place = n2  # 最小复杂度位置所在范围
        print("最大复杂度:%d" % self.max_completion_degree)
        print("最小复杂度:%d" % self.min_completion_degree)
        if self.min_completion_degree_trait == 0:
            print("最小复杂度所在范围: 在第 %d 行" % (self.min_completion_degree_place + 1))
        elif self.min_completion_degree_trait == 1:
            print("最小复杂度所在范围: 在第 %d 列 " % (self.min_completion_degree_place + 1))
        elif self.min_completion_degree_trait == 2:
            print("最小复杂度所在范围: 在第 %d 小九宫格 " % (self.min_completion_degree_place + 1))
        if self.min_completion_degree == 1:  # 若存在复杂度为 1 的情况立即填补
            self.only_one(self.min_completion_degree_trait, self.min_completion_degree_place)

    # 更新坐标
    """
    当待解数独每完成一个空格则立即对坐标进行添加与删除操作
    添加:获取空格在数独中的"位置",直接在坐标对应的子列表中添加"位置"即可 list.append(obj)
    删除:获取空格填补后的值以及在数独中的"位置",通过值确定坐标中对应子列表,再通过"位置"找到对应的下标,通过下标进行删除 del list[空格的值][下标]
    """

    def update_coordinate(self, value, horizontal, vertical, hor, ver):
        # 删除
        sign = 0
        for v in self.coordinate[0]:
            if v[0] == horizontal and v[1] == vertical and v[2] == hor and v[3] == ver:
                print("sign: {}".format(sign))
                del self.coordinate[0][sign]

                # self.coordinate[0].remove(self.coordinate[0][sign])
                break
            sign += 1
        # 添加
        print("value:", value)
        self.coordinate[value].append([horizontal, vertical, hor, ver])

    # 完成复杂度为 1 的空格
    def only_one(self, trait, place):
        horizontal = 0  # 大九宫格<橫>
        vertical = 0  # 大九宫格<竖>
        hor = 0
        ver = 0
        horizontal_temp = 0
        vertical_temp = 0
        hor_temp = 0
        ver_temp = 0
        li = list(range(10))
        flag = 0
        if trait == 0:
            horizontal = place // 3  # 获取复杂度为 1 的空格所在的大行
            hor = place - horizontal * 3  # 获取复杂度为 1 的空格所在的小行
            print("检测到第 {} 行存在复杂度为1的空格,它在第 {} 大行第 {} 小行,".format(place + 1, horizontal + 1, hor + 1))
            while vertical < 3:
                while ver < 3:
                    if self.unit[horizontal][vertical][hor][ver] == 0:  # 得到复杂度为 1 的空格的具体位置
                        vertical_temp = vertical
                        ver_temp = ver
                    else:
                        # 将列表中对应数值改为 0 ,意为该行已存在此数,大于 0 的数即为待填空格内的值
                        li[self.unit[horizontal][vertical][hor][ver]] = 0
                    ver += 1
                vertical += 1
                ver = 0
            self.unit[horizontal][vertical_temp][hor][ver_temp] = max(li)  # 将列表内唯一的值填入待填空格
            self.update_coordinate(max(li), horizontal, vertical_temp, hor, ver_temp)  # 更新与修改相关元素坐标
        elif trait == 1:
            vertical = place // 3  # 获取复杂度为 1 的空格所在的大列
            ver = place - vertical * 3  # 获取复杂度为 1 的空格所在的大列
            print("检测到第 {} 列存在复杂度为1的空格,它在第 {} 大列第 {} 小列,".format(place + 1, vertical + 1, ver + 1))
            while horizontal < 3:
                while hor < 3:
                    if self.unit[horizontal][vertical][hor][ver] == 0:  # 得到复杂度为 1 的空格的具体位置
                        horizontal_temp = horizontal
                        hor_temp = hor
                    else:
                        # 将列表中对应数值改为 0 ,意为该行已存在此数,大于 0 的数即为待填空格内的值
                        li[self.unit[horizontal][vertical][hor][ver]] = 0
                    hor += 1
                horizontal += 1
                hor = 0
            self.unit[horizontal_temp][vertical][hor_temp][ver] = max(li)  # 将列表内唯一的值填入待填空格
            self.update_coordinate(max(li), horizontal_temp, vertical, hor_temp, ver)  # 更新与修改相关元素坐标
        elif trait == 2:
            horizontal = place // 3  # 获取复杂度为 1 的空格所在的小九宫格
            vertical = place - horizontal * 3  # 获取复杂度为 1 的空格所在的小九宫格
            print("检测到第 {} 小九宫格存在复杂度为1的空格,它在第 {} 大行第 {} 大列,".format(place + 1, horizontal + 1, vertical + 1))
            while hor < 3:
                while ver < 3:
                    if self.unit[horizontal][vertical][hor][ver] == 0:  # 得到复杂度为 1 的空格的具体位置
                        hor_temp = hor
                        ver_temp = ver
                    else:
                        # 将列表中对应数值改为 0 ,意为该行已存在此数,大于 0 的数即为待填空格内的值
                        li[self.unit[horizontal][vertical][hor][ver]] = 0
                    ver += 1
                hor += 1
                ver = 0
            self.unit[horizontal][vertical][hor_temp][ver_temp] = max(li)  # 将列表内唯一的值填入待填空格
            self.update_coordinate(max(li), horizontal, vertical, hor_temp, ver_temp)  # 更新与修改相关元素坐标
        self.ergodic()  # 打印数独以及重新计算复杂度

    # 遍历所有空格,根据横列,竖列,以及所在小九宫格判断是否存在唯一解
    """
     only_one() 仅考虑横列、竖列、小九宫格中的一种
     three_dimensional() 通过排除法获取待填空格的所有取值,当只剩一个值可取时则将其填入
     Q:为什么不从复杂之和最低的开始判断?
     A:复杂度之和越低并不意味着易解,相反复杂度之和为19(横列[1,2]:7,竖列[3,4]:7,小九宫格[5,6,7,8]:5)存在唯一解<假设>
       若只看空格所在行列以及九宫格是不够的,即使复杂度为27也有可能将其解出,本方法不考虑此情况
    """

    def three_dimensional(self):
        for num in range(10):
            for lis in self.coordinate[num]:  # 从值为 0-9 的依次遍历,每次获取对应值的准确坐标
                print(1)

def main():
    # 前期
    squ = square()  # 创建一个"数独方格"对象
    squ.ergodic()  # 查看数独副本,更新数独复杂度
    # squ.input_sud()  # 录入待解数独样本
    # squ.ergodic()  # 查看数独副本

    # 中期


if __name__ == "__main__":
    main()
