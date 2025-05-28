input_file = "Comp-workshop-data-plaintext-tabdelimited.txt" 
male_tempratures = []
female_temperatures = [] 
female_heart_rates = []

# importing input file 
with open(input_file, 'r') as file:
    next(file)  # Skip header line
    next(file)
    for line in file:    # for iterating line by line 
        # Spliting by tab character
        males, females, beats_per_min = line.strip().split("\t")
        # converting str values into float 
        male_tempratures.append(float(males))
        female_temperatures.append(float(females))
        female_heart_rates.append(float(beats_per_min))

# funtion of calculating sum of all values 
def cal_sum(data_list):
    total_sum = 0
    for data in data_list:
        total_sum += data
    return total_sum

# function of calculating mean
def mean(data_list):
    total_sum = cal_sum(data_list)  #  sum of all values 
    total_count = len(data_list)  # total number of values
    return round((total_sum / total_count),2)  

# function of calculating standard deviation
def standard_deviation(data_list):
    average = mean(data_list) # calculating mean 
    diffenreces = []  # create to do sum of all square of (xi - mean of x)
    for data in data_list:
        diff = (data - average) ** 2  # calculating difference and make square
        diffenreces.append(diff)
    total_count = len(data_list)  # total number of values
    variance = cal_sum(diffenreces) / total_count  # formula of variance
    return round((variance ** 0.5),2) 

# function of calculating standard error of mean (SEM)
def standard_error(data_list):
    total_count = len(data_list) # total number of values
    SD = standard_deviation(data_list)
    return round(( SD / (total_count ** 0.5)),2)

# function of calculating gradient/slope and intercept for best fit straight line of the relationship between body temperature (x-axis) and heart rate (y-axis) in females
def linear_regression(x, y):
    total_count = len(x) # total number of values 
    product_xy=[] # for calulating products of sum 
    square_x = [] # for calculating squares of sum 
    
    for i in range(total_count):
        square_x.append(x[i] ** 2)
        product_xy.append(x[i] * y[i])

    # formula of gradient/slope
    b = ((total_count * cal_sum(product_xy))-(cal_sum(x) * cal_sum(y))) / ((total_count * cal_sum(square_x))-((cal_sum(x)**2)))
    # formula of intercept(a)
    a = ((cal_sum(y) * cal_sum(square_x))-(cal_sum(x) * cal_sum(product_xy))) / ((total_count * cal_sum(square_x))-(cal_sum(x)**2))
    
    return b,a # returning slope and intercept 

# printing outputs of Mean, Standard Deviation, and Standard Error of the Mean
print("Mean, Standard Deviation, and Standard Error of the Mean :")
print("Male Body Temperature :")
print(f" Mean = {mean(male_tempratures)}, SD = {standard_deviation(male_tempratures)}, SEM = {standard_error(male_tempratures)}")
print("Female Body Temperature :")
print(f" Mean = {mean(female_temperatures)}, SD = {standard_deviation(female_temperatures)}, SEM = {standard_error(female_temperatures)}")
print("Female Heart Rate :")
print(f" Mean = {mean(female_heart_rates)}, SD = {standard_deviation(female_heart_rates)}, SEM = {standard_error(female_heart_rates)}")

# performing linear regression on female body temperature vs female heart rate
slope, intercept = linear_regression(female_temperatures, female_heart_rates)

print(f"\nLinear Regression (Females: Body Temperature vs Heart Rate) y = a + bx :")
print(f"y = {intercept:.4f} + {slope:.4f}x")