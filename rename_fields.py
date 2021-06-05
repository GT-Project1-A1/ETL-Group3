# Field Map Dictionaries

# Fields are pulled from commercial_df
commercial_renamer = { #Original Field : Desired Field
    "GEOGRAPHY_CODE" : "country_code",
    "HS_CODE" : "hs_code",
    "UNIT_DESC" : "unit_descr",
    "Direction" : "direction",
    "Measure" : "measure",
    "YEAR_ID" : "year_id",
    "TIMEPERIOD_ID" : "month_id",
    "AMOUNT" : "amount"
}

# Fields are pulled from country_df
country_renamer = {#Original Field : Desired Field
    "GEOGRAPHY_CODE" : "country_code",
    "GEOGRAPHY_DESC" : "country_name",
}

# Fields are pulled from agg_temp_df
temp_renamer = { #Original Field : Desired Field
    "Country" : "country_name",
    "YEAR_ID" : "year_id",
    "MONTH_ID" : "month_id",
    "AverageTemperature" : "avg_temperature"
}

# Fields are pulled from fish_type
fish_renamer = {
    "HS_CODE" : "hs_code",
    "COMMODITY_DESC" : "commodity_desc",
    "FISH_TYPE" : "fish_type"
}