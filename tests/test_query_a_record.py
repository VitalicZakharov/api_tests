import pytest
import allure

#=======================================================================================================================
#==================================================== Code 200 =========================================================
#=======================================================================================================================

# @allure.issue("https://trac.brightpattern.com/ticket/24242")
@pytest.mark.usefixtures("query_a_record_post_request_with_an_existent_campaign_for_non_completed_record")
class Test_post_request_with_an_existent_campaign_for_non_completed_record():
    @allure.epic("test_query_a_record")
    @allure.feature("answer code 200")
    @allure.step('test_check_status_code_post_request_with_an_existent_campaign_for_non_completed_record')
    def test_check_status_code_post_request_with_an_existent_campaign_for_non_completed_record(self, query_a_record_post_request_with_an_existent_campaign_for_non_completed_record):
        print("request_result_status_code : ", query_a_record_post_request_with_an_existent_campaign_for_non_completed_record.status_code)
        assert "200" in str(
            query_a_record_post_request_with_an_existent_campaign_for_non_completed_record.status_code), "Answer status not 200 ; actual status code : " + str(
            query_a_record_post_request_with_an_existent_campaign_for_non_completed_record.status_code)

    @allure.epic("test_query_a_record")
    @allure.feature("answer code 200")
    @allure.step('test_check_answer_text_post_request_with_an_existent_campaign_for_non_completed_record')
    def test_check_answer_text_post_request_with_an_existent_campaign_for_non_completed_record(self, query_a_record_post_request_with_an_existent_campaign_for_non_completed_record):
        print("request_result_text : ", query_a_record_post_request_with_an_existent_campaign_for_non_completed_record.text)
        status = '{"entry":{"last name":"Name_Last1","first name":"Name_First1","agent id":"Test.1","phone2":"8000","date/time":"02-07-2027","caller id":"Test1","integer":"1234568","phone1":"6000"},"status":{"totalAttempts":0,"completed":false}}'
        assert status in str(
            query_a_record_post_request_with_an_existent_campaign_for_non_completed_record.text), "Answer text not " + status + " ; actual message : " + str(
            query_a_record_post_request_with_an_existent_campaign_for_non_completed_record.text)


# @allure.issue("https://trac.brightpattern.com/ticket/24242")
@pytest.mark.usefixtures("query_a_record_post_request_with_an_existent_campaign_for_completed_record")
class Test_post_request_with_an_existent_campaign_for_completed_record():
    @allure.epic("test_query_a_record")
    @allure.feature("answer code 200")
    @allure.step('test_check_status_code_post_request_with_an_existent_campaign_for_completed_record')
    def test_check_status_code_post_request_with_an_existent_campaign_for_completed_record(self, query_a_record_post_request_with_an_existent_campaign_for_completed_record):
        print("request_result_status_code : ", query_a_record_post_request_with_an_existent_campaign_for_completed_record.status_code)
        assert "200" in str(
            query_a_record_post_request_with_an_existent_campaign_for_completed_record.status_code), "Answer status not 200 ; actual status code : " + str(
            query_a_record_post_request_with_an_existent_campaign_for_completed_record.status_code)

    @allure.epic("test_query_a_record")
    @allure.feature("answer code 200")
    @allure.step('test_check_answer_text_post_request_with_an_existent_campaign_for_completed_record')
    def test_check_answer_text_post_request_with_an_existent_campaign_for_completed_record(self, query_a_record_post_request_with_an_existent_campaign_for_completed_record):
        print("request_result_text : ", query_a_record_post_request_with_an_existent_campaign_for_completed_record.text)
        status = '{"entry":{"last name":"Name_Last_C1","first name":"Name_First_C1","agent id":"Test.C1","phone2":"8005","date/time":"07-07-2071","caller id":"101","integer":"1","phone1":"7005"},"status":{"totalAttempts":0,"completed":false}}'
        assert status in str(
            query_a_record_post_request_with_an_existent_campaign_for_completed_record.text), "Answer text not " + status + " ; actual message : " + str(
            query_a_record_post_request_with_an_existent_campaign_for_completed_record.text)


@allure.issue("https://trac.brightpattern.com/ticket/22667")
@pytest.mark.usefixtures("query_a_record_post_request_with_a_non_existent_campaign")
class Test_post_request_with_a_non_existent_campaign():
    @allure.epic("test_query_a_record")
    @allure.feature("answer code 200")
    @allure.step('test_check_status_code_post_request_with_a_non_existent_campaign')
    def test_check_status_code_post_request_with_a_non_existent_campaign(self, query_a_record_post_request_with_a_non_existent_campaign):
        print("request_result_status_code : ", query_a_record_post_request_with_a_non_existent_campaign.status_code)
        assert "200" in str(
            query_a_record_post_request_with_a_non_existent_campaign.status_code), "Answer status not 200 ; actual status code : " + str(
            query_a_record_post_request_with_a_non_existent_campaign.status_code)

    @allure.epic("test_query_a_record")
    @allure.feature("answer code 200")
    @allure.step('test_check_answer_text_post_request_with_a_non_existent_campaign')
    def test_check_answer_text_post_request_with_a_non_existent_campaign(self, query_a_record_post_request_with_a_non_existent_campaign):
        print("request_result_text : ", query_a_record_post_request_with_a_non_existent_campaign.text)
        status = '{"entry":{"last name":"Name_Last0","first name":"Name_First0","agent id":"Test.0","phone2":"8000","date/time":"03-07-2027","caller id":"Test0","integer":"1234567","phone1":"7000","Completed":"#22667"}}'
        assert status in str(
            query_a_record_post_request_with_a_non_existent_campaign.text), "Answer text not " + status + " ; actual message : " + str(
            query_a_record_post_request_with_a_non_existent_campaign.text)


