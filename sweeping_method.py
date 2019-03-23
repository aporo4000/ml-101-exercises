# 掃き出し法
import numpy as np

#x = np.array([[2,2,3,10],[8,6,4,12],[11,8,6,14]])
#x[0] = x[0]/x[0][0]
#x[1] = x[1] - x[0]*x[1][0]
#x[2] = x[2] - x[0]*x[2][0]
#x[1] = x[1]/x[1][1]
#x[2] = x[2] - x[1]*x[2][1]
#x[2] = x[2]/x[2][2]

#x_3 = x[2][2]
#x_2 = x[1][3] - x[1][2]*x_3
#x_1 = x[0][3] - (x[0][1]*x_2+x[0][2]*x_3)


# n次元
#x = np.array([[2,2,3,10,11],[8,6,4,12,22],[11,8,6,14,44],[2,2,3,10,55]])
x = np.random.rand(3,4)

for i in range(len(x)):
    if np.all(x[i][:i]>0):
        for v in range(len(x[i][:i])):
            x[i] = x[i] - x[v]*x[i][v]
    if x[i][i] != 1:
        x[i] = x[i]/x[i][i]

# -0が出力をプラスの符号に変換
x = x+0.
print(x)

