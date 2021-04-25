import pdb
from models.city import City
from models.country import Country


from repositories import city_repository
from repositories import country_repository


city_repository.delete_all()
country_repository.delete_all()


country_1 = Country("Spain")
country_repository.save(country_1)

city_1 = City("Barcelona", country_1)
city_repository.save(city_1)

city_2 = City("Madrid", country_1)
city_repository.save(city_2)

city_3 = City("Valencia", country_1)
city_repository.save(city_3)

country_2 = Country("France")
country_repository.save(country_2)

city_4 = City("Paris", country_2)
city_repository.save(city_4)

city_5 = City("Lyon", country_2)
city_repository.save(city_5)



pdb.set_trace()




