import pytest
import allure

# @allure.suite('Test_add_many_records')

@pytest.mark.usefixtures("add_many_records_post_request_with_correct_body")
class Test_post_request_with_correct_body():
    @allure.epic("test_add_many_records")
    @allure.feature("answer code 200")
    @allure.step('test_check_status_code_post_request_with_correct_body')
    def test_check_status_code_post_request_with_correct_body(self, add_many_records_post_request_with_correct_body):
        print("request_result_status_code : ", add_many_records_post_request_with_correct_body.status_code)
        assert "200" in str(
            add_many_records_post_request_with_correct_body.status_code), "Answer status not 200 ; actual status code : " + str(
            add_many_records_post_request_with_correct_body.status_code)

    @allure.epic("test_add_many_records")
    @allure.feature("answer code 200")
    @allure.step('test_check_answer_text_post_request_with_correct_body')
    def test_check_answer_text_post_request_with_correct_body(self, add_many_records_post_request_with_correct_body):
        print("request_result_text : ", add_many_records_post_request_with_correct_body.text)
        status = "{\"added\":3}"
        assert status in add_many_records_post_request_with_correct_body.text, "Answer text not " + status + " ; actual message : " + str(
            add_many_records_post_request_with_correct_body.text)

@allure.issue("https://trac.brightpattern.com/ticket/24403")
@pytest.mark.usefixtures("add_many_records_post_request_with_a_duplicate_earlier_created_keys")
class Test_post_request_with_a_duplicate_earlier_created_keys():
    @allure.epic("test_add_many_records")
    @allure.feature("answer code 200")
    @allure.step('test_check_status_code_post_request_with_a_duplicate_earlier_created_keys')
    def test_check_status_code_post_request_with_a_duplicate_earlier_created_keys(self, add_many_records_post_request_with_a_duplicate_earlier_created_keys):
        print("request_result_status_code : ", add_many_records_post_request_with_a_duplicate_earlier_created_keys.status_code)
        assert "200" in str(
            add_many_records_post_request_with_a_duplicate_earlier_created_keys.status_code), "Answer status not 200 ; actual status code : " + str(
            add_many_records_post_request_with_a_duplicate_earlier_created_keys.status_code)

    @allure.epic("test_add_many_records")
    @allure.feature("answer code 200")
    @allure.step('test_check_answer_text_post_request_with_a_duplicate_earlier_created_keys')
    def test_check_answer_text_post_request_with_a_duplicate_earlier_created_keys(self, add_many_records_post_request_with_a_duplicate_earlier_created_keys):
        print("request_result_text : ", add_many_records_post_request_with_a_duplicate_earlier_created_keys.text)
        status = '{"added":2,"error":{"duplicateKey":[{"last name":"Name_Last20","first name":"Name_First20","agent id":"Test20","phone2":"9200","date/time":"01-07-2025","caller id":"Test20","integer":"123211","phone1":"9019"}]}}'
        assert status in str(
            add_many_records_post_request_with_a_duplicate_earlier_created_keys.text), "Answer text not " + status + " ; actual message : " + str(
            add_many_records_post_request_with_a_duplicate_earlier_created_keys.text)

@pytest.mark.usefixtures("add_many_records_post_request_with_incorrect_body_format_typization")
class Test_post_request_with_incorrect_body_format_typization():
    @allure.epic("test_add_many_records")
    @allure.feature("answer code 400")
    @allure.step('test_check_status_code_post_request_with_incorrect_body_format_typization')
    def test_check_status_code_post_request_with_incorrect_body_format_typization(self,
                                                                                  add_many_records_post_request_with_incorrect_body_format_typization):
        print("request_result_status_code : ", add_many_records_post_request_with_incorrect_body_format_typization.status_code)
        assert "400" in str(
            add_many_records_post_request_with_incorrect_body_format_typization.status_code), "Answer status not 400 ; actual status code : " + str(
            add_many_records_post_request_with_incorrect_body_format_typization.status_code)

    @allure.epic("test_add_many_records")
    @allure.feature("answer code 400")
    @allure.step('test_check_answer_text_post_request_with_incorrect_body_format_typization')
    def test_check_answer_text_post_request_with_incorrect_body_format_typization(self,
                                                                                  add_many_records_post_request_with_incorrect_body_format_typization):
        print("request_result_text : ", add_many_records_post_request_with_incorrect_body_format_typization.text)
        status = "Expected BEGIN_ARRAY but was BEGIN_OBJECT at line 1 column 2 path $"
        assert status in str(
            add_many_records_post_request_with_incorrect_body_format_typization.text), "Answer text not " + status + " ; actual message : " + str(
            add_many_records_post_request_with_incorrect_body_format_typization.text)


@pytest.mark.usefixtures("add_many_records_post_request_with_a_missing_required_field")
class Test_post_request_with_a_missing_required_field():
    @allure.epic("test_add_many_records")
    @allure.feature("answer code 200")
    @allure.step('test_check_status_code_post_request_with_a_missing_required_field')
    def test_check_status_code_post_request_with_a_missing_required_field(self, add_many_records_post_request_with_a_missing_required_field):
        print("request_result_status_code : ", add_many_records_post_request_with_a_missing_required_field.status_code)
        assert "200" in str(
            add_many_records_post_request_with_a_missing_required_field.status_code), "Answer status not 200 ; actual status code : " + str(
            add_many_records_post_request_with_a_missing_required_field.status_code)

    @allure.epic("test_add_many_records")
    @allure.feature("answer code 200")
    @allure.step('test_check_answer_text_post_request_with_a_missing_required_field')
    def test_check_answer_text_post_request_with_a_missing_required_field(self, add_many_records_post_request_with_a_missing_required_field):
        print("request_result_text : ", add_many_records_post_request_with_a_missing_required_field.text)
        status = '{"added":1,"error":{"missingRequired":[{"last name":"Name_Last21","first name":"Name_First21","agent id":"Test21","date/time":"01-07-2025","caller id":"Test21","integer":"123211","phone1":"9021"}],"missingKey":[{"last name":"Name_Last21_2","first name":"Name_First21_2","agent id":"Test21_2","phone2":"9212","date/time":"02-07-2025","caller id":"Test21_2","integer":"123212"}]}}'
        assert status in add_many_records_post_request_with_a_missing_required_field.text, "Answer text not " + status + " ; actual message : " + str(
            add_many_records_post_request_with_a_missing_required_field.text)

