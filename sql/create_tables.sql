/*
 create_tables.sql
*/

/*
This query creates a table 'users' which contains a serial 'user_pk' to use as unique if keys for users, with 'username' and 'password' being varchar(16). I chose 16 as the maximum length in part so that I could have a predictable text length to work with in UI, in addition to being a reasonable length so as to provide ample room for variation.  Additionally, the rubric states that it will not test for any longer.  I chose to have the ID be serial, largely because I do not require the ID to have any meaning besides serving as a primary key.  Using serial auto increments.  Additionally, this will allow an easier comparison with less overhead as it only compares an int, instead of a string as is the case with using the unique username.  Additionally, if ever the table needs to be iteratable, serial allows for an easy way to use a numerical index to send queries with.
 */

CREATE TABLE users (
	user_pk serial NOT NULL UNIQUE,
	username varchar(16) NOT NULL UNIQUE,
	password varchar(16) NOT NULL,
	role integer NOT NULL,
	active boolean NOT NULL
);

/*I do not think that I need roles as a separate table.  I only have two roles as of now, but others can be added at a later time. I am using int so it would allow for same use without overhead of a joined table. Logistics = 0; Facilities = 1; */

CREATE TABLE assets (
	asset_pk serial NOT NULL UNIQUE,
	asset_tag varchar(16) NOT NULL,
	description varchar(64)
);

CREATE TABLE facilities (
	facility_pk serial NOT NULL UNIQUE,
	common_name varchar(32),
	fcode varchar(6) 
);

/*Here, I am choosing to connect assets and facilities to an asset_at table.*/

CREATE TABLE asset_at (
	asset_fk integer REFERENCES assets(asset_pk),
	facility_fk integer REFERENCES facilities(facility_pk),
	acquired_dt timestamp,
	disposed boolean,
	disposed_dt timestamp
);

CREATE TABLE request ( 
	req_user_fk integer REFERENCES users(user_pk),
	asset_fk integer REFERENCES assets(asset_pk),
	src_fk integer REFERENCES facilities(facility_pk),
	dest_fk integer REFERENCES facilities(facility_pk),
	request_dt timestamp,
	app_user_fk integer REFERENCES users(user_pk),
	approved_dt timestamp
);

CREATE TABLE transit (
	src_fk integer REFERENCES facilities(facility_pk),
	load_dt timestamp,
	dest_fk integer REFERENCES facilities(facility_pk),
	unload_dt timestamp
);

