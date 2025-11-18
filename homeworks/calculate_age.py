dob_year = 1998
dob_month = 4
dob_day = 16
current_year = 2025
current_full_month =10
current_days = 12
number_of_days_in_month = 30

years = current_year - dob_year
months = current_full_month - dob_month
days = number_of_days_in_month - (current_days - dob_day)

print("This person is: \n" + str(years) + " years" + "\n" + str(months) + " months" + "\n" + str(days) + " days")