@allure.issue("https://trac.brightpattern.com/ticket/24407")
@pytest.mark.usefixtures("add_many_records_post_request_with_a_non_existent_field_name")
class Test_post_request_with_a_non_existent_field_name():
    @allure.epic("test_add_many_records")
    @allure.feature("answer code 200")
    @allure.step('test_check_status_code_post_request_with_a_non_existent_field_name')
    def test_check_status_code_post_request_with_a_non_existent_field_name(self, add_many_records_post_request_with_a_non_existent_field_name):
        print("request_result_status_code : ", add_many_records_post_request_with_a_non_existent_field_name.status_code)
        assert "200" in str(
            add_many_records_post_request_with_a_non_existent_field_name.status_code), "Answer status not 200 ; actual status code : " + str(
            add_many_records_post_request_with_a_non_existent_field_name.status_code)

    @allure.epic("test_add_many_records")
    @allure.feature("answer code 200")
    @allure.step('test_check_answer_text_post_request_with_a_non_existent_field_name')
    def test_check_answer_text_post_request_with_a_non_existent_field_name(self, add_many_records_post_request_with_a_non_existent_field_name):
        print("request_result_text : ", add_many_records_post_request_with_a_non_existent_field_name.text)
        status = "{\"added\":2}"
        assert status in str(
            add_many_records_post_request_with_a_non_existent_field_name.text), "Answer text not " + status + " ; actual message : " + str(
            add_many_records_post_request_with_a_non_existent_field_name.text)


@pytest.mark.usefixtures("add_many_records_post_request_with_non_existent_agent_username_in_an_agent_login_id_field")
class Test_post_request_with_non_existent_agent_username_in_an_agent_login_id_field():
    @allure.epic("test_add_many_records")
    @allure.feature("answer code 200")
    @allure.step('test_check_status_code_post_request_with_non_existent_agent_username_in_an_agent_login_id_field')
    def test_check_status_code_post_request_with_non_existent_agent_username_in_an_agent_login_id_field(self, add_many_records_post_request_with_non_existent_agent_username_in_an_agent_login_id_field):
        print("request_result_status_code : ", add_many_records_post_request_with_non_existent_agent_username_in_an_agent_login_id_field.status_code)
        assert "200" in str(
            add_many_records_post_request_with_non_existent_agent_username_in_an_agent_login_id_field.status_code), "Answer status not 200 ; actual status code : " + str(
            add_many_records_post_request_with_non_existent_agent_username_in_an_agent_login_id_field.status_code)

    @allure.epic("test_add_many_records")
    @allure.feature("answer code 200")
    @allure.step('test_check_answer_text_post_request_with_non_existent_agent_username_in_an_agent_login_id_field')
    def test_check_answer_text_post_request_with_non_existent_agent_username_in_an_agent_login_id_field(self, add_many_records_post_request_with_non_existent_agent_username_in_an_agent_login_id_field):
        print("request_result_text : ", add_many_records_post_request_with_non_existent_agent_username_in_an_agent_login_id_field.text)
        status = "{\"added\":3}"
        assert status in add_many_records_post_request_with_non_existent_agent_username_in_an_agent_login_id_field.text, "Answer text not " + status + " ; actual message : " + str(
            add_many_records_post_request_with_non_existent_agent_username_in_an_agent_login_id_field.text)


@pytest.mark.usefixtures("add_many_records_post_request_with_an_incorrectly_formatted_phone_number_in_a_caller_id_field")
class Test_post_request_with_an_incorrectly_formatted_phone_number_in_a_caller_id_field():
    @allure.epic("test_add_many_records")
    @allure.feature("answer code 200")
    @allure.step('test_check_status_code_post_request_with_an_incorrectly_formatted_phone_number_in_a_caller_id_field')
    def test_check_status_code_post_request_with_an_incorrectly_formatted_phone_number_in_a_caller_id_field(self, add_many_records_post_request_with_an_incorrectly_formatted_phone_number_in_a_caller_id_field):
        print("request_result_status_code : ", add_many_records_post_request_with_an_incorrectly_formatted_phone_number_in_a_caller_id_field.status_code)
        assert "200" in str(
            add_many_records_post_request_with_an_incorrectly_formatted_phone_number_in_a_caller_id_field.status_code), "Answer status not 200 ; actual status code : " + str(
            add_many_records_post_request_with_an_incorrectly_formatted_phone_number_in_a_caller_id_field.status_code)

    @allure.epic("test_add_many_records")
    @allure.feature("answer code 200")
    @allure.step('test_check_answer_text_post_request_with_an_incorrectly_formatted_phone_number_in_a_caller_id_field')
    def test_check_answer_text_post_request_with_an_incorrectly_formatted_phone_number_in_a_caller_id_field(self, add_many_records_post_request_with_an_incorrectly_formatted_phone_number_in_a_caller_id_field):
        print("request_result_text : ", add_many_records_post_request_with_an_incorrectly_formatted_phone_number_in_a_caller_id_field.text)
        status = "{\"added\":3}"
        assert status in add_many_records_post_request_with_an_incorrectly_formatted_phone_number_in_a_caller_id_field.text, "Answer text not " + status + " ; actual message : " + str(
            add_many_records_post_request_with_an_incorrectly_formatted_phone_number_in_a_caller_id_field.text)


@pytest.mark.usefixtures("add_many_records_post_request_with_an_incorrectly_date_time_number_in_a_date_time_field")
class Test_post_request_with_an_incorrectly_date_time_number_in_a_date_time_field():
    @allure.epic("test_add_many_records")
    @allure.feature("answer code 200")
    @allure.step('test_check_status_code_post_request_with_an_incorrectly_date_time_number_in_a_date_time_field')
    def test_check_status_code_post_request_with_an_incorrectly_date_time_number_in_a_date_time_field(self, add_many_records_post_request_with_an_incorrectly_date_time_number_in_a_date_time_field):
        print("request_result_status_code : ", add_many_records_post_request_with_an_incorrectly_date_time_number_in_a_date_time_field.status_code)
        assert "200" in str(
            add_many_records_post_request_with_an_incorrectly_date_time_number_in_a_date_time_field.status_code), "Answer status not 200 ; actual status code : " + str(
            add_many_records_post_request_with_an_incorrectly_date_time_number_in_a_date_time_field.status_code)

    @allure.epic("test_add_many_records")
    @allure.feature("answer code 200")
    @allure.step('test_check_answer_text_post_request_with_an_incorrectly_date_time_number_in_a_date_time_field')
    def test_check_answer_text_post_request_with_an_incorrectly_date_time_number_in_a_date_time_field(self, add_many_records_post_request_with_an_incorrectly_date_time_number_in_a_date_time_field):
        print("request_result_text : ", add_many_records_post_request_with_an_incorrectly_date_time_number_in_a_date_time_field.text)
        status = '{"added":2,"error":{"formatError":[{"last name":"Name_Last25","first name":"Name_First25","agent id":"Test25.1","phone2":"9250","date/time":"`~!@#$%^&*()_+ <>-[]{}|?/,.1","caller id":"10025","integer":"123251","phone1":"9025"}]}}'
        assert status in str(
            add_many_records_post_request_with_an_incorrectly_date_time_number_in_a_date_time_field.text), "Answer text not " + status + " ; actual message : " + str(
            add_many_records_post_request_with_an_incorrectly_date_time_number_in_a_date_time_field.text)


