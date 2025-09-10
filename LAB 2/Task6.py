countries = {
    "China": 1444216107,
    "India": 1393409038,
    "USA": 331893745,
    "Indonesia": 273523621,
    "Pakistan": 220892331,
    "Brazil": 212559409,
    "Nigeria": 206139589,
    "Bangladesh": 164689383,
    "Russia": 145934460,
    "Mexico": 128932753
}
Populated_countries = [] 
for i in range(0,3):
    max_val = 0
    for country in countries:
        if(countries[country]>max_val):
            max_val = countries[country]
            max_country = country
    Populated_countries.append(max_country)
    countries.pop(max_country)
print("Top 3 most populated countries are:")
print(Populated_countries)