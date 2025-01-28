def test_can_update_hiring_date(page):
    page.goto("/")
    page.goto("/add_employee")

    page.locator('input[name="name"]').fill("Jane Doe")
    page.locator('input[name="email"]').fill("janedoe@email.com")
    page.locator('input[name="address_line1"]').fill("123 Nowhere St")
    page.locator('input[name="city"]').fill("Somewhere")
    page.locator('input[name="zip_code"]').fill("50677")
    page.locator('input[name="hiring_date"]').fill("2025-01-28")
    page.locator('input[name="job_title"]').fill("Coffee Person")
    page.click("text='Add'")

    page.goto("/employees")
    page.get_by_role("link", name="Edit").nth(0).click()
    page.locator('a[href$="contract"]').click()
    hiring_date_field = page.locator('input[name="hiring_date"]')
    assert hiring_date_field.is_enabled(), "Hiring date field is not enabled"
