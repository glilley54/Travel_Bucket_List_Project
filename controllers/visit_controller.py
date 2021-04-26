from flask import Flask, render_template, request, redirect
from repositories import country_repository
from repositories import city_repository

from models.country import Country
from models.city import City

from flask import Blueprint

destinations_blueprint = Blueprint("visits", __name__)


@destinations_blueprint.route("/destinations")
def cities ():
    cities = city_repository.select_all() # NEW
    return render_template("destinations/index.html", all_cities = cities)

# NEW
# GET '/destinations/new'
@destinations_blueprint.route("/destinations/new", methods=['GET'])
def countries():
    countries = country_repository.select_all()
    return render_template("destinations/new.html", all_countries = countries)



# CREATE
# POST '/destinations'
@destinations_blueprint.route("/destinations",  methods=['POST'])
def create_city():
    city_name  = request.form['city']
    country = country_repository.select(request.form['country_id'])
    city = City(name, country , visited)
    city_repository.save(city)
    return redirect('/destinations')