@pytest.mark.usefixtures("query_a_record_post_request_without_a_last_name_parameter")
class Test_post_request_without_a_last_name_parameter():
    @allure.epic("test_query_a_record")
    @allure.feature("answer code 200")
    @allure.step('test_check_status_code_post_request_without_a_last_name_parameter')
    def test_check_status_code_post_request_without_a_last_name_parameter(self, query_a_record_post_request_without_a_last_name_parameter):
        print("request_result_status_code : ", query_a_record_post_request_without_a_last_name_parameter.status_code)
        assert "200" in str(
            query_a_record_post_request_without_a_last_name_parameter.status_code), "Answer status not 200 ; actual status code : " + str(
            query_a_record_post_request_without_a_last_name_parameter.status_code)

    @allure.epic("test_query_a_record")
    @allure.feature("answer code 200")
    @allure.step('test_check_answer_text_post_request_without_a_last_name_parameter')
    def test_check_answer_text_post_request_without_a_last_name_parameter(self, query_a_record_post_request_without_a_last_name_parameter):
        print("request_result_text : ", query_a_record_post_request_without_a_last_name_parameter.text)
#        status = '{"entry":{"last name":"User1","first name":"Test1","phone":"1001","date/time":"","integer":""}}'
        status = '{"entry":{"last name":"Updatelistrequest","first name":"Test1","phone":"+1001","date/time":"","integer":"789"}}'
        assert status in str(
            query_a_record_post_request_without_a_last_name_parameter.text), "Answer text not " + status + " ; actual message : " + str(
            query_a_record_post_request_without_a_last_name_parameter.text)


@pytest.mark.usefixtures("query_a_record_post_request_with_a_redundant_field")
class Test_post_request_with_a_redundant_field():
    @allure.epic("test_query_a_record")
    @allure.feature("answer code 200")
    @allure.step('test_check_status_code_post_request_with_a_redundant_field')
    def test_check_status_code_post_request_with_a_redundant_field(self, query_a_record_post_request_with_a_redundant_field):
        print("request_result_status_code : ", query_a_record_post_request_with_a_redundant_field.status_code)
        assert "200" in str(
            query_a_record_post_request_with_a_redundant_field.status_code), "Answer status not 200 ; actual status code : " + str(
            query_a_record_post_request_with_a_redundant_field.status_code)

    @allure.epic("test_query_a_record")
    @allure.feature("answer code 200")
    @allure.step('test_check_answer_text_post_request_with_a_redundant_field')
    def test_check_answer_text_post_request_with_a_redundant_field(self, query_a_record_post_request_with_a_redundant_field):
        print("request_result_text : ", query_a_record_post_request_with_a_redundant_field.text)
#        status = '{"entry":{"last name":"User1","first name":"Test1","phone":"1001","date/time":"","integer":""}}'
        status = '{"entry":{"last name":"Updatelistrequest","first name":"Test1","phone":"+1001","date/time":"","integer":"789"}}'
        assert status in str(
            query_a_record_post_request_with_a_redundant_field.text), "Answer text not " + status + " ; actual message : " + str(
            query_a_record_post_request_with_a_redundant_field.text)


@pytest.mark.usefixtures("query_a_record_post_request_with_with_incorrectly_formatted_value_in_an_integer_field")
class Test_post_request_with_with_incorrectly_formatted_value_in_an_integer_field():
    @allure.epic("test_query_a_record")
    @allure.feature("answer code 200")
    @allure.step('test_check_status_code_post_request_with_with_incorrectly_formatted_value_in_an_integer_field')
    def test_check_status_code_post_request_with_with_incorrectly_formatted_value_in_an_integer_field(self, query_a_record_post_request_with_with_incorrectly_formatted_value_in_an_integer_field):
        print("request_result_status_code : ", query_a_record_post_request_with_with_incorrectly_formatted_value_in_an_integer_field.status_code)
        assert "200" in str(
            query_a_record_post_request_with_with_incorrectly_formatted_value_in_an_integer_field.status_code), "Answer status not 200 ; actual status code : " + str(
            query_a_record_post_request_with_with_incorrectly_formatted_value_in_an_integer_field.status_code)

    @allure.epic("test_query_a_record")
    @allure.feature("answer code 200")
    @allure.step('test_check_answer_text_post_request_with_with_incorrectly_formatted_value_in_an_integer_field')
    def test_check_answer_text_post_request_with_with_incorrectly_formatted_value_in_an_integer_field(self, query_a_record_post_request_with_with_incorrectly_formatted_value_in_an_integer_field):
        print("request_result_text : ", query_a_record_post_request_with_with_incorrectly_formatted_value_in_an_integer_field.text)
#        status = '{"entry":{"last name":"User1","first name":"Test1","phone":"1001","date/time":"","integer":""}}'
        status = '{"entry":{"last name":"Updatelistrequest","first name":"Test1","phone":"+1001","date/time":"","integer":"789"}}'
        assert status in str(
            query_a_record_post_request_with_with_incorrectly_formatted_value_in_an_integer_field.text), "Answer text not " + status + " ; actual message : " + str(
            query_a_record_post_request_with_with_incorrectly_formatted_value_in_an_integer_field.text)


