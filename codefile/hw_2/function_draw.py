def draw_many( p,x ):
    for i in range(1,x):
        print(p,end="")

def draw_by_r( r ):
    for i in range(1,r):
        draw_many(' ',r-i)
        print('#',end="")
        if i>1:
            draw_many(' ',2*i-2)
            print('#',end="")
        print()
    for i in range(r-2,0,-1):
        draw_many(' ',r-i)
        print('#',end="")
        if i>1:
            draw_many(' ',2*i-2)
            print('#',end="")
        print()

draw_by_r(4)
draw_by_r(5)
draw_by_r(6)
draw_by_r(7)
draw_by_r(8)

