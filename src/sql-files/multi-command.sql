SELECT 
	COUNT(DISTINCT(id)), 
	form_name, 
	form_version,
	CASE WHEN answers LIKE '%nps_value%-1%' THEN 'closed_dialog' ELSE 'response' END has_responses,
	MIN(created_at) first_submission, 
	max(created_at) most_recent,
	Datepart(month, created_at) mon,
	DATEPART(y, created_at) yr
    
FROM dashboard_production_pii.foorm_submissions 
WHERE 
	form_name LIKE '%nps%' 
	-- AND created_at >= '2022-05-09'
	-- AND has_responses = 'response'
GROUP BY 2,3,4,7,8 
ORDER BY 
	has_responses, 
	yr, 
	mon
LIMIT 1000;


SELECT
  school_year,
  course_name,
  count(distinct(student_user_id)) num_students,
  count(distinct(teacher_user_id)) num_teachers,
  count(distinct(school_id)) num_schools,
  sum(teacher_trained) num_teachers_trained

FROM rosetta_historic_students_wip 
WHERE course_name IN ('csp')
GROUP BY 
  course_name,
  school_year
ORDER BY
  school_year ASC,
  course_name
LIMIT 100;
