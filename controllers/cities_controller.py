from flask import Flask, render_template, request, redirect
from repositories import country_repository
from repositories import city_repository

from models.country import Country
from models.city import City

from flask import Blueprint

cities_blueprint = Blueprint("cities", __name__)


@cities_blueprint.route("/cities")
def cities ():
    cities = city_repository.select_all() # NEW
    return render_template("cities/index.html", all_cities = cities)

# NEW
# GET '/cities/new'
@cities_blueprint.route("/cities/new", methods=['GET'])
def new_city():
    countries = country_repository.select_all()
    return render_template("/cities/new.html", all_countries = countries)



# CREATE
# POST '/cities
@cities_blueprint.route("/cities",  methods=['POST'])
def create_city():
    city_name  = request.form['city']
    country = country_repository.select(request.form['country_id'])
    city = City(city_name, country)
    city_repository.save(city)
    return redirect('/cities')