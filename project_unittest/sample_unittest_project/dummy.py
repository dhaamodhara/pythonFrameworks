unordered_list=[3,4,2,5,6]
ordered_list=[]
while unordered_list:
    minimum=unordered_list[0]
    for item in unordered_list:
        if item<minimum:
            minimum=item
    ordered_list.append(minimum)
    unordered_list.remove(minimum)
print(ordered_list)