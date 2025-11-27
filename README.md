# Country Data Management System

Team 5 — Davinder, Alison, Esteban (

## Project Overview

The Country Data Management System is a command-line application built in Python that allows users to manage, analyze, and compare economic and demographic data for multiple countries. The system focuses on structured handling of tax revenue, population statistics, growth rates, and mortality data across different years.

The project uses real-world data sourced from the World Bank World Development Indicators and provides an interactive interface for performing meaningful data operations.

## Data Source

The dataset (p_popular.csv) contains tax information on goods and services, population growth data, and death rates for 20 countries.
Source: [https://databank.worldbank.org/source/world-development-indicators](https://databank.worldbank.org/source/world-development-indicators)

## Key Features

* Add new country records with complete data
* Edit existing country data
* Permanently update and manage data stored in CSV files
* Delete country entries
* Search countries by name
* Compare data between two countries
* Calculate tax percentage variation between 2006 and 2021
* Display male-to-female population ratios
* Sort countries alphabetically
* Sort countries by population or growth in descending order

## System Design

The system follows an object-oriented approach using clearly separated modules:

Country Class (country.py)
Defines the structure of a single country with the following attributes:

* country_name
* country_code
* taxes_revenue_percentage
* education_pupils
* male_population
* female_population
* population_annual_growth
* number_of_deaths

Inventory System (CountryIRsystem.py)
Manages country collections, file operations, searching, sorting, editing, and deletion logic.

Application Controller (main.py)
Handles user interaction through a menu-based interface and connects user input to system operations.

## How to Run the Project

1. Clone or download the repository.

2. Ensure the following files are in the same directory:

   * main.py
   * CountryIRsystem.py
   * country.py
   * p_popular.csv
   * README.md

3. Run the program using:
   python main.py

## How to Use

After running the program, a menu will be displayed with numbered options. Users can select actions such as:

* Loading the dataset
* Adding or editing country data
* Searching for specific countries
* Performing comparisons and analysis
* Sorting and displaying country lists

Follow the on-screen prompts to input values or select a specific country.

## Example Use Cases

* Analyze population growth trends across multiple countries
* Compare tax revenue performance between years
* Maintain and update structured demographic data
* Perform country-level statistical comparisons

## File Structure

main.py
Controls program execution and user interaction

CountryIRsystem.py
Handles business logic and data processing

country.py
Defines the Country class structure and properties

p_popular.csv
Primary dataset used by the system

README.mdProject documentation

## Screenshots Folder
This section demonstrates the main functionality and user interaction flow of the Country Data Management System. Each screenshot shows real execution output from the command-line interface, highlighting how users navigate and perform operations within the system.

Main Menu Interface - Displays the primary user interface, showing all available options such as adding, editing, searching, comparing, and removing country data.

Adding a New Country -Shows the process of entering a new country record, including all required data fields and year selection.

Searching Country Data - Illustrates how the system retrieves and displays a country’s information based on the entered country name.

Comparing Countries - Demonstrates side-by-side comparison of two countries, allowing analysis of their tax revenue and population-related data.

Editing Country Data - Shows how existing country information can be modified by viewing current values and updating selected fields.

Removing a Country - Displays the process of deleting a country record from the system and confirming successful removal.

## Project Purpose

This project demonstrates practical implementation of:

* Object-Oriented Programming in Python
* File handling and data persistence
* Structured data analysis
* Command-line application design

It is an academic project and as part of a public portfolio to showcase data management and analytical programming skills.
