/*https://platform.stratascratch.com/coding/10078-find-matching-hosts-and-guests-in-a-way-that-they-are-both-of-the-same-gender-and-nationality?code_type=1*/
select distinct host_id,
    guest_id
from airbnb_hosts
    inner join airbnb_guests on airbnb_hosts.nationality = airbnb_guests.nationality
    and airbnb_hosts.gender = airbnb_guests.gender