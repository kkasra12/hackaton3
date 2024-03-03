insert into sector (name)
values ('electrnics'),
    ('food and beverages'),
    ('textile'),
    ('chemicals'),
    ('furniture');
insert into transportation (coeficient, name)
values (66, 'Truck'),
    (24, 'Train'),
    (15.5, 'short range Ship'),
    (7.5, 'long range ship');
truncate table resources cascade;
insert into resources (
        name,
        image,
        company,
        city,
        unit,
        price,
        availablity,
        techical_compliance,
        carbon_footprint,
        location_lat,
        location_long,
        blockchain_id,
        transportation_id,
        sector_id,
        detail
    )
values (
        'straws',
        'straws.jpeg',
        'EcoStraws Luxembourg',
        'Luxembourg',
        'kg',
        56.0,
        1,
        '{recyclable: True, biodegradable: False}',
        16.0,
        0.0,
        0.0,
        '',
        1,
        1,
        'Eco-friendly and stylish straws for your beverages.'
    ),
    (
        'lunch boxes',
        'lunchbox.jpg',
        'EcoBox Luxembourg',
        'Luxembourg',
        'kg',
        70.0,
        1,
        '{recyclable: True, biodegradable: False}',
        20.0,
        0.0,
        0.0,
        '',
        1,
        1,
        'Eco-friendly and microwave boxes for your food.'
    ),
    (
        'glasses',
        'cups.jpg',
        'EcoCups Luxembourg',
        'Luxembourg',
        'kg',
        55.0,
        1,
        '{recyclable: True, biodegradable: False}',
        27.0,
        0.0,
        0.0,
        '',
        1,
        1,
        'Eco-friendly and pollution free cups.'
    ),
    (
        'plates',
        'cardboard plates.jpg',
        'EcoPlates Luxembourg',
        'Luxembourg',
        'kg',
        65.0,
        1,
        '{recyclable: True, biodegradable: False}',
        36.0,
        0.0,
        0.0,
        '',
        1,
        1,
        'Eco-friendly and pollution free plates.'
    );
insert into producers (location_lat, location_long, email)
values (0.0, 0.0, 'test');