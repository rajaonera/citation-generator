create table theme(
    id serial primary key,
    name varchar(255)
);

create table auteur(
    id serial primary key,
    nom varchar(255)
);

CREATE TABLE citation(
    id serial primary key,
    auteur_id int references auteur(id),
    theme_id int references theme(id),
    citation text
);