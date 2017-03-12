INSERT INTO users (user_pk, username, password, role, active) VALUES (DEFAULT, 'Log1', 'log1', '0', 'TRUE');
INSERT INTO users (user_pk, username, password, role, active) VALUES (DEFAULT, 'Fac1', 'fac1', '1', 'TRUE');
INSERT INTO users (user_pk, username, password, role, active) VALUES (DEFAULT, 'Log2', 'log2', '0', 'TRUE');
INSERT INTO users (user_pk, username, password, role, active) VALUES (DEFAULT, 'Sus1', 'sus1', '0', 'FALSE');
INSERT INTO users (user_pk, username, password, role, active) VALUES (DEFAULT, 'Act1', 'act1', '0', 'TRUE');
INSERT INTO users (user_pk, username, password, role, active) VALUES (DEFAULT, 'Fac2', 'fac2', '1', 'TRUE');

INSERT INTO facilities (facility_pk, common_name, fcode) VALUES (DEFAULT, 'Headquarters', 'HQ');
INSERT INTO facilities (facility_pk, common_name, fcode) VALUES (DEFAULT, 'Washington DC', 'DC');
INSERT INTO facilities (facility_pk, common_name, fcode) VALUES (DEFAULT, 'Moon Base 5', 'MB005');
INSERT INTO facilities (facility_pk, common_name, fcode) VALUES (DEFAULT, 'Eugene', 'UG');
INSERT INTO facilities (facility_pk, common_name, fcode) VALUES (DEFAULT, 'White Fox 1', 'WF1');
INSERT INTO facilities (facility_pk, common_name, fcode) VALUES (DEFAULT, 'National City', 'NC');
INSERT INTO facilities (facility_pk, common_name, fcode) VALUES (DEFAULT, 'OSNAP Site 34', 'SITE34');

INSERT INTO assets (asset_pk, asset_tag, description) VALUES (DEFAULT, 'MIB NC-5000', 'Noisy Cricket');
INSERT INTO assets (asset_pk, asset_tag, description) VALUES (DEFAULT, 'LOST ST-WT', 'LOST Sticker - White');
INSERT INTO assets (asset_pk, asset_tag, description) VALUES (DEFAULT, 'LOST ST-BK', 'LOST Sticker - Black');
INSERT INTO assets (asset_pk, asset_tag, description) VALUES (DEFAULT, 'LOST ST-GN', 'LOST Sticker - Green');
INSERT INTO assets (asset_pk, asset_tag, description) VALUES (DEFAULT, 'MIB NX-5500', 'Noisy Cricket NX');

/*INSERT INTO asset_at (asset_fk, facility_fk, acquired_dt, disposed,) VALUES (SQL, SQL, 'datetime.datetime.utcnow().isoformat()', '0',);*/
INSERT INTO asset_at (asset_fk, facility_fk, acquired_dt, disposed, disposed_dt) VALUES (1, 1, '2017-03-06 00:00:00', '0');
INSERT INTO asset_at (asset_fk, facility_fk, acquired_dt, disposed, disposed_dt) VALUES (2, 3, '2017-03-06 00:00:00', '0');
INSERT INTO asset_at (asset_fk, facility_fk, acquired_dt, disposed, disposed_dt) VALUES (5, 3, '2017-03-06 00:00:00', '0');
INSERT INTO asset_at (asset_fk, facility_fk, acquired_dt, disposed, disposed_dt) VALUES (4, 1, '2017-03-06 00:00:00', '1', 2017-13-16 12:34:56);

/*INSERT INTO request (req_user_fk, asset_fk, src_fk, fk, request_dt, app_user_fk, approved_dt) VALUES (SQL, SQL, SQL, SQL, 'datetime.datetime.utcnow().isoformat()', SQL, 'datetime.datetime.utcnow().isoformat()',);*/
INSERT INTO request (req_user_fk, asset_fk, src_fk, dest_fk, request_dt, app_user_fk, approved_dt) VALUES ('1', '1', '2', '4', '2017-03-06 00:00:00', '2', '2017-03-06 00:00:00');
INSERT INTO request (req_user_fk, asset_fk, src_fk, dest_fk, request_dt, app_user_fk, approved_dt) VALUES ('1', '1', '2', '3', '2017-03-06 00:00:00', 2, '2017-03-06 00:00:00');

/*INSERT INTO transit(src_fk, load_dt, dest_fk, unload_dt,) VALUES (SQL, 'datetime.datetime.utcnow().isoformat()', SQL, 'datetime.datetime.utcnow().isoformat()',);*/
INSERT INTO transit(src_fk, load_dt, dest_fk, unload_dt) VALUES ('2', '2017-03-06 00:00:00', '3', '2017-03-06 00:00:00');


