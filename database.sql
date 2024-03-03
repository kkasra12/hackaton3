create table transportation (
    id serial primary key,
    coeficient float not null,
    name varchar(255) not null
);
create table sector(
    id serial primary key,
    name varchar(255) not null
);
create table resources (
    id serial primary key,
    name varchar(255) not null,
    image varchar(255) not null,
    company varchar(255) not null,
    city varchar(255) not null,
    unit varchar(255) not null,
    price float not null,
    availablity int not null,
    -- need a trigger that checks if the availablity is greater than 0 and less than 2
    techical_compliance varchar(255) not null,
    carbon_footprint float not null,
    location_lat float not null,
    location_long float not null,
    blockchain_id varchar(255) not null,
    transportation_id serial references transportation (id) not null,
    approved boolean default false,
    created_at timestamp default now(),
    sector_id serial references sector (id) not null,
    detail varchar(255) not null
);
create table producers (
    id serial primary key,
    location_lat float not null,
    location_long float not null,
    email varchar(255) not null
);
create table contract (
    id serial primary key,
    resources_id serial references resources(id) not null,
    producer_id serial references producers(id) not null,
    quantity int not null,
    created_at timestamp default now(),
    blockchain_id varchar(255) not null,
    approved boolean default false
);
-- function for getting all sectors
drop function if exists get_sectors;
create or replace function get_sectors() returns table(id_ int, name_ varchar(255)) as $$ begin return query
select id,
    name
from sector;
end;
$$ language plpgsql;
-- function for getting all resuorces in a sector
drop function if exists get_resources_in_sector;
create or replace function get_resources_in_sector(sector_id_ int) returns table(
        id int,
        name varchar(255),
        image varchar(255),
        detail varchar(255),
        company varchar(255),
        city varchar(255),
        price float,
        availablity int,
        techical_compliance varchar(255),
        carbon_footprint float,
        location_lat float,
        location_long float,
        transportation_coeficient float,
        approved boolean
    ) as $$ begin return query
select r.id,
    r.name,
    r.image,
    r.detail,
    r.company,
    r.city,
    r.price,
    r.availablity,
    r.techical_compliance,
    r.carbon_footprint,
    r.location_lat,
    r.location_long,
    t.coeficient,
    r.approved
from resources r
    join transportation t on r.transportation_id = t.id
where r.sector_id = sector_id_;
end;
$$ language plpgsql;