/*https://platform.stratascratch.com/coding/9924-find-libraries-who-havent-provided-the-email-address-in-2016-but-their-notice-preference-definition-is-set-to-email?code_type=1*/
select distinct(home_library_code)
from library_usage
where circulation_active_year = 2016
    and provided_email_address = false
    and notice_preference_definition = 'email'