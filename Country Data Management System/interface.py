from CountryIRsystem import *

class CountryInterface():
  @staticmethod
  def country_inventory_cl():

    def main_menu():
      print("*************************************************************")
      print("****       Welcome to the Country Data System           ****")
      print("*************************************************************")
      print("[0] - exit program")
      print("[1] - Input file name")
      print("[2] - Add new country")
      print("[3] - Search country data by the country name")
      print("[4] - Edit the country data")
      print("[5] - Remove country data")
      print("[6] - Descending order of the countries")
      print("[7] - Alphabetical order of the countries")
      print("[8] - Compare two countries")
      print("[9] - Compare a countries taxes (2006/2021)")
      print("[10] - check the ratio of female and male populations in the country")

    main_menu()

    new_inventory = CountryInventory()
    country_inventory_2021 = CountryInventory()
    country_inventory_2006 = CountryInventory()

    while True:
      option = int(input("Option: "))

      # EXIT PROGRAM
      if option == 0:
        print("Program exited")
        break

      # LOAD CSV
      elif option == 1:
        file_name = input("Enter the csv file name: ")
        new_inventory.populate_inventory(file_name, country_inventory_2021, country_inventory_2006)

      # ADD COUNTRY
      elif option == 2:
        country_name = input("Enter the country name: ")
        country_code = input("Enter the country code: ")
        taxes_revenue_percentage = int(input("Enter the tax revenue percentage country: "))
        male_population = int(input("Enter the male population: "))
        female_population = int(input("Enter the female population: "))
        population_annual_growth = float(input("Enter the population annual growth: "))
        number_of_deaths = int(input("Enter the number of deaths: "))
        education_pupils = int(input("Enter the education pupils: "))
        year = input("Is this data for 2006 or 2021? Enter year: ").strip()

        if year == "2006":
          country = country_inventory_2006.add_country(
            country_name, country_code, taxes_revenue_percentage,
            education_pupils, male_population, female_population,
            population_annual_growth, number_of_deaths
          )
          if country:
            country_inventory_2006.save_country_to_csv("data.csv", year, country)
            print("Country added to 2006 and saved")

        elif year == "2021":
          country = country_inventory_2021.add_country(
            country_name, country_code, taxes_revenue_percentage,
            education_pupils, male_population, female_population,
            population_annual_growth, number_of_deaths
          )
          if country:
            country_inventory_2021.save_country_to_csv("data.csv", year, country)
            print("Country added to 2021 and saved")

        else:
          print("Invalid year. Please enter 2006 or 2021.")

      # SEARCH COUNTRY
      elif option == 3:
        country_name = input("Enter the country name: ")
        country = country_inventory_2021.search_country(country_name)

        if country:
          print(country)
        else:
          country = country_inventory_2006.search_country(country_name)
          if country:
            print(country)
          else:
            print("Country not found")

      # EDIT COUNTRY
      elif option == 4:
        country_name = input("Enter the country name to edit: ")
        year = input("Is this country from 2006 or 2021? Enter year: ").strip()

        if year == "2006":
            inventory = country_inventory_2006
        elif year == "2021":
            inventory = country_inventory_2021
        else:
          print("Invalid year. Please enter 2006 or 2021.")
          continue  #prevents red line + bad logic

        country = inventory.search_country(country_name)

        if country is None:
          print("Country not found in selected year")
        else:
          print("\nCurrent Country Data:")
          print(country)

          country_code = input(f"Enter new country code [{country.country_code}]: ") or country.country_code
          taxes = input(f"Enter new tax revenue [{country.taxes_revenue_percentage}]: ") or country.taxes_revenue_percentage
          male = input(f"Enter new male population [{country.male_population}]: ") or country.male_population
          female = input(f"Enter new female population [{country.female_population}]: ") or country.female_population
          growth = input(f"Enter new population growth [{country.population_annual_growth}]: ") or country.population_annual_growth
          deaths = input(f"Enter new number of deaths [{country.number_of_deaths}]: ") or country.number_of_deaths
          pupils = input(f"Enter new education pupils [{country.education_pupils}]: ") or country.education_pupils

          updated_data = {
            "country_code": str(country_code),
            "taxes_revenue_percentage": float(taxes),
            "male_population": int(male),
            "female_population": int(female),
            "population_annual_growth": float(growth),
            "number_of_deaths": int(deaths),
            "education_pupils": int(pupils)
          }

          inventory.country_edit(country_name, updated_data)

          #PERMANENT UPDATE TO CSV
          inventory.update_country_in_csv("data.csv", year, country)

          print("Country edited and permanently saved to CSV")

      # REMOVE COUNTRY FIXED
      elif option == 5:
        print("Remove Country:")
        country_name = input("Enter the country name to remove: ")
        year = input("Is this country from 2006 or 2021? Enter year: ").strip()

        if year == "2006":
          before = len(country_inventory_2006.get_countries())
          country_inventory_2006.remove_country_data(country_name, year, "data.csv")
          after = len(country_inventory_2006.get_countries())

          if after < before:
            print(f"{country_name} removed from 2006 inventory")
          else:
            print(f"{country_name} not found in 2006")

        elif year == "2021":
          before = len(country_inventory_2021.get_countries())
          country_inventory_2021.remove_country_data(country_name, year,  "data.csv")
          after = len(country_inventory_2021.get_countries())

          if after < before:
            print(f"{country_name} removed from 2021 inventory")
          else:
            print(f"{country_name} not found in 2021")

        else:
          print("Invalid year. Please enter 2006 or 2021.")

      # DESCENDING
      elif option == 6:
        print("Descending Order:")
        country_inventory_2021.descending_country()

      # ALPHABETICAL
      elif option == 7:
        print("Alphabetical Order:")
        country_inventory_2021.sort_countries()

      # COMPARE COUNTRIES
      elif option == 8:
        c1 = input("Enter first country: ")
        c2 = input("Enter second country: ")
        print(country_inventory_2021.compare_countries(c1, c2))

      # COMPARE TAX
      elif option == 9:
        country_name = input("Enter the country name: ")
        print(country_inventory_2021.compare_tax_rate(country_name, country_inventory_2006, country_inventory_2021))

      # RATIO
      elif option == 10:
        country_name = input("Enter the country name: ")
        print(country_inventory_2021.ratio_male_female(country_name))

      else:
        print("Please try again")
        main_menu()
