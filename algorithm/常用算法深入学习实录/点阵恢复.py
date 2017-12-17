# 网格上有点, 已知6 * 7 网格的行列的点的数目, 还原网格

row = [2, 0, 4, 3, 4, 0]
col = [4, 1, 2, 2, 1, 2, 1]

grid = [[False for _ in range(len(col))] for _ in range(len(row))]
iSumRow = [0 for _ in range(len(row))]
iSumCol = [0 for _ in range(len(col))]
count = 1

def checkAndPrintResultIfOK():
    for i, v in enumerate(row):
        if not v == iSumRow[i]:
            # print("错解")
            return False
    for i, v in enumerate(col):
        if not v == iSumCol[i]:
            # print("错解")
            return False
    global count
    print("No.{}".format(count))
    count += 1
    for iRow in grid:
        for iCol in iRow:
            if iCol:
                print("*", end="")
            else:
                print("#", end="")
        print()
    return True

def true2One(x):
    if x is True:
        return 1
    else:
        return 0

def arrange_row(rowNo,begin = 0):
    """尝试安排一行, 似乎是排列树"""
    if rowNo >= len(row):
        return checkAndPrintResultIfOK()
    else:
        # 这一行不应该有黑点 或 这一行的黑点已经满了
        if row[rowNo] == 0 or iSumRow[rowNo] == row[rowNo]:
            arrange_row(rowNo + 1)
        else:  # 尝试添加一个黑点 针对位置的for
            for iCol in range(begin, len(col)):  # 对于这一行的每一列都尝试一下
                # 如果这个位置空着
                if grid[rowNo][iCol] is False:
                    grid[rowNo][iCol] = True
                    iSumRow[rowNo] += 1
                    iSumCol[iCol] += 1
                    # print("row {}:{}".format(rowNo,list(map(true2One,grid[rowNo]))))
                    # 这一列的点还没有满 而且 这一行的点没有满
                    if iSumCol[iCol] <= col[iCol] and iSumRow[rowNo] < row[rowNo]:
                        arrange_row(rowNo,iCol+1)  # 同一行的下一个位置
                    # 行满了
                    elif iSumRow[rowNo] == row[rowNo]:
                        arrange_row(rowNo + 1)  # 下一行

                    # 恢复污染 尝试下一种情况 该点不放
                    grid[rowNo][iCol] = False
                    iSumRow[rowNo] -= 1
                    iSumCol[iCol] -= 1


if __name__ == '__main__':
    arrange_row(0)
