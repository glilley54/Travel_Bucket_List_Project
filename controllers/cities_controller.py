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


    #show

@cities_blueprint.route("/cities/<id>", methods=['GET'])
def show_city(id):
    city = city_repository.select(id)
    return render_template('cities/show.html', city = city)

    #EDIT get 

@cities_blueprint.route("/cities/<id>/edit", methods=['GET'])
def edit_city(id):
    city = city_repository.select(id)
    country = country_repository.select_all()
    return render_template('cities/edit.html', city = city, all_countries = country)




    #UPDATE put


@cities_blueprint.route("/cities/<id>", methods=['POST'])
def update_city(id):
    city_name  = request.form['city']
    country = country_repository.select(request.form['country_id'])
    city = City(city_name, country,request.form['visited'],id)
    city_repository.update(city)
    return redirect('/cities')


    #DELETE

@cities_blueprint.route("/cities/<id>/delete", methods=['POST'])
def delete_city(id):
    city_repository.delete(id)
    return redirect('/cities')

   