@pytest.mark.usefixtures("add_many_records_post_request_with_a_date_time_field_set_to_a_moment_in_the_past")
class Test_post_request_with_a_date_time_field_set_to_a_moment_in_the_past():
    @allure.epic("test_add_many_records")
    @allure.feature("answer code 200")
    @allure.step('test_check_status_code_post_request_with_a_date_time_field_set_to_a_moment_in_the_past')
    def test_check_status_code_post_request_with_a_date_time_field_set_to_a_moment_in_the_past(self, add_many_records_post_request_with_a_date_time_field_set_to_a_moment_in_the_past):
        print("request_result_status_code : ", add_many_records_post_request_with_a_date_time_field_set_to_a_moment_in_the_past.status_code)
        assert "200" in str(
            add_many_records_post_request_with_a_date_time_field_set_to_a_moment_in_the_past.status_code), "Answer status not 200 ; actual status code : " + str(
            add_many_records_post_request_with_a_date_time_field_set_to_a_moment_in_the_past.status_code)

    @allure.epic("test_add_many_records")
    @allure.feature("answer code 200")
    @allure.step('test_check_answer_text_post_request_with_a_date_time_field_set_to_a_moment_in_the_past')
    def test_check_answer_text_post_request_with_a_date_time_field_set_to_a_moment_in_the_past(self, add_many_records_post_request_with_a_date_time_field_set_to_a_moment_in_the_past):
        print("request_result_text : ", add_many_records_post_request_with_a_date_time_field_set_to_a_moment_in_the_past.text)
        status = "{\"added\":3}"
        assert status in add_many_records_post_request_with_a_date_time_field_set_to_a_moment_in_the_past.text, "Answer text not " + status + " ; actual message : " + str(
            add_many_records_post_request_with_a_date_time_field_set_to_a_moment_in_the_past.text)


@pytest.mark.usefixtures("add_many_records_post_request_with_incorrectly_formatted_value_in_an_integer_field_all_rec")
class Test_post_request_with_incorrectly_formatted_value_in_an_integer_field_all_rec():
    @allure.epic("test_add_many_records")
    @allure.feature("answer code 400")
    @allure.step('test_check_status_code_post_request_with_incorrectly_formatted_value_in_an_integer_field_all_rec')
    def test_check_status_code_post_request_with_incorrectly_formatted_value_in_an_integer_field_all_rec(self,
                                                                                  add_many_records_post_request_with_incorrectly_formatted_value_in_an_integer_field_all_rec):
        print("request_result_status_code : ", add_many_records_post_request_with_incorrectly_formatted_value_in_an_integer_field_all_rec.status_code)
        assert "400" in str(
            add_many_records_post_request_with_incorrectly_formatted_value_in_an_integer_field_all_rec.status_code), "Answer status not 400 ; actual status code : " + str(
            add_many_records_post_request_with_incorrectly_formatted_value_in_an_integer_field_all_rec.status_code)

    @allure.epic("test_add_many_records")
    @allure.feature("answer code 400")
    @allure.step('test_check_answer_text_post_request_with_incorrectly_formatted_value_in_an_integer_field_all_rec')
    def test_check_answer_text_post_request_with_incorrectly_formatted_value_in_an_integer_field_all_rec(self,
                                                                                  add_many_records_post_request_with_incorrectly_formatted_value_in_an_integer_field_all_rec):
        print("request_result_text : ", add_many_records_post_request_with_incorrectly_formatted_value_in_an_integer_field_all_rec.text)
        status = 'For input string: "`Ñ~!@#$%^&*()_+ <>-[]{}|?/,.1"'
        assert status in str(
            add_many_records_post_request_with_incorrectly_formatted_value_in_an_integer_field_all_rec.text), "Answer text not " + status + " ; actual message : " + str(
            add_many_records_post_request_with_incorrectly_formatted_value_in_an_integer_field_all_rec.text)


@allure.issue("https://trac.brightpattern.com/ticket/24424")
@pytest.mark.usefixtures("add_many_records_post_request_with_incorrectly_formatted_value_in_an_integer_field_one_rec")
class Test_post_request_with_incorrectly_formatted_value_in_an_integer_field_one_rec():
    @allure.epic("test_add_many_records")
    @allure.feature("answer code 200")
    @allure.step('test_check_status_code_post_request_with_incorrectly_formatted_value_in_an_integer_field_one_rec')
    def test_check_status_code_post_request_with_incorrectly_formatted_value_in_an_integer_field_one_rec(self, add_many_records_post_request_with_incorrectly_formatted_value_in_an_integer_field_one_rec):
        print("request_result_status_code : ", add_many_records_post_request_with_incorrectly_formatted_value_in_an_integer_field_one_rec.status_code)
        assert "200" in str(
            add_many_records_post_request_with_incorrectly_formatted_value_in_an_integer_field_one_rec.status_code), "Answer status not 200 ; actual status code : " + str(
            add_many_records_post_request_with_incorrectly_formatted_value_in_an_integer_field_one_rec.status_code)

    @allure.epic("test_add_many_records")
    @allure.feature("answer code 200")
    @allure.step('test_check_answer_text_post_request_with_incorrectly_formatted_value_in_an_integer_field_one_rec')
    def test_check_answer_text_post_request_with_incorrectly_formatted_value_in_an_integer_field_one_rec(self, add_many_records_post_request_with_incorrectly_formatted_value_in_an_integer_field_one_rec):
        print("request_result_text : ", add_many_records_post_request_with_incorrectly_formatted_value_in_an_integer_field_one_rec.text)
        status = "{\"added\":2}"
        assert status in str(
            add_many_records_post_request_with_incorrectly_formatted_value_in_an_integer_field_one_rec.text), "Answer text not " + status + " ; actual message : " + str(
            add_many_records_post_request_with_incorrectly_formatted_value_in_an_integer_field_one_rec.text)


@pytest.mark.usefixtures("add_many_records_post_request_without_a_phone_field_not_required_field")
class Test_post_request_without_a_phone_field_not_required_field():
    @allure.epic("test_add_many_records")
    @allure.feature("answer code 200")
    @allure.step('test_check_status_code_post_request_without_a_phone_field_not_required_field')
    def test_check_status_code_post_request_without_a_phone_field_not_required_field(self,
                                                                                  add_many_records_post_request_without_a_phone_field_not_required_field):
        print("request_result_status_code : ", add_many_records_post_request_without_a_phone_field_not_required_field.status_code)
        assert "200" in str(
            add_many_records_post_request_without_a_phone_field_not_required_field.status_code), "Answer status not 200 ; actual status code : " + str(
            add_many_records_post_request_without_a_phone_field_not_required_field.status_code)

    @allure.epic("test_add_many_records")
    @allure.feature("answer code 200")
    @allure.step('test_check_answer_text_post_request_without_a_phone_field_not_required_field')
    def test_check_answer_text_post_request_without_a_phone_field_not_required_field(self,
                                                                                  add_many_records_post_request_without_a_phone_field_not_required_field):
        print("request_result_text : ", add_many_records_post_request_without_a_phone_field_not_required_field.text)
        status = '{"added":2,"error":{"missingRequired":[{"last name":"Name_Last29","first name":"Name_First29"}]}}'
        assert status in str(
            add_many_records_post_request_without_a_phone_field_not_required_field.text), "Answer text not " + status + " ; actual message : " + str(
            add_many_records_post_request_without_a_phone_field_not_required_field.text)


