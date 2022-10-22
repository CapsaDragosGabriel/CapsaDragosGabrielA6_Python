def check(*args,**kwargs):
    num=0
    for element in kwargs:
        if args.__contains__(kwargs[element]):
            num+=1
    return num

def main():
    print(check(1,2,3,4,x=1,y=2,z=3,w=5))

main()