if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    nums.pop()
    print(nums)
    nums += [7, 8, 9, 10]  # += use to append iterable or extends
    nums.extend([7, 8, 9, 0])
    print(nums)
    nums.append(11)
    print(nums)
    nums.reverse()
    print(nums)
    nums.sort()
    print(nums)

    head, *rest, tail = nums
    print(head)
    print(rest)
    print(tail)

    three_nums = [1, 2, 3]


    def product(a, b, c):
        return a * b * c


    print(product(1, 2, 3))
    print(product(*three_nums))

    four_nums = three_nums + [4]
    head, *rest = four_nums
    print(product(*rest))

    for i in range(len(four_nums)):
        print(four_nums[i])

    four_nums[0:2] = [9, 8, 7]
    print(four_nums)

    four_nums[1:2] = []
    four_nums.remove(4)
    four_nums.pop()
    del four_nums[0]
    print(four_nums)

    leaps = [year for year in range(2014, 2050)
             if year % 4 == 0 or (year % 4 != 0 and year % 400 == 0)]
    print(leaps)