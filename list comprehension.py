raw_list = ["abdul", "karachi", "maths" , "science"]
lowercased_list = [element.lower() for element in raw_list if len(element) > 5]
print(lowercased_list)