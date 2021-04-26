from flask import Flask, render_template, request, redirect
from repositories import country_repository
from repositories import city_repository

from models.country import Country
from models.city import City

from flask import Blueprint

visits_blueprint = Blueprint("visits", __name__)


@visits_blueprint.route("/visits")
def visits ():
    cities = city_repository.select_all() # NEW
    return render_template("visits/index.html", all_cities = cities)

# NEW
# GET '/visits/new'
@visits_blueprint.route("/visits/new", methods=['GET'])
def new_city():
    countries = country_repository.select_all()
    return render_template("/visits/new.html", all_countries = countries)



# CREATE
# POST '/visits'
@visits_blueprint.route("/visits",  methods=['POST'])
def create_visit():
    city_name  = request.form['city']
    country = country_repository.select(request.form['country_id'])
    city = City(city_name, country)
    city_repository.save(city)
    return redirect('/visits')