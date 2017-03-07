INSERT INTO users (user_pk, username, password, role, active,) VALUES (DEFAULT, 'Log1', 'log1', '0', 'TRUE',);
INSERT INTO users (user_pk, username, password, role, active,) VALUES (DEFAULT, 'Fac1', 'fac1', '1', 'TRUE',);
INSERT INTO users (user_pk, username, password, role, active,) VALUES (DEFAULT, 'Log2', 'log2', '0', 'TRUE',);
INSERT INTO users (user_pk, username, password, role, active,) VALUES (DEFAULT, 'Sus1', 'sus1', '0', 'FALSE',);
INSERT INTO users (user_pk, username, password, role, active,) VALUES (DEFAULT, 'Act1', 'act1', '0', 'TRUE',);
INSERT INTO users (user_pk, username, password, role, active,) VALUES (DEFAULT, 'Fac2', 'fac2', '1', 'TRUE',);

INSERT INTO facilities (facility_pk, common_name, fcode,) VALUES (DEFAULT, 'Headquarters', 'HQ',);
INSERT INTO facilities (facility_pk, common_name, fcode,) VALUES (DEFAULT, 'Washington DC', 'DC',);
INSERT INTO facilities (facility_pk, common_name, fcode,) VALUES (DEFAULT, 'Moon Base 5', 'MB005',);
INSERT INTO facilities (facility_pk, common_name, fcode,) VALUES (DEFAULT, 'Eugene', 'UG',);
INSERT INTO facilities (facility_pk, common_name, fcode,) VALUES (DEFAULT, 'WF1', 'White Fox 1',);
INSERT INTO facilities (facility_pk, common_name, fcode,) VALUES (DEFAULT, 'National City', 'NC',);
INSERT INTO facilities (facility_pk, common_name, fcode,) VALUES (DEFAULT, 'OSNAP Site 34', 'SITE34',);

INSERT INTO assets (asset_pk, asset_tag, description,) VALUES (DEFAULT, 'MIB NC-5000', 'Noisy Cricket',);
INSERT INTO assets (asset_pk, asset_tag, description,) VALUES (DEFAULT, 'LOST ST-WT', 'LOST Sticker - White',);
INSERT INTO assets (asset_pk, asset_tag, description,) VALUES (DEFAULT, 'LOST ST-BK', 'LOST Sticker - Black',);
INSERT INTO assets (asset_pk, asset_tag, description,) VALUES (DEFAULT, 'LOST ST-GN', 'LOST Sticker - Green',);
INSERT INTO assets (asset_pk, asset_tag, description,) VALUES (DEFAULT, 'MIB NX-5500', 'Noisy Cricket NX',);

/*INSERT INTO asset_at (asset_fk, facility_fk, acquired_dt, disposed,) VALUES (SQL, SQL, 'datetime.datetime.utcnow().isoformat()', '0',);*/
INSERT INTO asset_at (asset_fk, facility_fk, acquired_dt, disposed,) VALUES (1, 1, 'datetime.datetime.utcnow().isoformat()', '0',);
INSERT INTO asset_at (asset_fk, facility_fk, acquired_dt, disposed,) VALUES (2, 3, 'datetime.datetime.utcnow().isoformat()', '0',);
INSERT INTO asset_at (asset_fk, facility_fk, acquired_dt, disposed,) VALUES (5, 3, 'datetime.datetime.utcnow().isoformat()', '0',);
INSERT INTO asset_at (asset_fk, facility_fk, acquired_dt, disposed,) VALUES (4, 1, 'datetime.datetime.utcnow().isoformat()', '1',);

/*INSERT INTO request (requester_fk, asset_fk, facility_src_fk, facility_dest_fk, request_dt, approver_fk, approval_dt) VALUES (SQL, SQL, SQL, SQL, 'datetime.datetime.utcnow().isoformat()', SQL, 'datetime.datetime.utcnow().isoformat()',);*/
INSERT INTO request (requester_fk, asset_fk, facility_src_fk, facility_dest_fk, request_dt, approver_fk, approval_dt) VALUES ('1', '1', '2', '4', 'datetime.datetime.utcnow().isoformat()', '2', 'datetime.datetime.utcnow().isoformat()',);
INSERT INTO request (requester_fk, asset_fk, facility_src_fk, facility_dest_fk, request_dt, approver_fk, approval_dt) VALUES ('1', '1', '2', '3', 'datetime.datetime.utcnow().isoformat()', 2, 'datetime.datetime.utcnow().isoformat()',);

/*INSERT INTO transit(facility_src_fk, load_dt, facility_dest_fk, unload_dt,) VALUES (SQL, 'datetime.datetime.utcnow().isoformat()', SQL, 'datetime.datetime.utcnow().isoformat()',);*/
INSERT INTO transit(facility_src_fk, load_dt, facility_dest_fk, unload_dt,) VALUES ('2', 'datetime.datetime.utcnow().isoformat()', '3', 'datetime.datetime.utcnow().isoformat()',);


