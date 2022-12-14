def test(list):
    list=[19,7,19,16,5,3,5,5,2]
    return list.count(19)==2 and list.count(5)>=3
print(test(list))