@pytest.mark.usefixtures("query_a_record_post_request_with_an_empty_key_last_name")
class Test_post_request_with_an_empty_key_last_name():
    @allure.epic("test_query_a_record")
    @allure.feature("answer code 200")
    @allure.step('test_check_status_code_post_request_with_an_empty_key_last_name')
    def test_check_status_code_post_request_with_an_empty_key_last_name(self, query_a_record_post_request_with_an_empty_key_last_name):
        print("request_result_status_code : ", query_a_record_post_request_with_an_empty_key_last_name.status_code)
        assert "200" in str(
            query_a_record_post_request_with_an_empty_key_last_name.status_code), "Answer status not 200 ; actual status code : " + str(
            query_a_record_post_request_with_an_empty_key_last_name.status_code)

    @allure.epic("test_query_a_record")
    @allure.feature("answer code 200")
    @allure.step('test_check_answer_text_post_request_with_an_empty_key_last_name')
    def test_check_answer_text_post_request_with_an_empty_key_last_name(self, query_a_record_post_request_with_an_empty_key_last_name):
        print("request_result_text : ", query_a_record_post_request_with_an_empty_key_last_name.text)
        status = '{"entry":{"last name":"Name_Last_C1","first name":"Name_First_C1","agent id":"Test.C1","phone2":"8005","date/time":"07-07-2071","caller id":"101","integer":"1","phone1":"7005"},"status":{"totalAttempts":0,"completed":false}}'
        assert status in str(
            query_a_record_post_request_with_an_empty_key_last_name.text), "Answer text not " + status + " ; actual message : " + str(
            query_a_record_post_request_with_an_empty_key_last_name.text)

#=======================================================================================================================
#=======================================================================================================================
#=======================================================================================================================

#=======================================================================================================================
#==================================================== Code 404 =========================================================
#=======================================================================================================================

@pytest.mark.usefixtures("query_a_record_post_request_with_a_non_existent_record_key")
class Test_post_request_with_a_non_existent_record_key():
    @allure.epic("test_query_a_record")
    @allure.feature("answer code 404")
    @allure.step('test_check_status_code_post_request_with_a_non_existent_record_key')
    def test_check_status_code_post_request_with_a_non_existent_record_key(self, query_a_record_post_request_with_a_non_existent_record_key):
        print("request_result_status_code : ", query_a_record_post_request_with_a_non_existent_record_key.status_code)
        assert "404" in str(
            query_a_record_post_request_with_a_non_existent_record_key.status_code), "Answer status not 404 ; actual status code : " + str(
            query_a_record_post_request_with_a_non_existent_record_key.status_code)

    @allure.epic("test_query_a_record")
    @allure.feature("answer code 404")
    @allure.step('test_check_answer_text_post_request_with_a_non_existent_record_key')
    def test_check_answer_text_post_request_with_a_non_existent_record_key(self, query_a_record_post_request_with_a_non_existent_record_key):
        print("request_result_text : ", query_a_record_post_request_with_a_non_existent_record_key.text)
        status = 'record is not found'
        assert status in str(
            query_a_record_post_request_with_a_non_existent_record_key.text), "Answer text not " + status + " ; actual message : " + str(
            query_a_record_post_request_with_a_non_existent_record_key.text)


@pytest.mark.usefixtures("query_a_record_post_request_with_a_wrong_key_phone_parameter")
class Test_post_request_with_a_wrong_key_phone_parameter():
    @allure.epic("test_query_a_record")
    @allure.feature("answer code 404")
    @allure.step('test_check_status_code_post_request_with_a_wrong_key_phone_parameter')
    def test_check_status_code_post_request_with_a_wrong_key_phone_parameter(self, query_a_record_post_request_with_a_wrong_key_phone_parameter):
        print("request_result_status_code : ", query_a_record_post_request_with_a_wrong_key_phone_parameter.status_code)
        assert "404" in str(
            query_a_record_post_request_with_a_wrong_key_phone_parameter.status_code), "Answer status not 404 ; actual status code : " + str(
            query_a_record_post_request_with_a_wrong_key_phone_parameter.status_code)

    @allure.epic("test_query_a_record")
    @allure.feature("answer code 404")
    @allure.step('test_check_answer_text_post_request_with_a_wrong_key_phone_parameter')
    def test_check_answer_text_post_request_with_a_wrong_key_phone_parameter(self, query_a_record_post_request_with_a_wrong_key_phone_parameter):
        print("request_result_text : ", query_a_record_post_request_with_a_wrong_key_phone_parameter.text)
        status = 'record is not found'
        assert status in str(
            query_a_record_post_request_with_a_wrong_key_phone_parameter.text), "Answer text not " + status + " ; actual message : " + str(
            query_a_record_post_request_with_a_wrong_key_phone_parameter.text)

