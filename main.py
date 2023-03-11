# mylist=[3,6,5,2,4,4,5,1,5,5,5,4,54,5,684,6,16,81,561,68,16,841]
# j=0
# for i in range(0,len(mylist)):
#     if mylist[i]==5:
#         j=j+1
# print(j)


# for i in range(0,len(mylist)):
#     print(i)

# my_dic={
#     "user_zero":{'first_name':'milad','last_name':'yousefi','age':25,'marks':[6,2,5,1,5,4,2,5,6]},
#     "user_one":{'first_name':'ali','last_name':'eftekhari','age':23,'marks':[6,4,1,5,2,5,4,1,2]},
#     "user_two":{'first_name':'mahsa','last_name':'familbaragi','age':25,'marks':[6,4,1,5,3,5,4,1,2]},
# }
# print(my_dic['user_one']['marks'][0])


# list_test=list((1,2,3,6,5,2,1,5,4))
# print(list_test)

# thisdict = dict(name = "John", age = 36, country = "Norway")
# print(thisdict['name'])

# dict_man={
#     'key_one':'Test',
#     'key_two':25
# }
###### update dict with method first
# dict_man['key_two']=26
# print(dict_man['key_two'])

######### update dict with mtheod secondary
# dict_man.update({"key_two":43})
# print(dict_man['key_two'])

############ add a new element to the dict
# dict_man['key_three']=[2,3,2,5,1,5,2,6,96,5]
# print(dict_man['key_three'])

############ update a sub-element in to main element 
 
# print('Before My dict: ',my_dic['user_two'])
# my_dic['user_two']['marks'][1]=my_dic['user_two']['marks'][1]+2
# print("After My dict :",my_dic['user_two'])

############## add new element for my_dic (user four)
# my_dic['user_four']={'first_name':'Kazem','last_name':'athari','age':101,'marks':[0,0,0,0,2,0,0,0,0]}
# print(my_dic)


# list_test_akharkelas=[1,2,5,3,6,2,5,1]
# for k in range(0,len(list_test_akharkelas)):
#     print(list_test_akharkelas[k])

# for k in list_test_akharkelas:
#     print(k)

my_set={"milad","yousefi","ali"}
for j in my_set:
    print(j)