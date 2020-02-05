from airportweather import weather_test
import pytest
def test_cities_in_US():
	assert weather_test("Boston") == 1
	assert weather_test("Chicago") == 1
	assert weather_test("Stegenevieve") == 0
	assert weather_test("Newyork") == 0
	assert weather_test("San Francisco") == 0

def test_international():
	assert weather_test("Beijing") == 1
	assert weather_test("Tokyo") == 1