@allure.issue("https://trac.brightpattern.com/ticket/24743")
@pytest.mark.usefixtures("query_a_record_post_request_with_a_wrong_key_first_name_parameter")
class Test_post_request_with_a_wrong_key_first_name_parameter():
    @allure.epic("test_query_a_record")
    @allure.feature("answer code 404")
    @allure.step('test_check_status_code_post_request_with_a_wrong_key_first_name_parameter')
    def test_check_status_code_post_request_with_a_wrong_key_first_name_parameter(self, query_a_record_post_request_with_a_wrong_key_first_name_parameter):
        print("request_result_status_code : ", query_a_record_post_request_with_a_wrong_key_first_name_parameter.status_code)
        assert "404" in str(
            query_a_record_post_request_with_a_wrong_key_first_name_parameter.status_code), "Answer status not 404 ; actual status code : " + str(
            query_a_record_post_request_with_a_wrong_key_first_name_parameter.status_code)

    @allure.epic("test_query_a_record")
    @allure.feature("answer code 404")
    @allure.step('test_check_answer_text_post_request_with_a_wrong_key_first_name_parameter')
    def test_check_answer_text_post_request_with_a_wrong_key_first_name_parameter(self, query_a_record_post_request_with_a_wrong_key_first_name_parameter):
        print("request_result_text : ", query_a_record_post_request_with_a_wrong_key_first_name_parameter.text)
        status = 'record is not found'
        assert status in str(
            query_a_record_post_request_with_a_wrong_key_first_name_parameter.text), "Answer text not " + status + " ; actual message : " + str(
            query_a_record_post_request_with_a_wrong_key_first_name_parameter.text)


@allure.issue("https://trac.brightpattern.com/ticket/24751")
@pytest.mark.usefixtures("query_a_record_post_request_with_incorrect_body_format_delete_some_quotes")
class Test_post_request_with_incorrect_body_format_delete_some_quotes():
    @allure.epic("test_query_a_record")
    @allure.feature("answer code 404")
    @allure.step('test_check_status_code_post_request_with_incorrect_body_format_delete_some_quotes')
    def test_check_status_code_post_request_with_incorrect_body_format_delete_some_quotes(self, query_a_record_post_request_with_incorrect_body_format_delete_some_quotes):
        print("request_result_status_code : ", query_a_record_post_request_with_incorrect_body_format_delete_some_quotes.status_code)
        assert "404" in str(
            query_a_record_post_request_with_incorrect_body_format_delete_some_quotes.status_code), "Answer status not 404 ; actual status code : " + str(
            query_a_record_post_request_with_incorrect_body_format_delete_some_quotes.status_code)

    @allure.epic("test_query_a_record")
    @allure.feature("answer code 404")
    @allure.step('test_check_answer_text_post_request_with_incorrect_body_format_delete_some_quotes')
    def test_check_answer_text_post_request_with_incorrect_body_format_delete_some_quotes(self, query_a_record_post_request_with_incorrect_body_format_delete_some_quotes):
        print("request_result_text : ", query_a_record_post_request_with_incorrect_body_format_delete_some_quotes.text)
        status = 'record is not found'
        assert status in str(
            query_a_record_post_request_with_incorrect_body_format_delete_some_quotes.text), "Answer text not " + status + " ; actual message : " + str(
            query_a_record_post_request_with_incorrect_body_format_delete_some_quotes.text)


@pytest.mark.usefixtures("query_a_record_post_request_to_the_non_existent_list")
class Test_post_request_to_the_non_existent_list():
    @allure.epic("test_query_a_record")
    @allure.feature("answer code 404")
    @allure.step('test_check_status_code_post_request_to_the_non_existent_list')
    def test_check_status_code_post_request_to_the_non_existent_list(self, query_a_record_post_request_to_the_non_existent_list):
        print("request_result_status_code : ", query_a_record_post_request_to_the_non_existent_list.status_code)
        assert "404" in str(
            query_a_record_post_request_to_the_non_existent_list.status_code), "Answer status not 404 ; actual status code : " + str(
            query_a_record_post_request_to_the_non_existent_list.status_code)

    @allure.epic("test_query_a_record")
    @allure.feature("answer code 404")
    @allure.step('test_check_answer_text_post_request_to_the_non_existent_list')
    def test_check_answer_text_post_request_to_the_non_existent_list(self, query_a_record_post_request_to_the_non_existent_list):
        print("request_result_text : ", query_a_record_post_request_to_the_non_existent_list.text)
        status = 'calling list not found'
        assert status in str(
            query_a_record_post_request_to_the_non_existent_list.text), "Answer text not " + status + " ; actual message : " + str(
            query_a_record_post_request_to_the_non_existent_list.text)


@pytest.mark.usefixtures("query_a_record_post_request_with_invalid_url")
class Test_post_request_with_invalid_url():
    @allure.epic("test_query_a_record")
    @allure.feature("answer code 404")
    @allure.step('test_check_status_code_post_request_with_invalid_url')
    def test_check_status_code_post_request_with_invalid_url(self, query_a_record_post_request_with_invalid_url):
        print("request_result_status_code : ", query_a_record_post_request_with_invalid_url.status_code)
        assert "404" in str(
            query_a_record_post_request_with_invalid_url.status_code), "Answer status not 404 ; actual status code : " + str(
            query_a_record_post_request_with_invalid_url.status_code)

    @allure.epic("test_query_a_record")
    @allure.feature("answer code 404")
    @allure.step('test_check_answer_text_post_request_with_invalid_url')
    def test_check_answer_text_post_request_with_invalid_url(self, query_a_record_post_request_with_invalid_url):
        print("request_result_text : ", query_a_record_post_request_with_invalid_url.text)
        status = 'HTTP 404 Not Found'
        assert status in str(
            query_a_record_post_request_with_invalid_url.text), "Answer text not " + status + " ; actual message : " + str(
            query_a_record_post_request_with_invalid_url.text)


