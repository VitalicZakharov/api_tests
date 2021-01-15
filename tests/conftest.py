import sys

import pytest  # , allure
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
import json, os, os.path as path, requests

FIRST_DOMAIN_NAME = "ntm1"
DOMAIN = FIRST_DOMAIN_NAME + ".bugfocus.com"

# wanda
CLIENT_SECRET_WP = "cm9zB2oE0Ltef2f1C4BGpxi8fZz0xFeuDwlW8RqkCMmdXYkXqt4xLF7hQ0h9WRLx"
CLIENT_ID_WP = "wanda.bui"

# alan
CLIENT_SECRET = "ohabO6jkFxViFYzKxKfWYDSTr034TkXTslPeZP20pyjdHpxxiquXcqgqvUz0UWXg"
CLIENT_ID = "alan.jenks"

# system_admin
SYS_CLIENT_SECRET = "FwwKctoaWZ85lcSHNPLrH2Ec9ypPal0G3SiYDCWbtpPg01KXEQ0BNOvuVKBHTmsh"
SYS_CLIENT_ID = "admin"

EXAMPLE = "example.com"
BASE_URL = "https://" + DOMAIN + "//configapi//v2//"
AUTH_URL = "oauth//token"
SCOPE = [EXAMPLE]

HEADERS = {'content-type': 'application/json'}
AUTH_HEAD = {'content-type': 'application/x-www-form-urlencoded'}
HEADERS_IMP = {'content-type': 'application/zip'}

TENANT_PATH = path.abspath(path.join(__file__, "..")) + "\\artifacts\\tenant_example.com.zip"


@pytest.fixture(scope='session',autouse=True)
def precondition():
    deactivate_tenant()
    tenant_deletion()
    tenant_import()
    activate_tenant()

#@pytest.mark.usefixtures("precondition")

def tenant_import(name="get_sys_user_token"):
    HEADERS_IMP.update({'Authorization': 'Bearer ' + str(get_sys_user_token())})
    # open tenant zip
    with open(TENANT_PATH, 'rb') as file:
        result = requests.put(BASE_URL + "tenant", data=file, headers=HEADERS_IMP)

    assert "200" in str(result.status_code), "Tenant import answer status not 200 ; actual status code : " + str(
        result.status_code)
    assert "tenant imported" in str(
        result.text), "Tenant import answer not 'tenant imported' ; actual message : " + str(result.text)


def activate_tenant(name="get_sys_user_token"):
    HEADERS_IMP.update({'Authorization': 'Bearer ' + str(get_sys_user_token())})
    # Request body
    body = {
    }

    # Convert body request to json
    request_body = json.dumps(body)
    result = requests.post(BASE_URL + "tenant//" + EXAMPLE + "//activate", data=request_body, headers=HEADERS_IMP)

    assert "200" in str(result.status_code), "Tenant activation answer status not 200 ; actual status code : " + str(
        result.status_code)
    assert "INACTIVE -> ACTIVE" in str(
        result.text), "Tenant activation answer not 'INACTIVE -> ACTIVE' ; actual message : " + str(result.text)


def deactivate_tenant(name="get_sys_user_token"):
    HEADERS_IMP.update({'Authorization': 'Bearer ' + str(get_sys_user_token())})
    # Request body
    body = {
    }

    # Convert body request to json
    request_body = json.dumps(body)
    result = requests.post(BASE_URL + "tenant//" + EXAMPLE + "//deactivate", data=request_body, headers=HEADERS_IMP)

    assert "200" in str(result.status_code), "Tenant deactivation answer status not 200 ; actual status code : " + str(
        result.status_code)
    assert "ACTIVE -> INACTIVE" in str(
        result.text), "Tenant deactivation answer not 'ACTIVE -> INACTIVE' ; actual message : " + str(result.text)


def tenant_deletion(name="get_sys_user_token"):
    HEADERS_IMP.update({'Authorization': 'Bearer ' + str(get_sys_user_token())})
    # Request body
    body = {
    }

    # Convert body request to json
    request_body = json.dumps(body)
    result = requests.delete(BASE_URL + "tenant//" + EXAMPLE, data=request_body, headers=HEADERS_IMP)

    assert "200" in str(result.status_code), "Tenant deletion answer status not 200 ; actual status code : " + str(
        result.status_code)
    assert "tenant deleted" in str(
        result.text), "Tenant deletion answer not 'tenant deleted' ; actual message : " + str(result.text)


# @pytest.fixture(scope='session')
def get_sys_user_token():
    client = BackendApplicationClient(client_id=SYS_CLIENT_ID)
    session = OAuth2Session(client=client)

    token = session.fetch_token(token_url=BASE_URL + AUTH_URL,
                                client_id=SYS_CLIENT_ID,
                                client_secret=SYS_CLIENT_SECRET,
                                include_client_id=True)
    print("got system user token : ", token)
    return str(token)[
           str(token).find("'access_token': '") + len("'access_token': '"):str(token).find("', 'token_type'")]


@pytest.fixture(scope="class")
# @pytest.fixture
def get_user_token():
    global CLIENT_ID
    global CLIENT_SECRET
    global BASE_URL
    global AUTH_URL
    global SCOPE
    client = BackendApplicationClient(client_id=CLIENT_ID)
    session = OAuth2Session(client=client)

    token = session.fetch_token(token_url=BASE_URL + AUTH_URL,
                                client_id=CLIENT_ID,
                                client_secret=CLIENT_SECRET,
                                scope=SCOPE, include_client_id=True)

    print("got user token : ", token)
    return str(token)[
           str(token).find("'access_token': '") + len("'access_token': '"):str(token).find("', 'token_type'")]


@pytest.fixture(scope="class")
def get_user_without_permission_token():
    global CLIENT_ID_WP
    global CLIENT_SECRET_WP
    global BASE_URL
    global AUTH_URL
    global SCOPE
    client = BackendApplicationClient(client_id=CLIENT_ID_WP)
    session = OAuth2Session(client=client)

    token = session.fetch_token(token_url=BASE_URL + AUTH_URL,
                                client_id=CLIENT_ID_WP,
                                client_secret=CLIENT_SECRET_WP,
                                scope=SCOPE, include_client_id=True)

    print("got user token", token)
    return str(token)[
           str(token).find("'access_token': '") + len("'access_token': '"):str(token).find("', 'token_type'")]


