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

pdb.set_trace()




