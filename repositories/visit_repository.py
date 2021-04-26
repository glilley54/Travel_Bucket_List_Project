#from db.run_sql import run_sql

#from models.country import Country
#from models.city import City

#import repositories.country_repository as country_repository
#import repositories.city_repository as city_repository

#def save(visit):
    #sql = "INSERT INTO visits ( user_id, country_id, city_id) VALUES ( %s, %s, %s ) RETURNING id"
    #values = [visit.user.id, visit.country.id, visit.city_id]
    #results = run_sql( sql, values )
    #visit.id = results[0]['id']
   # return visit


#def select_all():
    #visits = []

    #sql = "SELECT * FROM visits"
    #results = run_sql(sql)

    #for row in results:
        #user = user_repository.select(row['user_id'])
        #country = country_repository.select(row['country_id'])
        #city = city_repository.select(row['city_id'])
       # visit = Visit(user, country, city,])
        #visits.append(visit)
    #return visits


#def location(visit):
    #sql = "SELECT * FROM locations WHERE id = %s"
    #values = [visit.location.id]
    #results = run_sql(sql, values)[0]
    #location = Location(results['name'], results['category'], results['id'])
    #return location





#def delete_all():
    #sql = "DELETE FROM visits"
    #run_sql(sql)

#def delete(id):
    #sql = "DELETE FROM visits WHERE id = %s"
    #values = [id]
    #run_sql(sql, values)
