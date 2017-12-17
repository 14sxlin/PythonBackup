# 小明一家过桥,每个人有过桥的时间,桥每次能过2个人
# 晚上必须点灯,灯拿在一个人手上,且只有一盏,能亮30分钟
# 最短的过桥方案和时间

people = ["小明", "弟弟", "爸爸", "妈妈", "爷爷"]
time = [1, 3, 6, 8, 15]
light_time = 30

schema = [-1 for _ in range(100)]
# 解数据结构
# 假设一家人打算从左往右过桥 schema[i] schema[i+1] 表示第i次过的人(两个人)
# schema[i+2] 表示带灯回去的人
position = [0 for _ in range(len(people))]  # 0 表示人在左边, 1 表示人在右边
index = 0
minTime = 99999
finalSchema = []


def crossBridge(rest, direction, currentTime):
    """
    :param rest: 左边剩下的人
    :param direction: 过桥的方向, 0 表示往右, 1 表示回来
    :return:
    """
    global minTime, finalSchema, index, schema
    if rest <= 0:
        if currentTime < minTime:
            minTime = currentTime
            finalSchema = [k for k in schema if k >= 0]
            print("\n\n可选方案如下:")
            for g in range(0, len(finalSchema), 3):
                print(" {} 和  {}  过桥, 花费: {} ".format(people[finalSchema[g]], people[finalSchema[g + 1]],
                                                      max(time[finalSchema[g]], time[finalSchema[g + 1]])), end=" ")
                if g + 2 < len(finalSchema):
                    print("  {} 带灯回去 花费: {}".format(people[finalSchema[g + 2]], time[finalSchema[g + 2]]))
            print("\ncost:", minTime)
    else:
        if direction == 0:  # 从左往右2个人过桥过桥
            for i in range(len(people)):  # 第一个人 在左边而且时间花费比之前的方案少
                if position[i] == 0 and time[i] + currentTime < minTime:
                    schema[index] = i  # 第index次由i过去
                    position[i] = 1
                    index += 1
                    for j in range(len(people)):  # 第二个人 第index+1次过去
                        twoPeopleTime = max(time[i], time[j])
                        if position[j] == direction and currentTime + twoPeopleTime < minTime:
                            schema[index] = j
                            position[j] = 1
                            index += 1
                            crossBridge(rest - 2, not direction, currentTime + twoPeopleTime)
                            schema[index] = -1
                            index -= 1
                            position[j] = 0
                    index -= 1
                    schema[index] = -1
                    position[i] = 0
        else:  # 从右往左一个人带灯回去
            for j in range(len(people)):
                if position[j] == 1 and time[j] + currentTime <= minTime:
                    schema[index] = j
                    index += 1
                    position[j] = 0
                    crossBridge(rest + 1, not direction, time[j] + currentTime)
                    position[j] = 1
                    index -= 1
                    schema[index] = -1
                    position[j] = 1


if __name__ == '__main__':
    crossBridge(len(people), 0, 0)
    print("时间花费:")
    for i, v in enumerate(people):
        print("{}({})".format(v, time[i]),end="\t")
    print("\n\n最终方案如下:")
    for g in range(0, len(finalSchema), 3):
        print(" {} 和  {}  过桥, 花费: {} ".format(people[finalSchema[g]], people[finalSchema[g + 1]],
                                              max(time[finalSchema[g]], time[finalSchema[g + 1]])), end=" ")
        if g + 2 < len(finalSchema):
            print("  {} 带灯回去 花费: {}".format(people[finalSchema[g + 2]], time[finalSchema[g + 2]]))
    print("\nfinal cost:", minTime)
