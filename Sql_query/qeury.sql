-- What is the overall attrition rate?
select count(*)*100/(select count(*) from employees) as atrriction_rate
from employees
where WORKING = 'no';

-- Which departments have the highest attrition?
select DEPARTMENT,count(*)*100/(select count(*) from employees as e2 where e1.DEPARTMENT = e2.DEPARTMENT)
from employees as e1
where WORKING = 'no'
group by DEPARTMENT;

-- Which job roles are most likely to leave?
select JOB_ROLE,count(*)*100/(select count(*) from employees as e2 where e1.JOB_ROLE = e2.JOB_ROLE)
from employees as e1
where WORKING = 'no'
group by JOB_ROLE;

-- Are employees leaving early (0–2 years) or after long time?
with cte as
(select *,
case
when EXPERIENCE_YEARS <= 2 then '2 year'
else 'more that 2 year'
end as year
from employees)
select 
year ,COUNT(CASE WHEN working = 'no' THEN 1 END) * 100 / COUNT(*) AS attrition_percentage
from cte as c1
group by year;

-- Are low salary employees more likely to leave?
with cte as
(select *,
case
when SALARY <= 45000 then 'low'
else 'high'
end as salary_gro
from employees)
select 
salary_gro ,count(case when working = 'no' THEN 1 END) *100/count(*) attrition_percentage
from cte 
group by salary_gro;

-- Which age group has highest attrition?
select AGE_GROUP,count(*)*100/(select count(*) from employees as e2 where e1.AGE_GROUP = e2.AGE_GROUP)
from employees as e1
where WORKING = 'no'
group by AGE_GROUP;

-- Does gender affect attrition rate?
select GENDER,count(*)*100/(select count(*) from employees)
from employees 
where WORKING = 'no'
group by GENDER;

-- Can we predict attrition based on salary, performance, and experience?
with cte as 
(select *,
case 
when salary <= 35000 and PERFORMANCE_RATING >=4 and EXPERIENCE_YEARS >= 10 then 'high_chanses'
when salary <= 45000 and PERFORMANCE_RATING >=4 and EXPERIENCE_YEARS >= 7 then 'mediam_chanses'
when salary <= 55000 and PERFORMANCE_RATING >=4 and EXPERIENCE_YEARS >= 5 then 'low_chanses' 
else 'other' 
end as try
from employees)
select
try,
COUNT(*) AS total_people,
SUM(CASE WHEN WORKING = 'no' THEN 1 ELSE 0 END) AS left_people,
SUM(CASE WHEN WORKING = 'no' THEN 1 ELSE 0 END) * 100.0 / COUNT(*) AS attrition_percentage
from cte
group by try;

-- Which combination leads to highest attrition: Low salary + high performance?
with cte as 
(select *,
case 
when salary <= 35000 and PERFORMANCE_RATING >=4  then 'Low salary + high performance'
when salary <= 45000 and PERFORMANCE_RATING >=4  then 'mediam salary + high performance'
when salary <= 55000 and PERFORMANCE_RATING >=4  then 'good salary + high performance' 
else 'other' 
end as salary_group
from employees)
select
salary_group,
COUNT(*) AS total_people,
SUM(CASE WHEN WORKING = 'no' THEN 1 ELSE 0 END) AS left_people,
SUM(CASE WHEN WORKING = 'no' THEN 1 ELSE 0 END) * 100 / COUNT(*) AS attrition_percentage
from cte
group by salary_group
ORDER BY attrition_percentage DESC
LIMIT 1;













