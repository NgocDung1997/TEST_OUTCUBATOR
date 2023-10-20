-- 1 :  Top 10 from_station,to_station has the most bike rentals 
WITH count_bike_rentals AS (
	select from_station_id,to_station_id , count(bikeid) total_bike_rentals
	from test_outcubator.trips
	group by from_station_id,to_station_id
    ORDER BY count(bikeid) desc
    limit 10
)
select from_station_name,to_station_name  ,total_bike_rentals
from test_outcubator.trips trips
INNER JOIN count_bike_rentals cbr
ON trips.from_station_id = cbr.from_station_id 
AND trips.to_station_id = cbr.to_station_id
;

-- 2. How many new bike rentals on 2019-08-16 and the running totals until that day of each from_station
WITH new_bike_rentals AS (
	select from_station_id , count(bikeid) total_new_bike
	from test_outcubator.trips
	WHERE STR_TO_DATE(start_time, '%Y-%m-%d') = STR_TO_DATE('2019-08-16','%Y-%m-%d') 
    group by from_station_id
),
	total_bike_rentals AS (
	select from_station_id , count(bikeid) total_bike
	from test_outcubator.trips
    group by from_station_id
),
   from_station_dim as (
    select from_station_id,from_station_name 
    from test_outcubator.station
   )
select dim.from_station_name,COALESCE(total_new_bike,0) , total_bike from from_station_dim dim
LEFT JOIN total_bike_rentals tbr
ON dim.from_station_id = tbr.from_station_id
LEFT JOIN new_bike_rentals nbr
ON dim.from_station_id = nbr.from_station_id;