@pytest.mark.usefixtures("query_a_record_post_request_with_the_incorrectly_formatted_value_phone_number_in_a_phone_field_non_numeric_symbol_other_than_plus")
class Test_post_request_with_the_incorrectly_formatted_value_phone_number_in_a_phone_field_non_numeric_symbol_other_than_plus():
    @allure.epic("test_query_a_record")
    @allure.feature("answer code 404")
    @allure.step('test_check_status_code_post_request_with_the_incorrectly_formatted_value_phone_number_in_a_phone_field_non_numeric_symbol_other_than_plus')
    def test_check_status_code_post_request_with_the_incorrectly_formatted_value_phone_number_in_a_phone_field_non_numeric_symbol_other_than_plus(self, query_a_record_post_request_with_the_incorrectly_formatted_value_phone_number_in_a_phone_field_non_numeric_symbol_other_than_plus):
        print("request_result_status_code : ", query_a_record_post_request_with_the_incorrectly_formatted_value_phone_number_in_a_phone_field_non_numeric_symbol_other_than_plus.status_code)
        assert "404" in str(
            query_a_record_post_request_with_the_incorrectly_formatted_value_phone_number_in_a_phone_field_non_numeric_symbol_other_than_plus.status_code), "Answer status not 404 ; actual status code : " + str(
            query_a_record_post_request_with_the_incorrectly_formatted_value_phone_number_in_a_phone_field_non_numeric_symbol_other_than_plus.status_code)

    @allure.epic("test_query_a_record")
    @allure.feature("answer code 404")
    @allure.step('test_check_answer_text_post_request_with_the_incorrectly_formatted_value_phone_number_in_a_phone_field_non_numeric_symbol_other_than_plus')
    def test_check_answer_text_post_request_with_the_incorrectly_formatted_value_phone_number_in_a_phone_field_non_numeric_symbol_other_than_plus(self, query_a_record_post_request_with_the_incorrectly_formatted_value_phone_number_in_a_phone_field_non_numeric_symbol_other_than_plus):
        print("request_result_text : ", query_a_record_post_request_with_the_incorrectly_formatted_value_phone_number_in_a_phone_field_non_numeric_symbol_other_than_plus.text)
        status = 'record is not found'
        assert status in str(
            query_a_record_post_request_with_the_incorrectly_formatted_value_phone_number_in_a_phone_field_non_numeric_symbol_other_than_plus.text), "Answer text not " + status + " ; actual message : " + str(
            query_a_record_post_request_with_the_incorrectly_formatted_value_phone_number_in_a_phone_field_non_numeric_symbol_other_than_plus.text)


@allure.issue("https://trac.brightpattern.com/ticket/24753")
@pytest.mark.usefixtures("query_a_record_post_request_with_the_value_phone_number_in_a_phone_field_using_symbol_plus")
class Test_post_request_with_the_value_phone_number_in_a_phone_field_using_symbol_plus():
    @allure.epic("test_query_a_record")
    @allure.feature("answer code 404")
    @allure.step('test_check_status_code_post_request_with_the_value_phone_number_in_a_phone_field_using_symbol_plus')
    def test_check_status_code_post_request_with_the_value_phone_number_in_a_phone_field_using_symbol_plus(self, query_a_record_post_request_with_the_value_phone_number_in_a_phone_field_using_symbol_plus):
        print("request_result_status_code : ", query_a_record_post_request_with_the_value_phone_number_in_a_phone_field_using_symbol_plus.status_code)
        assert "404" in str(
            query_a_record_post_request_with_the_value_phone_number_in_a_phone_field_using_symbol_plus.status_code), "Answer status not 404 ; actual status code : " + str(
            query_a_record_post_request_with_the_value_phone_number_in_a_phone_field_using_symbol_plus.status_code)

    @allure.epic("test_query_a_record")
    @allure.feature("answer code 404")
    @allure.step('test_check_answer_text_post_request_with_the_value_phone_number_in_a_phone_field_using_symbol_plus')
    def test_check_answer_text_post_request_with_the_value_phone_number_in_a_phone_field_using_symbol_plus(self, query_a_record_post_request_with_the_value_phone_number_in_a_phone_field_using_symbol_plus):
        print("request_result_text : ", query_a_record_post_request_with_the_value_phone_number_in_a_phone_field_using_symbol_plus.text)
        status = 'record is not found'
        assert status in str(
            query_a_record_post_request_with_the_value_phone_number_in_a_phone_field_using_symbol_plus.text), "Answer text not " + status + " ; actual message : " + str(
            query_a_record_post_request_with_the_value_phone_number_in_a_phone_field_using_symbol_plus.text)

#=======================================================================================================================
#=======================================================================================================================
#=======================================================================================================================

#=======================================================================================================================
#==================================================== Code 400 =========================================================
#=======================================================================================================================

