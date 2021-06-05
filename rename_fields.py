# Field Rename dictionaries.

commercial_renamer = { #Original Field : Desired Field
<<<<<<< Updated upstream
    "HS_CODE" : "",
    "COMMODITY_DESC" : "",
    "GEOGRAPHY_CODE" : "",
    "GEOGRAPHY_DESC" : "",
=======
    "HS_CODE" : "hs_code",
    "COMMODITY_DESC" : "commodity_desc",
    "GEOGRAPHY_CODE" : "country_code",
    "GEOGRAPHY_DESC" : "country_name",
>>>>>>> Stashed changes
    "ATTRIBUTE_DESC" : "",
    "UNIT_DESC" : "",
    "YEAR_ID" : "",
    "TIMEPERIOD_ID" : "",
    "AMOUNT" : "",
    "Direction" : "",
    "Measure" : "",
    "FISH_TYPE" : "",
}

country_renamer = {#Original Field : Desired Field
    "GEOGRAPHY_CODE" : "country_code",
    "GEOGRAPHY_DESC" : "country_name",


temp_renamer = { #Original Field : Desired Field
    "country" : "country_name",
    "YEAR_ID" : "year_id",
    "MONTH_ID" : "month_id",
    "AverageTemperature" : "avg_temperature"
}