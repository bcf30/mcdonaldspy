# some places are hardcoded cuz mcdonalds changed their
# code on the survey page
# remember to update

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

options = Options()
options.binary_location = "C:\\Users\\Ramir\\AppData\\Local\\Thorium\\Application"

def main():
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    try:

        driver.get("https://survey.medallia.ca/?McD-GSS-FeedlessSurvey")

        restaurant_input = wait_for_element(driver, By.NAME, "spl_q_mcd_gss_restaurant_number_text")
        restaurant_input.clear()
        restaurant_input.send_keys("14869")

        click_element(driver, By.NAME, "forward_main-pager")

        click_radio_by_value(driver, "onf_q_mcd_gss_age_range_enum", "2")

        click_next(driver)

        click_radio_by_value(driver, "onf_q_mcd_gss_memeber_mymcd_rewards_yn", "1")

        click_next(driver)

        date_input = wait_for_element(driver, By.ID, "cal_q_mcd_gss_visit_date_date_")
        date_input.clear()
        date_input.send_keys("03/27/2025")  # CHANGE FOR DIFFERENT DATE

        select_custom_dropdown_option(driver, "12 (12pm)")  # change for day

        select_visit_minutes(driver, "20")  # CHANGE FOR MINUTES

        amount_spent = wait_for_element(driver, By.ID, "spl_q_mcd_gss_amount_text")
        amount_spent.click()
        amount_spent.send_keys("9.01")  # CHANGE FOR DIFFERENT AMOUNT SPENT

        click_next(driver)

        click_radio_by_value(driver, "onf_q_mcd_gss_where_ordered_enum", "1")

        click_next(driver)

        click_radio_by_value(driver, "onf_q_mcd_gss_where_delivered_enum", "1")

        click_next(driver)

        click_radio_by_value(driver, "ch_q_mcd_gss_what_ordered_2_enum", "3")

        click_next(driver)

        click_radio_by_value(driver, "ch_q_mcd_gss_burger_item_with_big_arch_enum",
                             "7")  # CHANGE THE NUMBER IN BRACKETS FOR A DIFFERENT SANDWICH OPTION

        click_next(driver)

        click_radio_by_value(driver, "onf_q_mcd_gss_osat_enum", "5")
        click_radio_by_value(driver, "onf_q_mcd_gss_friendliness_rating_enum", "5")
        click_radio_by_value(driver, "onf_q_mcd_gss_service_speed_rating_enum", "5")
        click_radio_by_value(driver, "onf_q_mcd_gss_food_quality_rating_enum", "5")
        click_radio_by_value(driver, "onf_q_mcd_gss_restaurant_cleanliness_rating_enum", "5")
        click_radio_by_value(driver, "onf_q_mcd_gss_mymcd_reward_program_rating_enum", "5")

        click_next(driver)

        click_radio_by_value(driver, "onf_q_mcd_gss_accurate_order_yn", "1")

        click_radio_by_value(driver, "onf_q_mcd_gss_experienced_problem_yn", "2")

        click_next(driver)
        time.sleep(0.5)
        click_next(driver)
        time.sleep(0.5)

        click_radio_by_value(driver, "onf_q_mcd_gss_ltr_scale_enum", "5")
        click_next(driver)
        time.sleep(0.5)
        click_next(driver)

        click_radio_by_value(driver, "onf_q_mcd_gss_child_visit_yn", "2")

        click_next(driver)

        click_radio_by_value(driver, "onf_q_mcd_gss_coupon_via_email_enum", "1")
        click_element(driver, By.ID, "buttonFinish")

        email_input = wait_for_element(driver, By.ID, "spl_q_mcd_gss_coupon_email_email")
        email_input.clear()
        email_input.send_keys("ramiro.chen@outlook.com")

        # click_element(driver, By.ID, "buttonFinish") #this is the final button for submitting

        time.sleep(5)  #

    finally:
        driver.quit()


def select_custom_dropdown_option(driver, option_text):
    try:

        dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.CSS_SELECTOR,
                    "div[aria-label*='Please share the time of your visit'][role='button']",
                )
            )
        )
        ActionChains(driver).move_to_element(dropdown).click().perform()

        option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    f"//li[contains(@class,'dropdown_dropdownListItem') and contains(text(),'{option_text}')]",
                )
            )
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", option)
        driver.execute_script("arguments[0].click();", option)



    except Exception as e:

        raise


def select_visit_minutes(driver, minutes="20"):  # CHANGE FOR MINUTES

    try:

        dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "div[aria-label='Minutes:'][role='button']")
            )
        )
        ActionChains(driver).move_to_element(dropdown).click().perform()

        option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    f"//li[contains(@class,'dropdown_dropdownListItem') and text()='{minutes}']",
                )
            )
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", option)
        driver.execute_script("arguments[0].click();", option)



    except Exception as e:
        print(f"Failed to select minutes: {str(e)}")
        raise


def wait_for_element(driver, by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((by, value))
    )


def click_element(driver, by, value, timeout=10):
    element = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((by, value))
    )
    element.click()


def click_next(driver):
    click_element(driver, By.ID, "buttonNext")


def click_radio_by_value(driver, name, value):
    radio = wait_for_element(
        driver, By.CSS_SELECTOR, f"input[name='{name}'][value='{value}']"
    )
    driver.execute_script("arguments[0].click();", radio)


if __name__ == "__main__":
    main()