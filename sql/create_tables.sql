create table assets ( asset_pk serial, product_fk int, asset_tag varchar(10), description varchar(50), alt_description(50));

create table products ( product_pk serial, vendor varchar(10), description varchar(50), alt_description(50));

create table vehicles ( vehicle_pk serial, asset_fk int);

create table facilities ( facility_pk serial, fcode varchar(6), common_name varchar(25), location varchar(100));

create table asset_at ( asset_fk int, facility_fk int, arrive_dt timestamp, depart_dt timestamp);


