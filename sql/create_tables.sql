/*
 create_tables.sql
*/

/*
This query creates a table 'users' which contains a serial 'user_pk' to use as unique if keys for users, with 'username' and 'password' being varchar(16). I chose 16 as the maximum length in part so that I could have a predictable text length to work with in UI, in addition to being a reasonable length so as to provide ample room for variation.  Additionally, the rubric states that it will not test for any longer.  I chose to have the ID be serial, largely because I do not require the ID to have any meaning besides serving as a primary key.  Using serial auto increments.  Additionally, this will allow an easier comparison with less overhead as it only compares an int, instead of a string as is the case with using the unique username.  Additionally, if ever the table needs to be iteratable, serial allows for an easy way to use a numerical index to send queries with.
 */

CREATE TABLE users (
	user_pk serial NOT NULL,
	username varchar(16) NOT NULL UNIQUE,
	password varchar(16) NOT NULL,
	role boolean NOT NULL,
	active boolean NOT NULL
);

/*I do not think that I need roles as a separate table.  I only have two roles as of now so I am using boolean, but if others were added at a later time, changing to an int would allow for same use without overhead of a joined table. Logistics = 0; Facilities = 1; */

CREATE TABLE assets (
	asset_pk serial NOT NULL,
	asset_tag varchar(16) NOT NULL,
	description varchar(64)
);

CREATE TABLE facilities (
	facililty_pk serial NOT NULL,
	common_name varchar(32) NOT NULL
	fcode varchar(6) NOT NULL
);

/*Here, I am choosing to connect assets and facilities to an asset_status table.  I hope to later utilize this one table to reflect transit too, however, may change if that is not optimal.*/

CREATE TABLE asset_status (
	asset_fk integer REFERENCES assets.asset_pk,
	facility_fk integer REFERENCES facilities.facility_pk,
	arrival_dt date,
	departure_dt date,
	disposed boolean NOT NULL
);
