# Function to read data from file
def load_data(filename):
    males, females, heart_rates = [], [], []
    with open(filename, 'r') as file:
        next(file)  # Skip header line
        next(file)  # Skip header line

        for line in file:
            # Split by tab character
            male_temp, female_temp, heart_rate = line.strip().split("\t")
            # Convert to float
            males.append(float(male_temp))
            females.append(float(female_temp))
            heart_rates.append(float(heart_rate))
    return males, females, heart_rates

# Function to calculate mean
def mean(data):
    total = sum(data)
    count = len(data)
    return total / count

# Function to calculate standard deviation
def standard_deviation(data):
    avg = mean(data)
    variance = sum((x - avg) ** 2 for x in data) / len(data)
    return variance ** 0.5

# Function to calculate standard error of mean (SEM)
def standard_error(data):
    return standard_deviation(data) / (len(data) ** 0.5)

# Function to perform linear regression (Females: Temp vs Heart Rate)
def linear_regression(x, y):
    N = len(x)
    sum_x, sum_y = sum(x), sum(y)
    sum_xy = sum(x_i * y_i for x_i, y_i in zip(x, y))
    sum_x2 = sum(x_i ** 2 for x_i in x)
    
    # Compute slope (m)
    m = (N * sum_xy - sum_x * sum_y) / (N * sum_x2 - sum_x ** 2)
    # Compute intercept (b)
    b = (sum_y - m * sum_x) / N
    return m, b

# Main function
def main():
    # Load dataset
    filename = "Comp-workshop-data-plaintext-tabdelimited.txt"
    males, females, heart_rates = load_data(filename)

    # Compute and print statistics
    # print("Mean, Standard Deviation, and Standard Error of the Mean:")
    # for label, data in [("Male Body Temperature", males), 
    #                     ("Female Body Temperature", females), 
    #                     ("Female Heart Rate", heart_rates)]:
    #     print(f"{label}: Mean = {mean(data):.2f}, SD = {standard_deviation(data):.2f}, SEM = {standard_error(data):.2f}")

    # Perform linear regression on female body temperature vs heart rate
    slope, intercept = linear_regression(females, heart_rates)
    print(f"\nLinear Regression (Females: Temp vs Heart Rate): y = {slope:.4f}x + {intercept:.4f}")

# Run the program
if __name__ == "__main__":
    main()
