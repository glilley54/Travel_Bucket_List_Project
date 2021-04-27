from flask import Flask, render_template, request, redirect
from repositories import country_repository
from repositories import city_repository

from models.country import Country
from models.city import City

from flask import Blueprint

countries_blueprint = Blueprint("countries", __name__)


@countries_blueprint.route("/countries")
def countries ():
    countries= country_repository.select_all() 
    return render_template("countries/index.html", all_countries = countries)

# NEW
# GET '/countries/new'
@countries_blueprint.route("/countries/new", methods=['GET'])
def new_country():
    countries = country_repository.select_all()
    return render_template("/countries/new.html", all_countries = countries)



# CREATE
# POST '/countries
@countries_blueprint.route("/countries",  methods=['POST'])
def create_country ():
    country_name  = request.form['country']
    country = Country(country_name)
    country_repository.save(country)
    return redirect('/countries')