def getPageInput(page, name):
    return page.locator('input[name="' + name + '"]')


def create_user(page, name, email, addr1, addr2, city, zip, hiring, job):
    user_name = name
    user_email = email
    user_address = addr1
    user_address2 = addr2
    user_city = city
    user_zip = zip
    user_hiring_date = hiring
    user_job_title = job

    page.goto("https://f.se1.hr.dmerej.info/add_employee")

    name_input = getPageInput(page, "name")
    email_input = getPageInput(page, "email")
    address1_input = getPageInput(page, "address_line1")
    address2_input = getPageInput(page, "address_line2")
    city_input = getPageInput(page, "city")
    zip_input = getPageInput(page, "zip_code")
    hiring_date_input = getPageInput(page, "hiring_date")
    job_title_input = getPageInput(page, "job_title")

    name_input.fill(user_name)
    email_input.fill(user_email)
    address1_input.fill(user_address)
    address2_input.fill(user_address2)
    city_input.fill(user_city)
    zip_input.fill(user_zip)
    hiring_date_input.fill(user_hiring_date)
    job_title_input.fill(user_job_title)
    page.click("text='Add'")


def create_team(page, team_name):
    page.goto("/")
    page.goto("/add_team")
    name_input = page.locator('input[name="name"]')
    name_input.fill(team_name)
    page.click("text='Add'")
