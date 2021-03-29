BEGIN;
--
-- Create model Topping
--
CREATE TABLE "topping" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(100) NOT NULL);
--
-- Create model Pizza
--
CREATE TABLE "pizza" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(100) NOT NULL);
CREATE TABLE "pizza_toppings" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "pizza_id" integer NOT NULL REFERENCES "pizza" ("id") DEFERRABLE INITIALLY DEFERRED, "topping_id" integer NOT NULL REFERENCES "topping" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE UNIQUE INDEX "pizza_toppings_pizza_id_topping_id_8f3bc27a_uniq" ON "pizza_toppings" ("pizza_id", "topping_id");
CREATE INDEX "pizza_toppings_pizza_id_1d874c42" ON "pizza_toppings" ("pizza_id");
CREATE INDEX "pizza_toppings_topping_id_415abd80" ON "pizza_toppings" ("topping_id");
COMMIT;