@pytest.fixture(scope='class')
def add_record_post_request_with_correct_body(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//add//List_1_new.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "Integer": "123",
        "Date/Time": "01/07/2025 12:00 AM",
        #"Date/Time": "03-07-2025",
        "Caller id": "Test3",
        "Agent id": "Test3",
        "First name": "Name_First3",
        "Last name": "Name_Last3",
        "Phone1": "9003",
        "Phone2": "9010"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_record_post_request_with_a_duplicate_earlier_created_keys(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//add//List_1_new.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "Integer": "1234",
        "Date/Time": "01/07/2025 12:00 AM",
        #"Date/Time": "03-07-2025",
        "Caller id": "Test4",
        "Agent id": "Test4",
        "First name": "Name_First4",
        "Last name": "Name_Last4",
        "Phone1": "9003",
        "Phone2": "900"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_record_post_request_with_empty_key_field_account(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//add//List_3.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "Account": "",
        "First name": "Name_First17",
        "Last name": "Name_Last17",
        "Phone1": "+7 000 555 17"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_record_post_request_with_incorrectly_formatted_date_time_number_in_a_date_time_field(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//add//List_1_new.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "Integer": "1239",
        "Date/Time": "03A@!#$%^&*()-_:''<>\,.[]{}|/",
        "Caller id": "Test9",
        "Agent id": "Test9",
        "First name": "Name_First9",
        "Last name": "Name_Last9",
        "Phone1": "9009",
        "Phone2": "9090"
    }

    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_record_post_request_with_incorrectly_formatted_phone_number_country(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//add//List_3.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "Account": "1234516",
        "First name": "Name_First16",
        "Last name": "Name_Last16",
        "Phone1": "+7 000 555 16"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_record_post_request_with_incorrectly_formatted_phone_number_in_a_caller_id_field(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi/v2/callinglist/add/List_1_new.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "Integer": "1238",
        #"Date/Time": "03-07-2025",
        "Date/Time": "01/07/2025 12:00 AM",
        "Caller id": "1!@#$%^&*()Ab-_{}[\]/|?,.''2",
        "Agent id": "Test8",
        "First name": "Name_First8",
        "Last name": "Name_Last8",
        "Phone1": "9008",
        "Phone2": "9080"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_record_post_request_with_incorrectly_formatted_phone_number_in_a_phone_field(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//add//List_2.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "First name": "Name_First15",
        "Last name": "Name_Last15",
        "Phone1": "~!@#$%^&*()_=,.[]{}'/?|\:"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_record_post_request_with_missing_req_field(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//add//List_1_new.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "Integer": "1235",
        #"Date/Time": "03-07-2025",
        "Date/Time": "01/07/2025 12:00 AM",
        "Caller id": "Test5",
        "Agent id": "Test5",
        "First name": "Name_First5",
        "Last name": "Name_Last5",
        "Phone1": "9005"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_record_post_request_with_non_existent_agent_username_in_an_agent_login_id_field(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//add//List_1_new.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "Integer": "1237",
        #"Date/Time": "03-07-2025",
        "Date/Time": "01/07/2025 12:00 AM",
        "Caller id": "Test7",
        "Agent id": "Ri/!@#$%^&*();:<>,.{}''|?ck",
        "First name": "Name_First7",
        "Last name": "Name_Last7",
        "Phone1": "9007",
        "Phone2": "9070"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_record_post_request_with_space_in_the_key_field(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//add//List_3.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "Account": " ",
        "First name": " ",
        "Last name": " ",
        "Phone1": " "
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_record_post_request_with_a_date_time_field_set_to_a_moment_in_the_past(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//add//List_1_new.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "Integer": "12310",
        #"Date/Time": "03-07-813",
        "Date/Time": "01/07/1025 12:00 AM",
        "Caller id": "Test10",
        "Agent id": "Test10",
        "First name": "Name_First10",
        "Last name": "Name_Last10",
        "Phone1": "9010",
        "Phone2": "9100"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_record_post_request_with_incorrectly_formatted_value_in_an_integer_field(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//add//List_1_new.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "Integer": "abc",
        #"Date/Time": "03-07-2025",
        "Date/Time": "01/07/2025 12:00 AM",
        "Caller id": "Test11",
        "Agent id": "Test11",
        "First name": "Name_First11",
        "Last name": "Name_Last11",
        "Phone1": "9011",
        "Phone2": "9110"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_record_post_request_without_a_phone_field_req(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//add//List_1_new.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "Integer": "12312",
        #"Date/Time": "03-07-2025",
        "Date/Time": "01/07/2025 12:00 AM",
        "Caller id": "Test12",
        "Agent id": "Test12",
        "First name": "Name_First12",
        "Last name": "Name_Last12",
        "Phone1": "9012"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_record_post_request_without_a_phone_field_req_and_key(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//add//List_1_new.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "Integer": "12313",
        #"Date/Time": "03-07-2025",
        "Date/Time": "01/07/2025 12:00 AM",
        "Caller id": "Test13",
        "Agent id": "Test13",
        "First name": "Name_First13",
        "Last name": "Name_Last13",
        "Phone2": "9130"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_record_post_request_without_a_phone_fields(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//add//List_2.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "First name": "Name_First14",
        "Last name": "Name_Last14"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_record_post_request_with_do_not_authorize_session():
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//add//List_2.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str("token")})
    # Request body
    body = {
        "First name": "Name_First14",
        "Last name": "Name_Last14"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_record_post_request_with_authorize_session_for_user_without_permission(get_user_without_permission_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//add//List_2.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_without_permission_token)})
    # Request body
    body = {
        "First name": "Name_First14",
        "Last name": "Name_Last14"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_record_post_request_with_empty_body(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//add//List_2.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_record_post_request_with_a_first_name_field_only(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//add//List_1_new.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "First Name": "Test3"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_record_post_request_with_a_phone_field_only(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//add//List_2.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "Phone1": "1003"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_record_post_request_without_a_last_name_fields(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//add//List_2.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "First Name": "Test44",
        "Phone1": "1004"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_record_post_request_with_a_redundant_field(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//add//List_2.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "First Name": "Test5",
        "Phone1": "1005",
        "SOMETHING": "BLAH BLAH"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_record_post_request_with_incorrect_body_format_deleted_quotes(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//add//List_1_new.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    request_body = bytes("{\"First Name: Test6, Phone1: 1006\"}", 'utf-8')
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_record_post_request_with_incorrect_body_format_typization(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//add//List_1_new.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    request_body = bytes("First Name: Test6, Phone1: 1006", 'utf-8')
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_record_post_request_with_incorrect_body_format_a_redundant_comma_in_the_end(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//add//List_1_new.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    request_body = bytes('{"First Name": "Test6", "Phone1": "1006",}', 'utf-8')
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_record_post_request_with_a_duplicate_key_field_in_the_body(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//add//List_2.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    request_body = bytes('{"First Name": "Test6", "Phone1": "1006", "Phone1": "1006"}', 'utf-8')
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_record_post_request_with_empty_first_name_and_phone(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//add//List_1_new.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "First Name": "",
        "Phone1": ""
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_record_post_request_to_the_non_existent_list(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//add//List_not_exists.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "First Name": "Test6",
        "Phone1": "1006"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_record_post_request_with_invalid_url(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//add_invalid//List_TCTR.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "First Name": "Test6",
        "Phone": "1006"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_record_post_request_with_the_incorrectly_formatted_value_phone_number_in_a_phone_field_non_numeric_symbol_other_than_plus(
        get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//add//List_2.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "First name": "Name_Test11",
        "Last name": "Name_Test11",
        "Phone1": "9020abc"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_record_post_request_with_the_value_phone_number_in_a_phone_field_using_symbol_plus(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//add//List_2.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "First name": "Name_Test11",
        "Last name": "Name_Test11",
        "Phone1": "+1234567890"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_record_post_request_for_corrupted_on_importing_list_all_fields_are_correct(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//add//List_11.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "Integer": "123",
        "Date/Time": "03-07-2025",
        #"Date/Time": "02/07/2020 10:01 am",
        "Caller id": "Test3",
        "Agent id": "Test3",
        "First name": "Name_First3",
        "Last name": "Name_Last3",
        "Phone1": "9003",
        "Phone2": "9010"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_record_get_request_with_correct_body(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//add//List_1_new.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "Integer": "123",
        #"Date/Time": "03-07-2025",
        "Date/Time": "01/07/2025 12:00 AM",
        "Caller id": "Test3",
        "Agent id": "Test3",
        "First name": "Name_First3",
        "Last name": "Name_Last3",
        "Phone1": "9003",
        "Phone2": "9010"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.get(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_record_put_request_with_correct_body(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//add//List_1_new.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "Integer": "123",
        #"Date/Time": "03-07-2025",
        "Date/Time": "01/07/2025 12:00 AM",
        "Caller id": "Test3",
        "Agent id": "Test3",
        "First name": "Name_First3",
        "Last name": "Name_Last3",
        "Phone1": "9003",
        "Phone2": "9010"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.put(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_record_delete_request_with_correct_body(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//add//List_1_new.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "Integer": "123",
        #"Date/Time": "03-07-2025",
        "Date/Time": "01/07/2025 12:00 AM",
        "Caller id": "Test3",
        "Agent id": "Test3",
        "First name": "Name_First3",
        "Last name": "Name_Last3",
        "Phone1": "9003",
        "Phone2": "9010"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.delete(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_many_records_post_request_with_correct_body(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//addAll//List_1_new.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = [
        {
            "Integer": "123171",
            #"Date/Time": "01-07-2025",
            "Date/Time": "01/07/2025 12:00 AM",
            "Caller id": "Test19",
            "Agent id": "Test19",
            "First name": "Name_First19",
            "Last name": "Name_Last19",
            "Phone1": "9019",
            "Phone2": "9190"
        },
        {
            "Integer": "123172",
            #"Date/Time": "02-07-2025",
            "Date/Time": "01/07/2025 12:00 AM",
            "Caller id": "Test19_2",
            "Agent id": "Test19_2",
            "First name": "Name_First19_2",
            "Last name": "Name_Last19_2",
            "Phone1": "90192",
            "Phone2": "9192"
        },
        {
            "Integer": "123173",
            #"Date/Time": "03-07-2025",
            "Date/Time": "01/07/2025 12:00 AM",
            "Caller id": "Test19_3",
            "Agent id": "Test19_3",
            "First name": "Name_First19_3",
            "Last name": "Name_Last19_3",
            "Phone1": "90193",
            "Phone2": "9193"
        }
    ]
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_many_records_post_request_with_a_duplicate_earlier_created_keys(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//addAll//List_1.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = [
        {
            "Integer": "123211",
            #"Date/Time": "01-07-2025",
            "Date/Time": "01/07/2025 12:00 AM",
            "Caller id": "Test20",
            "Agent id": "Test20",
            "First name": "Name_First20",
            "Last name": "Name_Last20",
            "Phone1": "9019",
            "Phone2": "9200"
        },
        {
            "Integer": "123212",
            #"Date/Time": "02-07-2025",
            "Date/Time": "01/07/2025 12:00 AM",
            "Caller id": "Test20_2",
            "Agent id": "Test20_2",
            "First name": "Name_First20_2",
            "Last name": "Name_Last20_2",
            "Phone1": "90202",
            "Phone2": "9192"
        },
        {
            "Integer": "123213",
            #"Date/Time": "03-07-2025",
            "Date/Time": "01/07/2025 12:00 AM",
            "Caller id": "Test20_3",
            "Agent id": "Test20_3",
            "First name": "Name_First20_3",
            "Last name": "Name_Last20_3",
            "Phone1": "90203",
            "Phone2": "9193"
        }
    ]
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_many_records_post_request_with_incorrect_body_format_typization(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//addAll//List_1.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    request_body = bytes(str(
        {
            "Integer": "123211",
            #"Date/Time": "01-07-2025",
            "Date/Time": "01/07/2025 12:00 AM",
            "Caller id": "Test20",
            "Agent id": "Test20",
            "First name": "Name_First20",
            "Last name": "Name_Last20",
            "Phone1": "9019",
            "Phone2": "9200"
        }), 'utf-8')
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)

@pytest.fixture(scope='class')
def add_record_post_request_with_correct_but_different_datetime_format(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//add//List_1_new.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "Integer": "123",
        #"Date/Time": "02/07/2020 10:01 am",
        "Date/Time": "03-07-2025",
        "Caller id": "Test3",
        "Agent id": "Test3",
        "First name": "Name_First3",
        "Last name": "Name_Last3",
        "Phone1": "9003",
        "Phone2": "9010"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)

@pytest.fixture(scope='class')
def add_many_records_post_request_with_a_missing_required_field(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//addAll//List_1.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = [
        {
            "Integer": "123211",
            "Date/Time": "01-07-2025",
            "Caller id": "Test21",
            "Agent id": "Test21",
            "First name": "Name_First21",
            "Last name": "Name_Last21",
            "Phone1": "9021"
        },
        {
            "Integer": "123212",
            "Date/Time": "02-07-2025",
            "Caller id": "Test21_2",
            "Agent id": "Test21_2",
            "First name": "Name_First21_2",
            "Last name": "Name_Last21_2",
            "Phone2": "9212"
        },
        {
            "Integer": "123213",
            "Date/Time": "03-07-2025",
            "Caller id": "Test21_3",
            "Agent id": "Test21_3",
            "First name": "Name_First21_3",
            "Last name": "Name_Last21_3",
            "Phone1": "90213",
            "Phone2": "9213"
        }
    ]
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)

@pytest.fixture(scope='class')
def add_many_records_post_request_with_a_non_existent_field_name(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//addAll//List_1.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = [
        {
            "Integer": "123221",
            "Date/Time": "01-07-2022",
            "Caller id": "Test22",
            "Agent id": "Test22",
            "First name": "Name_First22",
            "Last name": "Name_Last22",
            "Phone1": "9022",
            "Phone2": "9220"
        },
        {
            "Unknown field": "test22",
            "Integer": "123222",
            "Date/Time": "02-07-2022",
            "Caller id": "Test22_2",
            "Agent id": "Test22_2",
            "First name": "Name_First22_2",
            "Last name": "Name_Last22_2",
            "Phone1": "90222",
            "Phone2": "9222"
        },
        {
            "Integer": "123223",
            "Date/Time": "03-07-2022",
            "Caller id": "Test22_3",
            "Agent id": "Test22_3",
            "First name": "Name_First22_3",
            "Last name": "Name_Last22_3",
            "Phone1": "90223",
            "Phone2": "9223"
        }
    ]
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_many_records_post_request_with_non_existent_agent_username_in_an_agent_login_id_field(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//addAll//List_1.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = [
        {
            "Integer": "123231",
            "Date/Time": "01-07-2023",
            "Caller id": "10023",
            "Agent id": "`~!@#$%^&*()_+ []{}|\?/,.1",
            "First name": "Name_First23",
            "Last name": "Name_Last23",
            "Phone1": "9023",
            "Phone2": "9230"
        },
        {
            "Integer": "123232",
            "Date/Time": "02-07-2023",
            "Caller id": "100232",
            "Agent id": "`~!@#$%^&*()_+ []{}|\?/,.2",
            "First name": "Name_First23_2",
            "Last name": "Name_Last23_2",
            "Phone1": "90232",
            "Phone2": "9232"
        },
        {
            "Integer": "123233",
            "Date/Time": "03-07-2023",
            "Caller id": "100233",
            "Agent id": "`~!@#$%^&*()_+ []{}|\?/,.3",
            "First name": "Name_First23_3",
            "Last name": "Name_Last23_3",
            "Phone1": "90233",
            "Phone2": "9233"
        }
    ]
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_many_records_post_request_with_an_incorrectly_formatted_phone_number_in_a_caller_id_field(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//addAll//List_1.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = [
        {
            "Integer": "123241",
            "Date/Time": "01-07-2024",
            "Caller id": "`a~!@#$%^&*()_+ []{}|\?/,.1",
            "Agent id": "Test24.1",
            "First name": "Name_First24",
            "Last name": "Name_Last24",
            "Phone1": "9024",
            "Phone2": "9240"
        },
        {
            "Integer": "123242",
            "Date/Time": "02-07-2024",
            "Caller id": "`a~!@#$%^&*()_+ []{}|\?/,.2",
            "Agent id": "Test24.2",
            "First name": "Name_First24_2",
            "Last name": "Name_Last24_2",
            "Phone1": "90242",
            "Phone2": "9242"
        },
        {
            "Integer": "123243",
            "Date/Time": "03-07-2024",
            "Caller id": "`a~!@#$%^&*()_+ []{}|\?/,.3",
            "Agent id": "Test24.3",
            "First name": "Name_First24_3",
            "Last name": "Name_Last24_3",
            "Phone1": "90243",
            "Phone2": "9243"
        }
    ]
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_many_records_post_request_with_an_incorrectly_date_time_number_in_a_date_time_field(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//addAll//List_1.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = [
        {
            "Integer": "123251",
            "Date/Time": "`~!@#$%^&*()_+ <>-[]{}|?/,.1",
            "Caller id": "10025",
            "Agent id": "Test25.1",
            "First name": "Name_First25",
            "Last name": "Name_Last25",
            "Phone1": "9025",
            "Phone2": "9250"
        },
        {
            "Integer": "123252",
            "Date/Time": "02-07-2025",
            "Caller id": "100252",
            "Agent id": "Test25.2",
            "First name": "Name_First25_2",
            "Last name": "Name_Last25_2",
            "Phone1": "90252",
            "Phone2": "9252"
        },
        {
            "Integer": "123253",
            "Date/Time": "02-07-2025",
            "Caller id": "100253",
            "Agent id": "Test25.3",
            "First name": "Name_First25_3",
            "Last name": "Name_Last25_3",
            "Phone1": "90253",
            "Phone2": "9253"
        }
    ]
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_many_records_post_request_with_a_date_time_field_set_to_a_moment_in_the_past(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//addAll//List_1.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = [
        {
            "Integer": "123261",
            "Date/Time": "01-07-826",
            "Caller id": "10026",
            "Agent id": "Test26.1",
            "First name": "Name_First26",
            "Last name": "Name_Last26",
            "Phone1": "9026",
            "Phone2": "9260"
        },
        {
            "Integer": "123262",
            "Date/Time": "02-07-826",
            "Caller id": "100262",
            "Agent id": "Test26.2",
            "First name": "Name_First26_2",
            "Last name": "Name_Last26_2",
            "Phone1": "90262",
            "Phone2": "9262"
        },
        {
            "Integer": "123263",
            "Date/Time": "03-07-826",
            "Caller id": "100263",
            "Agent id": "Test26.3",
            "First name": "Name_First26_3",
            "Last name": "Name_Last26_3",
            "Phone1": "90263",
            "Phone2": "9263"
        }
    ]
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_many_records_post_request_with_incorrectly_formatted_value_in_an_integer_field_all_rec(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//addAll//List_1.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = [
        {
            "Integer": "`ф~!@#$%^&*()_+ <>-[]{}|?/,.1",
            "Date/Time": "01-07-2027",
            "Caller id": "10027",
            "Agent id": "Test27.1",
            "First name": "Name_First27",
            "Last name": "Name_Last27",
            "Phone1": "9026",
            "Phone2": "9260"
        },
        {
            "Integer": "`ф~!@#$%^&*()_+ <>-[]{}|?/,.2",
            "Date/Time": "02-07-2027",
            "Caller id": "100272",
            "Agent id": "Test27.2",
            "First name": "Name_First27_2",
            "Last name": "Name_Last27_2",
            "Phone1": "90272",
            "Phone2": "9272"
        },
        {
            "Integer": "`ф~!@#$%^&*()_+ <>-[]{}|?/,.3",
            "Date/Time": "03-07-2027",
            "Caller id": "100273",
            "Agent id": "Test27.3",
            "First name": "Name_First27_3",
            "Last name": "Name_Last27_3",
            "Phone1": "90273",
            "Phone2": "9273"
        }
    ]
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_many_records_post_request_with_incorrectly_formatted_value_in_an_integer_field_one_rec(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//addAll//List_1.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = [
        {
            "Integer": "123281",
            "Date/Time": "01-07-2028",
            "Caller id": "10028",
            "Agent id": "Test28.1",
            "First name": "Name_First28",
            "Last name": "Name_Last28",
            "Phone1": "9028",
            "Phone2": "9280"
        },
        {
            "Integer": "`ф~!@#$%^&*()_+ <>-[]{}|?/,.2",
            "Date/Time": "02-07-2028",
            "Caller id": "100282",
            "Agent id": "Test28.2",
            "First name": "Name_First28_2",
            "Last name": "Name_Last28_2",
            "Phone1": "90282",
            "Phone2": "9282"
        },
        {
            "Integer": "123283",
            "Date/Time": "03-07-2028",
            "Caller id": "100283",
            "Agent id": "Test28.3",
            "First name": "Name_First28_3",
            "Last name": "Name_Last28_3",
            "Phone1": "90283",
            "Phone2": "9283"
        }
    ]
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_many_records_post_request_without_a_phone_field_not_required_field(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//addAll//List_2.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = [
        {
            "First name": "Name_First29",
            "Last name": "Name_Last29"
        },
        {
            "First name": "Name_First29_2",
            "Last name": "Name_Last29_2",
            "Phone1": "90292",
        },
        {
            "First name": "Name_First29_3",
            "Last name": "Name_Last29_3",
            "Phone1": "90293",
        }
    ]
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)

@pytest.fixture(scope='class')
def add_many_records_post_request_without_a_phone_field_required_field(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//addAll//List_1.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = [
        {
            "Integer": "123301",
            "Date/Time": "01-07-2030",
            "Caller id": "10030",
            "Agent id": "Test30.1",
            "First name": "Name_First30",
            "Last name": "Name_Last30",
            "Phone1": "9030",
            "Phone2": "9300"
        },
        {
            "Integer": "123302",
            "Date/Time": "02-07-2030",
            "Caller id": "100302",
            "Agent id": "Test30.2",
            "First name": "Name_First30_2",
            "Last name": "Name_Last30_2",
            "Phone1": "90302"
        },
        {
            "Integer": "123303",
            "Date/Time": "03-07-2030",
            "Caller id": "100303",
            "Agent id": "Test30.3",
            "First name": "Name_First30_3",
            "Last name": "Name_Last30_3",
            "Phone1": "90303",
            "Phone2": "9303"
        }
    ]
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_many_records_post_request_without_a_phone_field_required_field_and_key(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//addAll//List_1.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = [
        {
            "Integer": "123301",
            "Date/Time": "01-07-2031",
            "Caller id": "10031",
            "Agent id": "Test31.1",
            "First name": "Name_First31",
            "Last name": "Name_Last31",
            "Phone1": "9031",
            "Phone2": "9310"
        },
        {
            "Integer": "123312",
            "Date/Time": "02-07-2031",
            "Caller id": "100312",
            "Agent id": "Test31.2",
            "First name": "Name_First31_2",
            "Last name": "Name_Last31_2",
            "Phone2": "9312"

        },
        {
            "Integer": "123313",
            "Date/Time": "03-07-2031",
            "Caller id": "100313",
            "Agent id": "Test31.3",
            "First name": "Name_First31_3",
            "Last name": "Name_Last31_3",
            "Phone1": "90313",
            "Phone2": "9313"
        }
    ]
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_many_records_post_request_without_a_phone_field_empty_value(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//addAll//List_1.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = [
        {
            "Integer": "123321",
            "Date/Time": "01-07-2032",
            "Caller id": "10032",
            "Agent id": "Test32.1",
            "First name": "Name_First32",
            "Last name": "Name_Last32",
            "Phone1": "9032",
            "Phone2": "9320"
        },
        {
            "Integer": "123322",
            "Date/Time": "02-07-2032",
            "Caller id": "100322",
            "Agent id": "Test32.2",
            "First name": "Name_First32_2",
            "Last name": "Name_Last32_2",
            "Phone1": "",
            "Phone2": "9322"

        },
        {
            "Integer": "123323",
            "Date/Time": "03-07-2032",
            "Caller id": "100323",
            "Agent id": "Test32.3",
            "First name": "Name_First32_3",
            "Last name": "Name_Last32_3",
            "Phone1": "90323",
            "Phone2": "9323"
        }
    ]
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_many_records_post_request_without_a_phone_field_space_in_a_key_field(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//addAll//List_1.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = [
        {
            "Integer": "123331",
            "Date/Time": "01-07-2033",
            "Caller id": "10033",
            "Agent id": "Test33.1",
            "First name": "Name_First33",
            "Last name": "Name_Last33",
            "Phone1": "9033",
            "Phone2": "9330"
        },
        {
            "Integer": "123332",
            "Date/Time": "02-07-2033",
            "Caller id": "100332",
            "Agent id": "Test33.2",
            "First name": "Name_First33_2",
            "Last name": "Name_Last33_2",
            "Phone1": " ",
            "Phone2": "9332"

        },
        {
            "Integer": "123333",
            "Date/Time": "03-07-2033",
            "Caller id": "100333",
            "Agent id": "Test33.3",
            "First name": "Name_First33_3",
            "Last name": "Name_Last33_3",
            "Phone1": "90333",
            "Phone2": "9333"
        }
    ]
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_many_records_post_request_with_an_incorrectly_formatted_phone_number_in_a_phone_field_non_numeric_symbol_other_than_plus(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//addAll//List_1.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = [
        {
            "Integer": "123341",
            "Date/Time": "01/07/25 12:00 AM",
            "Caller id": "10034",
            "Agent id": "Test34.1",
            "First name": "Name_First34",
            "Last name": "Name_Last34",
            "Phone1": "9034",
            "Phone2": "9340"
        },
        {
            "Integer": "123342",
            "Date/Time": "01/07/25 12:00 AM",
            "Caller id": "100342",
            "Agent id": "Test34.2",
            "First name": "Name_First34_2",
            "Last name": "Name_Last34_2",
            "Phone1": "`ф~!@#$%^&*()_+ <>-[]{}|?/,.",
            "Phone2": "9342"

        },
        {
            "Integer": "123343",
            "Date/Time": "01/07/25 12:00 AM",
            "Caller id": "100343",
            "Agent id": "Test34.3",
            "First name": "Name_First34_3",
            "Last name": "Name_Last34_3",
            "Phone1": "90343",
            "Phone2": "9343"
        }
    ]
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_many_records_post_request_with_an_incorrectly_formatted_phone_number_in_a_phone_field_the_country_set_for_us_and_canada_the_number_starts_with_1_and_has_less_than_11(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//addAll//List_3.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = [
        {
            "Account": "1234535",
            "First name": "Name_First35",
            "Last name": "Name_Last35",
            "Phone1": "+1 601 555 5535"
        },
        {
            "Account": "12345352",
            "First name": "Name_First35_2",
            "Last name": "Name_Last35_2",
            "Phone1": "+1 000 555 116"
        },
        {
            "Account": "12345353",
            "First name": "Name_First35_3",
            "Last name": "Name_Last35_3",
            "Phone1": "16025555535"
        }
    ]
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_many_records_post_request_with_do_not_authorize_session():
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//addAll//List_1.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str("token")})
    # Request body
    body = [
        {
            "Integer": "123171",
            "Date/Time": "01-07-2025",
            "Caller id": "Test19",
            "Agent id": "Test19",
            "First name": "Name_First19",
            "Last name": "Name_Last19",
            "Phone1": "9019",
            "Phone2": "9190"
        },
        {
            "Integer": "123172",
            "Date/Time": "02-07-2025",
            "Caller id": "Test19_2",
            "Agent id": "Test19_2",
            "First name": "Name_First19_2",
            "Last name": "Name_Last19_2",
            "Phone1": "90192",
            "Phone2": "9192"
        },
        {
            "Integer": "123173",
            "Date/Time": "03-07-2025",
            "Caller id": "Test19_3",
            "Agent id": "Test19_3",
            "First name": "Name_First19_3",
            "Last name": "Name_Last19_3",
            "Phone1": "90193",
            "Phone2": "9193"
        }
    ]
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_many_records_post_request_with_authorize_session_for_user_without_permission(get_user_without_permission_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//addAll//List_1.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_without_permission_token)})
    # Request body
    body = [
        {
            "Integer": "123171",
            "Date/Time": "01-07-2025",
            "Caller id": "Test19",
            "Agent id": "Test19",
            "First name": "Name_First19",
            "Last name": "Name_Last19",
            "Phone1": "9019",
            "Phone2": "9190"
        },
        {
            "Integer": "123172",
            "Date/Time": "02-07-2025",
            "Caller id": "Test19_2",
            "Agent id": "Test19_2",
            "First name": "Name_First19_2",
            "Last name": "Name_Last19_2",
            "Phone1": "90192",
            "Phone2": "9192"
        },
        {
            "Integer": "123173",
            "Date/Time": "03-07-2025",
            "Caller id": "Test19_3",
            "Agent id": "Test19_3",
            "First name": "Name_First19_3",
            "Last name": "Name_Last19_3",
            "Phone1": "90193",
            "Phone2": "9193"
        }
    ]
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_many_records_post_request_without_parameters_empty_body(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//addAll//List_1.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = [
    ]
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_many_records_post_request_with_a_duplicated_in_one_request_values(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//addAll//List_2.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    request_body = bytes("[{\"Last Name\":\"User6\",\"Phone1\":\"1006\"},{\"Incorrect\":\"Test7\",\"Last Name\":\"User7\",\"Phone1\":\"1007\"},{\"First Name\":\"Test8\",\"Last Name\":\"User8\"},{\"First Name\":\"Test11\",\"Phone1\":\"1011\"},{\"First Name\":\"Test11\",\"Last Name\":\"User11\",\"Phone1\":\"1011\"}]", 'utf-8')
#        { "First Name":"Test9", "Phone":"1009"},

    # Convert body request to json
    #request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_many_records_post_request_with_an_incorrect_body_format(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//addAll//List_2.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    request_body = "[{\"First Name\":\"Test17\",Phone1:10017\"},{\"First Name\":\"Test18\",\"Last Name\":\"User18\",\"Phone1\":\"10018\"}]"
    # Convert body request to json
    #request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_many_records_post_request_with_an_incorrect_body_format_redundant_comma_in_the_end(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//addAll//List_2.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    request_body = bytes("[{\"First Name\":\"Test12\",\"Phone1\":\"10012\"},{\"First Name\":\"Test13\",\"Phone1\":\"10013\"}**,**]", 'utf-8')
    # Convert body request to json
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)

@pytest.fixture(scope='class')
def add_many_records_post_request_to_the_non_existent_list(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//addAll//List_not_exists.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = [
        {"First Name":"Test14", "Phone":"100014"},
        {"First Name":"Test15", "Last Name":"", "Phone":"10015"}
    ]
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_many_records_post_request_with_invalid_url(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//addAll_invalid//List_TCTR.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = [
        {"First Name":"Test14", "Phone":"100014"},
        {"First Name":"Test15", "Last Name":"", "Phone":"10015"}
    ]
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_many_records_post_request_with_incorrectly_formatted_phone_number_in_a_phone_field(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//addAll//List_2.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = [
        {"First Name":"Test14", "Phone1":"1qwerty00014"},
        {"First Name":"Test15", "Last Name":"User15", "Phone1":"10015"}
    ]
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_many_records_get_request_with_correct_body(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//addAll//List_1.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = [
        {
            "Integer": "123171",
            "Date/Time": "01-07-2025",
            "Caller id": "Test19",
            "Agent id": "Test19",
            "First name": "Name_First19",
            "Last name": "Name_Last19",
            "Phone1": "9019",
            "Phone2": "9190"
        },
        {
            "Integer": "123172",
            "Date/Time": "02-07-2025",
            "Caller id": "Test19_2",
            "Agent id": "Test19_2",
            "First name": "Name_First19_2",
            "Last name": "Name_Last19_2",
            "Phone1": "90192",
            "Phone2": "9192"
        },
        {
            "Integer": "123173",
            "Date/Time": "03-07-2025",
            "Caller id": "Test19_3",
            "Agent id": "Test19_3",
            "First name": "Name_First19_3",
            "Last name": "Name_Last19_3",
            "Phone1": "90193",
            "Phone2": "9193"
        }
    ]
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.get(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_many_records_put_request_with_correct_body(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//addAll//List_1.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = [
        {
            "Integer": "123171",
            "Date/Time": "01-07-2025",
            "Caller id": "Test19",
            "Agent id": "Test19",
            "First name": "Name_First19",
            "Last name": "Name_Last19",
            "Phone1": "9019",
            "Phone2": "9190"
        },
        {
            "Integer": "123172",
            "Date/Time": "02-07-2025",
            "Caller id": "Test19_2",
            "Agent id": "Test19_2",
            "First name": "Name_First19_2",
            "Last name": "Name_Last19_2",
            "Phone1": "90192",
            "Phone2": "9192"
        },
        {
            "Integer": "123173",
            "Date/Time": "03-07-2025",
            "Caller id": "Test19_3",
            "Agent id": "Test19_3",
            "First name": "Name_First19_3",
            "Last name": "Name_Last19_3",
            "Phone1": "90193",
            "Phone2": "9193"
        }
    ]
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.put(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_many_records_delete_request_with_correct_body(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//addAll//List_1.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = [
        {
            "Integer": "123171",
            "Date/Time": "01-07-2025",
            "Caller id": "Test19",
            "Agent id": "Test19",
            "First name": "Name_First19",
            "Last name": "Name_Last19",
            "Phone1": "9019",
            "Phone2": "9190"
        },
        {
            "Integer": "123172",
            "Date/Time": "02-07-2025",
            "Caller id": "Test19_2",
            "Agent id": "Test19_2",
            "First name": "Name_First19_2",
            "Last name": "Name_Last19_2",
            "Phone1": "90192",
            "Phone2": "9192"
        },
        {
            "Integer": "123173",
            "Date/Time": "03-07-2025",
            "Caller id": "Test19_3",
            "Agent id": "Test19_3",
            "First name": "Name_First19_3",
            "Last name": "Name_Last19_3",
            "Phone1": "90193",
            "Phone2": "9193"
        }
    ]
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.delete(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_records_to_dnc_post_request_to_any_non_existent_dnc_list(get_user_token):
    #wile https://trac.brightpattern.com/ticket/24443
    #request_url = "https://" + DOMAIN + "//configapi//v2//donotcalllist//add//List_not_exists.txt"
    request_url = "https://" + DOMAIN + "//configapi//v2//donotcalllist//add//List_not_exists"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = [
        "123456789",
        "9999999999"
    ]
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_record_post_request_with_body_from_other_list(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//add//List_TCTR.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "Integer": "123",
        "Date/Time": "02/07/2020 10:01 am",
        #"Date/Time": "03-07-2025",
        "Caller id": "Test3",
        "Agent id": "Test3",
        "First name": "Name_First3",
        "Last name": "Name_Last3",
        "Phone1": "9003",
        "Phone2": "9010"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_many_records_post_request_with_body_from_other_list(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//addAll//List.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = [
        {
            "Integer": "123171",
            "Date/Time": "01-07-2025",
            "Caller id": "Test19",
            "Agent id": "Test19",
            "First name": "Name_First19",
            "Last name": "Name_Last19",
            "Phone1": "9019",
            "Phone2": "9190"
        },
        {
            "Integer": "123172",
            "Date/Time": "02-07-2025",
            "Caller id": "Test19_2",
            "Agent id": "Test19_2",
            "First name": "Name_First19_2",
            "Last name": "Name_Last19_2",
            "Phone1": "90192",
            "Phone2": "9192"
        },
        {
            "Integer": "123173",
            "Date/Time": "03-07-2025",
            "Caller id": "Test19_3",
            "Agent id": "Test19_3",
            "First name": "Name_First19_3",
            "Last name": "Name_Last19_3",
            "Phone1": "90193",
            "Phone2": "9193"
        }
    ]
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_records_to_dnc_post_request_containing_correctly_formatted_numbers_to_dnc_of_type_internal_duplicates_and_not(get_user_token):
    #wile https://trac.brightpattern.com/ticket/24443
    #request_url = "https://" + DOMAIN + "//configapi//v2//donotcalllist//add//List_dnc_internal.txt"
    request_url = "https://" + DOMAIN + "//configapi//v2//donotcalllist//add//List_dnc_internal"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = [
        "9000",
        "9001",
        "9002",
        "9002",
        "9003"
    ]
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_records_to_dnc_post_request_containing_both_correctly_and_incorrectly_formatted_numbers_to_dnc_of_type_internal(get_user_token):
    #wile https://trac.brightpattern.com/ticket/24443
    #request_url = "https://" + DOMAIN + "//configapi//v2//donotcalllist//add//List_dnc_internal.txt"
    request_url = "https://" + DOMAIN + "//configapi//v2//donotcalllist//add//List_dnc_internal"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = [
        "abc",
        "9004",
        "~!@#$%^&*()_=+|/?,.",
        "9005",
        " ",
        "",
        "+9006"
    ]
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_records_to_dnc_post_request_containing_a_correctly_formatted_number_and_a_comment_to_dnc_of_type_internal_comment_not_correspond_any_existing_campaigns(get_user_token):
    #wile https://trac.brightpattern.com/ticket/24443
    #request_url = "https://" + DOMAIN + "//configapi//v2//donotcalllist//add//List_dnc_internal.txt"
    request_url = "https://" + DOMAIN + "//configapi//v2//donotcalllist//add//List_dnc_internal"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = [
        [
            "9007",
            "Comment for 9007 ~!@#$%^&*()_+=-[]{}\|,.<>?/`"
        ],
        [
            "9008",
            "Comment for 9008 ~!@#$%^&*()_+=-[]{}\|,.<>?/`"
        ]
    ]
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_records_to_dnc_post_request_containing_a_correctly_spelled_us_state_to_a_dnc_of_type_geographic(get_user_token):
    #wile https://trac.brightpattern.com/ticket/24443
    #request_url = "https://" + DOMAIN + "//configapi//v2//donotcalllist//add//List_dnc_state_province.txt"
    request_url = "https://" + DOMAIN + "//configapi//v2//donotcalllist//add//List_dnc_state_province"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = [
        "1415-418-6591"
    ]
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_records_to_dnc_post_request_containing_a_free_text_to_a_dnc_of_type_record_exclusion(get_user_token):
    #wile https://trac.brightpattern.com/ticket/24443
    #request_url = "https://" + DOMAIN + "//configapi//v2//donotcalllist//add//List_dnc_record_exclusion.txt"
    request_url = "https://" + DOMAIN + "//configapi//v2//donotcalllist//add//List_dnc_record_exclusion"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = [
        "field 1",
        "@test6 field2"
    ]
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_records_to_dnc_post_request_add_a_new_and_an_existing_records_containing_a_valid_us_postal_code_to_a_dnc_of_type_geographic_and_free_text(get_user_token):
    #wile https://trac.brightpattern.com/ticket/24443
    #request_url = "https://" + DOMAIN + "//configapi//v2//donotcalllist//add//List_dnc_postal.txt"
    request_url = "https://" + DOMAIN + "//configapi//v2//donotcalllist//add//List_dnc_postal"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = [
        [
            "90210",
            "California"
        ],
        [
            "10001",
            "New York"
        ]
    ]
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_records_to_dnc_post_request_add_a_record_containing_a_valid_us_postal_code_to_a_dnc_of_type_geographic_and_free_text(get_user_token):
    #wile https://trac.brightpattern.com/ticket/24443
    #request_url = "https://" + DOMAIN + "//configapi//v2//donotcalllist//add//List_dnc_postal.txt"
    request_url = "https://" + DOMAIN + "//configapi//v2//donotcalllist//add//List_dnc_postal"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = [
        [
            "02871",
            "Rhode Island"
        ],
        [
            "19147",
            "Pennsylvania"
        ]
    ]
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_records_to_dnc_post_request_add_2_records_containing_a_special_symbols_postal_code_to_a_dnc_of_type_geographic_and_free_text(get_user_token):
    #wile https://trac.brightpattern.com/ticket/24443
    #request_url = "https://" + DOMAIN + "//configapi//v2//donotcalllist//add//List_dnc_postal.txt"
    request_url = "https://" + DOMAIN + "//configapi//v2//donotcalllist//add//List_dnc_postal"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = [
        [
            "Comment1 !@#$%^&*()_+=-[]{}\|,.<>?/`",
            "Comment11 ~!@#$%^&*()_+=-[]{}\|,.<>?/`"
        ],
        [
            "Comment2 !@#$%^&*()_+=-[]{}\|,.<>?/`",
            "Comment22 ~!@#$%^&*()_+=-[]{}\|,.<>?/`"
        ]
    ]
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_records_to_dnc_post_request_add_nothing_for_1_record_for_a_dnc_of_type_geographic(get_user_token):
    #wile https://trac.brightpattern.com/ticket/24443
    #request_url = "https://" + DOMAIN + "//configapi//v2//donotcalllist//add//List_dnc_postal.txt"
    request_url = "https://" + DOMAIN + "//configapi//v2//donotcalllist//add//List_dnc_postal"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = [
        [
            "field 1",
            "field 2"
        ],
        [

        ],
        [
            "field 3",
            "field 4"
        ]
    ]
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_records_to_dnc_post_request_add_only_1_record_with_a_comment_for_a_dnc_of_type_geographic(get_user_token):
    #wile https://trac.brightpattern.com/ticket/24443
    #request_url = "https://" + DOMAIN + "//configapi//v2//donotcalllist//add//List_dnc_postal.txt"
    request_url = "https://" + DOMAIN + "//configapi//v2//donotcalllist//add//List_dnc_postal"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = [
        "22201",
        "Virginia"
    ]
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_records_to_dnc_post_request_add_a_record_containing_a_valid_us_area_code_to_a_dnc_of_type_area_codes_and_free_text(get_user_token):
    #wile https://trac.brightpattern.com/ticket/24443
    #request_url = "https://" + DOMAIN + "//configapi//v2//donotcalllist//add//List_dnc_area_code.txt"
    request_url = "https://" + DOMAIN + "//configapi//v2//donotcalllist//add//List_dnc_area_code"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = [
        [
            "417",
            "Springfield"
        ],
        [
            "418",
            "Quebec"
        ]
    ]
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_records_to_dnc_post_request_add_a_record_containing_an_incorrectly_formatted_us_area_code_to_a_dnc_of_type_area_codes(get_user_token):
    #wile https://trac.brightpattern.com/ticket/24443
    #request_url = "https://" + DOMAIN + "//configapi//v2//donotcalllist//add//List_dnc_area_code.txt"
    request_url = "https://" + DOMAIN + "//configapi//v2//donotcalllist//add//List_dnc_area_code"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = [
        [
            "001",
            "One"
        ],
        [
            "002a",
            "Two"
        ],
        [
            "T 3 !@#$%^&*()_+=-[]{}\|,.<>?/`",
            "Three 3 !@#$%^&*()_+=-[]{}\|,.<>?/`"
        ]
    ]
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_records_to_dnc_post_request_with_do_not_authorize_session():
    # wile https://trac.brightpattern.com/ticket/24443
    #request_url = "https://" + DOMAIN + "//configapi//v2//donotcalllist//add//List_dnc_internal.txt"
    request_url = "https://" + DOMAIN + "//configapi//v2//donotcalllist//add//List_dnc_internal"
    HEADERS.update({'Authorization': 'Bearer ' + str("token")})
    # Request body
    body = [
        [
            "9007",
            "Comment for 9007 ~!@#$%^&*()_+=-[]{}\|,.<>?/`"
        ],
        [
            "9008",
            "Comment for 9008 ~!@#$%^&*()_+=-[]{}\|,.<>?/`"
        ]
    ]
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_records_to_dnc_post_request_with_authorize_session_for_user_without_permission(get_user_without_permission_token):
    # wile https://trac.brightpattern.com/ticket/24443
    #request_url = "https://" + DOMAIN + "//configapi//v2//donotcalllist//add//List_dnc_internal.txt"
    request_url = "https://" + DOMAIN + "//configapi//v2//donotcalllist//add//List_dnc_internal"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_without_permission_token)})
    # Request body
    body = [
        [
            "9007",
            "Comment for 9007 ~!@#$%^&*()_+=-[]{}\|,.<>?/`"
        ],
        [
            "9008",
            "Comment for 9008 ~!@#$%^&*()_+=-[]{}\|,.<>?/`"
        ]
    ]
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_records_to_dnc_post_request_with_incorrect_body_format_typization(get_user_token):
    # wile https://trac.brightpattern.com/ticket/24443
    #request_url = "https://" + DOMAIN + "//configapi//v2//donotcalllist//add//List_dnc_internal.txt"
    request_url = "https://" + DOMAIN + "//configapi//v2//donotcalllist//add//List_dnc_internal"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    request_body = bytes("First Name: Test6, Phone1: 1006", 'utf-8')
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_records_to_dnc_get_request_with_correct_body(get_user_token):
    # wile https://trac.brightpattern.com/ticket/24443
    #request_url = "https://" + DOMAIN + "//configapi//v2//donotcalllist//add//List_dnc_internal.txt"
    request_url = "https://" + DOMAIN + "//configapi//v2//donotcalllist//add//List_dnc_internal"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = [
        [
            "9007",
            "Comment for 9007 ~!@#$%^&*()_+=-[]{}\|,.<>?/`"
        ],
        [
            "9008",
            "Comment for 9008 ~!@#$%^&*()_+=-[]{}\|,.<>?/`"
        ]
    ]
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.get(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_records_to_dnc_put_request_with_correct_body(get_user_token):
    # wile https://trac.brightpattern.com/ticket/24443
    #request_url = "https://" + DOMAIN + "//configapi//v2//donotcalllist//add//List_dnc_internal.txt"
    request_url = "https://" + DOMAIN + "//configapi//v2//donotcalllist//add//List_dnc_internal"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = [
        [
            "9007",
            "Comment for 9007 ~!@#$%^&*()_+=-[]{}\|,.<>?/`"
        ],
        [
            "9008",
            "Comment for 9008 ~!@#$%^&*()_+=-[]{}\|,.<>?/`"
        ]
    ]
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.put(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def add_records_to_dnc_delete_request_with_correct_body(get_user_token):
    # wile https://trac.brightpattern.com/ticket/24443
    #request_url = "https://" + DOMAIN + "//configapi//v2//donotcalllist//add//List_dnc_internal.txt"
    request_url = "https://" + DOMAIN + "//configapi//v2//donotcalllist//add//List_dnc_internal"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = [
        [
            "9007",
            "Comment for 9007 ~!@#$%^&*()_+=-[]{}\|,.<>?/`"
        ],
        [
            "9008",
            "Comment for 9008 ~!@#$%^&*()_+=-[]{}\|,.<>?/`"
        ]
    ]
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.delete(request_url, data=request_body, headers=HEADERS)


#@pytest.fixture(scope='class')
#def add_records_to_dnc_post_request_with_body_from_other_list(get_user_token):
#    # wile https://trac.brightpattern.com/ticket/24443
#    #request_url = "https://" + DOMAIN + "//configapi//v2//donotcalllist//add//List_dnc_internal.txt"
#    request_url = "https://" + DOMAIN + "//configapi//v2//donotcalllist//add//List_dnc_internal"
#    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
#    # Request body
#    body = [
#        [
#            "90210",
#            "California"
#        ],
#        [
#            "10001",
#            "New York"
#        ]
#    ]
#    # Convert body request to json
#    request_body = json.dumps(body)
#    print("request_url : ", request_url)
#    print("request_body : ", request_body)
#    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def delete_all_records_post_request_with_a_valid_list_assigned_to_multiple_campaigns(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//deleteAll//List_Delete1.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "First name": "Name_F55",
        "Last name": "Name_L55",
        "Phone1": "7"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def delete_all_records_post_request_with_a_valid_list_assigned_to_multiple_campaigns_empty_body(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//deleteAll//List_Delete2.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def delete_all_records_post_request_with_a_valid_list_assigned_to_multiple_campaigns_empty_body_and_list_without_records(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//deleteAll//List_Delete3.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def delete_all_records_post_request_with_an_invalid_list(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//deleteAll//invalid_List_Delete3.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "First name": "Name_F55",
        "Last name": "Name_L55",
        "Phone1": "7"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def delete_all_records_post_request_with_do_not_authorize_session():
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//deleteAll//List_Delete1.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str("token")})
    # Request body
    body = {
        "First name": "Name_F55",
        "Last name": "Name_L55",
        "Phone1": "7"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def delete_all_records_post_request_with_authorize_session_for_user_without_permission(get_user_without_permission_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//deleteAll//List_Delete1.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_without_permission_token)})
    # Request body
    body = {
        "First name": "Name_F55",
        "Last name": "Name_L55",
        "Phone1": "7"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def delete_all_records_post_request_with_invalid_url(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//add_invalid//List_Delete1.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "First name": "Name_F55",
        "Last name": "Name_L55",
        "Phone1": "7"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def delete_all_records_get_request_with_correct_body(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//deleteAll//List_Delete1.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "First name": "Name_F55",
        "Last name": "Name_L55",
        "Phone1": "7"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.get(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def delete_all_records_put_request_with_correct_body(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//deleteAll//List_Delete1.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "First name": "Name_F55",
        "Last name": "Name_L55",
        "Phone1": "7"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.put(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def delete_all_records_delete_request_with_correct_body(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//deleteAll//List_Delete1.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "First name": "Name_F55",
        "Last name": "Name_L55",
        "Phone1": "7"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.delete(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def delete_all_records_post_request_with_incorrect_body_format_typization(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//deleteAll//List_Delete1.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    request_body = bytes("{First name: Name_F55, Last name : Name_L55, Phone1: 7}", 'utf-8')
    #request_body = [{
    #    "First name": "Name_F55",
    #    "Last name": "Name_L55",
    #    "Phone1": "7"
    #}]
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)

@pytest.fixture(scope='class')
def delete_all_records_post_request_with_csv_list_format(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//deleteAll//List_Delete1.csv"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "First name": "Name_F55",
        "Last name": "Name_L55",
        "Phone1": "7"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def update_record_post_request_with_existent_record_key(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//update//List_1.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "Integer": "36",
        "Date/Time": "01-01-2036",
        "Caller id": "36",
        "Agent id": "agent.id36",
        "First name": "Name_F36",
        "Last name": "Name_L36",
        "Phone1": "7000",
        "Phone2": "1036"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def update_record_post_request_with_a_non_existent_record_key(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//update//List_1.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "Integer": "37",
        "Date/Time": "02-02-2037",
        "Caller id": "37",
        "Agent id": "agent.id37",
        "First name": "Name_F37",
        "Last name": "Name_L37",
        "Phone1": "8",
        "Phone2": "1000"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def update_record_post_request_with_an_incorrect_integer_value(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//update//List_1.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "Integer": "abc",
        "Date/Time": "02-02-2038",
        "Caller id": "38",
        "Agent id": "38",
        "First name": "Name_F38",
        "Last name": "Name_L38",
        "Phone1": "7000",
        "Phone2": "1038"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def update_record_post_request_with_an_incorrect_date_time_value(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//update//List_1.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "Integer": "39",
        "Date/Time": "`~!@#$%^&*()_+[]{}|\?/,.",
        "Caller id": "39",
        "Agent id": "agent.id39",
        "First name": "Name_F39",
        "Last name": "Name_L39",
        "Phone1": "7000",
        "Phone2": "1039"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def update_record_post_request_with_an_incorrect_caller_id(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//update//List_1.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "Integer": "40",
        "Date/Time": "02-02-2040",
        "Caller id": "`~!@#$%^&*()_+[]{}|\?/,.",
        "Agent id": "agent.id40",
        "First name": "Name_F40",
        "Last name": "Name_L40",
        "Phone1": "7000",
        "Phone2": "1040"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def update_record_post_request_with_an_incorrect_agent_id(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//update//List_1.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "Integer": "41",
        "Date/Time": "02-02-2041",
        "Caller id": "41",
        "Agent id": "`~!@#$%^&*()_+[]{}|\?/,.",
        "First name": "Name_F41",
        "Last name": "Name_L41",
        "Phone1": "7000",
        "Phone2": "1041"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def update_record_post_request_with_a_date_time_field_set_to_a_moment_in_the_past(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//update//List_1.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "Integer": "42",
        "Date/Time": "02-02-842",
        "Caller id": "42",
        "Agent id": "agent.id42",
        "First name": "Name_F42",
        "Last name": "Name_L42",
        "Phone1": "7000",
        "Phone2": "1042"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def update_record_post_request_without_a_phone_field_required_field(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//update//List_1.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "Integer": "43",
        "Date/Time": "02-02-2043",
        "Caller id": "43",
        "Agent id": "agent.id43",
        "First name": "Name_F43",
        "Last name": "Name_L43",
        "Phone1": "7000"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def update_record_post_request_without_a_phone_field_required_field_and_key(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//update//List_1.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "Integer": "44",
        "Date/Time": "02-02-2044",
        "Caller id": "44",
        "Agent id": "agent.id44",
        "First name": "Name_F44",
        "Last name": "Name_L44",
        "Phone2": "1044"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def update_record_post_request_without_a_phone_field_empty_value(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//update//List_1.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "Integer": "45",
        "Date/Time": "02-02-2045",
        "Caller id": "45",
        "Agent id": "agent.id45",
        "First name": "Name_F45",
        "Last name": "Name_L45",
        "Phone1": "",
        "Phone2": "1045"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def update_record_post_request_incorrectly_formatted_phone_number_in_a_phone_field(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//update//List_1.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "Integer": "46",
        "Date/Time": "02-02-2046",
        "Caller id": "46",
        "Agent id": "agent.id46",
        "First name": "Name_F46",
        "Last name": "Name_L46",
        "Phone1": "7000",
        "Phone2": "`~!@#$%^&*()_+[]{}|\?/,."
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def update_record_post_request_incorrectly_formatted_phone_number_in_a_phone_field_the_country_set_for_us_and_canada_the_number_starts_with_1_and_has_less_than_11_digits(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//update//List_3.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "Account": "1234567",
        "First name": "Name_First47",
        "Last name": "Name_Last47",
        "Phone1": "+7 000 555 47"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def update_record_post_request_with_a_non_existent_field_name(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//update//List_1.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "unknown": "un48",
        "Integer": "48",
        "Date/Time": "02-02-2048",
        "Caller id": "48",
        "Agent id": "agent.id48",
        "First name": "Name_F48",
        "Last name": "Name_L48",
        "Phone1": "7000",
        "Phone2": "1048"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def update_record_post_request_with_do_not_authorize_session():
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//update//List_1.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str("token")})
    # Request body
    body = {
        "Integer": "36",
        "Date/Time": "01-01-2036",
        "Caller id": "36",
        "Agent id": "agent.id36",
        "First name": "Name_F36",
        "Last name": "Name_L36",
        "Phone1": "7000",
        "Phone2": "1036"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def update_record_post_request_with_authorize_session_for_user_without_permission(get_user_without_permission_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//update//List_1.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_without_permission_token)})
    # Request body
    body = {
        "Integer": "36",
        "Date/Time": "01-01-2036",
        "Caller id": "36",
        "Agent id": "agent.id36",
        "First name": "Name_F36",
        "Last name": "Name_L36",
        "Phone1": "7000",
        "Phone2": "1036"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def update_record_post_request_without_parameters_empty_body(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//update//List_TCTR.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def update_record_post_request_without_a_key_phone_parameter_phone_field_doesnt_present_in_body(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//update//List_TCTR.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "First name": "Test1",
        "Last name": "Update list request"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def update_record_post_request_with_a_wrong_key_phone_parameter(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//update//List_TCTR.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "First name": "Test1",
        "Last name": "Update list request",
        "Phone": "1111"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def update_record_post_request_without_a_key_first_name_parameter(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//update//List_2.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "Last name": "Update list request",
        "Phone": "1001"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def update_record_post_request_with_a_wrong_key_first_name_parameter(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//update//List_2.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "First name": "Testik___1",
        "Last name": "Update list request",
        "Phone": "1001"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def update_record_post_request_without_a_last_name_parameter(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//update//List_TCTR.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "First name": "Test1",
        "Phone": "1001"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def update_record_post_request_with_incorrect_body_format_deleted_quotes(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//update//List_TCTR.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    request_body = bytes('{"First name": "Test1","Last name": "Updatelistrequest",Phone: 1001"}', 'utf-8')
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def update_record_post_request_with_incorrect_body_format_a_redundant_comma_in_the_end(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//update//List_TCTR.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    request_body = bytes('{"First name": "Test1","Last name": "Updatelistrequest","Phone": "1001" **, **}', 'utf-8')
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def update_record_post_request_to_the_non_existent_list(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//update//List_not_exists.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "First name": "Test1",
        "Phone": "1001"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def update_record_post_request_with_invalid_url(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//update_invalid//List_TCTR.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "First name": "Test1",
        "Phone": "1001"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def update_record_post_request_with_the_incorrectly_formatted_value_phone_number_in_a_phone_field_non_numeric_symbol_other_than_plus(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//update//List_TCTR.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "Integer": "789",
        "First name": "Test1",
        "Last name": "Updatelistrequest",
        "Phone": "10dc1"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def update_record_post_request_with_the_value_phone_number_in_a_phone_field_using_symbol_plus(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//update//List_TCTR.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "Integer": "789",
        "First name": "Test1",
        "Last name": "Updatelistrequest",
        "Phone": "+1001"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def update_record_post_request_with_body_from_other_list(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//update//List_1.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "Integer": "789",
        "First name": "Test1",
        "Last name": "Updatelistrequest",
        "Phone": "+1001"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def update_record_get_request_with_correct_body(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//update//List_TCTR.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "First name": "Test1",
        "Phone": "1001"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.get(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def update_record_put_request_with_correct_body(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//update//List_TCTR.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "First name": "Test1",
        "Phone": "1001"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.put(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def update_record_delete_request_with_correct_body(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//update//List_TCTR.txt"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "First name": "Test1",
        "Phone": "1001"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.delete(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def get_all_records_post_request_with_valid_list_campaign_fromtime_and_maxsize_start_index_from_0(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//getAll//List_Completed.txt//Camp_1"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "fromIndex": 0,
        "maxSize": 100
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def get_all_records_post_request_with_valid_list_campaign_fromtime_and_maxsize_start_index_from_2(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//getAll//List_Completed.txt//Camp_1"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "fromIndex": 2,
        "maxSize": 100
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def get_all_records_post_request_with_valid_list_campaign_fromtime_and_maxsize_start_index_from_3(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//getAll//List_Completed.txt//Camp_1"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "fromIndex": 3,
        "maxSize": 100
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def get_all_records_post_request_with_valid_list_campaign_fromtime_and_maxsize_maxsize_1_and_fromindex_more_than_0(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//getAll//List_Completed.txt//Camp_1"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "fromIndex": 1,
        "maxSize": 1
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def get_all_records_post_request_with_invalid_fromindex_value_fromindex_alphabetical(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//getAll//List_Completed.txt//Camp_1"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "fromIndex": 'a',
        "maxSize": 1
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def get_all_records_post_request_with_invalid_maxsize_value_maxsize_alphabetical(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//getAll//List_Completed.txt//Camp_1"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "fromIndex": 0,
        "maxSize": 'a'
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def get_all_records_post_request_with_valid_list_campaign_maxsize_but_without_fromindex(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//getAll//List_Completed.txt//Camp_1"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "maxSize": 10
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def get_all_records_post_request_with_valid_list_campaign_fromindex_but_without_maxsize(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//getAll//List_Completed.txt//Camp_1"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "fromIndex": 0
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def get_all_records_post_request_with_valid_list_and_campaign_that_are_not_associated(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//getAll//List_Completed.txt//campaign_that_are_not_associated"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "fromIndex": 0,
        "maxSize": 10
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def get_all_records_post_request_with_maxsize_set_to_1000(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//getAll//List_1000.csv//Camp_1"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "fromIndex": 0,
        "maxSize": 1000
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def get_all_records_post_request_with_maxsize_set_to_1001(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//getAll//List_1000.csv//Camp_1"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "fromIndex": 0,
        "maxSize": 1001
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def get_all_records_post_request_with_do_not_authorize_session():
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//getAll//List_Completed.txt//Camp_1"
    HEADERS.update({'Authorization': 'Bearer ' + str("token")})
    # Request body
    body = {
        "fromIndex": 0,
        "maxSize": 100
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def get_all_records_post_request_with_invalid_url(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//invalid_getAll//List_Completed.txt//Camp_1"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "fromIndex": 0,
        "maxSize": 100
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def get_all_records_post_request_to_the_non_existent_list(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//getAll//List_not_exists.txt//Camp_1"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "fromIndex": 0,
        "maxSize": 100
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def get_all_records_post_request_with_authorize_session_for_user_without_permission(get_user_without_permission_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//getAll//List_Completed.txt//Camp_1"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_without_permission_token)})
    # Request body
    body = {
        "fromIndex": 0,
        "maxSize": 100
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def get_all_records_get_request_with_correct_body(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//getAll//List_Completed.txt//Camp_1"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "fromIndex": 0,
        "maxSize": 100
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.get(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def get_all_records_put_request_with_correct_body(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//getAll//List_Completed.txt//Camp_1"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "fromIndex": 0,
        "maxSize": 100
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.put(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def get_all_records_delete_request_with_correct_body(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//getAll//List_Completed.txt//Camp_1"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "fromIndex": 0,
        "maxSize": 100
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.delete(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def get_all_records_post_request_with_incorrect_body_format_typization(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//getAll//List_Completed.txt//Camp_1"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    request_body = bytes('["fromIndex": 0,"maxSize: 100]', 'utf-8')
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def get_campaigns_post_request_to_get_campaigns_info(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//campaign//getAll//"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
#    body = {
#        "Integer": "123",
#        "Date/Time": "01/07/2025 12:00 AM",
#        #"Date/Time": "03-07-2025",
#        "Caller id": "Test3",
#        "Agent id": "Test3",
#        "First name": "Name_First3",
#        "Last name": "Name_Last3",
#        "Phone1": "9003",
#        "Phone2": "9010"
#    }
    # Convert body request to json
#    request_body = json.dumps(body)
    print("request_url : ", request_url)
#    print("request_body : ", request_body)
#    return requests.get(request_url, data=request_body, headers=HEADERS)
    return requests.get(request_url, headers=HEADERS)


@pytest.fixture(scope='class')
def get_completed_records_post_request_with_valid_list_campaign_fromtime_and_maxsize_2(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//getCompleted//List_Completed.txt//Camp_1"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "fromTime": "2013-03-01T13:15:06.456",
        "maxSize": "2"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def get_completed_records_post_request_with_valid_list_campaign_fromtime_and_maxsize_3(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//getCompleted//List_Completed.txt//Camp_1"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "fromTime": "2013-03-01T13:15:06.456",
        "maxSize": "3"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def get_completed_records_post_request_with_valid_list_campaign_maxsize_and_fromtime_in_the_future(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//getCompleted//List_Completed.txt//Camp_1"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "fromTime": "2073-03-01T13:15:06.456",
        "maxSize": "3"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def get_completed_records_post_request_with_valid_list_campaign_maxsize_but_without_fromtime(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//getCompleted//List_Completed.txt//Camp_1"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "maxSize": "3"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def get_completed_records_post_request_with_valid_list_campaign_fromtime_but_without_maxsize(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//getCompleted//List_Completed.txt//Camp_1"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "fromTime": "2013-03-01T13:15:06.456"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def get_completed_records_post_request_with_valid_list_and_campaign_that_are_not_associated(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//getCompleted//List_Completed.txt//campaign_that_are_not_associated"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "fromTime": "2073-03-01T13:15:06.456",
        "maxSize": "3"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def get_completed_records_post_request_with_an_invalid_list_and_valid_campaign(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//getCompleted//invalid_List_Completed.txt//Camp_1"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "fromTime": "2073-03-01T13:15:06.456",
        "maxSize": "3"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def get_completed_records_post_request_with_a_non_existent_query_parameter(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//getCompleted//List_Completed.txt//Camp_1"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "fromTime": "2073-03-01T13:15:06.456",
        "wtf": "3"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def get_completed_records_post_request_with_a_wrong_fromtime_format(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//getCompleted//List_Completed.txt//Camp_1"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "fromTime": "2003-03-03:15:06.456",
        "maxSize": "3"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def get_completed_records_post_request_with_maxsize_set_to_1000(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//getCompleted//List_1000.csv//Camp_1"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "fromTime": "2013-03-01T13:15:06.456",
        "maxSize": "1000"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def get_completed_records_post_request_maxSize_set_to_greater_than_1000(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//getCompleted//List_1000.csv//Camp_1"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "fromTime": "2013-03-01T13:15:06.456",
        "maxSize": "1001"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def get_completed_records_post_request_with_do_not_authorize_session():
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//getCompleted//List_Completed.txt//Camp_1"
    HEADERS.update({'Authorization': 'Bearer ' + str("token")})
    # Request body
    body = {
        "fromTime": "2013-03-01T13:15:06.456",
        "maxSize": "2"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def get_completed_records_post_request_with_invalid_url(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//invalid_getCompleted//List_Completed.txt//Camp_1"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "fromTime": "2013-03-01T13:15:06.456",
        "maxSize": "2"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


#@pytest.fixture(scope='class')
#def get_completed_records_post_request_to_the_non_existent_list(get_user_token):
#    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//getCompleted//invalid_List_Completed.txt//Camp_1"
#    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
#    # Request body
#    body = {
#        "fromTime": "2013-03-01T13:15:06.456",
#        "maxSize": "2"
#    }
#    # Convert body request to json
#    request_body = json.dumps(body)
#    print("request_url : ", request_url)
#    print("request_body : ", request_body)
#    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def get_completed_records_post_request_with_invalid_fromtime_value_fromtime_alphabetical(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//getCompleted//List_Completed.txt//Camp_1"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "fromTime": "ab",
        "maxSize": "2"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def get_completed_records_post_request_with_invalid_maxsize_value_maxsize_alphabetical(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//getCompleted//List_Completed.txt//Camp_1"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "fromTime": "2013-03-01T13:15:06.456",
        "maxSize": "ab"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def get_completed_records_post_request_with_authorize_session_for_user_without_permission(get_user_without_permission_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//getCompleted//List_Completed.txt//Camp_1"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_without_permission_token)})
    # Request body
    body = {
        "fromTime": "2013-03-01T13:15:06.456",
        "maxSize": "2"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def get_completed_records_get_request_with_correct_body(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//getCompleted//List_Completed.txt//Camp_1"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "fromTime": "2013-03-01T13:15:06.456",
        "maxSize": "2"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.get(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def get_completed_records_put_request_with_correct_body(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//getCompleted//List_Completed.txt//Camp_1"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "fromTime": "2013-03-01T13:15:06.456",
        "maxSize": "2"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.put(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def get_completed_records_delete_request_with_correct_body(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//getCompleted//List_Completed.txt//Camp_1"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "fromTime": "2013-03-01T13:15:06.456",
        "maxSize": "2"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.delete(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def get_completed_records_post_request_with_incorrect_body_format_typization(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//getCompleted//List_Completed.txt//Camp_1"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    request_body = bytes('{"fromTime": "2013-03-01T13:15:06.456","maxSize: 2"}', 'utf-8')
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def get_updated_records_post_request_with_valid_list_campaign_fromtime_and_maxsize_3(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//getChanged//List_Completed.txt//Camp_1"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "fromTime": "2003-03-01T13:15:06.456",
        "maxSize": "3"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)


@pytest.fixture(scope='class')
def get_updated_records_post_request_with_valid_list_campaign_fromtime_and_maxsize_1(get_user_token):
    request_url = "https://" + DOMAIN + "//configapi//v2//callinglist//getChanged//List_Completed.txt//Camp_1"
    HEADERS.update({'Authorization': 'Bearer ' + str(get_user_token)})
    # Request body
    body = {
        "fromTime": "2003-03-01T13:15:06.456",
        "maxSize": "1"
    }
    # Convert body request to json
    request_body = json.dumps(body)
    print("request_url : ", request_url)
    print("request_body : ", request_body)
    return requests.post(request_url, data=request_body, headers=HEADERS)