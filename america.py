'''
<Your Name>, <Grade> <Course>
Assignment: String Slicing
This assignment will demonstrate how to manipulate and print strings.
'''

# DO NOT EDIT THIS LINE
country = "the united states of america"

# 1. print the country in *lower case*
print(country.lower())

# 2. print country in *title case*
print(country.title())

# 3. print country in *upper case*
print(country.upper())

# 4. print the length of the country string as:
#    string length of country: <length>
print("lenght of country: " + str(len(country)))

# 5. slice the string "america" from country, upper case the 'a',
#    and store it in a variable named `short_name` with a value "America"
shortname = country[-7:].capitalize()
print(shortname)

# 6. concantentate a string value with `short_name` to
#    produce the name of the continent where the country resides
#    and print the result:
#    <title case country> is located within <title case continent>
country = "the united states of america"
continent_short_name = "North America" 
country_title = country.title()
continent = continent_short_name.title()
print(f"{country_title} is located within {continent}")

# 7. print a statement how we refer to people from the country:
#    People from <title case country> are called <title case of people in plural>
country = "The United States Of America"
people_name = "Americans"
country_title = country.title()
people_title = people_name.title()  
print(f"People from {country_title} are called {people_title}")
