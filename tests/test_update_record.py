import pytest
import allure

# @allure.issue("https://trac.brightpattern.com/ticket/24242")
@pytest.mark.usefixtures("update_record_post_request_with_existent_record_key")
class Test_post_request_with_existent_record_key():
    @allure.epic("test_update_record")
    @allure.feature("answer code 200")
    @allure.step('test_check_status_code_post_request_with_existent_record_key')
    def test_check_status_code_post_request_with_existent_record_key(self, update_record_post_request_with_existent_record_key):
        print("request_result_status_code : ", update_record_post_request_with_existent_record_key.status_code)
        assert "200" in str(
            update_record_post_request_with_existent_record_key.status_code), "Answer status not 200 ; actual status code : " + str(
            update_record_post_request_with_existent_record_key.status_code)

    @allure.epic("test_update_record")
    @allure.feature("answer code 200")
    @allure.step('test_check_answer_text_post_request_with_existent_record_key')
    def test_check_answer_text_post_request_with_existent_record_key(self, update_record_post_request_with_existent_record_key):
        print("request_result_text : ", update_record_post_request_with_existent_record_key.text)
        assert len(str(
            update_record_post_request_with_existent_record_key.text)) == 0, "Answer text not empty ; actual message : " + str(
            update_record_post_request_with_existent_record_key.text)


@pytest.mark.usefixtures("update_record_post_request_with_a_non_existent_record_key")
class Test_post_request_with_a_non_existent_record_key():
    @allure.epic("test_update_record")
    @allure.feature("answer code 404")
    @allure.step('test_check_status_code_post_request_with_a_non_existent_record_key')
    def test_check_status_code_post_request_with_a_non_existent_record_key(self, update_record_post_request_with_a_non_existent_record_key):
        print("request_result_status_code : ", update_record_post_request_with_a_non_existent_record_key.status_code)
        assert "404" in str(
            update_record_post_request_with_a_non_existent_record_key.status_code), "Answer status not 404 ; actual status code : " + str(
            update_record_post_request_with_a_non_existent_record_key.status_code)

    @allure.epic("test_update_record")
    @allure.feature("answer code 404")
    @allure.step('test_check_answer_text_post_request_with_a_non_existent_record_key')
    def test_check_answer_text_post_request_with_a_non_existent_record_key(self, update_record_post_request_with_a_non_existent_record_key):
        print("request_result_text : ", update_record_post_request_with_a_non_existent_record_key.text)
        status = "record is not found"
        assert status in str(
            update_record_post_request_with_a_non_existent_record_key.text), "Answer text not " + status + " ; actual message : " + str(
            update_record_post_request_with_a_non_existent_record_key.text)


