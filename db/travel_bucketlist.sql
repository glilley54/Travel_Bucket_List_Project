DROP TABLE IF EXISTS visits;
DROP TABLE IF EXISTS cities;
DROP TABLE IF EXISTS countries;



CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
   
);

CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    visited BOOLEAN,
    country_id INT REFERENCES countries(id) ON DELETE CASCADE

);

CREATE TABLE visits (
    id SERIAL PRIMARY KEY,
    date VARCHAR(255)
    city_id INT REFERENCES cities(id) ON DELETE CASCADE,
    visited BOOLEAN,
    

);


