import httpx
import sqlite3
from faker import Faker

def test_add_team():
    # Create a new team named 'devs'
    url = "http://127.0.0.1:8000/add_team"
    faker = Faker()
    team_name = faker.unique.word()
    response = httpx.post(url, follow_redirects=True, data={"name": team_name})
    response.raise_for_status()

    # Check that the team is in the db
    database_url = "../backend/db.sqlite3"
    with sqlite3.connect(database_url) as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        rows = cursor.execute("SELECT name FROM hr_team").fetchall()
        team_names = [row['name'] for row in rows]
        assert team_name in team_names
