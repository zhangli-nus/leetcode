# coding: utf-8

from collections import defaultdict


class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not len(matrix):
            return 0
        h, w = len(matrix), len(matrix[0])
        t = defaultdict(list)


        if matrix[0][0] == "1":
            t[0, 0] = [1, 1, 1, 1]  # 纵，横，往上
        else:
            t[0, 0] = [0, 0, 0, 0]  # 纵，横，往上

        for i in range(1, h):
            if matrix[i][0] == "1":
                t[i, 0] = [t[i - 1, 0][0] + 1, 1, t[i - 1, 0][2] + 1, 1]
            else:
                t[i, 0] = [0, 0, 0, 0]

        for i in range(1, w):
            if matrix[0][i] == "1":
                t[0, i] = [1, t[0, i - 1][1] + 1, 1, t[0, i - 1][3] + 1]
            else:
                t[0, i] = [0, 0, 0, 0]

        for i in range(1, h):
            for j in range(1, w):
                if matrix[i][j] == "1":
                    t[i, j] = [0, 0, 0, 0]
                    t[i, j][0] = t[i - 1, j][0] + 1
                    t[i, j][1] = t[i, j - 1][1] + 1
                    if matrix[i-1][j-1] == "1" and matrix[i-1][j] == "1" and matrix[i][j-1] == "1":
                        v1 = (min(t[i - 1, j - 1][2], t[i - 1, j][2]) + 1,
                              min(t[i - 1, j - 1][3], t[i, j - 1][3]) + 1)
                        v2 = (2, min(t[i-1, j][1], t[i, j-1][1]+1))
                        v3 = (min(t[i, j-1][0], t[i-1, j][0] + 1), 2)
                        if v1[0]*v1[1] >= v2[0]*v2[1] and v1[0]*v1[1] >= v3[0]*v3[1]:
                            t[i, j][2], t[i, j][3] = v1
                        else:
                            if v2[0]*v2[1]>v3[0]*v3[1]:
                                t[i, j][2], t[i, j][3] = v2
                            else:
                                t[i, j][2], t[i, j][3] = v3
                    else:
                        t[i, j][2] = 1
                        t[i, j][3] = 1
                else:
                    t[i, j] = [0, 0, 0, 0]

        max_h = -1
        for i in range(h):
            for j in range(w):
                print(i, "\t" , j, "\t", t[i, j])
                v = max(t[i, j][0], t[i, j][1], t[i, j][2] * t[i, j][3])
                if max_h < v:
                    max_h = v
        return max_h


if __name__ == '__main__':
    t = Solution()
    a = [["1","0","1","0"],["1","0","1","1"],["1","0","1","1"],["1","1","1","1"]]
    res = t.maximalRectangle(a)
    print(res)