#@pytest.mark.usefixtures("add_many_records_post_request_with_an_incorrectly_date_time_number_in_a_date_time_field")
#class Test_post_request_with_an_incorrectly_date_time_number_in_a_date_time_field():
#    @allure.epic("test_add_many_records")
#    @allure.feature("answer code 200")
#    @allure.step('test_check_status_code_post_request_with_an_incorrectly_date_time_number_in_a_date_time_field')
#    def test_check_status_code_post_request_with_an_incorrectly_date_time_number_in_a_date_time_field(self, add_many_records_post_request_with_an_incorrectly_date_time_number_in_a_date_time_field):
#        print("request_result_status_code : ", add_many_records_post_request_with_an_incorrectly_date_time_number_in_a_date_time_field.status_code)
#        assert "200" in str(
#            add_many_records_post_request_with_an_incorrectly_date_time_number_in_a_date_time_field.status_code), "Answer status not 200 ; actual status code : " + str(
#            add_many_records_post_request_with_an_incorrectly_date_time_number_in_a_date_time_field.status_code)

#    @allure.epic("test_add_many_records")
#    @allure.feature("answer code 200")
#    @allure.step('test_check_answer_text_post_request_with_an_incorrectly_date_time_number_in_a_date_time_field')
#    def test_check_answer_text_post_request_with_an_incorrectly_date_time_number_in_a_date_time_field(self, add_many_records_post_request_with_an_incorrectly_date_time_number_in_a_date_time_field):
#        print("request_result_text : ", add_many_records_post_request_with_an_incorrectly_date_time_number_in_a_date_time_field.text)
#        status = '{"added":2,"error":{"formatError":[{"last name":"Name_Last25","first name":"Name_First25","agent id":"Test25.1","phone2":"9250","date/time":"`~!@#$%^&*()_+ <>-[]{}|?/,.1","caller id":"10025","integer":"123251","phone1":"9025"}]}}'
#        assert status in str(
#            add_many_records_post_request_with_an_incorrectly_date_time_number_in_a_date_time_field.text), "Answer text not " + status + " ; actual message : " + str(
#            add_many_records_post_request_with_an_incorrectly_date_time_number_in_a_date_time_field.text)


@pytest.mark.usefixtures("add_many_records_post_request_without_a_phone_field_required_field")
class Test_post_request_without_a_phone_field_required_field():
    @allure.epic("test_add_many_records")
    @allure.feature("answer code 200")
    @allure.step('test_check_status_code_post_request_without_a_phone_field_required_field')
    def test_check_status_code_post_request_without_a_phone_field_required_field(self, add_many_records_post_request_without_a_phone_field_required_field):
        print("request_result_status_code : ", add_many_records_post_request_without_a_phone_field_required_field.status_code)
        assert "200" in str(
            add_many_records_post_request_without_a_phone_field_required_field.status_code), "Answer status not 200 ; actual status code : " + str(
            add_many_records_post_request_without_a_phone_field_required_field.status_code)

    @allure.epic("test_add_many_records")
    @allure.feature("answer code 200")
    @allure.step('test_check_answer_text_post_request_without_a_phone_field_required_field')
    def test_check_answer_text_post_request_without_a_phone_field_required_field(self, add_many_records_post_request_without_a_phone_field_required_field):
        print("request_result_text : ", add_many_records_post_request_without_a_phone_field_required_field.text)
        status = '{"added":2,"error":{"missingRequired":[{"last name":"Name_Last30_2","first name":"Name_First30_2","agent id":"Test30.2","date/time":"02-07-2030","caller id":"100302","integer":"123302","phone1":"90302"}]}}'
        assert status in str(
            add_many_records_post_request_without_a_phone_field_required_field.text), "Answer text not " + status + " ; actual message : " + str(
            add_many_records_post_request_without_a_phone_field_required_field.text)


@pytest.mark.usefixtures("add_many_records_post_request_without_a_phone_field_required_field_and_key")
class Test_post_request_without_a_phone_field_required_field_and_key():
    @allure.epic("test_add_many_records")
    @allure.feature("answer code 200")
    @allure.step('test_check_status_code_post_request_without_a_phone_field_required_field_and_key')
    def test_check_status_code_post_request_without_a_phone_field_required_field_and_key(self, add_many_records_post_request_without_a_phone_field_required_field_and_key):
        print("request_result_status_code : ", add_many_records_post_request_without_a_phone_field_required_field_and_key.status_code)
        assert "200" in str(
            add_many_records_post_request_without_a_phone_field_required_field_and_key.status_code), "Answer status not 200 ; actual status code : " + str(
            add_many_records_post_request_without_a_phone_field_required_field_and_key.status_code)

    @allure.epic("test_add_many_records")
    @allure.feature("answer code 200")
    @allure.step('test_check_answer_text_post_request_without_a_phone_field_required_field_and_key')
    def test_check_answer_text_post_request_without_a_phone_field_required_field_and_key(self, add_many_records_post_request_without_a_phone_field_required_field_and_key):
        print("request_result_text : ", add_many_records_post_request_without_a_phone_field_required_field_and_key.text)
        status = '{"added":2,"error":{"missingKey":[{"last name":"Name_Last31_2","first name":"Name_First31_2","agent id":"Test31.2","phone2":"9312","date/time":"02-07-2031","caller id":"100312","integer":"123312"}]}}'
        assert status in str(
            add_many_records_post_request_without_a_phone_field_required_field_and_key.text), "Answer text not " + status + " ; actual message : " + str(
            add_many_records_post_request_without_a_phone_field_required_field_and_key.text)


@pytest.mark.usefixtures("add_many_records_post_request_without_a_phone_field_empty_value")
class Test_post_request_without_a_phone_field_empty_value():
    @allure.epic("test_add_many_records")
    @allure.feature("answer code 200")
    @allure.step('test_check_status_code_post_request_without_a_phone_field_empty_value')
    def test_check_status_code_post_request_without_a_phone_field_empty_value(self, add_many_records_post_request_without_a_phone_field_empty_value):
        print("request_result_status_code : ", add_many_records_post_request_without_a_phone_field_empty_value.status_code)
        assert "200" in str(
            add_many_records_post_request_without_a_phone_field_empty_value.status_code), "Answer status not 200 ; actual status code : " + str(
            add_many_records_post_request_without_a_phone_field_empty_value.status_code)

    @allure.epic("test_add_many_records")
    @allure.feature("answer code 200")
    @allure.step('test_check_answer_text_post_request_without_a_phone_field_empty_value')
    def test_check_answer_text_post_request_without_a_phone_field_empty_value(self, add_many_records_post_request_without_a_phone_field_empty_value):
        print("request_result_text : ", add_many_records_post_request_without_a_phone_field_empty_value.text)
        status = '{"added":2,"error":{"missingKey":[{"last name":"Name_Last32_2","first name":"Name_First32_2","agent id":"Test32.2","phone2":"9322","date/time":"02-07-2032","caller id":"100322","integer":"123322","phone1":""}]}}'
        assert status in str(
            add_many_records_post_request_without_a_phone_field_empty_value.text), "Answer text not " + status + " ; actual message : " + str(
            add_many_records_post_request_without_a_phone_field_empty_value.text)


