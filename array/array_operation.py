
from itertools import groupby

ax=[1,2,1]
ay=['a','b','b']

az=zip(ax,ay)

for x,y in groupby(sorted(az),key=lambda _:_[0]):
    y_list=[v for k, v in y]
    print(y_list)


a1=[]
a1.append(['a',2])
a1.append(['b',4])
print(a1)

x,y=[*zip(*a1)]
print(x,y)

# ss=zip(*a1)
# for v in ss:
#     print(v)
