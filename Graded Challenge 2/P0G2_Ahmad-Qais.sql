'''
=================================================
Graded Challenge 2

Nama  : Ahmad Qais Alfiansyah
Batch : RMT-026

Program ini ditujukan untuk membuat database dan menyimpan olahan data dari Pandas.
Sehingga kedepannya, user sudah dapat menggunakan Postgresql untuk menyimpan data Financials

Nama database: Finance (Refer to nama team/department)
Nama tabel: 1. Transactions
2. Segments
3. Countries
4. Discounts

User yang dibuat:
1. Manager (All Access)
2. Supervisor (All Access)
3. Staff (Limited to SELECT only)
=================================================
'''

-- CREATE DATABASE finance;

BEGIN;

CREATE TABLE segments (
	segment_id SERIAL PRIMARY KEY,
	segment VARCHAR(50) UNIQUE
);

COPY segments(segment_id, segment)
FROM '/tmp/segments.csv'
DELIMITER ','
CSV HEADER;

CREATE TABLE countries (
	country_id SERIAL PRIMARY KEY,
	country VARCHAR(50) UNIQUE
);

COPY countries(country_id, country)
FROM '/tmp/countries.csv'
DELIMITER ','
CSV HEADER;

CREATE TABLE products (
	product_id SERIAL PRIMARY KEY,
	product VARCHAR(50) UNIQUE
);

COPY products(product_id, product)
FROM '/tmp/products.csv'
DELIMITER ','
CSV HEADER;

CREATE TABLE discounts (
	discount_id SERIAL PRIMARY KEY,
	discount VARCHAR(50) UNIQUE
);

COPY discounts(discount_id, discount)
FROM '/tmp/discounts.csv'
DELIMITER ','
CSV HEADER;

CREATE TABLE transactions (
	transaction_id SERIAL PRIMARY KEY,
	date DATE NOT NULL,
	segment VARCHAR(50) REFERENCES segments(segment),
	country VARCHAR(50) REFERENCES countries(country),
	product VARCHAR(50) REFERENCES products(product),
	discount_band VARCHAR(50) REFERENCES discounts(discount),
	units_sold NUMERIC,
	sale_price  NUMERIC,
	gross_sales NUMERIC,
	discount NUMERIC,
	sales NUMERIC,
	cogs NUMERIC,
	profit NUMERIC,
	manufacturing_price NUMERIC
);

COPY transactions(transaction_id,date,segment,country,product,discount_band,units_sold,sale_price,gross_sales,discount,sales,cogs,profit,manufacturing_price)
FROM '/tmp/transactions.csv'
DELIMITER ','
CSV HEADER;

CREATE USER manager WITH PASSWORD 'ftdsht8';
CREATE USER supervisor WITH PASSWORD 'rmt-026';
CREATE USER staff WITH PASSWORD '1234';

GRANT SELECT ON ALL TABLES IN SCHEMA public TO staff;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO manager;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO supervisor;

SELECT segment, SUM(profit) AS total_profit_tanpa_diskon
FROM transactions
WHERE discount <> 0
GROUP BY segment;

SELECT country, AVG(sales) AS sales_average, MIN(sales) AS sales_min, MAX(sales) AS sales_max
FROM transactions
GROUP BY country;

COMMIT;

ROLLBACK;












