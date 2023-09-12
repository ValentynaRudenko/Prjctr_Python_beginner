class Country:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def add(self, country):
        name = self.name + " " + country.name
        population = self.population + country.population
        instance = Country(name, population)
        return instance


bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)


bosnia_herzegovina = bosnia.add(herzegovina)
print(bosnia_herzegovina.name)
print(bosnia_herzegovina.population)
