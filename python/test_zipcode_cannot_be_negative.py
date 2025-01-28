def test_zipcode_cannot_be_negative(page):
    page.goto("/add_employee")

    page.locator('input[name="name"]').fill("Test User")
    page.locator('input[name="email"]').fill("testuser@gmail.com")
    page.locator('input[name="address_line1"]').fill("123 Main Street")
    page.locator('input[name="city"]').fill("Test City")
    page.locator('input[name="zip_code"]').fill("-12345")
    page.click("text='Add'")

    error_message = page.locator("span.error:has-text('Invalid ZIP code')")
    assert error_message.is_visible(), "Error message for invalid ZIP code was not displayed."
    assert page.url.endswith(
        "/add_employee"), "Form was submitted with an invalid ZIP code."
