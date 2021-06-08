-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/kJnQn1
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "country" (
    "country_code" int   NOT NULL,
    "country_name" varchar   NOT NULL,
    CONSTRAINT "pk_country" PRIMARY KEY (
        "country_code"
     ),
    CONSTRAINT "uc_country_country_name" UNIQUE (
        "country_name"
    )
);

CREATE TABLE "fish_type" (
    "commodity_id" int   NOT NULL,
    "hs_code" varchar   NOT NULL,
    "commodity_desc" varchar   NOT NULL,
    "fish_type" varchar   NOT NULL,
    CONSTRAINT "pk_fish_type" PRIMARY KEY (
        "commodity_id"
     )
);

CREATE TABLE "commercial" (
    "country_code" int   NOT NULL,
    "commodity_id" int   NOT NULL,
    "unit_descr" varchar   NOT NULL,
    "direction" varchar   NOT NULL,
    "measure" varchar   NOT NULL,
    "year_id" int   NOT NULL,
    "month_id" int   NOT NULL,
    "amount" float   NOT NULL,
    CONSTRAINT "pk_commercial" PRIMARY KEY (
        "country_code","commodity_id","unit_descr","direction","measure","year_id","month_id"
     )
);

CREATE TABLE "temp" (
    "country_name" varchar   NOT NULL,
    "year_id" int   NOT NULL,
    "month_id" int   NOT NULL,
    "avg_temperature" float   NOT NULL,
    CONSTRAINT "pk_temp" PRIMARY KEY (
        "country_name","year_id","month_id"
     )
);

ALTER TABLE "commercial" ADD CONSTRAINT "fk_commercial_country_code" FOREIGN KEY("country_code")
REFERENCES "country" ("country_code");

ALTER TABLE "commercial" ADD CONSTRAINT "fk_commercial_commodity_id" FOREIGN KEY("commodity_id")
REFERENCES "fish_type" ("commodity_id");

ALTER TABLE "temp" ADD CONSTRAINT "fk_temp_country_name" FOREIGN KEY("country_name")
REFERENCES "country" ("country_name");