@pytest.mark.usefixtures("add_many_records_post_request_without_a_phone_field_space_in_a_key_field")
class Test_post_request_without_a_phone_field_space_in_a_key_field():
    @allure.epic("test_add_many_records")
    @allure.feature("answer code 200")
    @allure.step('test_check_status_code_post_request_without_a_phone_field_space_in_a_key_field')
    def test_check_status_code_post_request_without_a_phone_field_space_in_a_key_field(self, add_many_records_post_request_without_a_phone_field_space_in_a_key_field):
        print("request_result_status_code : ", add_many_records_post_request_without_a_phone_field_space_in_a_key_field.status_code)
        assert "200" in str(
            add_many_records_post_request_without_a_phone_field_space_in_a_key_field.status_code), "Answer status not 200 ; actual status code : " + str(
            add_many_records_post_request_without_a_phone_field_space_in_a_key_field.status_code)

    @allure.epic("test_add_many_records")
    @allure.feature("answer code 200")
    @allure.step('test_check_answer_text_post_request_without_a_phone_field_space_in_a_key_field')
    def test_check_answer_text_post_request_without_a_phone_field_space_in_a_key_field(self, add_many_records_post_request_without_a_phone_field_space_in_a_key_field):
        print("request_result_text : ", add_many_records_post_request_without_a_phone_field_space_in_a_key_field.text)
        status = '{"added":2,"error":{"missingKey":[{"last name":"Name_Last33_2","first name":"Name_First33_2","agent id":"Test33.2","phone2":"9332","date/time":"02-07-2033","caller id":"100332","integer":"123332","phone1":" "}]}}'
        assert status in str(
            add_many_records_post_request_without_a_phone_field_space_in_a_key_field.text), "Answer text not " + status + " ; actual message : " + str(
            add_many_records_post_request_without_a_phone_field_space_in_a_key_field.text)

@allure.issue("https://trac.brightpattern.com/ticket/24410")
@pytest.mark.usefixtures("add_many_records_post_request_with_an_incorrectly_formatted_phone_number_in_a_phone_field_non_numeric_symbol_other_than_plus")
class Test_post_request_with_an_incorrectly_formatted_phone_number_in_a_phone_field_non_numeric_symbol_other_than_plus():
    @allure.epic("test_add_many_records")
    @allure.feature("answer code 200")
    @allure.step('test_check_status_code_post_request_with_an_incorrectly_formatted_phone_number_in_a_phone_field_non_numeric_symbol_other_than_plus')
    def test_check_status_code_post_request_with_an_incorrectly_formatted_phone_number_in_a_phone_field_non_numeric_symbol_other_than_plus(self, add_many_records_post_request_with_an_incorrectly_formatted_phone_number_in_a_phone_field_non_numeric_symbol_other_than_plus):
        print("request_result_status_code : ", add_many_records_post_request_with_an_incorrectly_formatted_phone_number_in_a_phone_field_non_numeric_symbol_other_than_plus.status_code)
        assert "200" in str(
            add_many_records_post_request_with_an_incorrectly_formatted_phone_number_in_a_phone_field_non_numeric_symbol_other_than_plus.status_code), "Answer status not 200 ; actual status code : " + str(
            add_many_records_post_request_with_an_incorrectly_formatted_phone_number_in_a_phone_field_non_numeric_symbol_other_than_plus.status_code)

    @allure.epic("test_add_many_records")
    @allure.feature("answer code 200")
    @allure.step('test_check_answer_text_post_request_with_an_incorrectly_formatted_phone_number_in_a_phone_field_non_numeric_symbol_other_than_plus')
    def test_check_answer_text_post_request_with_an_incorrectly_formatted_phone_number_in_a_phone_field_non_numeric_symbol_other_than_plus(self, add_many_records_post_request_with_an_incorrectly_formatted_phone_number_in_a_phone_field_non_numeric_symbol_other_than_plus):
        print("request_result_text : ", add_many_records_post_request_with_an_incorrectly_formatted_phone_number_in_a_phone_field_non_numeric_symbol_other_than_plus.text)
        status = '{"added":2} <Fill this response>'
        assert status in str(
            add_many_records_post_request_with_an_incorrectly_formatted_phone_number_in_a_phone_field_non_numeric_symbol_other_than_plus.text), "Answer text not " + status + " ; actual message : " + str(
            add_many_records_post_request_with_an_incorrectly_formatted_phone_number_in_a_phone_field_non_numeric_symbol_other_than_plus.text)

@allure.issue("https://trac.brightpattern.com/ticket/24411")
@pytest.mark.usefixtures("add_many_records_post_request_with_an_incorrectly_formatted_phone_number_in_a_phone_field_the_country_set_for_us_and_canada_the_number_starts_with_1_and_has_less_than_11")
class Test_post_request_with_an_incorrectly_formatted_phone_number_in_a_phone_field_the_country_set_for_us_and_canada_the_number_starts_with_1_and_has_less_than_11():
    @allure.epic("test_add_many_records")
    @allure.feature("answer code 200")
    @allure.step('test_check_status_code_post_request_with_an_incorrectly_formatted_phone_number_in_a_phone_field_the_country_set_for_us_and_canada_the_number_starts_with_1_and_has_less_than_11')
    def test_check_status_code_post_request_with_an_incorrectly_formatted_phone_number_in_a_phone_field_the_country_set_for_us_and_canada_the_number_starts_with_1_and_has_less_than_11(self, add_many_records_post_request_with_an_incorrectly_formatted_phone_number_in_a_phone_field_the_country_set_for_us_and_canada_the_number_starts_with_1_and_has_less_than_11):
        print("request_result_status_code : ", add_many_records_post_request_with_an_incorrectly_formatted_phone_number_in_a_phone_field_the_country_set_for_us_and_canada_the_number_starts_with_1_and_has_less_than_11.status_code)
        assert "200" in str(
            add_many_records_post_request_with_an_incorrectly_formatted_phone_number_in_a_phone_field_the_country_set_for_us_and_canada_the_number_starts_with_1_and_has_less_than_11.status_code), "Answer status not 200 ; actual status code : " + str(
            add_many_records_post_request_with_an_incorrectly_formatted_phone_number_in_a_phone_field_the_country_set_for_us_and_canada_the_number_starts_with_1_and_has_less_than_11.status_code)

    @allure.epic("test_add_many_records")
    @allure.feature("answer code 200")
    @allure.step('test_check_answer_text_post_request_with_an_incorrectly_formatted_phone_number_in_a_phone_field_the_country_set_for_us_and_canada_the_number_starts_with_1_and_has_less_than_11')
    def test_check_answer_text_post_request_with_an_incorrectly_formatted_phone_number_in_a_phone_field_the_country_set_for_us_and_canada_the_number_starts_with_1_and_has_less_than_11(self, add_many_records_post_request_with_an_incorrectly_formatted_phone_number_in_a_phone_field_the_country_set_for_us_and_canada_the_number_starts_with_1_and_has_less_than_11):
        print("request_result_text : ", add_many_records_post_request_with_an_incorrectly_formatted_phone_number_in_a_phone_field_the_country_set_for_us_and_canada_the_number_starts_with_1_and_has_less_than_11.text)
        status = '{"added":2} <Fill this response>'
        assert status in str(
            add_many_records_post_request_with_an_incorrectly_formatted_phone_number_in_a_phone_field_the_country_set_for_us_and_canada_the_number_starts_with_1_and_has_less_than_11.text), "Answer text not " + status + " ; actual message : " + str(
            add_many_records_post_request_with_an_incorrectly_formatted_phone_number_in_a_phone_field_the_country_set_for_us_and_canada_the_number_starts_with_1_and_has_less_than_11.text)


