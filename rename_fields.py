# Field Map Dictionaries
# {ORIGINAL_FIELD_NAME : desired_field_name}

# FIELDS PULLED FROM SUPER COMMERCIAL DATAFRAME
country_renamer = {
    "GEOGRAPHY_CODE" : "country_code",
    "GEOGRAPHY_DESC" : "country_name",
}
fish_renamer = {
    "COMMODITY_ID" : "commodity_id",
    "HS_CODE" : "hs_code",
    "COMMODITY_DESC" : "commodity_desc",
    "FISH_TYPE" : "fish_type"
}
commercial_renamer = {
    "GEOGRAPHY_CODE" : "country_code",
    "COMMODITY_ID" : "commodity_id",
    "UNIT_DESC" : "unit_descr",
    "DIRECTION" : "direction",
    "MEASURE" : "measure",
    "YEAR_ID" : "year_id",
    "TIMEPERIOD_ID" : "month_id",
    "AMOUNT" : "amount"
}


# FIELDS PULLED FROM AGGREGATE TEMPERATURE DATAFRAME
temp_renamer = {
    "Country" : "country_name",
    "YEAR_ID" : "year_id",
    "MONTH_ID" : "month_id",
    "AverageTemperature" : "avg_temperature"
}

