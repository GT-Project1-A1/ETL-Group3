# Field Rename dictionaries.

# Fields are pulled from commercial_df
commercial_renamer = { #Original Field : Desired Field
    "HS_CODE" : "hs_code",
    "COMMODITY_DESC" : "commodity_desc",
    "GEOGRAPHY_CODE" : "country_code",
    "GEOGRAPHY_DESC" : "country_name",
    "ATTRIBUTE_DESC" : "",
    "UNIT_DESC" : "",
    "YEAR_ID" : "",
    "TIMEPERIOD_ID" : "",
    "AMOUNT" : "",
    "Direction" : "",
    "Measure" : "",
    "FISH_TYPE" : "",
}

# Fields are pulled from commercial_df 
country_renamer = {#Original Field : Desired Field
    "GEOGRAPHY_CODE" : "country_code",
    "GEOGRAPHY_DESC" : "country_name",

# Fields are pulled from agg_temp_df
temp_renamer = { #Original Field : Desired Field
    "country" : "country_name",
    "YEAR_ID" : "year_id",
    "MONTH_ID" : "month_id",
    "AverageTemperature" : "avg_temperature"
}