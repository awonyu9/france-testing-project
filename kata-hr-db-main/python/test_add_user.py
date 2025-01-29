import httpx
import sqlite3
from faker import Faker

def test_add_user():
    # Create a new user 
    url = "http://127.0.0.1:8000/add_employee"
    faker = Faker()
    user_name = faker.unique.name()
    user_email = faker.unique.email()
    user_address1 = faker.unique.address()
    user_address2 = faker.unique.address()
    user_city = faker.unique.city()
    user_zip = faker.unique.zipcode()
    user_hiring_date = faker.unique.date()
    user_job_title = faker.unique.job()

    response = httpx.post(url, follow_redirects=True, data={"name": user_name, "email": user_email, "address_line1": user_address1, "address_line2": user_address2, "city": user_city, "zip_code": user_zip, "hiring_date": user_hiring_date, "job_title": user_job_title})
    response.raise_for_status()

    # Check that the team is in the db
    database_url = "../backend/db.sqlite3"
    with sqlite3.connect(database_url) as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        rows = cursor.execute("SELECT name FROM hr_basicinfo").fetchall()
        user_names = [row['name'] for row in rows]
        assert user_name in user_names
