import re
from playwright.sync_api import Playwright, sync_playwright, expect
from dotenv import dotenv_values


def run(playwright: Playwright) -> None:
    my_secrets = dotenv_values(".env")
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://automationteststore.com/")
    page.get_by_role("link", name="Login or register").click()
    page.locator("#loginFrm_loginname").click()
    page.locator("#loginFrm_loginname").fill(my_secrets["USERNAME"])
    page.locator("#loginFrm_password").click()
    page.locator("#loginFrm_password").fill(my_secrets["PASSWORD"])
    page.get_by_role("button", name=" Login").click()
    page.get_by_role("link", name="APPAREL & ACCESSORIES").hover()
    page.get_by_role("link", name="T-shirts").click()
    page.locator("#sort").select_option("p.price-DESC")
    page.goto("https://automationteststore.com/index.php?rt=product/category&path=68_70&sort=p.price-DESC&limit=20")
    page.get_by_role("link", name="").first.click()
    page.get_by_role("link", name=" Add to Cart").click()
    page.get_by_role("link", name="APPAREL & ACCESSORIES").hover()
    page.get_by_role("link", name="T-shirts").click()
    page.locator("#sort").select_option("p.price-DESC")
    page.goto("https://automationteststore.com/index.php?rt=product/category&path=68_70&sort=p.price-DESC&limit=20")
    page.get_by_role("link", name="").nth(1).click()
    page.get_by_role("link").filter(has_text=re.compile(r"^$")).nth(1).click()
    page.get_by_role("link", name=" Add to Cart").click()
    page.locator("#cart_checkout1").click()
    page.get_by_role("button", name=" Confirm Order").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)