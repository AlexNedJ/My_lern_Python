# function power_set(flowers)
#     fragrances <- Set.new
#     fragrances.add(Set.new)
#     for each flower in flowers
#         new_fragrances<- copy(fragrances)
#         for each fragrances in new_fragrances
#             fragrances.add(flower)
#             fragrances<- fragrances+new_fragrances
# return fragrances

def power_set(array):
    result = [[]]
    for element in array:
        new_list = [x.copy() for x in result] #result.copy()
        for subset in new_list:
            subset.append(element)
        result += new_list
    return result

dates="rose","lily","daisy","tulip"

print(power_set(dates))