@pytest.mark.usefixtures("add_many_records_post_request_with_do_not_authorize_session")
class Test_post_request_with_do_not_authorize_session():
    @allure.epic("test_add_many_records")
    @allure.feature("answer code 401")
    @allure.step('test_check_status_code_post_request_with_do_not_authorize_session')
    def test_check_status_code_post_request_with_do_not_authorize_session(self,
                                                                          add_many_records_post_request_with_do_not_authorize_session):
        print("request_result_status_code : ", add_many_records_post_request_with_do_not_authorize_session.status_code)
        assert "401" in str(
            add_many_records_post_request_with_do_not_authorize_session.status_code), "Answer status not 401 ; actual status code : " + str(
            add_many_records_post_request_with_do_not_authorize_session.status_code)

    @allure.epic("test_add_many_records")
    @allure.feature("answer code 401")
    @allure.step('test_check_answer_text_post_request_with_do_not_authorize_session')
    def test_check_answer_text_post_request_with_do_not_authorize_session(self,
                                                                          add_many_records_post_request_with_do_not_authorize_session):
        print("request_result_text : ", add_many_records_post_request_with_do_not_authorize_session.text)
        status = "Session is not authenticated"
        assert status in str(
            add_many_records_post_request_with_do_not_authorize_session.text), "Answer text not " + status + " ; actual message : " + str(
            add_many_records_post_request_with_do_not_authorize_session.text)


@allure.issue("https://trac.brightpattern.com/ticket/24588")
@pytest.mark.usefixtures("add_many_records_post_request_with_authorize_session_for_user_without_permission")
class Test_post_request_with_authorize_session_for_user_without_permission():
    @allure.epic("test_add_many_records")
    @allure.feature("answer code 403")
    @allure.step('test_check_status_code_post_request_with_authorize_session_for_user_without_permission')
    def test_check_status_code_post_request_with_authorize_session_for_user_without_permission(self,
                                                                                               add_many_records_post_request_with_authorize_session_for_user_without_permission):
        print("request_result_status_code : ", add_many_records_post_request_with_authorize_session_for_user_without_permission.status_code)
        assert "403" in str(
            add_many_records_post_request_with_authorize_session_for_user_without_permission.status_code), "Answer status not 403 ; actual status code : " + str(
            add_many_records_post_request_with_authorize_session_for_user_without_permission.status_code)

    @allure.epic("test_add_many_records")
    @allure.feature("answer code 403")
    @allure.step('test_check_answer_text_post_request_with_authorize_session_for_user_without_permission')
    def test_check_answer_text_post_request_with_authorize_session_for_user_without_permission(self,
                                                                                               add_many_records_post_request_with_authorize_session_for_user_without_permission):
        print("request_result_text : ", add_many_records_post_request_with_authorize_session_for_user_without_permission.text)
        status = "Access denied addAll"
        assert status in str(
            add_many_records_post_request_with_authorize_session_for_user_without_permission.text), "Answer text not " + status + " ; actual message : " + str(
            add_many_records_post_request_with_authorize_session_for_user_without_permission.text)


@pytest.mark.usefixtures("add_many_records_post_request_without_parameters_empty_body")
class Test_post_request_without_parameters_empty_body():
    @allure.epic("test_add_many_records")
    @allure.feature("answer code 200")
    @allure.step('test_check_status_code_post_request_without_parameters_empty_body')
    def test_check_status_code_post_request_without_parameters_empty_body(self, add_many_records_post_request_without_parameters_empty_body):
        print("request_result_status_code : ", add_many_records_post_request_without_parameters_empty_body.status_code)
        assert "200" in str(
            add_many_records_post_request_without_parameters_empty_body.status_code), "Answer status not 200 ; actual status code : " + str(
            add_many_records_post_request_without_parameters_empty_body.status_code)

    @allure.epic("test_add_many_records")
    @allure.feature("answer code 200")
    @allure.step('test_check_answer_text_post_request_without_parameters_empty_body')
    def test_check_answer_text_post_request_without_parameters_empty_body(self, add_many_records_post_request_without_parameters_empty_body):
        print("request_result_text : ", add_many_records_post_request_without_parameters_empty_body.text)
        status = "{\"added\":0}"
        assert status in str(
            add_many_records_post_request_without_parameters_empty_body.text), "Answer text not " + status + " ; actual message : " + str(
            add_many_records_post_request_without_parameters_empty_body.text)

@allure.issue("https://trac.brightpattern.com/ticket/24403")
@pytest.mark.usefixtures("add_many_records_post_request_with_a_duplicated_in_one_request_values")
class Test_post_request_with_a_duplicated_in_one_request_values():
    @allure.epic("test_add_many_records")
    @allure.feature("answer code 200")
    @allure.step('test_check_status_code_post_request_with_a_duplicated_in_one_request_values')
    def test_check_status_code_post_request_with_a_duplicated_in_one_request_values(self, add_many_records_post_request_with_a_duplicated_in_one_request_values):
        print("request_result_status_code : ", add_many_records_post_request_with_a_duplicated_in_one_request_values.status_code)
        assert "200" in str(
            add_many_records_post_request_with_a_duplicated_in_one_request_values.status_code), "Answer status not 200 ; actual status code : " + str(
            add_many_records_post_request_with_a_duplicated_in_one_request_values.status_code)

    @allure.epic("test_add_many_records")
    @allure.feature("answer code 200")
    @allure.step('test_check_answer_text_post_request_with_a_duplicated_in_one_request_values')
    def test_check_answer_text_post_request_with_a_duplicated_in_one_request_values(self, add_many_records_post_request_with_a_duplicated_in_one_request_values):
        print("request_result_text : ", add_many_records_post_request_with_a_duplicated_in_one_request_values.text)
        status = '{"added":1,"error":{"missingRequired":[{"last name":"User8","first name":"Test8"}],"missingKey":[{"last name":"User6","phone1":"1006"},{"last name":"User7","incorrect":"Test7","phone1":"1007"}],"duplicateKey":[{"last name":"User11","first name":"Test11","phone":"1011"}]}}'
        assert status in str(
            add_many_records_post_request_with_a_duplicated_in_one_request_values.text), "Answer text not " + status + " ; actual message : " + str(
            add_many_records_post_request_with_a_duplicated_in_one_request_values.text)

