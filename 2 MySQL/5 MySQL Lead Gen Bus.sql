Select * From billing;
# 1. What query would you run to get the total revenue for March of 2012?
Select DATE_FORMAT(charged_datetime, '%M') As 'month', sum(amount) As 'revenue' From billing Where year(charged_datetime)= 2012 And month(charged_datetime) = 3 Group By year(charged_datetime);
# 2. What query would you run to get total revenue collected from the client with an id of 2?
Select client_id, sum(amount) As 'total_revenue' From billing Where client_id = 2 Group By client_id ;
# 3. What query would you run to get all the sites that client=10 owns?
Select domain_name As 'website', client_id From sites Where client_id = 10 Group By domain_name;
# 4. What query would you run to get total # of sites created per month per year for the client with an id of 1? What about for client=20?
Select client_id, count(site_id) As 'number_of_websites', date_format(created_datetime, '%M') As 'monthcreated', year(created_datetime) As 'yearreated' from sites Where client_id =1 Group By site_id;
Select client_id, count(site_id) As 'number_of_websites', date_format(created_datetime, '%M') As 'monthcreated', year(created_datetime) As 'yearreated' from sites Where client_id =20 Group By site_id;
# 5. What query would you run to get the total # of leads generated for each of the sites between January 1, 2011 to February 15, 2011?
Select domain_name As 'website', count(leads_id) As 'number_of_leads', date_format(registered_datetime, '%M %d, %Y') As 'date_generated' From leads 
Left Join sites On leads.site_id = sites.site_id 
Where registered_datetime >= '2011-01-01' And registered_datetime <= '2011-02-15' 
Group By leads.leads_id;
# 6. What query would you run to get a list of client names and the total # of leads we've generated for each of our clients between January 1, 2011 to December 31, 2011?
Select * from clients;
Select * from leads;
Select *  from clients Left Join leads On leads.leads_id = clients.client_id;
Select concat(clients.first_name," ", clients.last_name) As 'client_name',  count(sites.client_id) As 'number_of_leads' 
From clients 
Left Join sites On sites.client_id = clients.client_id  
Left Join leads On sites.site_id = leads.site_id  
Where registered_datetime >= '2011-01-01' And registered_datetime <= '2011-12-31'
Group By sites.client_id;
# 7. What query would you run to get a list of client names and the total # of leads we've generated for each client each month between months 1 - 6 of Year 2011?
Select concat(clients.first_name," ", clients.last_name) As 'client_name'
,count(sites.client_id) As 'number_of_leads', date_format(leads.registered_datetime, '%M') As 'month_generated' 
From clients 
Left Join sites On sites.client_id = clients.client_id  
Left Join leads On sites.site_id = leads.site_id  
Where month(registered_datetime) <= 6
And year(registered_datetime) = 2011
Group By leads.site_id
Order By date_format(registered_datetime, '%m');
# 8. What query would you run to get a list of client names and the total # of leads we've generated for each of our clients' sites between January 1, 2011 to December 31, 2011? Order this query by client id.  Come up with a second query that shows all the clients, the site name(s), and the total number of leads generated from each site for all time.
Select concat(clients.first_name," ", clients.last_name) As 'client_name'
, sites.domain_name As 'website'
, count(leads.leads_id) As 'number_of_leads'
, date_format(leads.registered_datetime, '%M %d, %Y') As 'date_generated'
From clients
Left Join sites On sites.client_id = clients.client_id  
Left Join leads On sites.site_id = leads.site_id  
Where registered_datetime >= '2011-01-01' And registered_datetime <= '2011-12-31'
Group By leads.site_id
Order By clients.client_id, registered_datetime;

Select concat(clients.first_name," ", clients.last_name) As 'client_name'
, sites.domain_name As 'website'
, count(leads.leads_id) As 'number_of_leads'
From clients
Left Join sites On sites.client_id = clients.client_id  
Left Join leads On sites.site_id = leads.site_id  
Group By leads.site_id
Order By clients.client_id;

# 9. Write a single query that retrieves total revenue collected from each client for each month of the year. Order it by client id.
Select concat(clients.first_name," ", clients.last_name) As 'client_name'
, sum(billing.amount) As 'total_revenue'
, date_format(billing.charged_datetime, '%M') As 'month_charge'
, date_format(billing.charged_datetime, '%Y') As 'year_charge'
From clients
Left Join billing On clients.client_id =billing.client_id  
Where billing.amount > 0
Group By concat(clients.last_name, clients.first_name, date_format(billing.charged_datetime,'%M-%Y'))
Order By concat(clients.last_name, clients.first_name), billing.charged_datetime;

# 10. Write a single query that retrieves all the sites that each client owns. Group the results so that each row shows a new client. It will become clearer when you add a new field called 'sites' that has all the sites that the client owns. (HINT: use GROUP_CONCAT)
Select concat(clients.first_name," ", clients.last_name) As 'client_name'
, group_concat(Distinct sites.domain_name separator ' / ') As 'sites'
From clients
Left Join sites On clients.client_Id = sites.client_Id
Group By clients.client_id;