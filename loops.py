#list is data structure to add multipe values . these multiple
# can be same or different data types.
list_of_cloud=['gcp', 'aws','digitalOcean','azure']
print(list_of_cloud)
list_of_cloud.append('IBM')
print(list_of_cloud)
list_of_cloud.insert(1,'orwcle')
print(list_of_cloud)

# count no of elements in list

print(len(list_of_cloud))

# iterate list with the help of loop

for cloud in list_of_cloud:
    print(cloud)

for i in range(0,10):
    print(i+1)