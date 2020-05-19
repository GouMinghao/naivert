from multiprocessing import Pool
def f(a):
    return a*2

p = Pool(processes=2)
# for x,y in zip((1,2,3),(4,5,6)):
#     print(x,y)
a = p.map(f,range(10))
print(a)
