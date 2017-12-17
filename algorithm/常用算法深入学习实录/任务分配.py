cost = [[2, 12, 5, 32],
        [8, 15, 7, 11],
        [24, 18, 9, 6],
        [21, 1, 8, 28]]  # 行表示任务序号,列表示工人花费的时间

pnum = len(cost[0])  # 工人数
tnum = len(cost)  # 任务数

taskMap = [0 for _ in range(tnum)]  # taskMap[i] 表示工人i完成任务taskMap[i]
minCost = sum([sum(i) for i in cost])
finalTaskMap = [0 for _ in range(tnum)]


def arrange(iTask, currentCost):
    global minCost, finalTaskMap
    if iTask >= tnum:
        print("得到方案: cost:{}".format(currentCost))
        minCost = currentCost
        finalTaskMap = taskMap.copy()
        for i in taskMap:
            print("工人{} 完成任务{}".format(i, taskMap[i]))
    else:  # 对于当前任务 task[iTask]
        for i in range(pnum):  # 每个工人,按位置
            tempCost = currentCost + cost[iTask][i]
            # 如果工人空闲 且花销比前面的小 避免重复
            if taskMap[i] == 0 and currentCost + cost[iTask][i] <= tempCost <= minCost:
                taskMap[i] = iTask
                arrange(iTask + 1, tempCost)
                taskMap[i] = 0  # 恢复


if __name__ == '__main__':
    arrange(0, 0)
    print("最终方案: cost:{}".format(minCost))
    for i, v in enumerate(finalTaskMap):
        print("工人{} 完成任务{} cost:{}".format(i, v,cost[v][i]))
