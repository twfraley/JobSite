# TODO: All the things that make it link with Google Cloud Talent API

from google.cloud import talent_v4beta1
import six


# Set project_id variable
def get_project_id():
    return 'jobsite@marine-balm-251400.iam.gserviceaccount.com'


def sample_create_company(display_name, external_id):
    """Create Company"""

    client = talent_v4beta1.CompanyServiceClient()

    # project_id = 'Your Google Cloud Project ID'
    # tenant_id = 'Your Tenant ID (using tenancy is optional)'
    # display_name = 'My Company Name'
    # external_id = 'Identifier of this company in my system'

    project_id = get_project_id()

    if isinstance(display_name, six.binary_type):
        display_name = display_name.decode('utf-8')
    if isinstance(external_id, six.binary_type):
        external_id = external_id.decode('utf-8')
    parent = client.tenant_path(project_id)
    company = {'display_name': display_name, 'external_id': external_id}

    response = client.create_company(parent, company)
    print('Created Company')
    print('Name: {}'.format(response.name))
    print('Display Name: {}'.format(response.display_name))
    print('External ID: {}'.format(response.external_id))


def sample_create_job(company_name, requisition_id,
                      title, description, job_application_url, address_one,
                      address_two, language_code):
    """Create Job"""

    client = talent_v4beta1.JobServiceClient()
    project_id = get_project_id()

    # project_id = 'Your Google Cloud Project ID'
    # tenant_id = 'Your Tenant ID (using tenancy is optional)'
    # company_name = 'Company name, e.g. projects/your-project/companies/company-id'
    # requisition_id = 'Job requisition ID, aka Posting ID. Unique per job.'
    # title = 'Software Engineer'
    # description = 'This is a description of this <i>wonderful</i> job!'
    # job_application_url = 'https://www.example.org/job-posting/123'
    # address_one = '1600 Amphitheatre Parkway, Mountain View, CA 94043'
    # address_two = '111 8th Avenue, New York, NY 10011'
    # language_code = 'en-US'

    if isinstance(project_id, six.binary_type):
        project_id = project_id.decode('utf-8')
    if isinstance(company_name, six.binary_type):
        company_name = company_name.decode('utf-8')
    if isinstance(requisition_id, six.binary_type):
        requisition_id = requisition_id.decode('utf-8')
    if isinstance(title, six.binary_type):
        title = title.decode('utf-8')
    if isinstance(description, six.binary_type):
        description = description.decode('utf-8')
    if isinstance(job_application_url, six.binary_type):
        job_application_url = job_application_url.decode('utf-8')
    if isinstance(address_one, six.binary_type):
        address_one = address_one.decode('utf-8')
    if isinstance(address_two, six.binary_type):
        address_two = address_two.decode('utf-8')
    if isinstance(language_code, six.binary_type):
        language_code = language_code.decode('utf-8')
    parent = client.tenant_path(project_id)
    uris = [job_application_url]
    application_info = {'uris': uris}
    addresses = [address_one, address_two]
    job = {
        'company': company_name,
        'requisition_id': requisition_id,
        'title': title,
        'description': description,
        'application_info': application_info,
        'addresses': addresses,
        'language_code': language_code
    }

    response = client.create_job(parent, job)
    print('Created job: {}'.format(response.name))


def sample_get_job(job_id):
    """Get Job"""

    client = talent_v4beta1.JobServiceClient()
    project_id = get_project_id()

    # project_id = 'Your Google Cloud Project ID'
    # tenant_id = 'Your Tenant ID (using tenancy is optional)'
    # job_id = 'Job ID'

    if isinstance(project_id, six.binary_type):
        project_id = project_id.decode('utf-8')
    if isinstance(job_id, six.binary_type):
        job_id = job_id.decode('utf-8')
    name = client.job_path(project_id, job_id)

    response = client.get_job(name)
    print('Job name: {}'.format(response.name))
    print('Requisition ID: {}'.format(response.requisition_id))
    print('Title: {}'.format(response.title))
    print('Description: {}'.format(response.description))
    print('Posting language: {}'.format(response.language_code))
    for address in response.addresses:
        print('Address: {}'.format(address))
    for email in response.application_info.emails:
        print('Email: {}'.format(email))
    for website_uri in response.application_info.uris:
        print('Website: {}'.format(website_uri))


def sample_search_jobs(query):
    """
    Search Jobs with histogram queries

    Args:
      query Histogram query
      More info on histogram facets, constants, and built-in functions:
      https://godoc.org/google.golang.org/genproto/googleapis/cloud/talent/v4beta1#SearchJobsRequest
      :param query:
    """

    client = talent_v4beta1.JobServiceClient()
    project_id = get_project_id()

    # project_id = 'Your Google Cloud Project ID'
    # tenant_id = 'Your Tenant ID (using tenancy is optional)'
    # query = 'count(base_compensation, [bucket(12, 20)])'

    if isinstance(project_id, six.binary_type):
        project_id = project_id.decode('utf-8')
    if isinstance(query, six.binary_type):
        query = query.decode('utf-8')
    parent = client.tenant_path(project_id)
    domain = 'www.example.com'
    session_id = 'Hashed session identifier'
    user_id = 'Hashed user identifier'
    request_metadata = {
        'domain': domain,
        'session_id': session_id,
        'user_id': user_id
    }
    histogram_queries_element = {'histogram_query': query}
    histogram_queries = [histogram_queries_element]

    # Iterate over all results
    for response_item in client.search_jobs(
            parent, request_metadata, histogram_queries=histogram_queries):
        print('Job summary: {}'.format(response_item.job_summary))
        print('Job title snippet: {}'.format(response_item.job_title_snippet))
        job = response_item.job
        print('Job name: {}'.format(job.name))
        print('Job title: {}'.format(job.title))

