h=[1,8,6,2,5,4,8,3,7]
def max_pl(h):
    lt=0
    rt=len(h)-1
    best_res=0
    while lt< rt:
        water= (rt-lt) * min(h[lt], h[rt])
        if water> best_res:
            best_res= water
        if h[lt] < h[rt]:
            lt +=1
        else:
            rt-=1
    return best_res
print(max_pl(h))
