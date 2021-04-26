import pdb
from models.city import City
from models.country import Country


from repositories import city_repository
from repositories import country_repository


city_repository.delete_all()
country_repository.delete_all()


country_1 = Country("Spain")
country_repository.save(country_1)

country_2 = Country("France")
country_repository.save(country_2)

country_3 = Country("USA")
country_repository.save(country_3)

country_4 = Country("Canada")
country_repository.save(country_4)

country_5 = Country("Australia")
country_repository.save(country_5)

country_6 = Country("Switzerland")
country_repository.save(country_6)

country_7 = Country("Scotland")
country_repository.save(country_7)

country_8 = Country("Germany")
country_repository.save(country_8)

country_9 = Country("Italy")
country_repository.save(country_9)

country_10 = Country("Croatia")
country_repository.save(country_10)

city_1 = City("Barcelona", country_1)
city_repository.save(city_1)

city_2 = City("Madrid", country_1)
city_repository.save(city_2)

city_3 = City("Valencia", country_1)
city_repository.save(city_3)



city_4 = City("Paris", country_2)
city_repository.save(city_4)

city_5 = City("Lyon", country_2)
city_repository.save(city_5)



pdb.set_trace()




