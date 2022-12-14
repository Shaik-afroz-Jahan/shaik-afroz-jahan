def test(list):
    list=[2,4,3,3,3,5,7,8]
    return len(list)==8 and list.count(list[4])==3
print(test(list))