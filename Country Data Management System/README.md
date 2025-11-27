# Team 5 ( Davinder, Alison and Esteban)
## Purpose of the Data
p_popular.csv contains tax information on goods/services, population growth data, death rates within 20 different countries https://databank.worldbank.org/source/world-development-indicators
## Questions to ask Dr.Hatem
- What do we do when we encounter data that is '..'
- Are we even allowed to create a new inventory to handle both 2006 & 2021 inventories? Is that even allowed? Is there a better way?

## Country Class
`country.py` contains the following variables/properties:
- country_name
- country_code 
- taxes_revenue_percentage_2006
- education_pupils
- male_population
- female_population
- population_annual_growth
- number_of_deaths

## Tasks
Edit country and its data in the system 
Tax percentage raise between 2006-2021
Compare two countries' available data 
Search by available countries 
Sort countries by Alphabetical order 
Ratio male to female population 
Descending (greatest to least) order of country data (growth data, population numbers, etc.) 
Delete countries’ data 
Add a new country entry with all lits information 

## Main App
`main.py` creates a country from the Country class and outputs data
The main application provides a command-line interface where the user selects actions such as adding, editing, deleting, comparing, and sorting countries. All operations interact with the country inventories and the CSV file.

## How to Use the System

## Run the program using: python main.py

When the menu appears, choose one of the numbered options:

Option 1: Load the CSV file (enter data.csv or the provided dataset filename).
Option 2: Add a new country with all required data.
Option 3: Search for a country by name.
Option 4: Edit an existing country’s data.
Option 5: Remove a country from the system.
Option 6: Display countries in descending order by selected data.
Option 7: Display countries in alphabetical order.
Option 8: Compare data between two countries.
Option 9: Compare tax percentages between 2006 and 2021.
Option 10: View male to female population ratio.

Follow the on-screen prompts to enter values or select specific countries.

All changes such as edits and deletions are reflected in the system and can be designed to update the CSV file permanently based on implementation.
This system is designed to help manage, analyze, and compare country-level economic and population data efficiently using a structured and user-friendly interface.
