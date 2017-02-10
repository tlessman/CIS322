INSERT INTO facilities VALUES ( DEFAULT, 'MB005', 'Moon Base 5', 'CLASSIFIED');
INSERT INTO facilities VALUES ( DEFAULT, 'HQ', 'Headquarters', 'Eugene, OR, USA');
INSERT INTO products VALUES ( DEFAULT, 'Staples', 'notepad', 'legal yellow');
INSERT INTO products VALUES ( DEFAULT, 'OfficeMax', 'quad ruled notepad', '100 pages');
INSERT INTO assets VALUES ( DEFAULT, 1, 'STNP01', 'CLASSIFIED', 'DO NOT REMOVE');
INSERT INTO assets VALUES ( DEFAULT, 2, 'OMNPQ1', 'Engineering Paper', '59/100');
INSERT INTO asset_at VALUES ( 1, 2, '04/20/86 19:55:32');
INSERT INTO convoys VALUES ( DEFAULT, 'MB005-c34f52', 1, 2, '10/25/85 03:22:43', '04/20/86 19:54:58');
INSERT INTO asset_on VALUES ( 1, 1, '10/25/85 03:22:43', '04/20/86 19:54:58');