@allure.issue("https://trac.brightpattern.com/ticket/21501")
#@allure.issue("https://trac.brightpattern.com/ticket/24409")
@pytest.mark.usefixtures("add_many_records_post_request_with_an_incorrect_body_format")
class Test_post_request_with_an_incorrect_body_format():
    @allure.epic("test_add_many_records")
    @allure.feature("answer code 200")
    @allure.step('test_check_status_code_post_request_with_an_incorrect_body_format')
    def test_check_status_code_post_request_with_an_incorrect_body_format(self, add_many_records_post_request_with_an_incorrect_body_format):
        print("request_result_status_code : ", add_many_records_post_request_with_an_incorrect_body_format.status_code)
        assert "200" in str(
            add_many_records_post_request_with_an_incorrect_body_format.status_code), "Answer status not 200 ; actual status code : " + str(
            add_many_records_post_request_with_an_incorrect_body_format.status_code)

    @allure.epic("test_add_many_records")
    @allure.feature("answer code 200")
    @allure.step('test_check_answer_text_post_request_with_an_incorrect_body_format')
    def test_check_answer_text_post_request_with_an_incorrect_body_format(self, add_many_records_post_request_with_an_incorrect_body_format):
        print("request_result_text : ", add_many_records_post_request_with_an_incorrect_body_format.text)
        status = '{"added": 1,"error": {"formatError": [{"first name":"Test17",phone1:10017"]}}}'
        assert status in str(
            add_many_records_post_request_with_an_incorrect_body_format.text), "Answer text not " + status + " ; actual message : " + str(
            add_many_records_post_request_with_an_incorrect_body_format.text)


@pytest.mark.usefixtures("add_many_records_post_request_with_an_incorrect_body_format_redundant_comma_in_the_end")
class Test_post_request_with_an_incorrect_body_format_redundant_comma_in_the_end():
    @allure.epic("test_add_many_records")
    @allure.feature("answer code 400")
    @allure.step('test_check_status_code_post_request_with_an_incorrect_body_format_redundant_comma_in_the_end')
    def test_check_status_code_post_request_with_an_incorrect_body_format_redundant_comma_in_the_end(self,
                                                                                  add_many_records_post_request_with_an_incorrect_body_format_redundant_comma_in_the_end):
        print("request_result_status_code : ", add_many_records_post_request_with_an_incorrect_body_format_redundant_comma_in_the_end.status_code)
        assert "400" in str(
            add_many_records_post_request_with_an_incorrect_body_format_redundant_comma_in_the_end.status_code), "Answer status not 400 ; actual status code : " + str(
            add_many_records_post_request_with_an_incorrect_body_format_redundant_comma_in_the_end.status_code)

    @allure.epic("test_add_many_records")
    @allure.feature("answer code 400")
    @allure.step('test_check_answer_text_post_request_with_an_incorrect_body_format_redundant_comma_in_the_end')
    def test_check_answer_text_post_request_with_an_incorrect_body_format_redundant_comma_in_the_end(self,
                                                                                  add_many_records_post_request_with_an_incorrect_body_format_redundant_comma_in_the_end):
        print("request_result_text : ", add_many_records_post_request_with_an_incorrect_body_format_redundant_comma_in_the_end.text)
        status = "Unterminated array at line 1 column 84 path $[2]"
        assert status in str(
            add_many_records_post_request_with_an_incorrect_body_format_redundant_comma_in_the_end.text), "Answer text not " + status + " ; actual message : " + str(
            add_many_records_post_request_with_an_incorrect_body_format_redundant_comma_in_the_end.text)


@pytest.mark.usefixtures("add_many_records_post_request_to_the_non_existent_list")
class Test_post_request_to_the_non_existent_list():
    @allure.epic("test_add_many_records")
    @allure.feature("answer code 404")
    @allure.step('test_check_status_code_post_request_to_the_non_existent_list')
    def test_check_status_code_post_request_to_the_non_existent_list(self, add_many_records_post_request_to_the_non_existent_list):
        print("request_result_status_code : ", add_many_records_post_request_to_the_non_existent_list.status_code)
        assert "404" in str(
            add_many_records_post_request_to_the_non_existent_list.status_code), "Answer status not 404 ; actual status code : " + str(
            add_many_records_post_request_to_the_non_existent_list.status_code)

    @allure.epic("test_add_many_records")
    @allure.feature("answer code 404")
    @allure.step('test_check_answer_text_post_request_to_the_non_existent_list')
    def test_check_answer_text_post_request_to_the_non_existent_list(self, add_many_records_post_request_to_the_non_existent_list):
        print("request_result_text : ", add_many_records_post_request_to_the_non_existent_list.text)
        status = "calling list not found"
        assert status in str(
            add_many_records_post_request_to_the_non_existent_list.text), "Answer text not " + status + " ; actual message : " + str(
            add_many_records_post_request_to_the_non_existent_list.text)


@pytest.mark.usefixtures("add_many_records_post_request_with_invalid_url")
class Test_post_request_with_invalid_url():
    @allure.epic("test_add_many_records")
    @allure.feature("answer code 404")
    @allure.step('test_check_status_code_post_request_with_invalid_url')
    def test_check_status_code_post_request_with_invalid_url(self, add_many_records_post_request_with_invalid_url):
        print("request_result_status_code : ", add_many_records_post_request_with_invalid_url.status_code)
        assert "404" in str(
            add_many_records_post_request_with_invalid_url.status_code), "Answer status not 404 ; actual status code : " + str(
            add_many_records_post_request_with_invalid_url.status_code)

    @allure.epic("test_add_many_records")
    @allure.feature("answer code 404")
    @allure.step('test_check_answer_text_post_request_with_invalid_url')
    def test_check_answer_text_post_request_with_invalid_url(self, add_many_records_post_request_with_invalid_url):
        print("request_result_text : ", add_many_records_post_request_with_invalid_url.text)
        status = "HTTP 404 Not Found"
        assert status in str(
            add_many_records_post_request_with_invalid_url.text), "Answer text not " + status + " ; actual message : " + str(
            add_many_records_post_request_with_invalid_url.text)


