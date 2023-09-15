l1 = ['customer_name', 'age', 'phone_no.']
l2 = ['Anand', 25, 9799797, 'Troodon', 25, 234334, 'xyz', 11, 1343434]

# Initialize an empty dictionary to store the mapping
mapping = {}
name_list= []
age_list = []
phone_no_list = []
flag = 1
age_flag = 2
ph_flag = 3



for keys in l1:
    for index,item in enumerate(l2):
        if keys == l1[0]:
            if index==0 or index%3==0:
                name_list.append(item)
                mapping[keys] = name_list
        if keys == l1[1]:
            if index==1 or index==flag +3:
                age_list.append(item)
                flag=index
                mapping[keys] = age_list
        if keys == l1[2]:
            if index == 2 or index == ph_flag +3:
                phone_no_list.append(item)
                ph_flag = index
                mapping[keys] = phone_no_list


print(mapping)