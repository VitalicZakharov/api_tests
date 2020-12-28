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


@allure.issue("https://trac.brightpattern.com/ticket/24583")
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
        status = "Access denied update"
        assert status in str(
            update_record_post_request_with_authorize_session_for_user_without_permission.text), "Answer text not " + status + " ; actual message : " + str(
            update_record_post_request_with_authorize_session_for_user_without_permission.text)


@pytest.mark.usefixtures("update_record_post_request_without_parameters_empty_body")
class Test_post_request_without_parameters_empty_body():
    @allure.epic("test_update_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_status_code_post_request_without_parameters_empty_body')
    def test_check_status_code_post_request_without_parameters_empty_body(self, update_record_post_request_without_parameters_empty_body):
        print("request_result_status_code : ", update_record_post_request_without_parameters_empty_body.status_code)
        assert "400" in str(
            update_record_post_request_without_parameters_empty_body.status_code), "Answer status not 400 ; actual status code : " + str(
            update_record_post_request_without_parameters_empty_body.status_code)

    @allure.epic("test_update_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_answer_text_post_request_without_parameters_empty_body')
    def test_check_answer_text_post_request_without_parameters_empty_body(self, update_record_post_request_without_parameters_empty_body):
        print("request_result_text : ", update_record_post_request_without_parameters_empty_body.text)
        status = 'missing key: first name, phone1'
        assert status in str(
            update_record_post_request_without_parameters_empty_body.text), "Answer text not " + status + " ; actual message : " + str(
            update_record_post_request_without_parameters_empty_body.text)


@pytest.mark.usefixtures("update_record_post_request_without_a_key_phone_parameter_phone_field_doesnt_present_in_body")
class Test_post_request_without_a_key_phone_parameter_phone_field_doesnt_present_in_body():
    @allure.epic("test_update_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_status_code_post_request_without_a_key_phone_parameter_phone_field_doesnt_present_in_body')
    def test_check_status_code_post_request_without_a_key_phone_parameter_phone_field_doesnt_present_in_body(self, update_record_post_request_without_a_key_phone_parameter_phone_field_doesnt_present_in_body):
        print("request_result_status_code : ", update_record_post_request_without_a_key_phone_parameter_phone_field_doesnt_present_in_body.status_code)
        assert "400" in str(
            update_record_post_request_without_a_key_phone_parameter_phone_field_doesnt_present_in_body.status_code), "Answer status not 400 ; actual status code : " + str(
            update_record_post_request_without_a_key_phone_parameter_phone_field_doesnt_present_in_body.status_code)

    @allure.epic("test_update_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_answer_text_post_request_without_a_key_phone_parameter_phone_field_doesnt_present_in_body')
    def test_check_answer_text_post_request_without_a_key_phone_parameter_phone_field_doesnt_present_in_body(self, update_record_post_request_without_a_key_phone_parameter_phone_field_doesnt_present_in_body):
        print("request_result_text : ", update_record_post_request_without_a_key_phone_parameter_phone_field_doesnt_present_in_body.text)
        status = 'missing key: phone1'
        assert status in str(
            update_record_post_request_without_a_key_phone_parameter_phone_field_doesnt_present_in_body.text), "Answer text not " + status + " ; actual message : " + str(
            update_record_post_request_without_a_key_phone_parameter_phone_field_doesnt_present_in_body.text)


@pytest.mark.usefixtures("update_record_post_request_with_a_wrong_key_phone_parameter")
class Test_post_request_with_a_wrong_key_phone_parameter():
    @allure.epic("test_update_record")
    @allure.feature("answer code 404")
    @allure.step('test_check_status_code_post_request_with_a_wrong_key_phone_parameter')
    def test_check_status_code_post_request_with_a_wrong_key_phone_parameter(self, update_record_post_request_with_a_wrong_key_phone_parameter):
        print("request_result_status_code : ", update_record_post_request_with_a_wrong_key_phone_parameter.status_code)
        assert "404" in str(
            update_record_post_request_with_a_wrong_key_phone_parameter.status_code), "Answer status not 404 ; actual status code : " + str(
            update_record_post_request_with_a_wrong_key_phone_parameter.status_code)

    @allure.epic("test_update_record")
    @allure.feature("answer code 404")
    @allure.step('test_check_answer_text_post_request_with_a_wrong_key_phone_parameter')
    def test_check_answer_text_post_request_with_a_wrong_key_phone_parameter(self, update_record_post_request_with_a_wrong_key_phone_parameter):
        print("request_result_text : ", update_record_post_request_with_a_wrong_key_phone_parameter.text)
        status = "record is not found"
        assert status in str(
            update_record_post_request_with_a_wrong_key_phone_parameter.text), "Answer text not " + status + " ; actual message : " + str(
            update_record_post_request_with_a_wrong_key_phone_parameter.text)


@pytest.mark.usefixtures("update_record_post_request_without_a_key_first_name_parameter")
class Test_post_request_without_a_key_first_name_parameter():
    @allure.epic("test_update_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_status_code_post_request_without_a_key_first_name_parameter')
    def test_check_status_code_post_request_without_a_key_first_name_parameter(self, update_record_post_request_without_a_key_first_name_parameter):
        print("request_result_status_code : ", update_record_post_request_without_a_key_first_name_parameter.status_code)
        assert "400" in str(
            update_record_post_request_without_a_key_first_name_parameter.status_code), "Answer status not 400 ; actual status code : " + str(
            update_record_post_request_without_a_key_first_name_parameter.status_code)

    @allure.epic("test_update_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_answer_text_post_request_without_a_key_first_name_parameter')
    def test_check_answer_text_post_request_without_a_key_first_name_parameter(self, update_record_post_request_without_a_key_first_name_parameter):
        print("request_result_text : ", update_record_post_request_without_a_key_first_name_parameter.text)
        status = 'missing key: first name'
        assert status in str(
            update_record_post_request_without_a_key_first_name_parameter.text), "Answer text not " + status + " ; actual message : " + str(
            update_record_post_request_without_a_key_first_name_parameter.text)


@pytest.mark.usefixtures("update_record_post_request_with_a_wrong_key_first_name_parameter")
class Test_post_request_with_a_wrong_key_first_name_parameter():
    @allure.epic("test_update_record")
    @allure.feature("answer code 404")
    @allure.step('test_check_status_code_post_request_with_a_wrong_key_first_name_parameter')
    def test_check_status_code_post_request_with_a_wrong_key_first_name_parameter(self, update_record_post_request_with_a_wrong_key_first_name_parameter):
        print("request_result_status_code : ", update_record_post_request_with_a_wrong_key_first_name_parameter.status_code)
        assert "404" in str(
            update_record_post_request_with_a_wrong_key_first_name_parameter.status_code), "Answer status not 404 ; actual status code : " + str(
            update_record_post_request_with_a_wrong_key_first_name_parameter.status_code)

    @allure.epic("test_update_record")
    @allure.feature("answer code 404")
    @allure.step('test_check_answer_text_post_request_with_a_wrong_key_first_name_parameter')
    def test_check_answer_text_post_request_with_a_wrong_key_first_name_parameter(self, update_record_post_request_with_a_wrong_key_first_name_parameter):
        print("request_result_text : ", update_record_post_request_with_a_wrong_key_first_name_parameter.text)
        status = "record is not found"
        assert status in str(
            update_record_post_request_with_a_wrong_key_first_name_parameter.text), "Answer text not " + status + " ; actual message : " + str(
            update_record_post_request_with_a_wrong_key_first_name_parameter.text)


@pytest.mark.usefixtures("update_record_post_request_without_a_last_name_parameter")
class Test_post_request_without_a_last_name_parameter():
    @allure.epic("test_update_record")
    @allure.feature("answer code 200")
    @allure.step('test_check_status_code_post_request_without_a_last_name_parameter')
    def test_check_status_code_post_request_without_a_last_name_parameter(self, update_record_post_request_without_a_last_name_parameter):
        print("request_result_status_code : ", update_record_post_request_without_a_last_name_parameter.status_code)
        assert "200" in str(
            update_record_post_request_without_a_last_name_parameter.status_code), "Answer status not 200 ; actual status code : " + str(
            update_record_post_request_without_a_last_name_parameter.status_code)

    @allure.epic("test_update_record")
    @allure.feature("answer code 200")
    @allure.step('test_check_answer_text_post_request_without_a_last_name_parameter')
    def test_check_answer_text_post_request_without_a_last_name_parameter(self, update_record_post_request_without_a_last_name_parameter):
        print("request_result_text : ", update_record_post_request_without_a_last_name_parameter.text)
        assert len(str(
            update_record_post_request_without_a_last_name_parameter.text)) == 0, "Answer text not empty ; actual message : " + str(
            update_record_post_request_without_a_last_name_parameter.text)


@pytest.mark.usefixtures("update_record_post_request_with_incorrect_body_format_deleted_quotes")
class Test_post_request_with_incorrect_body_format_deleted_quotes():
    @allure.epic("test_update_record")
    @allure.feature("answer code 404")
    @allure.step('test_check_status_code_post_request_with_incorrect_body_format_deleted_quotes')
    def test_check_status_code_post_request_with_incorrect_body_format_deleted_quotes(self,
                                                                                      update_record_post_request_with_incorrect_body_format_deleted_quotes):
        print("request_result_status_code : ", update_record_post_request_with_incorrect_body_format_deleted_quotes.status_code)
        assert "404" in str(
            update_record_post_request_with_incorrect_body_format_deleted_quotes.status_code), "Answer status not 404 ; actual status code : " + str(
            update_record_post_request_with_incorrect_body_format_deleted_quotes.status_code)

    @allure.epic("test_update_record")
    @allure.feature("answer code 404")
    @allure.step('test_check_answer_text_post_request_with_incorrect_body_format_deleted_quotes')
    def test_check_answer_text_post_request_with_incorrect_body_format_deleted_quotes(self,
                                                                                      update_record_post_request_with_incorrect_body_format_deleted_quotes):
        print("request_result_text : ", update_record_post_request_with_incorrect_body_format_deleted_quotes.text)
        status = "record is not found"
        assert status in str(
            update_record_post_request_with_incorrect_body_format_deleted_quotes.text), "Answer text not " + status + " ; actual message : " + str(
            update_record_post_request_with_incorrect_body_format_deleted_quotes.text)


#@allure.issue("https://trac.brightpattern.com/ticket/22826")
@pytest.mark.usefixtures("update_record_post_request_with_incorrect_body_format_a_redundant_comma_in_the_end")
class Test_post_request_with_incorrect_body_format_a_redundant_comma_in_the_end():
    @allure.epic("test_update_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_status_code_post_request_with_incorrect_body_format_a_redundant_comma_in_the_end')
    def test_check_status_code_post_request_with_incorrect_body_format_a_redundant_comma_in_the_end(self,
                                                                                                    update_record_post_request_with_incorrect_body_format_a_redundant_comma_in_the_end):
        print("request_result_status_code : ", update_record_post_request_with_incorrect_body_format_a_redundant_comma_in_the_end.status_code)
        assert "400" in str(
            update_record_post_request_with_incorrect_body_format_a_redundant_comma_in_the_end.status_code), "Answer status not 400 ; actual status code : " + str(
            update_record_post_request_with_incorrect_body_format_a_redundant_comma_in_the_end.status_code)

    @allure.epic("test_update_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_answer_text_post_request_with_incorrect_body_format_a_redundant_comma_in_the_end')
    def test_check_answer_text_post_request_with_incorrect_body_format_a_redundant_comma_in_the_end(self,
                                                                                                    update_record_post_request_with_incorrect_body_format_a_redundant_comma_in_the_end):
        print("request_result_text : ", update_record_post_request_with_incorrect_body_format_a_redundant_comma_in_the_end.text)
        status = "Unterminated object at line 1 column 74 path $"
        assert status in str(
            update_record_post_request_with_incorrect_body_format_a_redundant_comma_in_the_end.text), "Answer text not " + status + " ; actual message : " + str(
            update_record_post_request_with_incorrect_body_format_a_redundant_comma_in_the_end.text)


@pytest.mark.usefixtures("update_record_post_request_to_the_non_existent_list")
class Test_post_request_to_the_non_existent_list():
    @allure.epic("test_update_record")
    @allure.feature("answer code 404")
    @allure.step('test_check_status_code_post_request_to_the_non_existent_list')
    def test_check_status_code_post_request_to_the_non_existent_list(self, update_record_post_request_to_the_non_existent_list):
        print("request_result_status_code : ", update_record_post_request_to_the_non_existent_list.status_code)
        assert "404" in str(
            update_record_post_request_to_the_non_existent_list.status_code), "Answer status not 404 ; actual status code : " + str(
            update_record_post_request_to_the_non_existent_list.status_code)

    @allure.epic("test_update_record")
    @allure.feature("answer code 404")
    @allure.step('test_check_answer_text_post_request_to_the_non_existent_list')
    def test_check_answer_text_post_request_to_the_non_existent_list(self, update_record_post_request_to_the_non_existent_list):
        print("request_result_text : ", update_record_post_request_to_the_non_existent_list.text)
        status = "calling list not found"
        assert status in str(
            update_record_post_request_to_the_non_existent_list.text), "Answer text not " + status + " ; actual message : " + str(
            update_record_post_request_to_the_non_existent_list.text)


@pytest.mark.usefixtures("update_record_post_request_with_invalid_url")
class Test_post_request_with_invalid_url():
    @allure.epic("test_update_record")
    @allure.feature("answer code 404")
    @allure.step('test_check_status_code_post_request_with_invalid_url')
    def test_check_status_code_post_request_with_invalid_url(self, update_record_post_request_with_invalid_url):
        print("request_result_status_code : ", update_record_post_request_with_invalid_url.status_code)
        assert "404" in str(
            update_record_post_request_with_invalid_url.status_code), "Answer status not 404 ; actual status code : " + str(
            update_record_post_request_with_invalid_url.status_code)

    @allure.epic("test_update_record")
    @allure.feature("answer code 404")
    @allure.step('test_check_answer_text_post_request_with_invalid_url')
    def test_check_answer_text_post_request_with_invalid_url(self, update_record_post_request_with_invalid_url):
        print("request_result_text : ", update_record_post_request_with_invalid_url.text)
        status = "HTTP 404 Not Found"
        assert status in str(
            update_record_post_request_with_invalid_url.text), "Answer text not " + status + " ; actual message : " + str(
            update_record_post_request_with_invalid_url.text)


@pytest.mark.usefixtures("update_record_post_request_with_the_incorrectly_formatted_value_phone_number_in_a_phone_field_non_numeric_symbol_other_than_plus")
class Test_post_request_with_the_incorrectly_formatted_value_phone_number_in_a_phone_field_non_numeric_symbol_other_than_plus():
    @allure.epic("test_update_record")
    @allure.feature("answer code 404")
    @allure.step('test_check_status_code_post_request_with_the_incorrectly_formatted_value_phone_number_in_a_phone_field_non_numeric_symbol_other_than_plus')
    def test_check_status_code_post_request_with_the_incorrectly_formatted_value_phone_number_in_a_phone_field_non_numeric_symbol_other_than_plus(self, update_record_post_request_with_the_incorrectly_formatted_value_phone_number_in_a_phone_field_non_numeric_symbol_other_than_plus):
        print("request_result_status_code : ", update_record_post_request_with_the_incorrectly_formatted_value_phone_number_in_a_phone_field_non_numeric_symbol_other_than_plus.status_code)
        assert "404" in str(
            update_record_post_request_with_the_incorrectly_formatted_value_phone_number_in_a_phone_field_non_numeric_symbol_other_than_plus.status_code), "Answer status not 404 ; actual status code : " + str(
            update_record_post_request_with_the_incorrectly_formatted_value_phone_number_in_a_phone_field_non_numeric_symbol_other_than_plus.status_code)

    @allure.epic("test_update_record")
    @allure.feature("answer code 404")
    @allure.step('test_check_answer_text_post_request_with_the_incorrectly_formatted_value_phone_number_in_a_phone_field_non_numeric_symbol_other_than_plus')
    def test_check_answer_text_post_request_with_the_incorrectly_formatted_value_phone_number_in_a_phone_field_non_numeric_symbol_other_than_plus(self, update_record_post_request_with_the_incorrectly_formatted_value_phone_number_in_a_phone_field_non_numeric_symbol_other_than_plus):
        print("request_result_text : ", update_record_post_request_with_the_incorrectly_formatted_value_phone_number_in_a_phone_field_non_numeric_symbol_other_than_plus.text)
        status = "record is not found"
        assert status in str(
            update_record_post_request_with_the_incorrectly_formatted_value_phone_number_in_a_phone_field_non_numeric_symbol_other_than_plus.text), "Answer text not " + status + " ; actual message : " + str(
            update_record_post_request_with_the_incorrectly_formatted_value_phone_number_in_a_phone_field_non_numeric_symbol_other_than_plus.text)


@pytest.mark.usefixtures("update_record_post_request_with_the_value_phone_number_in_a_phone_field_using_symbol_plus")
class Test_post_request_with_the_value_phone_number_in_a_phone_field_using_symbol_plus():
    @allure.epic("test_update_record")
    @allure.feature("answer code 404")
    @allure.step('test_check_status_code_post_request_with_the_value_phone_number_in_a_phone_field_using_symbol_plus')
    def test_check_status_code_post_request_with_the_value_phone_number_in_a_phone_field_using_symbol_plus(self, update_record_post_request_with_the_value_phone_number_in_a_phone_field_using_symbol_plus):
        print("request_result_status_code : ", update_record_post_request_with_the_value_phone_number_in_a_phone_field_using_symbol_plus.status_code)
        assert "404" in str(
            update_record_post_request_with_the_value_phone_number_in_a_phone_field_using_symbol_plus.status_code), "Answer status not 404 ; actual status code : " + str(
            update_record_post_request_with_the_value_phone_number_in_a_phone_field_using_symbol_plus.status_code)

    @allure.epic("test_update_record")
    @allure.feature("answer code 404")
    @allure.step('test_check_answer_text_post_request_with_the_value_phone_number_in_a_phone_field_using_symbol_plus')
    def test_check_answer_text_post_request_with_the_value_phone_number_in_a_phone_field_using_symbol_plus(self, update_record_post_request_with_the_value_phone_number_in_a_phone_field_using_symbol_plus):
        print("request_result_text : ", update_record_post_request_with_the_value_phone_number_in_a_phone_field_using_symbol_plus.text)
        status = "record is not found"
        assert status in str(
            update_record_post_request_with_the_value_phone_number_in_a_phone_field_using_symbol_plus.text), "Answer text not " + status + " ; actual message : " + str(
            update_record_post_request_with_the_value_phone_number_in_a_phone_field_using_symbol_plus.text)


@pytest.mark.usefixtures("update_record_post_request_with_body_from_other_list")
class Test_post_request_with_body_from_other_list():
    @allure.epic("test_update_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_status_code_post_request_with_body_from_other_list')
    def test_check_status_code_post_request_with_body_from_other_list(self, update_record_post_request_with_body_from_other_list):
        print("request_result_status_code : ", update_record_post_request_with_body_from_other_list.status_code)
        assert "400" in str(
            update_record_post_request_with_body_from_other_list.status_code), "Answer status not 400 ; actual status code : " + str(
            update_record_post_request_with_body_from_other_list.status_code)

    @allure.epic("test_update_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_answer_text_post_request_with_body_from_other_list')
    def test_check_answer_text_post_request_with_body_from_other_list(self, update_record_post_request_with_body_from_other_list):
        print("request_result_text : ", update_record_post_request_with_body_from_other_list.text)
        status = "missing key: phone1"
        assert status in str(
            update_record_post_request_with_body_from_other_list.text), "Answer text not " + status + " ; actual message : " + str(
            update_record_post_request_with_body_from_other_list.text)


@allure.issue("https://trac.brightpattern.com/ticket/24582")
@pytest.mark.usefixtures("update_record_get_request_with_correct_body")
class Test_get_request_with_correct_body():
    @allure.epic("test_update_record")
    @allure.feature("answer code 405")
    @allure.step('test_check_status_code_get_request_with_correct_body')
    def test_check_status_code_get_request_with_correct_body(self, update_record_get_request_with_correct_body):
        print("request_result_status_code : ", update_record_get_request_with_correct_body.status_code)
        assert "405" in str(
            update_record_get_request_with_correct_body.status_code), "Answer status not 405 ; actual status code : " + str(
            update_record_get_request_with_correct_body.status_code)

    @allure.epic("test_update_record")
    @allure.feature("answer code 405")
    @allure.step('test_check_answer_text_get_request_with_correct_body')
    def test_check_answer_text_get_request_with_correct_body(self, update_record_get_request_with_correct_body):
        print("request_result_text : ", update_record_get_request_with_correct_body.text)
        status = "Method Not Allowed"
        assert status in str(
            update_record_get_request_with_correct_body.text), "Answer text not " + status + " ; actual message : " + str(
            update_record_get_request_with_correct_body.text)


@allure.issue("https://trac.brightpattern.com/ticket/24582")
@pytest.mark.usefixtures("update_record_put_request_with_correct_body")
class Test_put_request_with_correct_body():
    @allure.epic("test_update_record")
    @allure.feature("answer code 405")
    @allure.step('test_check_status_code_put_request_with_correct_body')
    def test_check_status_code_put_request_with_correct_body(self, update_record_put_request_with_correct_body):
        print("request_result_status_code : ", update_record_put_request_with_correct_body.status_code)
        assert "405" in str(
            update_record_put_request_with_correct_body.status_code), "Answer status not 405 ; actual status code : " + str(
            update_record_put_request_with_correct_body.status_code)

    @allure.epic("test_update_record")
    @allure.feature("answer code 405")
    @allure.step('test_check_answer_text_put_request_with_correct_body')
    def test_check_answer_text_put_request_with_correct_body(self, update_record_put_request_with_correct_body):
        print("request_result_text : ", update_record_put_request_with_correct_body.text)
        status = "Method Not Allowed"
        assert status in str(
            update_record_put_request_with_correct_body.text), "Answer text not " + status + " ; actual message : " + str(
            update_record_put_request_with_correct_body.text)


@allure.issue("https://trac.brightpattern.com/ticket/24582")
@pytest.mark.usefixtures("update_record_delete_request_with_correct_body")
class Test_delete_request_with_correct_body():
    @allure.epic("test_update_record")
    @allure.feature("answer code 405")
    @allure.step('test_check_status_code_delete_request_with_correct_body')
    def test_check_status_code_delete_request_with_correct_body(self, update_record_delete_request_with_correct_body):
        print("request_result_status_code : ", update_record_delete_request_with_correct_body.status_code)
        assert "405" in str(
            update_record_delete_request_with_correct_body.status_code), "Answer status not 405 ; actual status code : " + str(
            update_record_delete_request_with_correct_body.status_code)

    @allure.epic("test_update_record")
    @allure.feature("answer code 405")
    @allure.step('test_check_answer_text_delete_request_with_correct_body')
    def test_check_answer_text_delete_request_with_correct_body(self, update_record_delete_request_with_correct_body):
        print("request_result_text : ", update_record_delete_request_with_correct_body.text)
        status = "Method Not Allowed"
        assert status in str(
            update_record_delete_request_with_correct_body.text), "Answer text not " + status + " ; actual message : " + str(
            update_record_delete_request_with_correct_body.text)