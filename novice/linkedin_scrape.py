from linkedin import linkedin
import json

API_KEY = '75tw50028mrz4c'
API_SECRET = 'wVV52Bu6D3SUL6RL'
USER_TOKEN = 'bfedc055-07c4-4082-b43a-b6124a9cae1f'
USER_SECRET = '5780ec36-e5c8-4b16-87d4-20a69ad5f5bb'
RETURN_URL = ''

auth = linkedin.LinkedInDeveloperAuthentication(API_KEY, API_SECRET, 
                                USER_TOKEN, USER_SECRET, 
                                RETURN_URL, 
                                permissions=linkedin.PERMISSIONS.enums.values())

app = linkedin.LinkedInApplication(auth)

#app.get_profile()
#try:
email_domain = 'babelgum.com'
matched_companies = app.get_company_by_email_domain(email_domain)
print matched_companies
print matched_companies['_total']
print matched_companies['values']
if matched_companies['_total'] != 1:
    print "didn't find unique company"
for company in matched_companies['values']:
    print company['id'], company['name']
    company_details=app.get_companies(company_ids=[company['id']],selectors=['name','email-domains','company-type','ticker','website-url','industries','employee-count-range','status','logo-url','locations'])
    print company_details
    #for 
    
#except:
#    print "couldn't find company with domain: " + email_domain
