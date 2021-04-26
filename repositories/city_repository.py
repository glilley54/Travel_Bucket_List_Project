from db.run_sql import run_sql

from models.city import City
from models.country import Country
import repositories.country_repository as country_repository


#CREATE CITY IN DB

def save(city):
    sql = "INSERT INTO cities (name, visited, country_id) VALUES (%s, %s, %s) RETURNING *"
    values = [city.name, city.visited, city.country.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    city.id = id
    return city

#SELECT ALL CITIES IN DB
     
def select_all():
    cities = []

    sql = "SELECT * FROM cities"
    results = run_sql(sql)

    for row in results:
        country = country_repository.select(row['country_id'])
        city = City(row['name'],row['visited'],country, row['id'] )
        tasks.append(city)
    return cities

    #SELECT PARTICULAR CITY BY ID

def select(id):
    city = None
    sql = "SELECT * FROM cities WHERE id = %s"
    values =[id]
    result = run_sql(sql, values)[0]

    if result is not None:
        country = country_repository.select(row['country_id'])
        city = City(result['name'], result['visited'],country, result['id'] )
    return city

# UPDATE/EDIT CITY

def update(city):
    sql = "UPDATE cities SET (name, visited, country_id) = (%s, %s, %s) WHERE id = %s"
    values = [city.name, city.visited, city.country_id, city.city_id]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE  FROM cities"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM cities WHERE id = %s"
    values = [id]
    run_sql(sql, values)