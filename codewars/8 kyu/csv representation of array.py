def to_csv_text(array):
    flat_list = []
    for sublist in array:
      for item in sublist:
        flat_list.append(item)
        flat_list.append('\n')
    return flat_list


print(to_csv_text([[0, 1, 2, 3, 4],
                   [10, 11, 12, 13, 14],
                   [20, 21, 22, 23, 24],
                   [30, 31, 32, 33, 34]]))

# output
#  '0,1,2,3,4\n'
#     +'10,11,12,13,14\n'
#     +'20,21,22,23,24\n'
#     +'30,31,32,33,34'
