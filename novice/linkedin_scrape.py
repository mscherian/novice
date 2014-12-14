from linkedin import linkedin,exceptions

API_KEY = '75drk9wgoawyy1'
API_SECRET = 'bwYU7zc1f1loLUTF'
USER_TOKEN = 'be484f54-b0bf-45f1-977d-67ed78800474'
USER_SECRET = 'fb5f5551-1424-46ea-a05b-a951ee194c82'
RETURN_URL = ''
auth = linkedin.LinkedInDeveloperAuthentication(API_KEY, API_SECRET, \
                                USER_TOKEN, USER_SECRET, \
                                RETURN_URL, \
                                permissions=linkedin.PERMISSIONS.enums.values())
app = linkedin.LinkedInApplication(auth)

input_file=open('/home/matt/Desktop/Datadumps/LinkedIn/company_domains.csv','r')
output_file=open('/home/matt/Desktop/Datadumps/LinkedIn/LinkedIn_data.csv','w')
output_file_header='name,industry,type,employee_count,email_domains,web-url,logo-url\n'
output_file.write(output_file_header)

input_count=0
invalid_domain_count=0
no_domain_match_count=0
multiple_match_count=0
output_count=0
#app.get_profile()
for line in input_file:
    company_data=line.split(',')
    #email_domain='babelgum.com'
    email_domain = company_data[1].rstrip()
    #print email_domain
    try:
        matched_companies = app.get_company_by_email_domain(email_domain)
        #print matched_companies
        input_count+=1
        if matched_companies['_total'] != 1:
            print "didn't find unique company"
            multiple_match_count+=1
    except exceptions.LinkedInError:
        print "couldn't find matching company for " + email_domain
        no_domain_match_count+=1
        continue
    except ValueError:
        print "invalid email domain: " + email_domain
        invalid_domain_count+=1
        continue
    for company in matched_companies['values']:
        output_count+=1
        #print company['id'], company['name']
        company_details=app.get_companies(company_ids=[company['id']], \
                        selectors=['name','email-domains','company-type','website-url', \
                        'industries','employee-count-range','status','logo-url'])
        #print company_details
        industry_code = company_details['values'][0]['industries']['values'][0]['code']
        industry_name = company_details['values'][0]['industries']['values'][0]['name']
        #status = company_details['values'][0]['status']['name']
        name = company_details['values'][0]['name']
        domains = ''
        for domain in company_details['values'][0]['emailDomains']['values']:
            domains = domains + domain + ';'
        employee_count = company_details['values'][0]['employeeCountRange']['name']
        web_url = company_details['values'][0]['websiteUrl']
        logo_url = company_details['values'][0]['logoUrl']
        company_type = company_details['values'][0]['companyType']['name']
        #print name, industry_name, status, domains, employee_count, web_url, logo_url, company_type
        output_text = name + ',' + industry_name +  ',' + company_type + ',' + \
                      employee_count + ',' + domains + ',' + web_url + ',' + logo_url + '\n'
        output_file.write(output_text)
    
print input_count, invalid_domain_count, no_domain_match_count, mutiple_match_count, output_count