@allure.issue("https://trac.brightpattern.com/ticket/24412")
@pytest.mark.usefixtures("add_many_records_post_request_with_incorrectly_formatted_phone_number_in_a_phone_field")
class Test_post_request_with_incorrectly_formatted_phone_number_in_a_phone_field():
    @allure.epic("test_add_many_records")
    @allure.feature("answer code 200")
    @allure.step('test_check_status_code_post_request_with_incorrectly_formatted_phone_number_in_a_phone_field')
    def test_check_status_code_post_request_with_incorrectly_formatted_phone_number_in_a_phone_field(self, add_many_records_post_request_with_incorrectly_formatted_phone_number_in_a_phone_field):
        print("request_result_status_code : ", add_many_records_post_request_with_incorrectly_formatted_phone_number_in_a_phone_field.status_code)
        assert "200" in str(
            add_many_records_post_request_with_incorrectly_formatted_phone_number_in_a_phone_field.status_code), "Answer status not 200 ; actual status code : " + str(
            add_many_records_post_request_with_incorrectly_formatted_phone_number_in_a_phone_field.status_code)

    @allure.epic("test_add_many_records")
    @allure.feature("answer code 200")
    @allure.step('test_check_answer_text_post_request_with_incorrectly_formatted_phone_number_in_a_phone_field')
    def test_check_answer_text_post_request_with_incorrectly_formatted_phone_number_in_a_phone_field(self, add_many_records_post_request_with_incorrectly_formatted_phone_number_in_a_phone_field):
        print("request_result_text : ", add_many_records_post_request_with_incorrectly_formatted_phone_number_in_a_phone_field.text)
        status = '{"added": 1,"error": {"formatError": [{"first name":"Test14","phone":"1qwerty00014"]}}}'
        assert status in str(
            add_many_records_post_request_with_incorrectly_formatted_phone_number_in_a_phone_field.text), "Answer text not " + status + " ; actual message : " + str(
            add_many_records_post_request_with_incorrectly_formatted_phone_number_in_a_phone_field.text)


#@allure.issue("https://trac.brightpattern.com/ticket/24396")
@pytest.mark.usefixtures("add_many_records_get_request_with_correct_body")
class Test_get_request_with_correct_body():
    @allure.epic("test_add_many_records")
    @allure.feature("answer code 405")
    @allure.step('test_check_status_code_get_request_with_correct_body')
    def test_check_status_code_get_request_with_correct_body(self, add_many_records_get_request_with_correct_body):
        print("request_result_status_code : ", add_many_records_get_request_with_correct_body.status_code)
        assert "405" in str(
            add_many_records_get_request_with_correct_body.status_code), "Answer status not 405 ; actual status code : " + str(
            add_many_records_get_request_with_correct_body.status_code)

    @allure.epic("test_add_many_records")
    @allure.feature("answer code 405")
    @allure.step('test_check_answer_text_get_request_with_correct_body')
    def test_check_answer_text_get_request_with_correct_body(self, add_many_records_get_request_with_correct_body):
        print("request_result_text : ", add_many_records_get_request_with_correct_body.text)
        status = "Method Not Allowed"
        assert status in str(
            add_many_records_get_request_with_correct_body.text), "Answer text not " + status + " ; actual message : " + str(
            add_many_records_get_request_with_correct_body.text)


#@allure.issue("https://trac.brightpattern.com/ticket/24396")
@pytest.mark.usefixtures("add_many_records_put_request_with_correct_body")
class Test_put_request_with_correct_body():
    @allure.epic("test_add_many_records")
    @allure.feature("answer code 405")
    @allure.step('test_check_status_code_put_request_with_correct_body')
    def test_check_status_code_put_request_with_correct_body(self, add_many_records_put_request_with_correct_body):
        print("request_result_status_code : ", add_many_records_put_request_with_correct_body.status_code)
        assert "405" in str(
            add_many_records_put_request_with_correct_body.status_code), "Answer status not 405 ; actual status code : " + str(
            add_many_records_put_request_with_correct_body.status_code)

    @allure.epic("test_add_many_records")
    @allure.feature("answer code 405")
    @allure.step('test_check_answer_text_put_request_with_correct_body')
    def test_check_answer_text_put_request_with_correct_body(self, add_many_records_put_request_with_correct_body):
        print("request_result_text : ", add_many_records_put_request_with_correct_body.text)
        status = "Method Not Allowed"
        assert status in str(
            add_many_records_put_request_with_correct_body.text), "Answer text not " + status + " ; actual message : " + str(
            add_many_records_put_request_with_correct_body.text)


#@allure.issue("https://trac.brightpattern.com/ticket/24396")
@pytest.mark.usefixtures("add_many_records_delete_request_with_correct_body")
class Test_delete_request_with_correct_body():
    @allure.epic("test_add_many_records")
    @allure.feature("answer code 405")
    @allure.step('test_check_status_code_delete_request_with_correct_body')
    def test_check_status_code_delete_request_with_correct_body(self, add_many_records_delete_request_with_correct_body):
        print("request_result_status_code : ", add_many_records_delete_request_with_correct_body.status_code)
        assert "405" in str(
            add_many_records_delete_request_with_correct_body.status_code), "Answer status not 405 ; actual status code : " + str(
            add_many_records_delete_request_with_correct_body.status_code)

    @allure.epic("test_add_many_records")
    @allure.feature("answer code 405")
    @allure.step('test_check_answer_text_delete_request_with_correct_body')
    def test_check_answer_text_delete_request_with_correct_body(self, add_many_records_delete_request_with_correct_body):
        print("request_result_text : ", add_many_records_delete_request_with_correct_body.text)
        status = "Method Not Allowed"
        assert status in str(
            add_many_records_delete_request_with_correct_body.text), "Answer text not " + status + " ; actual message : " + str(
            add_many_records_delete_request_with_correct_body.text)


@allure.issue("https://trac.brightpattern.com/ticket/24404")
@pytest.mark.usefixtures("add_many_records_post_request_with_body_from_other_list")
class Test_post_request_with_body_from_other_list():
    @allure.epic("test_add_many_records")
    @allure.feature("answer code 400")
    @allure.step('test_check_status_code_post_request_with_body_from_other_list')
    def test_check_status_code_post_request_with_body_from_other_list(self, add_many_records_post_request_with_body_from_other_list):
        print("request_result_status_code : ", add_many_records_post_request_with_body_from_other_list.status_code)
        assert "400" in str(
            add_many_records_post_request_with_body_from_other_list.status_code), "Answer status not 400 ; actual status code : " + str(
            add_many_records_post_request_with_body_from_other_list.status_code)

    @allure.epic("test_add_many_records")
    @allure.feature("answer code 400")
    @allure.step('test_check_answer_text_post_request_with_body_from_other_list')
    def test_check_answer_text_post_request_with_body_from_other_list(self, add_many_records_post_request_with_body_from_other_list):
        print("request_result_text : ", add_many_records_post_request_with_body_from_other_list.text)
        status = "Some valid message"
        assert status in str(
            add_many_records_post_request_with_body_from_other_list.text), "Answer text not " + status + " ; actual message : " + str(
            add_many_records_post_request_with_body_from_other_list.text)
