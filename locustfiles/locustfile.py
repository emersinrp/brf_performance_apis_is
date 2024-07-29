import os
from locust import HttpUser, TaskSet, task, between
from dotenv import load_dotenv
from helpers.payloads import person_account_souk_payload
from helpers.utils import get_random_top_skip
from helpers.logging_rules import logger

load_dotenv()

class APITasks(TaskSet):
    headers = {
        'Authorization': os.getenv('AUTHORIZATION_HEADER'),
        'Content-Type': os.getenv('CONTENT_TYPE_HEADER')
    }

    def log_request(self, response, name, payload=None):
        response_time = response.elapsed.total_seconds()
        if response.status_code == 200:
            logger.info(f"Success: {name} | Status Code: {response.status_code} | Response Time: {response_time}s | URL: {response.url}")
        else:
            logger.error(f"Failure: {name} | Status Code: {response.status_code} | Response Time: {response_time}s | URL: {response.url} | Payload: {payload} | Response: {response.text}")

    @task
    def person_account_souk(self):
        name = "Person account Souk - IS"
        print(f"Executing: {name}")
        url = os.getenv('PERSON_ACCOUNT_SOUK_URL')
        payload = person_account_souk_payload
        with self.client.post(url, json=payload, headers=self.headers, name=name, catch_response=True) as response:
            self.log_request(response, name, payload)

    @task
    def person_customer(self):
        name = "Person Customer - IS"
        print(f"Executing: {name}")
        top, skip = get_random_top_skip()
        url = f"{os.getenv('PERSON_CUSTOMER_URL')}?%24top={top}&%24skip={skip}"
        with self.client.get(url, headers=self.headers, name=name, catch_response=True) as response:
            self.log_request(response, name)

    @task
    def person_delivery_window(self):
        name = "Person Delivery Window - IS"
        print(f"Executing: {name}")
        top, skip = get_random_top_skip()
        url = f"{os.getenv('PERSON_DELIVERY_WINDOW_URL')}?%24top={top}&%24skip={skip}"
        with self.client.get(url, headers=self.headers, name=name, catch_response=True) as response:
            self.log_request(response, name)

    @task
    def financial_credit(self):
        name = "Financial Credit - IS"
        print(f"Executing: {name}")
        top, skip = get_random_top_skip()
        url = f"{os.getenv('FINANCIAL_CREDIT_URL')}?%24top={top}&%24skip={skip}"
        with self.client.get(url, headers=self.headers, name=name, catch_response=True) as response:
            self.log_request(response, name)

    @task
    def financial_material(self):
        name = "Financial Material - IS"
        print(f"Executing: {name}")
        top, skip = get_random_top_skip()
        url = f"{os.getenv('FINANCIAL_MATERIAL_URL')}?%24top={top}&%24skip={skip}"
        with self.client.get(url, headers=self.headers, name=name, catch_response=True) as response:
            self.log_request(response, name)

    @task
    def product_stock(self):
        name = "Product Stock - IS"
        print(f"Executing: {name}")
        top, skip = get_random_top_skip()
        url = f"{os.getenv('PRODUCT_STOCK_URL')}?%24top={top}&%24skip={skip}"
        with self.client.get(url, headers=self.headers, name=name, catch_response=True) as response:
            self.log_request(response, name)

    @task
    def utils_description(self):
        name = "Utils Description - IS"
        print(f"Executing: {name}")
        top, skip = get_random_top_skip()
        url = f"{os.getenv('UTILS_DESCRIPTION_URL')}?%24top={top}&%24skip={skip}"
        with self.client.get(url, headers=self.headers, name=name, catch_response=True) as response:
            self.log_request(response, name)

    @task
    def order(self):
        name = "Operation Order - IS"
        print(f"Executing: {name}")
        top, skip = get_random_top_skip()
        url = f"{os.getenv('ORDER_URL')}?%24top={top}&%24skip={skip}"
        with self.client.get(url, headers=self.headers, name=name, catch_response=True) as response:
            self.log_request(response, name)

class APIUser(HttpUser):
    tasks = [APITasks]
    wait_time = between(1, 5)
    host = os.getenv('BASE_HOST')  # Especificar o host base aqui

if __name__ == "__main__":
    import os
    os.system("locust -f locustfile.py")
