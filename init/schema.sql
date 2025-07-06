CREATE DATABASE IF NOT EXISTS pokedex;

CREATE TABLE IF NOT EXISTS `pokedex`.`pokemons` (
    pokemon_id BIGINT NOT NULL,
    pkn_name VARCHAR(255) NOT NULL UNIQUE,
    type_1 VARCHAR(255) NOT NULL,
    type_2 VARCHAR(255),
    generation BIGINT NOT NULL,
    is_legendary BIGINT NOT NULL,
    PRIMARY KEY (pokemon_id)
);
