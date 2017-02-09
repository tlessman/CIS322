
/*Asset Tables*/

create table vehicles ( 
	vehicle_pk serial, 
	asset_fk int
);
create table facilities ( 
	facility_pk serial, 
	fcode varchar(8), 
	common_name varchar(32), 
	location varchar(100)
);
create table asset_at (
       	asset_fk int, 
	facility_fk int, 
	arrive_dt timestamp, 
	depart_dt timestamp
);
create table convoys (
       	convoy_pk serial, 
	request varchar(16), 
	source_fk int, 
	dest_fk int, 
	depart_dt timestamp, 
	arrive_dt timestamp
);
create table used_by (
       	vehicle_fk int, 
	convoy_fk int
);
create table asset_on (
       	asset_fk int, 
	convoy_fk int, 
	load_dt timestamp, 
	unload_dt timestamp
);
create table products ( 
	product_pk serial primary key,
       	vendor varchar(16), 
	description varchar(64), 
	alt_description varchar(64));

create table assets ( 
	asset_pk serial primary key,  
	product_fk integer REFERENCES products (product_pk),
	asset_tag varchar(16), 
	description varchar(64), 
	alt_description varchar(64)
);


/*User Tables*/
create table users ( 
	user_pk serial, 
	username varchar(16), 
	active boolean
);
create table roles (
       	role_pk serial, 
	title varchar(16)
);
create table user_is (
       	user_fk int, 
	role_fk int
);
create table user_supports (
       	user_ft int, 
	facility_fk int
);


/*Security Tables*/
create table levels (
	level_pk serial, 
	abbrv varchar(8), 
	comment varchar(32)
);
create table compartments (
	compartment_pk serial, 
	abbrv varchar(8), 
	comment varchar(32)
);
create table security_tags (
	tag_pk serial, 
	level_fk int, 
	compartment_fk int, 
	user_fk int, 
	product_fk int, 
	asset_fk int
);

