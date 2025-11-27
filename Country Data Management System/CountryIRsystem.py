#IRSystem Implementation
import csv  #needed to read/write csv
from os import remove
from country import Country


class CountryInventory():

  def __init__(self):
    self.__list_countries = []

  #Search, Tax percentage, compare
  def search_country(self, country_name):
    assert country_name is not None
    for country in self.__list_countries:
      if country.country_name == country_name:
        return country

  #Sorts Countries by Alphabetical Order
  #check this source: https://docs.python.org/3/howto/sorting.html
  def sort_countries(self):
    sorted_array = sorted(self.__list_countries, key=lambda country:country.country_name)
    for country in sorted_array:
      print(country)
    return sorted_array

  #Ratio of female and male population by specified country
  def ratio_male_female(self, country_name):
    country = self.search_country(country_name)
    if country is not None:
      ratio = int(country.male_population / country.female_population * 100)
      return ratio
    else:
      return None

  #get_countries and get_inventory
  def get_countries(self):
    return self.__list_countries

  def get_inventory(self):
    return f"Countries:({self.get_countries()})"

  def add_country(self, country_name, country_code, tax_revenue_percentage,
                  education_pupils, male_population, female_population,
                  population_annual_growth, number_of_deaths):

    country = Country()
    country.country_name = country_name
    country.country_code = country_code
    country.taxes_revenue_percentage = tax_revenue_percentage
    country.education_pupils = education_pupils
    country.male_population = male_population
    country.female_population = female_population
    country.population_annual_growth = population_annual_growth
    country.number_of_deaths = number_of_deaths

    #append country to inventory
    self.__list_countries.append(country)
    return country  

  #Remove country data functionality
  def remove_country_data(self, country_name, year, filename="data.csv"):
    assert country_name is not None

    # -------- REMOVE FROM MEMORY --------
    country = self.search_country(country_name)
    if country is not None:
        self.__list_countries.remove(country)

    # -------- REMOVE FROM CSV PERMANENTLY --------
    import csv
    temp_rows = []

    with open(filename, "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] == "Year":
                temp_rows.append(row)
            elif not (row[2] == country_name and str(row[0]) == str(year)):
                temp_rows.append(row)

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(temp_rows)

    return self.__list_countries

    

  #Descending order
  def descending_country(self):
    sorted_array = sorted(self.__list_countries, key=lambda country:country.country_name, reverse=True)
    for country in sorted_array:
      print(country)

  #country edit functionality
  def country_edit(self, country_name, new_data: dict):
    country = self.search_country(country_name)
    #checks if country is in the list
    if country is None:
       return None
    for key, value in new_data.items():
        setattr(country, key, value)
    return country
  
  def update_country_in_csv(self, filename, year, country):
    import csv
    rows = []

    with open(filename, "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[2] == country.country_name and str(row[0]) == str(year):
                rows.append([
                    year,
                    f"YR{year}",
                    country.country_name,
                    country.country_code,
                    country.taxes_revenue_percentage,
                    country.education_pupils,
                    country.female_population,
                    country.male_population,
                    country.population_annual_growth,
                    country.number_of_deaths
                ])
            else:
                rows.append(row)

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)



  def compare_tax_rate(self, country_name,country_inventory_2006,country_inventory_2021):
    country_2006 = country_inventory_2006.search_country(country_name)
    country_2021 = country_inventory_2021.search_country(country_name)
    
    #check to avoid NoneType crash
    if country_2006 is None or country_2021 is None:
      return "Tax data for 2006 or 2021 is missing for this country."

    rate_2006 = country_2006.taxes_revenue_percentage
    rate_2021 = country_2021.taxes_revenue_percentage
    print(f'2006: {rate_2006}  2021: {rate_2021}')
    #finds the difference in tax revenue percentage
    if rate_2021 - rate_2006 > 0:
      return f"There was an increase in revenue percentage of taxes (2006-2021) by {rate_2021 - rate_2006}"
    elif rate_2021 - rate_2006 < 0:
      return f"There was a decrease in revenue percentage of taxes (2006-2021) by {rate_2006 - rate_2021}"
    else:
      return f"The revenue percentage of taxes (2006-2021) stayed the same"

  def compare_countries(self, country_name1, country_name2):
    #selects specific country from list of countries using the name
    country1 = self.search_country(country_name1)
    country2 = self.search_country(country_name2)
    #checks if country is in the list
    if country1 is None:
      return None
    if country2 is None:
      return None
    return f"(A) {country1} \n(B) {country2}"

  #append a single country to CSV
  def save_country_to_csv(self, filename, year, country):
    with open(filename, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow([
            year,                     # Column 1: Year
            f"YR{year}",             # Column 2: Time code
            country.country_name,   # Column 3: Country Name
            country.country_code,   # Column 4: Country Code
            country.taxes_revenue_percentage,  # Column 5
            country.education_pupils,         # Column 6
            country.female_population,        # Column 7
            country.male_population,          # Column 8
            country.population_annual_growth, # Column 9
            country.number_of_deaths          # Column 10
        ])


  #print(inventory)
  def populate_inventory(self,name_file,country_inventory_2021,country_inventory_2006):
    with open(name_file, 'r') as csvfile:
      csv_reader = csv.reader(csvfile, delimiter=",")
      #skips over first line
      next(csv_reader)

      #loops through csv file; each line is a list
      for line in csv_reader:
        #get values from csv
        population_annual_growth = line[8]
        #FEMALE POPULATION
        if isinstance(line[6], str):
          female_population = 1
        else:
          female_population = line[6]
        #MALE POPULATION
        male_population = int(float(line[7]))
        #COUNTRY NAME
        if isinstance(line[2], str):
          country_name = line[2]
        #COUNTRY CODE
        if isinstance(line[3], str):
          country_code = line[3]
        #NUMBER OF DEATHS
        if isinstance(line[9], str):
          number_of_deaths = 1
        else:
          number_of_deaths = int(line[9])
        #EDUCATION PUPILS
        if isinstance(line[5], str):
          education_pupils = 1
        else:
          education_pupils = int(line[5])
        #TAXES REVENUE PERCENTAGE
        #This be the winner!!!
        if line[4] == "..":
          taxes_revenue_percentage = 1
        elif isinstance(line[4], str):
          taxes_revenue_percentage = float(line[4])
        # else:
        #   taxes_revenue_percentage = float(line[4])

        #check if data is from 2006
        #add country to appropriate inventory

        if int(line[0]) == 2006:
          country_inventory_2006.add_country(country_name, country_code,
                                             taxes_revenue_percentage,
                                             education_pupils, male_population,
                                             female_population,
                                             population_annual_growth,
                                             number_of_deaths)
        else:
          country_inventory_2021.add_country(country_name, country_code,
                                             taxes_revenue_percentage,
                                             education_pupils, male_population,
                                             female_population,
                                             population_annual_growth,
                                             number_of_deaths)
      #print(country_inventory_2006.sort_countries())
