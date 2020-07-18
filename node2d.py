# def node2d(r,res,angle):
#     x=[]
#     y=[]
#     temp=-1+1/res
#     while temp<=(1-1/res):
#         x.append(temp)
#         y.append(temp)
#         temp+=2/res
#     if angle !=1:
#          angle=0
#     node=[]
#     newnode=[]
#     nodenum=[]
#     for i in range(2):
#             node.append([])
#             newnode.append([])
#     for i in range(res):
#         for j in range(res):
#             node[0].append(x[i])
#             node[1].append(y[j])
#     for i in range(res*res):
#         if (node[0][i])**2+(node[1][i])**2<=r**2:
#             temp0=node[0][i]
#             temp1=node[1][i]
#             newnode[0].append(temp0)
#             newnode[1].append(temp1)
#             nodenum.append(i)
#     return newnode



import numpy as np

class mesh2d:   
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def isInUnitCircle(self):
        if ((self.x**2+self.y**2)<=1):
            return True
        else:
            return False

res = 32
r=1

nNode = [[0, 0, 0]]

mseq = np.linspace(-1+1/res, 1-1/res, res)

print(nNode)

seq = 1
for nx in mseq:
    for ny in mseq:
        cNode = mesh2d(nx,ny)
        if cNode.isInUnitCircle() :
            nNode.append([r*nx,r*ny,seq])
            seq += 1

print(seq)