@allure.issue("https://trac.brightpattern.com/ticket/24743")
@pytest.mark.usefixtures("query_a_record_post_request_with_an_empty_key_first_name")
class Test_post_request_with_an_empty_key_first_name():
    @allure.epic("test_query_a_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_status_code_post_request_with_an_empty_key_first_name')
    def test_check_status_code_post_request_with_an_empty_key_first_name(self, query_a_record_post_request_with_an_empty_key_first_name):
        print("request_result_status_code : ", query_a_record_post_request_with_an_empty_key_first_name.status_code)
        assert "400" in str(
            query_a_record_post_request_with_an_empty_key_first_name.status_code), "Answer status not 400 ; actual status code : " + str(
            query_a_record_post_request_with_an_empty_key_first_name.status_code)

    @allure.epic("test_query_a_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_answer_text_post_request_with_an_empty_key_first_name')
    def test_check_answer_text_post_request_with_an_empty_key_first_name(self, query_a_record_post_request_with_an_empty_key_first_name):
        print("request_result_text : ", query_a_record_post_request_with_an_empty_key_first_name.text)
        status = 'missing key: first_name'
        assert status in str(
            query_a_record_post_request_with_an_empty_key_first_name.text), "Answer text not " + status + " ; actual message : " + str(
            query_a_record_post_request_with_an_empty_key_first_name.text)


@pytest.mark.usefixtures("query_a_record_post_request_with_an_empty_key_phone")
class Test_post_request_with_an_empty_key_phone():
    @allure.epic("test_query_a_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_status_code_post_request_with_an_empty_key_phone')
    def test_check_status_code_post_request_with_an_empty_key_phone(self, query_a_record_post_request_with_an_empty_key_phone):
        print("request_result_status_code : ", query_a_record_post_request_with_an_empty_key_phone.status_code)
        assert "400" in str(
            query_a_record_post_request_with_an_empty_key_phone.status_code), "Answer status not 400 ; actual status code : " + str(
            query_a_record_post_request_with_an_empty_key_phone.status_code)

    @allure.epic("test_query_a_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_answer_text_post_request_with_an_empty_key_phone')
    def test_check_answer_text_post_request_with_an_empty_key_phone(self, query_a_record_post_request_with_an_empty_key_phone):
        print("request_result_text : ", query_a_record_post_request_with_an_empty_key_phone.text)
        status = 'missing key: phone1'
        assert status in str(
            query_a_record_post_request_with_an_empty_key_phone.text), "Answer text not " + status + " ; actual message : " + str(
            query_a_record_post_request_with_an_empty_key_phone.text)


@pytest.mark.usefixtures("query_a_record_post_request_with_phone_key_field_as_space")
class Test_post_request_with_phone_key_field_as_space():
    @allure.epic("test_query_a_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_status_code_post_request_with_phone_key_field_as_space')
    def test_check_status_code_post_request_with_phone_key_field_as_space(self, query_a_record_post_request_with_phone_key_field_as_space):
        print("request_result_status_code : ", query_a_record_post_request_with_phone_key_field_as_space.status_code)
        assert "400" in str(
            query_a_record_post_request_with_phone_key_field_as_space.status_code), "Answer status not 400 ; actual status code : " + str(
            query_a_record_post_request_with_phone_key_field_as_space.status_code)

    @allure.epic("test_query_a_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_answer_text_post_request_with_phone_key_field_as_space')
    def test_check_answer_text_post_request_with_phone_key_field_as_space(self, query_a_record_post_request_with_phone_key_field_as_space):
        print("request_result_text : ", query_a_record_post_request_with_phone_key_field_as_space.text)
        status = 'missing key: phone1'
        assert status in str(
            query_a_record_post_request_with_phone_key_field_as_space.text), "Answer text not " + status + " ; actual message : " + str(
            query_a_record_post_request_with_phone_key_field_as_space.text)


@pytest.mark.usefixtures("query_a_record_post_request_without_parameters")
class Test_post_request_without_parameters():
    @allure.epic("test_query_a_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_status_code_post_request_without_parameters')
    def test_check_status_code_post_request_without_parameters(self, query_a_record_post_request_without_parameters):
        print("request_result_status_code : ", query_a_record_post_request_without_parameters.status_code)
        assert "400" in str(
            query_a_record_post_request_without_parameters.status_code), "Answer status not 400 ; actual status code : " + str(
            query_a_record_post_request_without_parameters.status_code)

    @allure.epic("test_query_a_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_answer_text_post_request_without_parameters')
    def test_check_answer_text_post_request_without_parameters(self, query_a_record_post_request_without_parameters):
        print("request_result_text : ", query_a_record_post_request_without_parameters.text)
        status = 'missing key: phone'
        assert status in str(
            query_a_record_post_request_without_parameters.text), "Answer text not " + status + " ; actual message : " + str(
            query_a_record_post_request_without_parameters.text)


@pytest.mark.usefixtures("query_a_record_post_request_without_a_key_phone_parameter")
class Test_post_request_without_a_key_phone_parameter():
    @allure.epic("test_query_a_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_status_code_post_request_without_a_key_phone_parameter')
    def test_check_status_code_post_request_without_a_key_phone_parameter(self, query_a_record_post_request_without_a_key_phone_parameter):
        print("request_result_status_code : ", query_a_record_post_request_without_a_key_phone_parameter.status_code)
        assert "400" in str(
            query_a_record_post_request_without_a_key_phone_parameter.status_code), "Answer status not 400 ; actual status code : " + str(
            query_a_record_post_request_without_a_key_phone_parameter.status_code)

    @allure.epic("test_query_a_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_answer_text_post_request_without_a_key_phone_parameter')
    def test_check_answer_text_post_request_without_a_key_phone_parameter(self, query_a_record_post_request_without_a_key_phone_parameter):
        print("request_result_text : ", query_a_record_post_request_without_a_key_phone_parameter.text)
        status = 'missing key: phone'
        assert status in str(
            query_a_record_post_request_without_a_key_phone_parameter.text), "Answer text not " + status + " ; actual message : " + str(
            query_a_record_post_request_without_a_key_phone_parameter.text)


@allure.issue("https://trac.brightpattern.com/ticket/24743")
@pytest.mark.usefixtures("query_a_record_post_request_without_a_key_first_name_parameter")
class Test_post_request_without_a_key_first_name_parameter():
    @allure.epic("test_query_a_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_status_code_post_request_without_a_key_first_name_parameter')
    def test_check_status_code_post_request_without_a_key_first_name_parameter(self, query_a_record_post_request_without_a_key_first_name_parameter):
        print("request_result_status_code : ", query_a_record_post_request_without_a_key_first_name_parameter.status_code)
        assert "400" in str(
            query_a_record_post_request_without_a_key_first_name_parameter.status_code), "Answer status not 400 ; actual status code : " + str(
            query_a_record_post_request_without_a_key_first_name_parameter.status_code)

    @allure.epic("test_query_a_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_answer_text_post_request_without_a_key_first_name_parameter')
    def test_check_answer_text_post_request_without_a_key_first_name_parameter(self, query_a_record_post_request_without_a_key_first_name_parameter):
        print("request_result_text : ", query_a_record_post_request_without_a_key_first_name_parameter.text)
        status = 'missing key: first name'
        assert status in str(
            query_a_record_post_request_without_a_key_first_name_parameter.text), "Answer text not " + status + " ; actual message : " + str(
            query_a_record_post_request_without_a_key_first_name_parameter.text)


#@allure.issue("https://trac.brightpattern.com/ticket/24228")
@pytest.mark.usefixtures("query_a_record_post_request_with_incorrect_body_format_add_a_redudant_comma_in_the_end")
class Test_post_request_with_incorrect_body_format_add_a_redudant_comma_in_the_end():
    @allure.epic("test_query_a_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_status_code_post_request_with_incorrect_body_format_add_a_redudant_comma_in_the_end')
    def test_check_status_code_post_request_with_incorrect_body_format_add_a_redudant_comma_in_the_end(self, query_a_record_post_request_with_incorrect_body_format_add_a_redudant_comma_in_the_end):
        print("request_result_status_code : ", query_a_record_post_request_with_incorrect_body_format_add_a_redudant_comma_in_the_end.status_code)
        assert "400" in str(
            query_a_record_post_request_with_incorrect_body_format_add_a_redudant_comma_in_the_end.status_code), "Answer status not 400 ; actual status code : " + str(
            query_a_record_post_request_with_incorrect_body_format_add_a_redudant_comma_in_the_end.status_code)

    @allure.epic("test_query_a_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_answer_text_post_request_with_incorrect_body_format_add_a_redudant_comma_in_the_end')
    def test_check_answer_text_post_request_with_incorrect_body_format_add_a_redudant_comma_in_the_end(self, query_a_record_post_request_with_incorrect_body_format_add_a_redudant_comma_in_the_end):
        print("request_result_text : ", query_a_record_post_request_with_incorrect_body_format_add_a_redudant_comma_in_the_end.text)
        status = 'Expected name at line 1 column 64 path $'
        assert status in str(
            query_a_record_post_request_with_incorrect_body_format_add_a_redudant_comma_in_the_end.text), "Answer text not " + status + " ; actual message : " + str(
            query_a_record_post_request_with_incorrect_body_format_add_a_redudant_comma_in_the_end.text)

#=======================================================================================================================
#=======================================================================================================================
#=======================================================================================================================

#=======================================================================================================================
#==================================================== Code 401 =========================================================
#=======================================================================================================================

@pytest.mark.usefixtures("query_a_record_post_request_with_do_not_authorize_session")
class Test_post_request_with_do_not_authorize_session():
    @allure.epic("test_query_a_record")
    @allure.feature("answer code 401")
    @allure.step('test_check_status_code_post_request_with_do_not_authorize_session')
    def test_check_status_code_post_request_with_do_not_authorize_session(self,
                                                                          query_a_record_post_request_with_do_not_authorize_session):
        print("request_result_status_code : ", query_a_record_post_request_with_do_not_authorize_session.status_code)
        assert "401" in str(
            query_a_record_post_request_with_do_not_authorize_session.status_code), "Answer status not 401 ; actual status code : " + str(
            query_a_record_post_request_with_do_not_authorize_session.status_code)

    @allure.epic("test_query_a_record")
    @allure.feature("answer code 401")
    @allure.step('test_check_answer_text_post_request_with_do_not_authorize_session')
    def test_check_answer_text_post_request_with_do_not_authorize_session(self,
                                                                          query_a_record_post_request_with_do_not_authorize_session):
        print("request_result_text : ", query_a_record_post_request_with_do_not_authorize_session.text)
        status = "Session is not authenticated"
        assert status in str(
            query_a_record_post_request_with_do_not_authorize_session.text), "Answer text not " + status + " ; actual message : " + str(
            query_a_record_post_request_with_do_not_authorize_session.text)

#=======================================================================================================================
#=======================================================================================================================
#=======================================================================================================================

#=======================================================================================================================
#==================================================== Code 403 =========================================================
#=======================================================================================================================

#@allure.issue("https://trac.brightpattern.com/ticket/24588")
@pytest.mark.usefixtures("query_a_record_post_request_with_authorize_session_for_user_without_permission")
class Test_post_request_with_authorize_session_for_user_without_permission():
    @allure.epic("test_query_a_record")
    @allure.feature("answer code 403")
    @allure.step('test_check_status_code_post_request_with_authorize_session_for_user_without_permission')
    def test_check_status_code_post_request_with_authorize_session_for_user_without_permission(self,
                                                                                               query_a_record_post_request_with_authorize_session_for_user_without_permission):
        print("request_result_status_code : ", query_a_record_post_request_with_authorize_session_for_user_without_permission.status_code)
        assert "403" in str(
            query_a_record_post_request_with_authorize_session_for_user_without_permission.status_code), "Answer status not 403 ; actual status code : " + str(
            query_a_record_post_request_with_authorize_session_for_user_without_permission.status_code)

    @allure.epic("test_query_a_record")
    @allure.feature("answer code 403")
    @allure.step('test_check_answer_text_post_request_with_authorize_session_for_user_without_permission')
    def test_check_answer_text_post_request_with_authorize_session_for_user_without_permission(self,
                                                                                               query_a_record_post_request_with_authorize_session_for_user_without_permission):
        print("request_result_text : ", query_a_record_post_request_with_authorize_session_for_user_without_permission.text)
        status = "User authenticated but does not have sufficient privileges"
        assert status in str(
            query_a_record_post_request_with_authorize_session_for_user_without_permission.text), "Answer text not " + status + " ; actual message : " + str(
            query_a_record_post_request_with_authorize_session_for_user_without_permission.text)

#=======================================================================================================================
#=======================================================================================================================
#=======================================================================================================================

#=======================================================================================================================
#==================================================== Code 405 =========================================================
#=======================================================================================================================

#@allure.issue("https://trac.brightpattern.com/ticket/24265")
@pytest.mark.usefixtures("query_a_record_get_request_with_correct_body")
class Test_get_request_with_correct_body():
    @allure.epic("test_query_a_record")
    @allure.feature("answer code 405")
    @allure.step('test_check_status_code_get_request_with_correct_body')
    def test_check_status_code_get_request_with_correct_body(self, query_a_record_get_request_with_correct_body):
        print("request_result_status_code : ", query_a_record_get_request_with_correct_body.status_code)
        assert "405" in str(
            query_a_record_get_request_with_correct_body.status_code), "Answer status not 405 ; actual status code : " + str(
            query_a_record_get_request_with_correct_body.status_code)

    @allure.epic("test_query_a_record")
    @allure.feature("answer code 405")
    @allure.step('test_check_answer_text_get_request_with_correct_body')
    def test_check_answer_text_get_request_with_correct_body(self, query_a_record_get_request_with_correct_body):
        print("request_result_text : ", query_a_record_get_request_with_correct_body.text)
        status = "Method Not Allowed"
        assert status in str(
            query_a_record_get_request_with_correct_body.text), "Answer text not " + status + " ; actual message : " + str(
            query_a_record_get_request_with_correct_body.text)
        # assert len(str(get_request_with_correct_body.text)) == 0, "Answer text not empty ; actual message : " + str(get_request_with_correct_body.text)


#@allure.issue("https://trac.brightpattern.com/ticket/24265")
@pytest.mark.usefixtures("query_a_record_put_request_with_correct_body")
class Test_put_request_with_correct_body():
    @allure.epic("test_query_a_record")
    @allure.feature("answer code 405")
    @allure.step('test_check_status_code_put_request_with_correct_body')
    def test_check_status_code_put_request_with_correct_body(self, query_a_record_put_request_with_correct_body):
        print("request_result_status_code : ", query_a_record_put_request_with_correct_body.status_code)
        assert "405" in str(
            query_a_record_put_request_with_correct_body.status_code), "Answer status not 405 ; actual status code : " + str(
            query_a_record_put_request_with_correct_body.status_code)

    @allure.epic("test_query_a_record")
    @allure.feature("answer code 405")
    @allure.step('test_check_answer_text_put_request_with_correct_body')
    def test_check_answer_text_put_request_with_correct_body(self, query_a_record_put_request_with_correct_body):
        print("request_result_text : ", query_a_record_put_request_with_correct_body.text)
        status = "Method Not Allowed"
        assert status in str(
            query_a_record_put_request_with_correct_body.text), "Answer text not " + status + " ; actual message : " + str(
            query_a_record_put_request_with_correct_body.text)


#@allure.issue("https://trac.brightpattern.com/ticket/24265")
@pytest.mark.usefixtures("query_a_record_delete_request_with_correct_body")
class Test_delete_request_with_correct_body():
    @allure.epic("test_query_a_record")
    @allure.feature("answer code 405")
    @allure.step('test_check_status_code_delete_request_with_correct_body')
    def test_check_status_code_delete_request_with_correct_body(self, query_a_record_delete_request_with_correct_body):
        print("request_result_status_code : ", query_a_record_delete_request_with_correct_body.status_code)
        assert "405" in str(
            query_a_record_delete_request_with_correct_body.status_code), "Answer status not 405 ; actual status code : " + str(
            query_a_record_delete_request_with_correct_body.status_code)

    @allure.epic("test_query_a_record")
    @allure.feature("answer code 405")
    @allure.step('test_check_answer_text_delete_request_with_correct_body')
    def test_check_answer_text_delete_request_with_correct_body(self, query_a_record_delete_request_with_correct_body):
        print("request_result_text : ", query_a_record_delete_request_with_correct_body.text)
        status = "Method Not Allowed"
        assert status in str(
            query_a_record_delete_request_with_correct_body.text), "Answer text not " + status + " ; actual message : " + str(
            query_a_record_delete_request_with_correct_body.text)

#=======================================================================================================================
#=======================================================================================================================
#=======================================================================================================================