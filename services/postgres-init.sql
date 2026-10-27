CREATE TABLE orders (order_id text PRIMARY KEY, amount bigint NOT NULL CHECK (amount >= 0));
INSERT INTO orders VALUES ('O001', 100000), ('O002', 200000), ('O003', 50000);
