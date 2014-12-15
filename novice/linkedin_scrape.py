from linkedin import linkedin,exceptions
import io

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
log_file=open('/home/matt/Desktop/Datadumps/LinkedIn/LinkedIn_api__calls_log.txt','w')
output_file_header='name,industry,type,employee_count,email_domains,web-url,logo-url\n'
output_file.write(output_file_header)

input_count=0
invalid_domain_count=0
no_domain_match_count=0
multiple_match_count=0
output_count=0
#app.get_profile()
for line in input_file:
    company_data=line.decode('utf-8').split(',')
    #email_domain='babelgum.com'
    email_domain = company_data[1].rstrip()
    #print email_domain
    try:
        matched_companies = app.get_company_by_email_domain(email_domain)
        #print matched_companies
        input_count+=1
        if matched_companies['_total'] != 1:
            log_string = "didn't find unique company for " + email_domain + '\n'
            log_file.write(log_string)
            print log_string
            multiple_match_count+=1
    except exceptions.LinkedInError:
        log_string = "couldn't find matching company for " + email_domain + '\n'
        log_file.write(log_string)
        print log_string
        no_domain_match_count+=1
        continue
    except ValueError:
        log_string = "invalid email domain: " + email_domain + '\n'
        log_file.write(log_string)
        print log_string
        invalid_domain_count+=1
        continue
    for company in matched_companies['values']:
        #print company['id'], company['name']
        try:
            company_details=app.get_companies(company_ids=[company['id']], \
                        selectors=['name','email-domains','company-type','website-url', \
                        'industries','employee-count-range','status','logo-url'])
            #print company_details
            output_count+=1
        except exceptions.LinkedInError:
            log_string = "couldn't get details for company\n"
            log_file.write(log_string)
            print log_string
            continue
        try:
            industry_name = company_details['values'][0]['industries']['values'][0]['name']
            industry_name = industry_name.decode('utf-8')
        except:
            industry_name = 'N/A'
        try:
            status = company_details['values'][0]['status']['name']
            status = status.decode('utf-8')
        except:
            status = 'N/A'
        try:
            name = company_details['values'][0]['name']
            name = name.decode('utf-8')
        except:
            name = 'N/A'
        try:
            domains = ''
            for domain in company_details['values'][0]['emailDomains']['values']:
                domains = domains + domain.decode('utf-8') + ';'
        except:
            domains = ''
        try:
            employee_count = company_details['values'][0]['employeeCountRange']['name']
            employee_count.decode('utf-8')
        except:
            employee_count = 'N/A'
        try:
            web_url = company_details['values'][0]['websiteUrl']
            web_url = web_url.decode('utf-8')
        except:
            web_url = 'N/A'
        try:
            logo_url = company_details['values'][0]['logoUrl']
            logo_url = logo_url.decode('utf-8')
        except:
            logo_url = 'N/A'
        try:
            company_type = company_details['values'][0]['companyType']['name']
            company_type = company_type.decode('utf-8')
        except:
            company_type = 'N/A'
        #print name, industry_name, status, domains, employee_count, web_url, logo_url, company_type
        output_text = name + ',' + industry_name +  ',' + company_type + ',' + \
                      employee_count + ',' + domains + ',' + web_url + ',' + logo_url + '\n'
        output_file.write(output_text.encode('utf-8'))
    
print input_count, invalid_domain_count, no_domain_match_count, mutiple_match_count, output_count
