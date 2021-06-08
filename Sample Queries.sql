/* List out all countries*/
select * from country;

/* List all commodities*/
select * from fish_type;

/* List all rows in commercial*/
select * from commercial

/* List all rows in temp*/
select * from temp

/* Find out how much fish does US import from Greenland each year by weight*/
Select year_id, c.country_name, ft.fish_type, sum(amount) as TotalImportWeight from commercial as com
join country as c
on com.country_code = c.country_code
join fish_type as ft
on com.commodity_id = ft.commodity_id
where c.country_name = 'Greenland' and direction = 'US Import' and measure = 'QTY'
group by year_id, c.country_name, ft.fish_type
order by year_id

/* Find out how much Salmon does US import from Canada in July 1992 by value.*/
Select year_id, month_id, c.country_name, ft.fish_type, sum(amount) as TotalImportValue from commercial as com
join country as c
on com.country_code = c.country_code
join fish_type as ft
on com.commodity_id = ft.commodity_id
where direction = 'US Import' and measure = 'VLU' and c.country_name = 'Canada' and year_id = '1992' and month_id ='7' and fish_type = 'Salmon'
group by year_id,month_id, c.country_name, ft.fish_type

/* Sort total US fish export by dollar value by country for year 2000*/
Select c.country_name, sum(amount) as TotalImportValue from commercial as com
join country as c
on com.country_code = c.country_code
where direction = 'US Export' and measure = 'VLU' and year_id = '2000' and c.country_code != 1
group by c.country_name
order by TotalImportValue desc

/* Sort total US fish export by dollar value by country for year 2000 and the countries average tempature in 2000*/
Select c.country_name, sum(amount) as TotalImportValue, country_temp.avg_temp from commercial as com
join country as c
on com.country_code = c.country_code
left join 
(select country_name, year_id, avg(avg_temperature) as avg_temp
 from temp 
 where year_id = 2000
 group by country_name, year_id
) as country_temp
on country_temp.country_name = c.country_name and com.year_id = country_temp.year_id
where direction = 'US Export' and measure = 'VLU' and com.year_id = '2000' and c.country_code != 1
group by c.country_name, country_temp.avg_temp
order by TotalImportValue desc

/* Join temp and commerical table*/
Select * from commercial as com
join country as c
on com. country_code = c.country_code
left join temp as t
on c.country_name = t.country_name and com.year_id = t.year_id and com.month_id = t.month_id
where avg_temperature is not null
