list_to_sort = [[3, 2, 3], [2, 0, 2], [3, 0, 1]]
sorted_list = sorted(list_to_sort, key=lambda x: (x[1], x[2])) #x[1] to pierwszy warunek sortowania. Jeśli są te same wartości to obiera warunek x[2].
print(list_to_sort)
print(sorted_list)
