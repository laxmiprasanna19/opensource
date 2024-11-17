x,y = map(int,input().split())
c_c = x * 100
if(c_c >= y):
    print(0)
else:
    a_p = (y - c_c + 99) //100
    print(a_p)
