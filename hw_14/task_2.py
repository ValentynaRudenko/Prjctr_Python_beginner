class Country:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __add__(self, country):
        return Country(self.name + " " + country.name,
                       self.population + country.population)


bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)

bosnia_herzegovina = bosnia + herzegovina
print(bosnia_herzegovina.population)
print(bosnia_herzegovina.name)
