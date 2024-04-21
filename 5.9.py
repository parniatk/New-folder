# (compute future tuition)
#first year
tuition_year_1 = 10000

#Rate of increase
annual_increase = 5

# number of year
number_of_years = 10

# Tuition for future years
for year in range(1, number_of_years + 1):
    tuition_year = tuition_year_1 * (1 + annual_increase / 100) ** (year)
    print(f"Tuition for the year {year}: {tuition_year:.2f} ")