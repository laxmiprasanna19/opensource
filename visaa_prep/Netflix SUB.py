x,y,w,z=map(int,input().split())
if(x+y >= z) or (y+w>=z) or (x+w >= z):
    print("YES")
else:
    print("NO")
        
