import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants.AccuConstants import *
from time import sleep

class TestAccuWeather:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(base_url)
        
    def teardown_method(self):
        self.driver.quit()

    def test_01_search_city(self):
        search_box = self.driver.find_element(By.CSS_SELECTOR, search_box_CSS)
        search_box.send_keys("İstanbul")
        sleep(1)
        istanbul_search_box = self.driver.find_element(By.XPATH, istanbul_search_box_XPATH)
        istanbul_search_box.click()                                
        sleep(2) 

    def test_02_select_current_location(self):
        search_box = self.driver.find_element(By.CSS_SELECTOR, search_box_CSS)
        search_box.click()
        sleep(2) 
        current_location = self.driver.find_element(By.XPATH, current_location_XPATH)
        current_location.click()
        sleep(2)

    def test_03_search_invalid_city(self):
        search_box = self.driver.find_element(By.CSS_SELECTOR, search_box_CSS)
        search_box.send_keys("sssssaaa")
        sleep(2)
        search_icon = self.driver.find_element(By.CSS_SELECTOR, search_icon_CSS)
        search_icon.click()
        sleep(5)
        result_Message = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH, result_Message_XPATH)))
        assert result_Message.text == "Sonuç bulunamadı."
        sleep(2)
        result_Message2 = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH, result_Message2_XPATH)))
        assert result_Message2.text == "Şehir, posta kodu veya ilgi alanı aramayı deneyin."

    def test_04_current_day_weather(self):
        search_box = self.driver.find_element(By.CSS_SELECTOR, search_box_CSS)
        search_box.send_keys("İstanbul")
        sleep(1)
        istanbul_search_box = self.driver.find_element(By.XPATH, istanbul_search_box_XPATH)
        istanbul_search_box.click()                                
        sleep(1)
        today = self.driver.find_element(By.XPATH, today_XPATH)
        today.click()
        sleep(5)
        day_real_feel_shade_message = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH, day_real_feel_shade_XPATH)))
        assert day_real_feel_shade_message.text == "RealFeel Shade™"

        day_wind_message = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH, day_wind_XPATH)))
        assert day_wind_message.text == "Rüzgar"

        day_strong_wind_message = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH, day_strong_wind_XPATH)))
        assert day_strong_wind_message.text == "Rüzgar Hamleleri"

        day_air_quality = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH, day_air_quality_XPATH)))
        assert day_air_quality.text == "Hava Kalitesi"
        sleep(2)

    def test_05_hourly_weather(self):
        search_box = self.driver.find_element(By.CSS_SELECTOR, search_box_CSS)
        search_box.send_keys("İstanbul")
        sleep(1)
        istanbul_search_box = self.driver.find_element(By.XPATH, istanbul_search_box_XPATH)
        istanbul_search_box.click()                                
        sleep(1)
        hourly = self.driver.find_element(By.XPATH, hourly_XPATH)
        hourly.click()
        sleep(5)

    def test_06_daily_forecast(self):
        search_box = self.driver.find_element(By.CSS_SELECTOR, search_box_CSS)
        search_box.send_keys("İstanbul")
        sleep(1)
        istanbul_search_box = self.driver.find_element(By.XPATH, istanbul_search_box_XPATH)
        istanbul_search_box.click()                                
        sleep(1)
        daily = self.driver.find_element(By.XPATH, daily_XPATH)
        daily.click()
        sleep(5)

    def test__07_hourly_forecast_radar(self):
        search_box = self.driver.find_element(By.CSS_SELECTOR, search_box_CSS)
        search_box.send_keys("İstanbul")
        sleep(1)
        istanbul_search_box = self.driver.find_element(By.XPATH, istanbul_search_box_XPATH)
        istanbul_search_box.click()                                
        sleep(1)
        hourly_radar = self.driver.find_element(By.XPATH, hourly_radar_XPATH)
        hourly_radar.click()
        sleep(5)

    def test_08_minutecast(self):
        search_box = self.driver.find_element(By.CSS_SELECTOR, search_box_CSS)
        search_box.send_keys("İstanbul")
        sleep(1)
        istanbul_search_box = self.driver.find_element(By.XPATH, istanbul_search_box_XPATH)
        istanbul_search_box.click()                                
        sleep(1)
        minutecast = self.driver.find_element(By.XPATH, minutecast_XPATH)
        minutecast.click()
        sleep(5)

    def test_09_day_night_forecast(self):
        search_box = self.driver.find_element(By.CSS_SELECTOR, search_box_CSS)
        search_box.send_keys("İstanbul")
        sleep(1)
        istanbul_search_box = self.driver.find_element(By.XPATH, istanbul_search_box_XPATH)
        istanbul_search_box.click()                                
        sleep(1)
        day_night_forecast = self.driver.find_element(By.XPATH, day_night_forecast_XPATH)
        day_night_forecast.click()
        sleep(5)
    def test_10_air_quality(self):
        search_box = self.driver.find_element(By.CSS_SELECTOR, search_box_CSS)
        search_box.send_keys("İstanbul")
        sleep(1)
        istanbul_search_box = self.driver.find_element(By.XPATH, istanbul_search_box_XPATH)
        istanbul_search_box.click()                                
        sleep(1)
        air_quality = self.driver.find_element(By.XPATH, air_quality_XPATH)
        air_quality.click()
        sleep(5)

    def test_11_health_and_activities(self):
        search_box = self.driver.find_element(By.CSS_SELECTOR, search_box_CSS)
        search_box.send_keys("İstanbul")
        sleep(1)
        istanbul_search_box = self.driver.find_element(By.XPATH, istanbul_search_box_XPATH)
        istanbul_search_box.click()                                
        sleep(3)
        health_and_activities = self.driver.find_element(By.XPATH, health_and_activities_XPATH)
        health_and_activities.click()
        sleep(5)
        
    def test_12_weather_news(self):
        search_box = self.driver.find_element(By.CSS_SELECTOR, search_box_CSS)
        search_box.send_keys("İstanbul")
        sleep(1)
        istanbul_search_box = self.driver.find_element(By.XPATH, istanbul_search_box_XPATH)
        istanbul_search_box.click()                                
        sleep(1)
        weather_news = self.driver.find_element(By.CSS_SELECTOR, weather_news_CSS)
        weather_news.click()
        sleep(5)