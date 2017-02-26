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
	role_fk integer NOT NULL REFERENCES roles.role_pk
);

CREATE TABLE roles(
	role_pk serial NOT NULL,
	name varchar(16) NOT NULL
);

CREATE TABLE assets(
	asset_pk serial NOT NULL,
	asset_tag varchar(16) NOT NULL,
	description varchar(64)
);

CREATE TABLE facilities)
	facililty_pk serial NOT NULL,
	common_name varchar(32) NOT NULL
	fcode varchar(6) NOT NULL
);


