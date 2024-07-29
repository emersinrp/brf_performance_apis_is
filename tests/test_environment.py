import os
import json
from dotenv import load_dotenv
import requests

load_dotenv()

def test_environment_variables():
    required_vars = [
        'BASE_HOST', 'PERSON_ACCOUNT_SOUK_URL', 'PERSON_CUSTOMER_URL', 
        'PERSON_DELIVERY_WINDOW_URL', 'FINANCIAL_CREDIT_URL', 
        'FINANCIAL_MATERIAL_URL', 'PRODUCT_STOCK_URL', 
        'UTILS_DESCRIPTION_URL', 'ORDER_URL', 
        'AUTHORIZATION_HEADER', 'CONTENT_TYPE_HEADER'
    ]
    for var in required_vars:
        assert os.getenv(var) is not None, f"Environment variable {var} is not set"

def test_endpoints_accessibility():
    headers = {
        'Authorization': os.getenv('AUTHORIZATION_HEADER'),
        'Content-Type': os.getenv('CONTENT_TYPE_HEADER')
    }
    
    base_url = os.getenv('BASE_HOST')
    
    urls_with_params = [
        ("Person Customer - IS", f"{base_url}/http/ygg/person/customer?%24top=60&%24skip=0"),
        ("Person Delivery Window - IS", f"{base_url}/http/ygg/person/delivery_window?%24top=60&%24skip=0"),
        ("Financial Credit - IS", f"{base_url}/http/ygg/financial/credit?%24top=5&%24skip=0"),
        ("Financial Material - IS", f"{base_url}/http/ygg/financial/material?%24skip=6&%24top=10"),
        ("Product Stock - IS", f"{base_url}/http/ygg/product/stock?%24top=200&%24skip=0"),
        ("Utils Description - IS", f"{base_url}/http/ygg/utils/description?%24skip=6&%24top=10"),
        ("Order - IS", f"{base_url}/http/ygg/operation/order?%24top=2&%24skip=0")
    ]
    
    for name, url in urls_with_params:
        print(f"Testing URL: {url}")
        print(f"Request Headers: {headers}")
        response = requests.get(url, headers=headers)
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Headers: {response.headers}")
        print(f"Response Body: {response.text}")
        assert response.status_code == 200, (
            f"Endpoint {url} is not accessible, status code: {response.status_code}, "
            f"response: {response.text}"
        )

def test_person_account_souk_post():
    headers = {
        'Authorization': os.getenv('AUTHORIZATION_HEADER'),
        'Content-Type': os.getenv('CONTENT_TYPE_HEADER')
    }
    url = os.getenv('PERSON_ACCOUNT_SOUK_URL')
    payload = {
        "packageCount": 1,
        "packageSize": 1,
        "tp_process": 32
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.request.body:
        print(f"Sent Payload: {response.request.body}")
    else:
        print("No payload was sent in the request.")
    
    assert response.status_code == 200, (
        f"Endpoint {url} is not accessible, status code: {response.status_code}, "
        f"payload: {json.dumps(payload)}, response: {response.text}"
    )
