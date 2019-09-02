# RecruitRoosterTest

Created by Thomas Fraley using Django, hosted on Heroku.

Web app is live here: https://safe-mesa-54979.herokuapp.com/

## About the App
The JobSite! web app is a side project made by Thomas Fraley.  JobSite is a fictitious company that needed a new talent acquisition page.  To solve their hiring woes, I made a super slick job site for the company.  It features a searchable list of jobs (managed by JobSite personell) to which anyone can apply.  The applicant can upload their resume and cover letter in response to a job posting.  JobSite personell can then interact with the applications through the Django admin site.

## Running the app
_The following assumes you're on macOS or linux.  If you're on Windows, well then you're on your own.  Unfortunately I don't have the capability to test this on Windows at the moment._

**To run this locally,** clone it to your machine and spin up a new virtual environment.  For help creating a virtual environment, check this out: https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/

From the app root, run `pip install -r requirements.txt` and wait for everything to install.  This will make sure the app requirements and dependencies are installed in the virtual environment before we run the app.

You'll need Postgres installed and running on your machine.  For help with this, check this out: http://www.postgresqltutorial.com/install-postgresql/

From the terminal, run `createdb jobsite` and wait for confirmation that postgres has spun up a new database.

Once your postgres database is up and running, create a new file (still in the root) named `.env` and add this line to the file: `DATABASE_URL=postgres://localhost:5432/jobsite`.  

Once .env is saved, run (still in the root) `./manage.py migrate` to run migrations.

Congratulations!  You should be good to go.

## Known issues
Right now the site admins can only create job listings through the Django admin portal; Ideally this would be accomplished in-app, or at least the admin portal should be styled and formatted for different levels of admin users.

Still to-do:
- [ ] Create user login, homepage to view all of a particular user's applications
- [ ] Incorporate Google Cloud Talent API
- [ ] Styling - less "default bootstrappy"

## Technologies and techniques:
- Python 3.7
- Django
- PostgreSQL
- Heroku
- HTML5 (Django templates)
- CSS3 (lots of Bootstrap)
- reversible data migrations for database populations
- django crispy forms for form styling
- .env file for local/production environmental variables
- file uploads, storage, and retrieval in server filesystem
