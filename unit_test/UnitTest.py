import unittest


class Tests(unittest.TestCase):
    def test_most_near_not_visit(self):
        visit = [True for _ in range(0, len(pre_order))]

        visit[3] = False
        visit[5] = False
        self.assertEqual(most_near_not_visit(visit), 3)
        self.assertEqual(most_near_not_visit(visit, 4, 7), 5)

def most_near_not_visit(visit, begin=0, end=len(in_order_visit)):
        """在visit[begin,end]中左边第一个为False的index"""
        for index, v in enumerate(visit[begin:end], begin):
            if not v:
                return index
        return -1