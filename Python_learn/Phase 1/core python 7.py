L =["apple","sushi","pizza"]
T = ("japan","iceland","israel")
D = {"name":"yuval","age":22,"hobby":"coding"}
for i in L:
    print("i want to eat",i)
for i in T:
    print("i want to visit",i)
for i in D:
    print(i + ":", D[i])


people = {

    "yuval" : {"age":22,"hobby":"coding"},
    "shachar": {"age":10, "hobby":"minecraft"},
    "amit" : {"age":18, "hobby": "coding"}
}

enter_name = input("enter name")
if enter_name in people:    
    for i in people[enter_name]:
        print(i + ":", people[enter_name][i])

else:
    print("not found")