@allure.issue("https://trac.brightpattern.com/ticket/22527")
@pytest.mark.usefixtures("update_record_post_request_with_an_incorrect_integer_value")
class Test_post_request_with_an_incorrect_integer_value():
    @allure.epic("test_update_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_status_code_post_request_with_an_incorrect_integer_value')
    def test_check_status_code_post_request_with_an_incorrect_integer_value(self, update_record_post_request_with_an_incorrect_integer_value):
        print("request_result_status_code : ", update_record_post_request_with_an_incorrect_integer_value.status_code)
        assert "400" in str(
            update_record_post_request_with_an_incorrect_integer_value.status_code), "Answer status not 400 ; actual status code : " + str(
            update_record_post_request_with_an_incorrect_integer_value.status_code)

    @allure.epic("test_update_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_answer_text_post_request_with_an_incorrect_integer_value')
    def test_check_answer_text_post_request_with_an_incorrect_integer_value(self, update_record_post_request_with_an_incorrect_integer_value):
        print("request_result_text : ", update_record_post_request_with_an_incorrect_integer_value.text)
        status = 'For input string: "abc"'
        assert status in str(
            update_record_post_request_with_an_incorrect_integer_value.text), "Answer text not " + status + " ; actual message : " + str(
            update_record_post_request_with_an_incorrect_integer_value.text)


@allure.issue("https://trac.brightpattern.com/ticket/22524")
@pytest.mark.usefixtures("update_record_post_request_with_an_incorrect_date_time_value")
class Test_post_request_with_an_incorrect_date_time_value():
    @allure.epic("test_update_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_status_code_post_request_with_an_incorrect_date_time_value')
    def test_check_status_code_post_request_with_an_incorrect_date_time_value(self, update_record_post_request_with_an_incorrect_date_time_value):
        print("request_result_status_code : ", update_record_post_request_with_an_incorrect_date_time_value.status_code)
        assert "400" in str(
            update_record_post_request_with_an_incorrect_date_time_value.status_code), "Answer status not 400 ; actual status code : " + str(
            update_record_post_request_with_an_incorrect_date_time_value.status_code)

    @allure.epic("test_update_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_answer_text_post_request_with_an_incorrect_date_time_value')
    def test_check_answer_text_post_request_with_an_incorrect_date_time_value(self, update_record_post_request_with_an_incorrect_date_time_value):
        print("request_result_text : ", update_record_post_request_with_an_incorrect_date_time_value.text)
        status = 'Invalid format: "`~!@#$%^&*()_+[]{}|\?/,."'
        assert status in str(
            update_record_post_request_with_an_incorrect_date_time_value.text), "Answer text not " + status + " ; actual message : " + str(
            update_record_post_request_with_an_incorrect_date_time_value.text)


@pytest.mark.usefixtures("update_record_post_request_with_an_incorrect_caller_id")
class Test_post_request_with_an_incorrect_caller_id():
    @allure.epic("test_update_record")
    @allure.feature("answer code 200")
    @allure.step('test_check_status_code_post_request_with_an_incorrect_caller_id')
    def test_check_status_code_post_request_with_an_incorrect_caller_id(self, update_record_post_request_with_an_incorrect_caller_id):
        print("request_result_status_code : ", update_record_post_request_with_an_incorrect_caller_id.status_code)
        assert "200" in str(
            update_record_post_request_with_an_incorrect_caller_id.status_code), "Answer status not 200 ; actual status code : " + str(
            update_record_post_request_with_an_incorrect_caller_id.status_code)

    @allure.epic("test_update_record")
    @allure.feature("answer code 200")
    @allure.step('test_check_answer_text_post_request_with_an_incorrect_caller_id')
    def test_check_answer_text_post_request_with_an_incorrect_caller_id(self, update_record_post_request_with_an_incorrect_caller_id):
        print("request_result_text : ", update_record_post_request_with_an_incorrect_caller_id.text)
        assert len(str(
            update_record_post_request_with_an_incorrect_caller_id.text)) == 0, "Answer text not empty ; actual message : " + str(
            update_record_post_request_with_an_incorrect_caller_id.text)


@pytest.mark.usefixtures("update_record_post_request_with_an_incorrect_agent_id")
class Test_post_request_with_an_incorrect_agent_id():
    @allure.epic("test_update_record")
    @allure.feature("answer code 200")
    @allure.step('test_check_status_code_post_request_with_an_incorrect_agent_id')
    def test_check_status_code_post_request_with_an_incorrect_agent_id(self, update_record_post_request_with_an_incorrect_agent_id):
        print("request_result_status_code : ", update_record_post_request_with_an_incorrect_agent_id.status_code)
        assert "200" in str(
            update_record_post_request_with_an_incorrect_agent_id.status_code), "Answer status not 200 ; actual status code : " + str(
            update_record_post_request_with_an_incorrect_agent_id.status_code)

    @allure.epic("test_update_record")
    @allure.feature("answer code 200")
    @allure.step('test_check_answer_text_post_request_with_an_incorrect_agent_id')
    def test_check_answer_text_post_request_with_an_incorrect_caller_id(self, update_record_post_request_with_an_incorrect_agent_id):
        print("request_result_text : ", update_record_post_request_with_an_incorrect_agent_id.text)
        assert len(str(
            update_record_post_request_with_an_incorrect_agent_id.text)) == 0, "Answer text not empty ; actual message : " + str(
            update_record_post_request_with_an_incorrect_agent_id.text)


@pytest.mark.usefixtures("update_record_post_request_with_a_date_time_field_set_to_a_moment_in_the_past")
class Test_post_request_with_a_date_time_field_set_to_a_moment_in_the_past():
    @allure.epic("test_update_record")
    @allure.feature("answer code 200")
    @allure.step('test_check_status_code_post_request_with_a_date_time_field_set_to_a_moment_in_the_past')
    def test_check_status_code_post_request_with_a_date_time_field_set_to_a_moment_in_the_past(self, update_record_post_request_with_a_date_time_field_set_to_a_moment_in_the_past):
        print("request_result_status_code : ", update_record_post_request_with_a_date_time_field_set_to_a_moment_in_the_past.status_code)
        assert "200" in str(
            update_record_post_request_with_a_date_time_field_set_to_a_moment_in_the_past.status_code), "Answer status not 200 ; actual status code : " + str(
            update_record_post_request_with_a_date_time_field_set_to_a_moment_in_the_past.status_code)

    @allure.epic("test_update_record")
    @allure.feature("answer code 200")
    @allure.step('test_check_answer_text_post_request_with_a_date_time_field_set_to_a_moment_in_the_past')
    def test_check_answer_text_post_request_with_an_incorrect_caller_id(self, update_record_post_request_with_a_date_time_field_set_to_a_moment_in_the_past):
        print("request_result_text : ", update_record_post_request_with_a_date_time_field_set_to_a_moment_in_the_past.text)
        assert len(str(
            update_record_post_request_with_a_date_time_field_set_to_a_moment_in_the_past.text)) == 0, "Answer text not empty ; actual message : " + str(
            update_record_post_request_with_a_date_time_field_set_to_a_moment_in_the_past.text)


@pytest.mark.usefixtures("update_record_post_request_without_a_phone_field_required_field")
class Test_post_request_without_a_phone_field_required_field():
    @allure.epic("test_update_record")
    @allure.feature("answer code 200")
    @allure.step('test_check_status_code_post_request_without_a_phone_field_required_field')
    def test_check_status_code_post_request_without_a_phone_field_required_field(self, update_record_post_request_without_a_phone_field_required_field):
        print("request_result_status_code : ", update_record_post_request_without_a_phone_field_required_field.status_code)
        assert "200" in str(
            update_record_post_request_without_a_phone_field_required_field.status_code), "Answer status not 200 ; actual status code : " + str(
            update_record_post_request_without_a_phone_field_required_field.status_code)

    @allure.epic("test_update_record")
    @allure.feature("answer code 200")
    @allure.step('test_check_answer_text_post_request_without_a_phone_field_required_field')
    def test_check_answer_text_post_request_with_an_incorrect_caller_id(self, update_record_post_request_without_a_phone_field_required_field):
        print("request_result_text : ", update_record_post_request_without_a_phone_field_required_field.text)
        assert len(str(
            update_record_post_request_without_a_phone_field_required_field.text)) == 0, "Answer text not empty ; actual message : " + str(
            update_record_post_request_without_a_phone_field_required_field.text)


#@allure.issue("https://trac.brightpattern.com/ticket/22524")
@pytest.mark.usefixtures("update_record_post_request_without_a_phone_field_required_field_and_key")
class Test_post_request_without_a_phone_field_required_field_and_key():
    @allure.epic("test_update_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_status_code_post_request_without_a_phone_field_required_field_and_key')
    def test_check_status_code_post_request_without_a_phone_field_required_field_and_key(self, update_record_post_request_without_a_phone_field_required_field_and_key):
        print("request_result_status_code : ", update_record_post_request_without_a_phone_field_required_field_and_key.status_code)
        assert "400" in str(
            update_record_post_request_without_a_phone_field_required_field_and_key.status_code), "Answer status not 400 ; actual status code : " + str(
            update_record_post_request_without_a_phone_field_required_field_and_key.status_code)

    @allure.epic("test_update_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_answer_text_post_request_without_a_phone_field_required_field_and_key')
    def test_check_answer_text_post_request_without_a_phone_field_required_field_and_key(self, update_record_post_request_without_a_phone_field_required_field_and_key):
        print("request_result_text : ", update_record_post_request_without_a_phone_field_required_field_and_key.text)
        status = 'missing key: phone1'
        assert status in str(
            update_record_post_request_without_a_phone_field_required_field_and_key.text), "Answer text not " + status + " ; actual message : " + str(
            update_record_post_request_without_a_phone_field_required_field_and_key.text)


@pytest.mark.usefixtures("update_record_post_request_without_a_phone_field_empty_value")
class Test_post_request_without_a_phone_field_empty_value():
    @allure.epic("test_update_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_status_code_post_request_without_a_phone_field_empty_value')
    def test_check_status_code_post_request_without_a_phone_field_empty_value(self, update_record_post_request_without_a_phone_field_empty_value):
        print("request_result_status_code : ", update_record_post_request_without_a_phone_field_empty_value.status_code)
        assert "400" in str(
            update_record_post_request_without_a_phone_field_empty_value.status_code), "Answer status not 400 ; actual status code : " + str(
            update_record_post_request_without_a_phone_field_empty_value.status_code)

    @allure.epic("test_update_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_answer_text_post_request_without_a_phone_field_empty_value')
    def test_check_answer_text_post_request_without_a_phone_field_empty_value(self, update_record_post_request_without_a_phone_field_empty_value):
        print("request_result_text : ", update_record_post_request_without_a_phone_field_empty_value.text)
        status = 'missing key: phone1'
        assert status in str(
            update_record_post_request_without_a_phone_field_empty_value.text), "Answer text not " + status + " ; actual message : " + str(
            update_record_post_request_without_a_phone_field_empty_value.text)


@allure.issue("https://trac.brightpattern.com/ticket/22561")
@pytest.mark.usefixtures("update_record_post_request_incorrectly_formatted_phone_number_in_a_phone_field")
class Test_post_request_incorrectly_formatted_phone_number_in_a_phone_field():
    @allure.epic("test_update_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_status_code_post_request_incorrectly_formatted_phone_number_in_a_phone_field')
    def test_check_status_code_post_request_incorrectly_formatted_phone_number_in_a_phone_field(self, update_record_post_request_incorrectly_formatted_phone_number_in_a_phone_field):
        print("request_result_status_code : ", update_record_post_request_incorrectly_formatted_phone_number_in_a_phone_field.status_code)
        assert "400" in str(
            update_record_post_request_incorrectly_formatted_phone_number_in_a_phone_field.status_code), "Answer status not 400 ; actual status code : " + str(
            update_record_post_request_incorrectly_formatted_phone_number_in_a_phone_field.status_code)

    @allure.epic("test_update_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_answer_text_post_request_incorrectly_formatted_phone_number_in_a_phone_field')
    def test_check_answer_text_post_request_incorrectly_formatted_phone_number_in_a_phone_field(self, update_record_post_request_incorrectly_formatted_phone_number_in_a_phone_field):
        print("request_result_text : ", update_record_post_request_incorrectly_formatted_phone_number_in_a_phone_field.text)
        status = '<fill response>>'
        assert status in str(
            update_record_post_request_incorrectly_formatted_phone_number_in_a_phone_field.text), "Answer text not " + status + " ; actual message : " + str(
            update_record_post_request_incorrectly_formatted_phone_number_in_a_phone_field.text)


@allure.issue("https://trac.brightpattern.com/ticket/22559")
@pytest.mark.usefixtures("update_record_post_request_incorrectly_formatted_phone_number_in_a_phone_field_the_country_set_for_us_and_canada_the_number_starts_with_1_and_has_less_than_11_digits")
class Test_post_request_incorrectly_formatted_phone_number_in_a_phone_field_the_country_set_for_us_and_canada_the_number_starts_with_1_and_has_less_than_11_digits():
    @allure.epic("test_update_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_status_code_post_request_incorrectly_formatted_phone_number_in_a_phone_field_the_country_set_for_us_and_canada_the_number_starts_with_1_and_has_less_than_11_digits')
    def test_check_status_code_post_request_incorrectly_formatted_phone_number_in_a_phone_field_the_country_set_for_us_and_canada_the_number_starts_with_1_and_has_less_than_11_digits(self, update_record_post_request_incorrectly_formatted_phone_number_in_a_phone_field_the_country_set_for_us_and_canada_the_number_starts_with_1_and_has_less_than_11_digits):
        print("request_result_status_code : ", update_record_post_request_incorrectly_formatted_phone_number_in_a_phone_field_the_country_set_for_us_and_canada_the_number_starts_with_1_and_has_less_than_11_digits.status_code)
        assert "400" in str(
            update_record_post_request_incorrectly_formatted_phone_number_in_a_phone_field_the_country_set_for_us_and_canada_the_number_starts_with_1_and_has_less_than_11_digits.status_code), "Answer status not 400 ; actual status code : " + str(
            update_record_post_request_incorrectly_formatted_phone_number_in_a_phone_field_the_country_set_for_us_and_canada_the_number_starts_with_1_and_has_less_than_11_digits.status_code)

    @allure.epic("test_update_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_answer_text_post_request_incorrectly_formatted_phone_number_in_a_phone_field_the_country_set_for_us_and_canada_the_number_starts_with_1_and_has_less_than_11_digits')
    def test_check_answer_text_post_request_incorrectly_formatted_phone_number_in_a_phone_field_the_country_set_for_us_and_canada_the_number_starts_with_1_and_has_less_than_11_digits(self, update_record_post_request_incorrectly_formatted_phone_number_in_a_phone_field_the_country_set_for_us_and_canada_the_number_starts_with_1_and_has_less_than_11_digits):
        print("request_result_text : ", update_record_post_request_incorrectly_formatted_phone_number_in_a_phone_field_the_country_set_for_us_and_canada_the_number_starts_with_1_and_has_less_than_11_digits.text)
        status = 'invalid US/Canada phone number'
        assert status in str(
            update_record_post_request_incorrectly_formatted_phone_number_in_a_phone_field_the_country_set_for_us_and_canada_the_number_starts_with_1_and_has_less_than_11_digits.text), "Answer text not " + status + " ; actual message : " + str(
            update_record_post_request_incorrectly_formatted_phone_number_in_a_phone_field_the_country_set_for_us_and_canada_the_number_starts_with_1_and_has_less_than_11_digits.text)


@allure.issue("https://trac.brightpattern.com/ticket/21500")
@pytest.mark.usefixtures("update_record_post_request_with_a_non_existent_field_name")
class Test_post_request_with_a_non_existent_field_name():
    @allure.epic("test_update_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_status_code_post_request_with_a_non_existent_field_name')
    def test_check_status_code_post_request_with_a_non_existent_field_name(self, update_record_post_request_with_a_non_existent_field_name):
        print("request_result_status_code : ", update_record_post_request_with_a_non_existent_field_name.status_code)
        assert "400" in str(
            update_record_post_request_with_a_non_existent_field_name.status_code), "Answer status not 400 ; actual status code : " + str(
            update_record_post_request_with_a_non_existent_field_name.status_code)

    @allure.epic("test_update_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_answer_text_post_request_with_a_non_existent_field_name')
    def test_check_answer_text_post_request_with_a_non_existent_field_name(self, update_record_post_request_with_a_non_existent_field_name):
        print("request_result_text : ", update_record_post_request_with_a_non_existent_field_name.text)
        status = '<fill response>>'
        assert status in str(
            update_record_post_request_with_a_non_existent_field_name.text), "Answer text not " + status + " ; actual message : " + str(
            update_record_post_request_with_a_non_existent_field_name.text)


@pytest.mark.usefixtures("update_record_post_request_with_do_not_authorize_session")
class Test_post_request_with_do_not_authorize_session():
    @allure.epic("test_update_record")
    @allure.feature("answer code 401")
    @allure.step('test_check_status_code_post_request_with_do_not_authorize_session')
    def test_check_status_code_post_request_with_do_not_authorize_session(self,
                                                                          update_record_post_request_with_do_not_authorize_session):
        print("request_result_status_code : ", update_record_post_request_with_do_not_authorize_session.status_code)
        assert "401" in str(
            update_record_post_request_with_do_not_authorize_session.status_code), "Answer status not 401 ; actual status code : " + str(
            update_record_post_request_with_do_not_authorize_session.status_code)

    @allure.epic("test_update_record")
    @allure.feature("answer code 401")
    @allure.step('test_check_answer_text_post_request_with_do_not_authorize_session')
    def test_check_answer_text_post_request_with_do_not_authorize_session(self,
                                                                          update_record_post_request_with_do_not_authorize_session):
        print("request_result_text : ", update_record_post_request_with_do_not_authorize_session.text)
        status = "Session is not authenticated"
        assert status in str(
            update_record_post_request_with_do_not_authorize_session.text), "Answer text not " + status + " ; actual message : " + str(
            update_record_post_request_with_do_not_authorize_session.text)


@pytest.mark.usefixtures("update_record_post_request_with_authorize_session_for_user_without_permission")
class Test_post_request_with_authorize_session_for_user_without_permission():
    @allure.epic("test_update_record")
    @allure.feature("answer code 403")
    @allure.step('test_check_status_code_post_request_with_authorize_session_for_user_without_permission')
    def test_check_status_code_post_request_with_authorize_session_for_user_without_permission(self,
                                                                                               update_record_post_request_with_authorize_session_for_user_without_permission):
        print("request_result_status_code : ", update_record_post_request_with_authorize_session_for_user_without_permission.status_code)
        assert "403" in str(
            update_record_post_request_with_authorize_session_for_user_without_permission.status_code), "Answer status not 403 ; actual status code : " + str(
            update_record_post_request_with_authorize_session_for_user_without_permission.status_code)

    @allure.epic("test_update_record")
    @allure.feature("answer code 403")
    @allure.step('test_check_answer_text_post_request_with_authorize_session_for_user_without_permission')
    def test_check_answer_text_post_request_with_authorize_session_for_user_without_permission(self,
                                                                                               update_record_post_request_with_authorize_session_for_user_without_permission):
        print("request_result_text : ", update_record_post_request_with_authorize_session_for_user_without_permission.text)
        status = "Access denied deleteAll"
        assert status in str(
            update_record_post_request_with_authorize_session_for_user_without_permission.text), "Answer text not " + status + " ; actual message : " + str(
            update_record_post_request_with_authorize_session_for_user_without_permission.text)
