BEGIN;

--
-- Create model MySpecialUser
--
CREATE TABLE "my_special_user" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "supervisor_id" integer NOT NULL UNIQUE REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED,
    "user_id" integer NOT NULL UNIQUE REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED
);

COMMIT;