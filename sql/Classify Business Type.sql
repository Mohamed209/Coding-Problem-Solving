#https://platform.stratascratch.com/coding/9726-classify-business-type?code_type=1
SELECT distinct business_name,
    CASE
        WHEN business_name ilike any(array ['%school%']) THEN 'school'
        WHEN lower(business_name) like any(array ['%restaurant%']) THEN 'restaurant'
        WHEN lower(business_name) like any(array ['%cafe%', '%café%', '%coffee%']) THEN 'cafe'
        ELSE 'other'
    END AS business_type
FROM sf_restaurant_health_violations