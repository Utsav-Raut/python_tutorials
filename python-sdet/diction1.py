def sample(value):
    sum1=0
    for i in value:
        print("i = ",i)
        if i%2!=0:
            sum1+=value[i]
        else:
            sum1-=i
        print("sum=",sum1)
    print(sum1)
dict1={1:2,2:4,3:6,5:8}
sample(dict1)