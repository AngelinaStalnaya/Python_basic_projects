nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

nice_list = [part for elem in nice_list for part in elem]
nice_list = [symbol for part in nice_list for symbol in part]

print(nice_list)
