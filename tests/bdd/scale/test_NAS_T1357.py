# coding=utf-8
"""SCALE UI: feature tests."""

import time
from function import (
    wait_on_element,
    is_element_present,
    attribute_value_exist,
    wait_on_element_disappear,
)
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
    parsers
)
import pytest
pytestmark = [pytest.mark.debug_test]

@scenario('features/NAS-T1357.feature', 'Apps Page - Validate deleting a container image')
def test_apps_page__validate_deleting_a_container_image():
    """Apps Page - Validate deleting a container image."""


@given('the browser is open, navigate to the SCALE URL, and login')
def the_browser_is_open_navigate_to_the_scale_url_and_login(driver, nas_ip, root_password):
    """the browser is open, navigate to the SCALE URL, and login."""
    if nas_ip not in driver.current_url:
        driver.get(f"http://{nas_ip}")
        assert wait_on_element(driver, 10, '//input[@data-placeholder="Username"]')
    if not is_element_present(driver, '//mat-list-item[@ix-auto="option__Dashboard"]'):
        assert wait_on_element(driver, 10, '//input[@data-placeholder="Username"]')
        driver.find_element_by_xpath('//input[@data-placeholder="Username"]').clear()
        driver.find_element_by_xpath('//input[@data-placeholder="Username"]').send_keys('root')
        driver.find_element_by_xpath('//input[@data-placeholder="Password"]').clear()
        driver.find_element_by_xpath('//input[@data-placeholder="Password"]').send_keys(root_password)
        assert wait_on_element(driver, 5, '//button[@name="signin_button"]')
        driver.find_element_by_xpath('//button[@name="signin_button"]').click()
    else:
        assert wait_on_element(driver, 5, '//mat-list-item[@ix-auto="option__Dashboard"]', 'clickable')
        driver.find_element_by_xpath('//mat-list-item[@ix-auto="option__Dashboard"]').click()


@when('on the Dashboard, click on apps')
def on_the_dashboard_click_on_apps(driver):
    """on the Dashboard, click on apps."""
    assert wait_on_element(driver, 10, '//span[contains(.,"Dashboard")]')
    assert wait_on_element(driver, 10, '//mat-list-item[@ix-auto="option__Apps"]', 'clickable')
    driver.find_element_by_xpath('//mat-list-item[@ix-auto="option__Apps"]').click()


@then('Stop machinaris from running')
def stop_machinaris_from_running(driver):
    """Stop machinaris from running."""
    if is_element_present(driver, '//mat-ink-bar[@style="visibility: visible; left: 0px; width: 183px;"]') is False:
        assert wait_on_element(driver, 10, '//div[contains(text(),"Installed Applications")]', 'clickable')
        driver.find_element_by_xpath('//div[contains(text(),"Installed Applications")]').click()
    assert wait_on_element(driver, 45, '//mat-card[contains(.,"machinaris")]//span[contains(.,"Stop")]', 'clickable')
    driver.find_element_by_xpath('//mat-card[contains(.,"machinaris")]//span[contains(.,"Stop")]').click()


@then('Verify the application has stopped')
def verify_the_application_has_stopped(driver):
    """Verify the application has stopped."""
    assert wait_on_element(driver, 5, '//h1[contains(.,"Stopping")]')
    assert wait_on_element_disappear(driver, 60, '//h1[contains(.,"Stopping")]')
    assert wait_on_element(driver, 15, '//mat-card[contains(.,"machinaris-test")]//span[contains(.,"STOPPED ")]')


@then('open available applications')
def open_available_applications(driver):
    """open available applications."""
    assert wait_on_element(driver, 10, '//div[contains(text(),"Available Applications")]', 'clickable')
    driver.find_element_by_xpath('//div[contains(text(),"Available Applications")]').click()
    assert wait_on_element(driver, 7, '//div[contains(.,"Available Applications")]')


@then('when the Apps page loads, open Manager Docker Images')
def when_the_apps_page_loads_open_manager_docker_images(driver):
    """when the Apps page loads, open Manager Docker Images."""
    assert wait_on_element(driver, 10, '//div[contains(text(),"Manage Docker Images")]', 'clickable')
    driver.find_element_by_xpath('//div[contains(text(),"Manage Docker Images")]').click()


@then('click the three dots icon for machinaris')
def click_the_three_dots_icon_for_machinaris(driver):
    """click the three dots icon for machinaris."""
    assert wait_on_element(driver, 20, '//tr[contains(.,"machinaris")]//mat-icon[contains(.,"more_vert")]', 'clickable')
    driver.find_element_by_xpath('//tr[contains(.,"machinaris")]//mat-icon[contains(.,"more_vert")]').click()


@then('click delete')
def click_delete(driver):
    """click delete."""
    assert wait_on_element(driver, 20, '//button//span[contains(.,"Delete")]', 'clickable')
    driver.find_element_by_xpath('//button//span[contains(.,"Delete")]').click()

@then('confirm')
def confirm(driver):
    """confirm."""
    assert wait_on_element(driver, 2, '//mat-checkbox[@ix-auto="checkbox__CONFIRM"]', 'clickable')
    driver.find_element_by_xpath('//mat-checkbox[@ix-auto="checkbox__CONFIRM"]').click()
    wait_on_element(driver, 10, '//button[@ix-auto="button__DELETE"]', 'clickable')
    driver.find_element_by_xpath('//button[@ix-auto="button__DELETE"]').click()


@then('confirm image is deleted')
def confirm_image_is_deleted(driver):
    """confirm image is deleted."""
    assert wait_on_element(driver, 10, '//*[contains(.,"Please wait")]')
    assert wait_on_element_disappear(driver, 30, '//*[contains(.,"Please wait")]')

    assert wait_on_element(driver, 20, '//tr[contains(.,"machinaris")]') is False





