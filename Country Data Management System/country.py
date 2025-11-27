class Country: 

  def __init__(self):
    self._country_name = ""
    self._country_code = 0
    self._taxes_revenue_percentage = 0
    self._education_pupils = 0
    self._male_population = 0
    self._female_population = 0
    self._population_annual_growth = 0
    self._number_of_deaths = 0
    self._taxes_revenue_percentage_2006 = 0

#GETTER: gets the percentage of the annual tax revenue 
  @property
  def taxes_revenue_percentage_2006(self):
    return self._taxes_revenue_percentage_2006

#SETTER: Sets the value for the taxes revenue percentage
  @taxes_revenue_percentage_2006.setter
  def taxes_revenue_percentage_2006(self, taxes_revenue_percentage_2006):
    assert taxes_revenue_percentage_2006 > 0  #Set if value if higher than zero
    self._taxes_revenue_percentage_2006 = taxes_revenue_percentage_2006

##Country Name
#Getter: return the country name

  @property
  def country_name(self):
    return self._country_name

#SETTER: Set the country name

  @country_name.setter
  def country_name(self, country_name):
    self._country_name = country_name

##Number of death
#GETTER: return the amount of number of death

  @property
  def number_of_deaths(self):
    return self._number_of_deaths

#SETTER: set the amount of number of death

  @number_of_deaths.setter
  def number_of_deaths(self, number_of_deaths):
    assert number_of_deaths > 0
    self._number_of_deaths = number_of_deaths

##Country Code
#GETTER: return the country code

  @property
  def country_code(self):
    return self._country_code

#SETTER: Set the country code.
  @country_code.setter
  def country_code(self, country_code):
    self._country_code = country_code

  # function implementations for education and tax percentage

  ##EDUCATION
  #GETTER: gets/returns the amount of education pupils
  @property
  def education_pupils(self):
    return self._education_pupil

  #SETTER: Sets the amount of education pupils in the country
  @education_pupils.setter
  def education_pupils(self, education_pupils):
    assert education_pupils > 0
    self._education_pupil = education_pupils

  ##TAX PERCENTAGES
  #GETTER: gets the percentage of the annual tax revenue
  @property
  def taxes_revenue_percentage(self):
    return self._taxes_revenue_percentage

  #SETTER: Sets the value for the taxes revenue percentage
  @taxes_revenue_percentage.setter
  def taxes_revenue_percentage(self, taxes_revenue_percentage):
    assert taxes_revenue_percentage > 0  #Set if value if higher than zero
    self._taxes_revenue_percentage = taxes_revenue_percentage

  ##POPULATION
  #GETTER: returns annual population growth as percentage
  @property
  def population_annual_growth(self):
    return self._population_annual_growth

  #SETTER: Sets annual population growth (percentage)
  @population_annual_growth.setter
  def population_annual_growth(self, population_annual_growth):
    self._population_annual_growth = population_annual_growth

    ##MALE POPULATION
    #GETTER: returns amount of male population
  @property
  def male_population(self):
    return self._male_population
  #SETTER: Sets amount of male population

  @male_population.setter
  def male_population(self, male_population):
    assert male_population >= 0  # there can not be negative populations
    self._male_population = male_population

  ##FEMALE POPULATION
  #GETTER: returns amount of female population

  @property
  def female_population(self):
    return self._female_population

  #SETTER: Sets amount of female population

  @female_population.setter
  def female_population(self, female_population):
    assert female_population >= 0  # there can not be negative populations
    self._female_population = female_population

  def __str__(self):
    return f"Country: {self.country_name}, {self.country_code}, {self.taxes_revenue_percentage},{self.education_pupils},{self.male_population},{self.female_population},{self.population_annual_growth},{self.number_of_deaths},{self.taxes_revenue_percentage_2006}"
  def __lt__(self, another):
    return self.country_name < another.country_name