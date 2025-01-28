def test_address2_not_become_address1(page):
    page.goto("https://f.se1.hr.dmerej.info/add_employee")

    page.locator('input[name="name"]').fill("Mark Doe")
    page.locator('input[name="email"]').fill("email@email.com")
    page.locator('input[name="address_line1"]').fill("address 1")
    page.locator('input[name="address_line2"]').fill("address 2")
    page.locator('input[name="city"]').fill("Paris")
    page.locator('input[name="zip_code"]').fill("75017")
    page.locator('input[name="hiring_date"]').fill("2025-01-28")
    page.locator('input[name="job_title"]').fill("CEO")
    page.click("text='Add'")

    page.goto("/employees")
    page.get_by_role("link", name="Edit").nth(0).click()
    page.locator('a[href$="address"]').click()
    address2 = page.locator('input[name="address_line2"]').input_value()
    page.click("text='Update'")
    page.get_by_role("link", name="Update address").click()

    address1 = page.locator('input[name="address_line1"]').input_value()
    updated_address2 = page.locator('input[name="address_line2"]').input_value()
    assert updated_address2 != address1, f"Address 2 ('{updated_address2}') unexpectedly matches Address 1 ('{address1}')."