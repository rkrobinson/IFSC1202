# Step 1: Create an empty two-dimensional list called "properties"
properties = []

# Open the CSV file and read the data
try:
    with open('Exam_Two_Properties.csv', 'r') as file:  # Make sure the filename is in quotes
        for line in file:
            # Step 2: Split each line into a one-dimensional list using a comma as the delimiter
            property_data = line.strip().split(',')
            
            # Step 3: Convert the price (column 4) to a floating-point number
            property_data[4] = float(property_data[4])
            
            # Step 4: Append the one-dimensional list to the "properties" list
            properties.append(property_data)

except FileNotFoundError:
    print("The file 'Exam_Two_Properties.csv' was not found.")
    exit()

# Step 6: Create an empty two-dimensional list called "zipcodes"
zipcodes = []

# Step 7: Loop through all rows in the "properties" list
for property in properties:
    prop_zipcode = property[3]  # Zip Code (Column 3)
    prop_price = property[4]    # Price (Column 4)

    # Step 8: Loop through the "zipcodes" list to check for matching zip codes
    match_found = False
    for zipcode_row in zipcodes:
        if zipcode_row[0] == prop_zipcode:  # If zip code matches
            # Increment the number of properties (Column 1)
            zipcode_row[1] += 1
            # Add the price of the property to the sum (Column 2)
            zipcode_row[2] += prop_price
            match_found = True
            break

    # Step 9: If no match is found, append a new row to "zipcodes"
    if not match_found:
        zipcodes.append([prop_zipcode, 1, prop_price])

# Step 10: Print the report heading
print("\nReport:")
print(f"{'Zipcode':<10} {'Count':<10} {'Average Price':<15}")

# Step 11: Loop through the "zipcodes" list and print each row
for zipcode_row in zipcodes:
    zipcode = zipcode_row[0]
    count = zipcode_row[1]
    sum_price = zipcode_row[2]
    average_price = sum_price / count  # Calculate average price
    print(f"{zipcode:<10} {count:<10} ${average_price:,.2f}")
