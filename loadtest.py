# hit https://restful-booker.herokuapp.com
# path /booking

from locust import HttpUser, task, between
import time
from lxml import html
import random

class BookingHotel(HttpUser):
	wait_time = between(1, 5)
	host = "https://restful-booker.herokuapp.com"

	@task(1)
	def get_booking(self):
		with self.client.get("/booking", name="Get Booking", catch_response=True) as response:
			if response.status_code == 200:
				response.success()
			else:
				response.failure("Something wrong got response error")