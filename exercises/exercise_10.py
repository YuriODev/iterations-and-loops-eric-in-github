
# Define the conversion function
def pounds_to_kilograms(pounds):
    return pounds * 0.453592

# Create a list of pounds values
pounds_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


print("Pounds", "Kilograms")

for pounds in pounds_list:
    
    kilograms = pounds_to_kilograms(pounds)

    print(pounds, kilograms)