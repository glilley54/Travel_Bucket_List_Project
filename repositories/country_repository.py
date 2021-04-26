from db.run_sql import run_sql

from models.country import Country
from models.city import City



#CREATE COUNTRY IN DB

def save(country):
    sql = "INSERT INTO countries (name, visited) VALUES (%s, %s) RETURNING *"
    values = [country.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    country.id = id
    return country

#SELECT ALL Countries FROM DB
     
def select_all():
    countries = []

    sql = "SELECT * FROM countries"
    results = run_sql(sql)

    for row in results:
        country = Country(row['name'],row['id'] )
        tasks.append(country)
    return countries

    #SELECT PARTICULAR COUNTRY BY ID

def select(id):
    city = None
    sql = "SELECT * FROM countries WHERE id = %s"
    values =[id]
    result = run_sql(sql, values)[0]

    if result is not None:
        
        contry = Country(result['name'], result['id'] )
    return country

# UPDATE/EDIT COUNTRY

def update(country):
    sql = "UPDATE countries SET (name, visited) = (%s, %s) WHERE id = %s"
    values = [country.name, country.id]
    run_sql(sql, values)

#DELETE ALL COUNTRIES

def delete_all():
    sql = "DELETE  FROM countries"
    run_sql(sql)

# DELETE SPECIFIC COUNTRY

def delete(id):
    sql = "DELETE  FROM countries WHERE id = %s"
    values = [id]
    run_sql(sql, values)
