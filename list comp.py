sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow', 'Teapink']
new_list = [val for index, val in enumerate(sample_list) if index not in [0, 4, 5]]
print(new_list)