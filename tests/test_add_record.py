import allure
import pytest

#=======================================================================================================================
#==================================================== Code 200 =========================================================
#=======================================================================================================================

# @allure.issue("https://trac.brightpattern.com/ticket/24242")
@pytest.mark.usefixtures("add_record_post_request_with_correct_body")
#@pytest.mark.parametrize("add_record_post_request_with_correct_body",["body", "url_path"], [({"Integer": "123","Date/Time": "03-07-2025","Caller id": "Test3","Agent id": "Test3","First name": "Name_First3","Last name": "Name_Last3","Phone1": "9003","Phone2": "9010"}, "add//List_1.txt")])
#class Test_post_request_with_correct_body("add_record_post_request_with_correct_body"):
class Test_post_request_with_correct_body():
    @allure.epic("test_add_record")
    @allure.feature("answer code 200")
    @allure.step('test_check_status_code_post_request_with_correct_body')
    def test_check_status_code_post_request_with_correct_body(self, add_record_post_request_with_correct_body):
        print("request_result_status_code : ", add_record_post_request_with_correct_body.status_code)
        assert "200" in str(
            add_record_post_request_with_correct_body.status_code), "Answer status not 200 ; actual status code : " + str(
            add_record_post_request_with_correct_body.status_code)

    @allure.epic("test_add_record")
    @allure.feature("answer code 200")
    @allure.step('test_check_answer_text_post_request_with_correct_body')
    def test_check_answer_text_post_request_with_correct_body(self, add_record_post_request_with_correct_body):
        print("request_result_text : ", add_record_post_request_with_correct_body.text)
        assert len(str(
            add_record_post_request_with_correct_body.text)) == 0, "Answer text not empty ; actual message : " + str(
            add_record_post_request_with_correct_body.text)


# @allure.issue("https://trac.brightpattern.com/ticket/24228")
@pytest.mark.usefixtures("add_record_post_request_with_incorrectly_formatted_phone_number_in_a_caller_id_field")
class Test_post_request_with_incorrectly_formatted_phone_number_in_a_caller_id_field():
    @allure.epic("test_add_record")
    @allure.feature("answer code 200")
    @allure.step('test_check_status_code_post_request_with_incorrectly_formatted_phone_number_in_a_caller_id_field')
    def test_check_status_code_post_request_with_incorrectly_formatted_phone_number_in_a_caller_id_field(self,
                                                                                                         add_record_post_request_with_incorrectly_formatted_phone_number_in_a_caller_id_field):
        print("request_result_status_code : ", add_record_post_request_with_incorrectly_formatted_phone_number_in_a_caller_id_field.status_code)
        assert "200" in str(
            add_record_post_request_with_incorrectly_formatted_phone_number_in_a_caller_id_field.status_code), "Answer status not 200 ; actual status code : " + str(
            add_record_post_request_with_incorrectly_formatted_phone_number_in_a_caller_id_field.status_code)

    @allure.epic("test_add_record")
    @allure.feature("answer code 200")
    @allure.step('test_check_answer_text_post_request_with_incorrectly_formatted_phone_number_in_a_caller_id_field')
    def test_check_answer_text_post_request_with_incorrectly_formatted_phone_number_in_a_caller_id_field(self,
                                                                                                         add_record_post_request_with_incorrectly_formatted_phone_number_in_a_caller_id_field):
        print("request_result_text : ", add_record_post_request_with_incorrectly_formatted_phone_number_in_a_caller_id_field.text)
        assert len(str(
            add_record_post_request_with_incorrectly_formatted_phone_number_in_a_caller_id_field.text)) == 0, "Answer text not empty ; actual message : " + str(
            add_record_post_request_with_incorrectly_formatted_phone_number_in_a_caller_id_field.text)


@pytest.mark.usefixtures("add_record_post_request_with_non_existent_agent_username_in_an_agent_login_id_field")
class Test_post_request_with_non_existent_agent_username_in_an_agent_login_id_field():
    @allure.epic("test_add_record")
    @allure.feature("answer code 200")
    @allure.step('test_check_status_code_post_request_with_non_existent_agent_username_in_an_agent_login_id_field')
    def test_check_status_code_post_request_with_non_existent_agent_username_in_an_agent_login_id_field(self,
                                                                                                        add_record_post_request_with_non_existent_agent_username_in_an_agent_login_id_field):
        print("request_result_status_code : ", add_record_post_request_with_non_existent_agent_username_in_an_agent_login_id_field.status_code)
        assert "200" in str(
            add_record_post_request_with_non_existent_agent_username_in_an_agent_login_id_field.status_code), "Answer status not 200 ; actual status code : " + str(
            add_record_post_request_with_non_existent_agent_username_in_an_agent_login_id_field.status_code)

    @allure.epic("test_add_record")
    @allure.feature("answer code 200")
    @allure.step('test_check_answer_text_post_request_with_non_existent_agent_username_in_an_agent_login_id_field')
    def test_check_answer_text_post_request_with_non_existent_agent_username_in_an_agent_login_id_field(self,
                                                                                                        add_record_post_request_with_non_existent_agent_username_in_an_agent_login_id_field):
        print("request_result_text : ", add_record_post_request_with_non_existent_agent_username_in_an_agent_login_id_field.text)
        assert len(str(
            add_record_post_request_with_non_existent_agent_username_in_an_agent_login_id_field.text)) == 0, "Answer text not empty ; actual message : " + str(
            add_record_post_request_with_non_existent_agent_username_in_an_agent_login_id_field.text)


@pytest.mark.usefixtures("add_record_post_request_with_a_date_time_field_set_to_a_moment_in_the_past")
class Test_post_request_with_a_date_time_field_set_to_a_moment_in_the_past():
    @allure.epic("test_add_record")
    @allure.feature("answer code 200")
    @allure.step('test_check_status_code_post_request_with_a_date_time_field_set_to_a_moment_in_the_past')
    def test_check_status_code_post_request_with_a_date_time_field_set_to_a_moment_in_the_past(self,
                                                                                               add_record_post_request_with_a_date_time_field_set_to_a_moment_in_the_past):
        print("request_result_status_code : ", add_record_post_request_with_a_date_time_field_set_to_a_moment_in_the_past.status_code)
        assert "200" in str(
            add_record_post_request_with_a_date_time_field_set_to_a_moment_in_the_past.status_code), "Answer status not 200 ; actual status code : " + str(
            add_record_post_request_with_a_date_time_field_set_to_a_moment_in_the_past.status_code)

    @allure.epic("test_add_record")
    @allure.feature("answer code 200")
    @allure.step('test_check_answer_text_post_request_with_a_date_time_field_set_to_a_moment_in_the_past')
    def test_check_answer_text_post_request_with_a_date_time_field_set_to_a_moment_in_the_past(self,
                                                                                               add_record_post_request_with_a_date_time_field_set_to_a_moment_in_the_past):
        print("request_result_text : ", add_record_post_request_with_a_date_time_field_set_to_a_moment_in_the_past.text)
        assert len(str(
            add_record_post_request_with_a_date_time_field_set_to_a_moment_in_the_past.text)) == 0, "Answer text not empty ; actual message : " + str(
            add_record_post_request_with_a_date_time_field_set_to_a_moment_in_the_past.text)


#@allure.issue("https://trac.brightpattern.com/ticket/24228")
@pytest.mark.usefixtures("add_record_post_request_without_a_last_name_fields")
class Test_post_request_without_a_last_name_fields():
    @allure.epic("test_add_record")
    @allure.feature("answer code 200")
    @allure.step('test_check_status_code_post_request_without_a_last_name_fields')
    def test_check_status_code_post_request_without_a_last_name_fields(self, add_record_post_request_without_a_last_name_fields):
        print("request_result_status_code : ", add_record_post_request_without_a_last_name_fields.status_code)
        assert "200" in str(
            add_record_post_request_without_a_last_name_fields.status_code), "Answer status not 200 ; actual status code : " + str(
            add_record_post_request_without_a_last_name_fields.status_code)

    @allure.epic("test_add_record")
    @allure.feature("answer code 200")
    @allure.step('test_check_answer_text_post_request_without_a_last_name_fields')
    def test_check_answer_text_post_request_without_a_last_name_fields(self, add_record_post_request_without_a_last_name_fields):
        print("request_result_text : ", add_record_post_request_without_a_last_name_fields.text)
        assert len(str(
            add_record_post_request_without_a_last_name_fields.text)) == 0, "Answer text not empty ; actual message : " + str(
            add_record_post_request_without_a_last_name_fields.text)


#@allure.issue("https://trac.brightpattern.com/ticket/24253")
@pytest.mark.usefixtures("add_record_post_request_with_the_value_phone_number_in_a_phone_field_using_symbol_plus")
class Test_post_request_with_the_value_phone_number_in_a_phone_field_using_symbol_plus():
    @allure.epic("test_add_record")
    @allure.feature("answer code 200")
    @allure.step('test_check_status_code_post_request_with_the_value_phone_number_in_a_phone_field_using_symbol_plus')
    def test_check_status_code_post_request_with_the_value_phone_number_in_a_phone_field_using_symbol_plus(self,
                                                                                                           add_record_post_request_with_the_value_phone_number_in_a_phone_field_using_symbol_plus):
        print("request_result_status_code : ", add_record_post_request_with_the_value_phone_number_in_a_phone_field_using_symbol_plus.status_code)
        assert "200" in str(
            add_record_post_request_with_the_value_phone_number_in_a_phone_field_using_symbol_plus.status_code), "Answer status not 200 ; actual status code : " + str(
            add_record_post_request_with_the_value_phone_number_in_a_phone_field_using_symbol_plus.status_code)

    @allure.epic("test_add_record")
    @allure.feature("answer code 200")
    @allure.step('test_check_answer_text_post_request_with_the_value_phone_number_in_a_phone_field_using_symbol_plus')
    def test_check_answer_text_post_request_with_the_value_phone_number_in_a_phone_field_using_symbol_plus(self,
                                                                                                           add_record_post_request_with_the_value_phone_number_in_a_phone_field_using_symbol_plus):
        print("request_result_text : ", add_record_post_request_with_the_value_phone_number_in_a_phone_field_using_symbol_plus.text)
        assert len(str(
            add_record_post_request_with_the_value_phone_number_in_a_phone_field_using_symbol_plus.text)) == 0, "Answer text not empty ; actual message : " + str(
            add_record_post_request_with_the_value_phone_number_in_a_phone_field_using_symbol_plus.text)

#=======================================================================================================================
#=======================================================================================================================
#=======================================================================================================================

#=======================================================================================================================
#==================================================== Code 409 =========================================================
#=======================================================================================================================

#@allure.issue("https://trac.brightpattern.com/ticket/21499")
#@allure.issue("https://trac.brightpattern.com/ticket/24228")
@allure.issue("https://trac.brightpattern.com/ticket/24597")
@pytest.mark.usefixtures("add_record_post_request_with_a_duplicate_earlier_created_keys")
class Test_post_request_with_a_duplicate_earlier_created_keys():
    @allure.epic("test_add_record")
    @allure.feature("answer code 409")
    @allure.step('test_check_status_code_post_request_with_a_duplicate_earlier_created_keys')
    def test_check_status_code_request_with_a_duplicate_earlier_created_keys(self,
                                                                             add_record_post_request_with_a_duplicate_earlier_created_keys):
        print("request_result_status_code : ", add_record_post_request_with_a_duplicate_earlier_created_keys.status_code)
        assert "409" in str(
            add_record_post_request_with_a_duplicate_earlier_created_keys.status_code), "Answer status not 409 ; actual status code : " + str(
            add_record_post_request_with_a_duplicate_earlier_created_keys.status_code)

    @allure.epic("test_add_record")
    @allure.feature("answer code 409")
    @allure.step('test_check_answer_text_request_with_a_duplicate_earlier_created_keys')
    def test_check_answer_text_request_with_a_duplicate_earlier_created_keys(self,
                                                                             add_record_post_request_with_a_duplicate_earlier_created_keys):
        print("request_result_text : ", add_record_post_request_with_a_duplicate_earlier_created_keys.text)
        status = 'E11000 duplicate key error collection: servicepattern.callingListeb3e7794085649949a502eed642b7d34 index: f6_1 dup key: { : "9003" }'
        assert status in str(
            add_record_post_request_with_a_duplicate_earlier_created_keys.text), "Answer text not " + status + " ; actual message : " + str(
            add_record_post_request_with_a_duplicate_earlier_created_keys.text)

#=======================================================================================================================
#=======================================================================================================================
#=======================================================================================================================

#=======================================================================================================================
#==================================================== Code 400 =========================================================
#=======================================================================================================================

# @allure.issue("https://trac.brightpattern.com/ticket/24230")
@pytest.mark.usefixtures("add_record_post_request_with_empty_key_field_account")
class Test_post_request_with_empty_key_field_account():
    @allure.epic("test_add_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_status_code_post_request_with_empty_key_field_account')
    def test_check_status_code_post_request_with_empty_key_field_account(self,
                                                                         add_record_post_request_with_empty_key_field_account):
        print("request_result_status_code : ", add_record_post_request_with_empty_key_field_account.status_code)
        assert "400" in str(
            add_record_post_request_with_empty_key_field_account.status_code), "Answer status not 400 ; actual status code : " + str(
            add_record_post_request_with_empty_key_field_account.status_code)

    @allure.epic("test_add_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_answer_text_post_request_with_empty_key_field_account')
    def test_check_answer_text_post_request_with_empty_key_field_account(self,
                                                                         add_record_post_request_with_empty_key_field_account):
        print("request_result_text : ", add_record_post_request_with_empty_key_field_account.text)
        status = "missing key: account"
        assert status in str(
            add_record_post_request_with_empty_key_field_account.text), "Answer text not " + status + " ; actual message : " + str(
            add_record_post_request_with_empty_key_field_account.text)


#@allure.issue("https://trac.brightpattern.com/ticket/22524")
# @allure.issue("https://trac.brightpattern.com/ticket/24228")
@pytest.mark.usefixtures("add_record_post_request_with_incorrectly_formatted_date_time_number_in_a_date_time_field")
class Test_post_request_with_incorrectly_formatted_date_time_number_in_a_date_time_field():
    @allure.epic("test_add_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_status_code_post_request_with_incorrectly_formatted_date_time_number_in_a_date_time_field')
    def test_check_status_code_post_request_with_incorrectly_formatted_date_time_number_in_a_date_time_field(self,
                                                                                                             add_record_post_request_with_incorrectly_formatted_date_time_number_in_a_date_time_field):
        print("request_result_status_code : ", add_record_post_request_with_incorrectly_formatted_date_time_number_in_a_date_time_field.status_code)
        assert "400" in str(
            add_record_post_request_with_incorrectly_formatted_date_time_number_in_a_date_time_field.status_code), "Answer status not 400 ; actual status code : " + str(
            add_record_post_request_with_incorrectly_formatted_date_time_number_in_a_date_time_field.status_code)

    @allure.epic("test_add_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_answer_text_post_request_with_incorrectly_formatted_date_time_number_in_a_date_time_field')
    def test_check_answer_text_post_request_with_incorrectly_formatted_date_time_number_in_a_date_time_field(self,
                                                                                                             add_record_post_request_with_incorrectly_formatted_date_time_number_in_a_date_time_field):
        print("request_result_text : ", add_record_post_request_with_incorrectly_formatted_date_time_number_in_a_date_time_field.text)
        status = "Error parsing datetime value, please enter date in the correct format 'MM/dd/yyyy hh:mm a'"
        assert status in str(
            add_record_post_request_with_incorrectly_formatted_date_time_number_in_a_date_time_field.text), "Answer text not " + status + " ; actual message : " + str(
            add_record_post_request_with_incorrectly_formatted_date_time_number_in_a_date_time_field.text)


#@allure.issue("https://trac.brightpattern.com/ticket/22559")
@pytest.mark.usefixtures("add_record_post_request_with_incorrectly_formatted_phone_number_country")
class Test_post_request_with_incorrectly_formatted_phone_number_country():
    @allure.epic("test_add_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_status_code_post_request_with_incorrectly_formatted_phone_number_country')
    def test_check_status_code_post_request_with_incorrectly_formatted_phone_number_country(self,
                                                                                            add_record_post_request_with_incorrectly_formatted_phone_number_country):
        print("request_result_status_code : ", add_record_post_request_with_incorrectly_formatted_phone_number_country.status_code)
        assert "400" in str(
            add_record_post_request_with_incorrectly_formatted_phone_number_country.status_code), "Answer status not 400 ; actual status code : " + str(
            add_record_post_request_with_incorrectly_formatted_phone_number_country.status_code)

    @allure.epic("test_add_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_answer_text_post_request_with_incorrectly_formatted_phone_number_country')
    def test_check_answer_text_post_request_with_incorrectly_formatted_phone_number_country(self,
                                                                                            add_record_post_request_with_incorrectly_formatted_phone_number_country):
        print("request_result_text : ", add_record_post_request_with_incorrectly_formatted_phone_number_country.text)
        status = "invalid US/Canada phone number"
        assert status in str(
            add_record_post_request_with_incorrectly_formatted_phone_number_country.text), "Answer text not " + status + " ; actual message : " + str(
            add_record_post_request_with_incorrectly_formatted_phone_number_country.text)


@allure.issue("https://trac.brightpattern.com/ticket/22561")
@pytest.mark.usefixtures("add_record_post_request_with_incorrectly_formatted_phone_number_in_a_phone_field")
class Test_post_request_with_incorrectly_formatted_phone_number_in_a_phone_field():
    @allure.epic("test_add_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_status_code_post_request_with_incorrectly_formatted_phone_number_in_a_phone_field')
    def test_check_status_code_post_request_with_incorrectly_formatted_phone_number_in_a_phone_field(self,
                                                                                                     add_record_post_request_with_incorrectly_formatted_phone_number_in_a_phone_field):
        print("request_result_status_code : ", add_record_post_request_with_incorrectly_formatted_phone_number_in_a_phone_field.status_code)
        assert "400" in str(
            add_record_post_request_with_incorrectly_formatted_phone_number_in_a_phone_field.status_code), "Answer status not 400 ; actual status code : " + str(
            add_record_post_request_with_incorrectly_formatted_phone_number_in_a_phone_field.status_code)

    @allure.epic("test_add_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_answer_text_post_request_with_incorrectly_formatted_phone_number_in_a_phone_field')
    def test_check_answer_text_post_request_with_incorrectly_formatted_phone_number_in_a_phone_field(self,
                                                                                                     add_record_post_request_with_incorrectly_formatted_phone_number_in_a_phone_field):
        print("request_result_text : ", add_record_post_request_with_incorrectly_formatted_phone_number_in_a_phone_field.text)
        status = "<fill this response>"
        assert status in str(
            add_record_post_request_with_incorrectly_formatted_phone_number_in_a_phone_field.text), "Answer text not " + status + " ; actual message : " + str(
            add_record_post_request_with_incorrectly_formatted_phone_number_in_a_phone_field.text)


@pytest.mark.usefixtures("add_record_post_request_with_missing_req_field")
class Test_post_request_with_missing_req_field():
    @allure.epic("test_add_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_status_code_post_request_with_missing_req_field')
    def test_check_status_code_post_request_with_missing_req_field(self, add_record_post_request_with_missing_req_field):
        print("request_result_status_code : ", add_record_post_request_with_missing_req_field.status_code)
        assert "400" in str(
            add_record_post_request_with_missing_req_field.status_code), "Answer status not 400 ; actual status code : " + str(
            add_record_post_request_with_missing_req_field.status_code)

    @allure.epic("test_add_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_answer_text_post_request_with_missing_req_field')
    def test_check_answer_text_post_request_with_missing_req_field(self, add_record_post_request_with_missing_req_field):
        print("request_result_text : ", add_record_post_request_with_missing_req_field.text)
        status = "missing required field: phone2"
        assert status in str(
            add_record_post_request_with_missing_req_field.text), "Answer text not " + status + " ; actual message : " + str(
            add_record_post_request_with_missing_req_field.text)


@pytest.mark.usefixtures("add_record_post_request_with_space_in_the_key_field")
class Test_post_request_with_space_in_the_key_field():
    @allure.epic("test_add_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_status_code_post_request_with_space_in_the_key_field')
    def test_check_status_code_post_request_with_space_in_the_key_field(self, add_record_post_request_with_space_in_the_key_field):
        print("request_result_status_code : ", add_record_post_request_with_space_in_the_key_field.status_code)
        assert "400" in str(
            add_record_post_request_with_space_in_the_key_field.status_code), "Answer status not 400 ; actual status code : " + str(
            add_record_post_request_with_space_in_the_key_field.status_code)

    @allure.epic("test_add_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_answer_text_post_request_with_space_in_the_key_field')
    def test_check_answer_text_post_request_with_space_in_the_key_field(self, add_record_post_request_with_space_in_the_key_field):
        print("request_result_text : ", add_record_post_request_with_space_in_the_key_field.text)
        status = "missing key: account"
        assert status in str(
            add_record_post_request_with_space_in_the_key_field.text), "Answer text not " + status + " ; actual message : " + str(
            add_record_post_request_with_space_in_the_key_field.text)


@allure.issue("https://trac.brightpattern.com/ticket/22527")
@pytest.mark.usefixtures("add_record_post_request_with_incorrectly_formatted_value_in_an_integer_field")
class Test_post_request_with_incorrectly_formatted_value_in_an_integer_field():
    @allure.epic("test_add_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_status_code_post_request_with_incorrectly_formatted_value_in_an_integer_field')
    def test_check_status_code_post_request_with_incorrectly_formatted_value_in_an_integer_field(self,
                                                                                                 add_record_post_request_with_incorrectly_formatted_value_in_an_integer_field):
        print("request_result_status_code : ", add_record_post_request_with_incorrectly_formatted_value_in_an_integer_field.status_code)
        assert "400" in str(
            add_record_post_request_with_incorrectly_formatted_value_in_an_integer_field.status_code), "Answer status not 400 ; actual status code : " + str(
            add_record_post_request_with_incorrectly_formatted_value_in_an_integer_field.status_code)

    @allure.epic("test_add_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_answer_text_post_request_with_incorrectly_formatted_value_in_an_integer_field')
    def test_check_answer_text_post_request_with_incorrectly_formatted_value_in_an_integer_field(self,
                                                                                                 add_record_post_request_with_incorrectly_formatted_value_in_an_integer_field):
        print("request_result_text : ", add_record_post_request_with_incorrectly_formatted_value_in_an_integer_field.text)
        status = "Bad request (missing required fields or format not understood)"
        assert status in str(
            add_record_post_request_with_incorrectly_formatted_value_in_an_integer_field.text), "Answer text not " + status + " ; actual message : " + str(
            add_record_post_request_with_incorrectly_formatted_value_in_an_integer_field.text)


@pytest.mark.usefixtures("add_record_post_request_without_a_phone_field_req")
class Test_post_request_without_a_phone_field_req():
    @allure.epic("test_add_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_status_code_post_request_without_a_phone_field_req')
    def test_check_status_code_post_request_without_a_phone_field_req(self, add_record_post_request_without_a_phone_field_req):
        print("request_result_status_code : ", add_record_post_request_without_a_phone_field_req.status_code)
        assert "400" in str(
            add_record_post_request_without_a_phone_field_req.status_code), "Answer status not 400 ; actual status code : " + str(
            add_record_post_request_without_a_phone_field_req.status_code)

    @allure.epic("test_add_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_answer_text_post_request_without_a_phone_field_req')
    def test_check_answer_text_post_request_without_a_phone_field_req(self, add_record_post_request_without_a_phone_field_req):
        print("request_result_text : ", add_record_post_request_without_a_phone_field_req.text)
        status = "missing key: phone1"
        assert status in str(
            add_record_post_request_without_a_phone_field_req.text), "Answer text not " + status + " ; actual message : " + str(
            add_record_post_request_without_a_phone_field_req.text)


@pytest.mark.usefixtures("add_record_post_request_without_a_phone_field_req_and_key")
class Test_post_request_without_a_phone_field_req_and_key():
    @allure.epic("test_add_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_status_code_post_request_without_a_phone_field_req_and_key')
    def test_check_status_code_post_request_without_a_phone_field_req_and_key(self,
                                                                              add_record_post_request_without_a_phone_field_req_and_key):
        print("request_result_status_code : ", add_record_post_request_without_a_phone_field_req_and_key.status_code)
        assert "400" in str(
            add_record_post_request_without_a_phone_field_req_and_key.status_code), "Answer status not 400 ; actual status code : " + str(
            add_record_post_request_without_a_phone_field_req_and_key.status_code)

    @allure.epic("test_add_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_answer_text_post_request_without_a_phone_field_req_and_key')
    def test_check_answer_text_post_request_without_a_phone_field_req_and_key(self,
                                                                              add_record_post_request_without_a_phone_field_req_and_key):
        print("request_result_text : ", add_record_post_request_without_a_phone_field_req_and_key.text)
        status = "missing key: phone1"
        assert status in str(
            add_record_post_request_without_a_phone_field_req_and_key.text), "Answer text not " + status + " ; actual message : " + str(
            add_record_post_request_without_a_phone_field_req_and_key.text)


@pytest.mark.usefixtures("add_record_post_request_without_a_phone_fields")
class Test_post_request_without_a_phone_fields():
    @allure.epic("test_add_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_status_code_post_request_without_a_phone_fields')
    def test_check_status_code_post_request_without_a_phone_fields(self, add_record_post_request_without_a_phone_fields):
        print("request_result_status_code : ", add_record_post_request_without_a_phone_fields.status_code)
        assert "400" in str(
            add_record_post_request_without_a_phone_fields.status_code), "Answer status not 400 ; actual status code : " + str(
            add_record_post_request_without_a_phone_fields.status_code)

    @allure.epic("test_add_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_answer_text_post_request_without_a_phone_fields')
    def test_check_answer_text_post_request_without_a_phone_fields(self, add_record_post_request_without_a_phone_fields):
        print("request_result_text : ", add_record_post_request_without_a_phone_fields.text)
        status = "missing required field: at least one phone field"
        assert status in str(
            add_record_post_request_without_a_phone_fields.text), "Answer text not " + status + " ; actual message : " + str(
            add_record_post_request_without_a_phone_fields.text)


#@allure.issue("https://trac.brightpattern.com/ticket/24254")
@pytest.mark.usefixtures("add_record_post_request_with_empty_body")
class Test_post_request_with_empty_body():
    @allure.epic("test_add_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_status_code_post_request_with_empty_body')
    def test_check_status_code_post_request_with_empty_body(self, add_record_post_request_with_empty_body):
        print("request_result_status_code : ", add_record_post_request_with_empty_body.status_code)
        assert "400" in str(
            add_record_post_request_with_empty_body.status_code), "Answer status not 400 ; actual status code : " + str(
            add_record_post_request_with_empty_body.status_code)

    @allure.epic("test_add_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_answer_text_post_request_with_empty_body')
    def test_check_answer_text_post_request_with_empty_body(self, add_record_post_request_with_empty_body):
        print("request_result_text : ", add_record_post_request_with_empty_body.text)
        status = "missing key: first name"
        assert status in str(
            add_record_post_request_with_empty_body.text), "Answer text not " + status + " ; actual message : " + str(
            add_record_post_request_with_empty_body.text)


# @allure.issue("https://trac.brightpattern.com/ticket/24228")
@pytest.mark.usefixtures("add_record_post_request_with_a_first_name_field_only")
class Test_post_request_with_a_first_name_field_only():
    @allure.epic("test_add_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_status_code_post_request_with_a_first_name_field_only')
    def test_check_status_code_post_request_with_a_first_name_field_only(self,
                                                                         add_record_post_request_with_a_first_name_field_only):
        print("request_result_status_code : ", add_record_post_request_with_a_first_name_field_only.status_code)
        assert "400" in str(
            add_record_post_request_with_a_first_name_field_only.status_code), "Answer status not 400 ; actual status code : " + str(
            add_record_post_request_with_a_first_name_field_only.status_code)

    @allure.epic("test_add_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_answer_text_post_request_with_a_first_name_field_only')
    def test_check_answer_text_post_request_with_a_first_name_field_only(self,
                                                                         add_record_post_request_with_a_first_name_field_only):
        print("request_result_text : ", add_record_post_request_with_a_first_name_field_only.text)
        status = "missing key: phone"
        assert status in str(
            add_record_post_request_with_a_first_name_field_only.text), "Answer text not " + status + " ; actual message : " + str(
            add_record_post_request_with_a_first_name_field_only.text)


#@allure.issue("https://trac.brightpattern.com/ticket/24251")
@pytest.mark.usefixtures("add_record_post_request_with_a_phone_field_only")
class Test_post_request_with_a_phone_field_only():
    @allure.epic("test_add_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_status_code_post_request_with_a_phone_field_only')
    def test_check_status_code_post_request_with_a_phone_field_only(self, add_record_post_request_with_a_phone_field_only):
        print("request_result_status_code : ", add_record_post_request_with_a_phone_field_only.status_code)
        assert "400" in str(
            add_record_post_request_with_a_phone_field_only.status_code), "Answer status not 400 ; actual status code : " + str(
            add_record_post_request_with_a_phone_field_only.status_code)

    @allure.epic("test_add_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_answer_text_post_request_with_a_phone_field_only')
    def test_check_answer_text_post_request_with_a_phone_field_only(self, add_record_post_request_with_a_phone_field_only):
        print("request_result_text : ", add_record_post_request_with_a_phone_field_only.text)
        status = "missing key: first name"
        assert status in str(
            add_record_post_request_with_a_phone_field_only.text), "Answer text not " + status + " ; actual message : " + str(
            add_record_post_request_with_a_phone_field_only.text)


@allure.issue("https://trac.brightpattern.com/ticket/21500")
@pytest.mark.usefixtures("add_record_post_request_with_a_redundant_field")
class Test_post_request_with_a_redundant_field():
    @allure.epic("test_add_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_status_code_post_request_with_a_redundant_field')
    def test_check_status_code_post_request_with_a_redundant_field(self, add_record_post_request_with_a_redundant_field):
        print("request_result_status_code : ", add_record_post_request_with_a_redundant_field.status_code)
        assert "400" in str(
            add_record_post_request_with_a_redundant_field.status_code), "Answer status not 400 ; actual status code : " + str(
            add_record_post_request_with_a_redundant_field.status_code)

    @allure.epic("test_add_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_answer_text_post_request_with_a_redundant_field')
    def test_check_answer_text_post_request_with_a_redundant_field(self, add_record_post_request_with_a_redundant_field):
        print("request_result_text : ", add_record_post_request_with_a_redundant_field.text)
        status = "Record isn't added to the list"
        assert status in str(
            add_record_post_request_with_a_redundant_field.text), "Answer text not " + status + " ; actual message : " + str(
            add_record_post_request_with_a_redundant_field.text)


@pytest.mark.usefixtures("add_record_post_request_with_incorrect_body_format_deleted_quotes")
class Test_post_request_with_incorrect_body_format_deleted_quotes():
    @allure.epic("test_add_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_status_code_post_request_with_incorrect_body_format_deleted_quotes')
    def test_check_status_code_post_request_with_incorrect_body_format_deleted_quotes(self,
                                                                                      add_record_post_request_with_incorrect_body_format_deleted_quotes):
        print("request_result_status_code : ", add_record_post_request_with_incorrect_body_format_deleted_quotes.status_code)
        assert "400" in str(
            add_record_post_request_with_incorrect_body_format_deleted_quotes.status_code), "Answer status not 400 ; actual status code : " + str(
            add_record_post_request_with_incorrect_body_format_deleted_quotes.status_code)

    @allure.epic("test_add_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_answer_text_post_request_with_incorrect_body_format_deleted_quotes')
    def test_check_answer_text_post_request_with_incorrect_body_format_deleted_quotes(self,
                                                                                      add_record_post_request_with_incorrect_body_format_deleted_quotes):
        print("request_result_text : ", add_record_post_request_with_incorrect_body_format_deleted_quotes.text)
        status = "Expected ':' at line 1 column 36 path $"
        assert status in str(
            add_record_post_request_with_incorrect_body_format_deleted_quotes.text), "Answer text not " + status + " ; actual message : " + str(
            add_record_post_request_with_incorrect_body_format_deleted_quotes.text)


@allure.issue("https://trac.brightpattern.com/ticket/22826")
@pytest.mark.usefixtures("add_record_post_request_with_incorrect_body_format_a_redundant_comma_in_the_end")
class Test_post_request_with_incorrect_body_format_a_redundant_comma_in_the_end():
    @allure.epic("test_add_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_status_code_post_request_with_incorrect_body_format_a_redundant_comma_in_the_end')
    def test_check_status_code_post_request_with_incorrect_body_format_a_redundant_comma_in_the_end(self,
                                                                                                    add_record_post_request_with_incorrect_body_format_a_redundant_comma_in_the_end):
        print("request_result_status_code : ", add_record_post_request_with_incorrect_body_format_a_redundant_comma_in_the_end.status_code)
        assert "400" in str(
            add_record_post_request_with_incorrect_body_format_a_redundant_comma_in_the_end.status_code), "Answer status not 400 ; actual status code : " + str(
            add_record_post_request_with_incorrect_body_format_a_redundant_comma_in_the_end.status_code)

    @allure.epic("test_add_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_answer_text_post_request_with_incorrect_body_format_a_redundant_comma_in_the_end')
    def test_check_answer_text_post_request_with_incorrect_body_format_a_redundant_comma_in_the_end(self,
                                                                                                    add_record_post_request_with_incorrect_body_format_a_redundant_comma_in_the_end):
        print("request_result_text : ", add_record_post_request_with_incorrect_body_format_a_redundant_comma_in_the_end.text)
        status = "Expected name at line 1 column 43 path $"
        assert status in str(
            add_record_post_request_with_incorrect_body_format_a_redundant_comma_in_the_end.text), "Answer text not " + status + " ; actual message : " + str(
            add_record_post_request_with_incorrect_body_format_a_redundant_comma_in_the_end.text)


#@allure.issue("https://trac.brightpattern.com/ticket/24250")
@pytest.mark.usefixtures("add_record_post_request_with_a_duplicate_key_field_in_the_body")
class Test_post_request_with_a_duplicate_key_field_in_the_body():
    @allure.epic("test_add_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_status_code_post_request_with_a_duplicate_key_field_in_the_body')
    def test_check_status_code_post_request_with_a_duplicate_key_field_in_the_body(self,
                                                                                   add_record_post_request_with_a_duplicate_key_field_in_the_body):
        print("request_result_status_code : ", add_record_post_request_with_a_duplicate_key_field_in_the_body.status_code)
        assert "400" in str(
            add_record_post_request_with_a_duplicate_key_field_in_the_body.status_code), "Answer status not 400 ; actual status code : " + str(
            add_record_post_request_with_a_duplicate_key_field_in_the_body.status_code)

    @allure.epic("test_add_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_answer_text_post_request_with_a_duplicate_key_field_in_the_body')
    def test_check_answer_text_post_request_with_a_duplicate_key_field_in_the_body(self,
                                                                                   add_record_post_request_with_a_duplicate_key_field_in_the_body):
        print("request_result_text : ", add_record_post_request_with_a_duplicate_key_field_in_the_body.text)
        status = "duplicate key: Phone1"
        assert status in str(
            add_record_post_request_with_a_duplicate_key_field_in_the_body.text), "Answer text not " + status + " ; actual message : " + str(
            add_record_post_request_with_a_duplicate_key_field_in_the_body.text)


@pytest.mark.usefixtures("add_record_post_request_with_empty_first_name_and_phone")
class Test_post_request_with_empty_first_name_and_phone():
    @allure.epic("test_add_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_status_code_post_request_with_empty_first_name_and_phone')
    def test_check_status_code_post_request_with_empty_first_name_and_phone(self,
                                                                            add_record_post_request_with_empty_first_name_and_phone):
        print("request_result_status_code : ", add_record_post_request_with_empty_first_name_and_phone.status_code)
        assert "400" in str(
            add_record_post_request_with_empty_first_name_and_phone.status_code), "Answer status not 400 ; actual status code : " + str(
            add_record_post_request_with_empty_first_name_and_phone.status_code)

    @allure.epic("test_add_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_answer_text_post_request_with_empty_first_name_and_phone')
    def test_check_answer_text_post_request_with_empty_first_name_and_phone(self,
                                                                            add_record_post_request_with_empty_first_name_and_phone):
        print("request_result_text : ", add_record_post_request_with_empty_first_name_and_phone.text)
        status = "missing key: phone"
        assert status in str(
            add_record_post_request_with_empty_first_name_and_phone.text), "Answer text not " + status + " ; actual message : " + str(
            add_record_post_request_with_empty_first_name_and_phone.text)


#@allure.issue("https://trac.brightpattern.com/ticket/24253")
@allure.issue("https://trac.brightpattern.com/ticket/22561")
@pytest.mark.usefixtures(
    "add_record_post_request_with_the_incorrectly_formatted_value_phone_number_in_a_phone_field_non_numeric_symbol_other_than_plus")
class Test_post_request_with_the_incorrectly_formatted_value_phone_number_in_a_phone_field_non_numeric_symbol_other_than_plus():
    @allure.epic("test_add_record")
    @allure.feature("answer code 400")
    @allure.step(
        'test_check_status_code_post_request_with_the_incorrectly_formatted_value_phone_number_in_a_phone_field_non_numeric_symbol_other_than_plus')
    def test_check_status_code_post_request_with_the_incorrectly_formatted_value_phone_number_in_a_phone_field_non_numeric_symbol_other_than_plus(
            self,
            add_record_post_request_with_the_incorrectly_formatted_value_phone_number_in_a_phone_field_non_numeric_symbol_other_than_plus):
        print("request_result_status_code : ", add_record_post_request_with_the_incorrectly_formatted_value_phone_number_in_a_phone_field_non_numeric_symbol_other_than_plus.status_code)
        assert "400" in str(
            add_record_post_request_with_the_incorrectly_formatted_value_phone_number_in_a_phone_field_non_numeric_symbol_other_than_plus.status_code), "Answer status not 400 ; actual status code : " + str(
            add_record_post_request_with_the_incorrectly_formatted_value_phone_number_in_a_phone_field_non_numeric_symbol_other_than_plus.status_code)

    @allure.epic("test_add_record")
    @allure.feature("answer code 400")
    @allure.step(
        'test_check_answer_text_post_request_with_the_incorrectly_formatted_value_phone_number_in_a_phone_field_non_numeric_symbol_other_than_plus')
    def test_check_answer_text_post_request_with_the_incorrectly_formatted_value_phone_number_in_a_phone_field_non_numeric_symbol_other_than_plus(
            self,
            add_record_post_request_with_the_incorrectly_formatted_value_phone_number_in_a_phone_field_non_numeric_symbol_other_than_plus):
        print("request_result_text : ", add_record_post_request_with_the_incorrectly_formatted_value_phone_number_in_a_phone_field_non_numeric_symbol_other_than_plus.text)
        status = "Some error message that Phone should be numeric"
        assert status in str(
            add_record_post_request_with_the_incorrectly_formatted_value_phone_number_in_a_phone_field_non_numeric_symbol_other_than_plus.text), "Answer text not " + status + " ; actual message : " + str(
            add_record_post_request_with_the_incorrectly_formatted_value_phone_number_in_a_phone_field_non_numeric_symbol_other_than_plus.text)


#@allure.issue("https://trac.brightpattern.com/ticket/24229")
@pytest.mark.usefixtures("add_record_post_request_for_corrupted_on_importing_list_all_fields_are_correct")
class Test_post_request_for_corrupted_on_importing_list_all_fields_are_correct():
    @allure.epic("test_add_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_status_code_post_request_for_corrupted_on_importing_list_all_fields_are_correct')
    def test_check_status_code_post_request_for_corrupted_on_importing_list_all_fields_are_correct(self,
                                                                                                   add_record_post_request_for_corrupted_on_importing_list_all_fields_are_correct):
        print("request_result_status_code : ", add_record_post_request_for_corrupted_on_importing_list_all_fields_are_correct.status_code)
        assert "400" in str(
            add_record_post_request_for_corrupted_on_importing_list_all_fields_are_correct.status_code), "Answer status not 400 ; actual status code : " + str(
            add_record_post_request_for_corrupted_on_importing_list_all_fields_are_correct.status_code)

    @allure.epic("test_add_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_answer_text_post_request_for_corrupted_on_importing_list_all_fields_are_correct')
    def test_check_answer_text_post_request_for_corrupted_on_importing_list_all_fields_are_correct(self,
                                                                                                   add_record_post_request_for_corrupted_on_importing_list_all_fields_are_correct):
        print("request_result_text : ", add_record_post_request_for_corrupted_on_importing_list_all_fields_are_correct.text)
        status = "Error parsing datetime value, please enter date in the correct format 'MM/dd/yyyy HH:mm a'"
        assert status in str(
            add_record_post_request_for_corrupted_on_importing_list_all_fields_are_correct.text), "Answer text not " + status + " ; actual message : " + str(
            add_record_post_request_for_corrupted_on_importing_list_all_fields_are_correct.text)


@pytest.mark.usefixtures("add_record_post_request_with_incorrect_body_format_typization")
class Test_post_request_with_incorrect_body_format_typization():
    @allure.epic("test_add_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_status_code_post_request_with_incorrect_body_format_typization')
    def test_check_status_code_post_request_with_incorrect_body_format_typization(self,
                                                                                  add_record_post_request_with_incorrect_body_format_typization):
        print("request_result_status_code : ", add_record_post_request_with_incorrect_body_format_typization.status_code)
        assert "400" in str(
            add_record_post_request_with_incorrect_body_format_typization.status_code), "Answer status not 400 ; actual status code : " + str(
            add_record_post_request_with_incorrect_body_format_typization.status_code)

    @allure.epic("test_add_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_answer_text_post_request_with_incorrect_body_format_typization')
    def test_check_answer_text_post_request_with_incorrect_body_format_typization(self,
                                                                                  add_record_post_request_with_incorrect_body_format_typization):
        print("request_result_text : ", add_record_post_request_with_incorrect_body_format_typization.text)
        status = "Expected BEGIN_OBJECT but was STRING at line 1 column 1 path $"
        assert status in str(
            add_record_post_request_with_incorrect_body_format_typization.text), "Answer text not " + status + " ; actual message : " + str(
            add_record_post_request_with_incorrect_body_format_typization.text)


#@allure.issue("https://trac.brightpattern.com/ticket/22524")
@pytest.mark.usefixtures("add_record_post_request_with_correct_but_different_datetime_format")
class Test_post_request_with_correct_but_different_datetime_format():
    @allure.epic("test_add_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_status_code_post_request_with_correct_but_different_datetime_format')
    def test_check_status_code_post_request_with_correct_but_different_datetime_format(self, add_record_post_request_with_correct_but_different_datetime_format):
        print("request_result_status_code : ", add_record_post_request_with_correct_but_different_datetime_format.status_code)
        assert "400" in str(
            add_record_post_request_with_correct_but_different_datetime_format.status_code), "Answer status not 200 ; actual status code : " + str(
            add_record_post_request_with_correct_but_different_datetime_format.status_code)

    @allure.epic("test_add_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_answer_text_post_request_with_correct_but_different_datetime_format')
    def test_check_answer_text_post_request_with_correct_but_different_datetime_format(self, add_record_post_request_with_correct_but_different_datetime_format):
        print("request_result_text : ", add_record_post_request_with_correct_but_different_datetime_format.text)
        status = "Error parsing datetime value, please enter date in the correct format 'MM/dd/yyyy hh:mm a'"
        assert status in str(
            add_record_post_request_with_correct_but_different_datetime_format.text), "Answer text not " + status + " ; actual message : " + str(
            add_record_post_request_with_correct_but_different_datetime_format.text)


#@allure.issue("https://trac.brightpattern.com/ticket/24434")
@pytest.mark.usefixtures("add_record_post_request_with_body_from_other_list")
class Test_post_request_with_body_from_other_list():
    @allure.epic("test_add_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_status_code_post_request_with_body_from_other_list')
    def test_check_status_code_post_request_with_body_from_other_list(self, add_record_post_request_with_body_from_other_list):
        print("request_result_status_code : ", add_record_post_request_with_body_from_other_list.status_code)
        assert "400" in str(
            add_record_post_request_with_body_from_other_list.status_code), "Answer status not 400 ; actual status code : " + str(
            add_record_post_request_with_body_from_other_list.status_code)

    @allure.epic("test_add_record")
    @allure.feature("answer code 400")
    @allure.step('test_check_answer_text_post_request_with_body_from_other_list')
    def test_check_answer_text_post_request_with_body_from_other_list(self, add_record_post_request_with_body_from_other_list):
        print("request_result_text : ", add_record_post_request_with_body_from_other_list.text)
        status = "missing key: phone"
        assert status in str(
            add_record_post_request_with_body_from_other_list.text), "Answer text not " + status + " ; actual message : " + str(
            add_record_post_request_with_body_from_other_list.text)

#=======================================================================================================================
#=======================================================================================================================
#=======================================================================================================================

#=======================================================================================================================
#==================================================== Code 401 =========================================================
#=======================================================================================================================

@pytest.mark.usefixtures("add_record_post_request_with_do_not_authorize_session")
class Test_post_request_with_do_not_authorize_session():
    @allure.epic("test_add_record")
    @allure.feature("answer code 401")
    @allure.step('test_check_status_code_post_request_with_do_not_authorize_session')
    def test_check_status_code_post_request_with_do_not_authorize_session(self,
                                                                          add_record_post_request_with_do_not_authorize_session):
        print("request_result_status_code : ", add_record_post_request_with_do_not_authorize_session.status_code)
        assert "401" in str(
            add_record_post_request_with_do_not_authorize_session.status_code), "Answer status not 401 ; actual status code : " + str(
            add_record_post_request_with_do_not_authorize_session.status_code)

    @allure.epic("test_add_record")
    @allure.feature("answer code 401")
    @allure.step('test_check_answer_text_post_request_with_do_not_authorize_session')
    def test_check_answer_text_post_request_with_do_not_authorize_session(self,
                                                                          add_record_post_request_with_do_not_authorize_session):
        print("request_result_text : ", add_record_post_request_with_do_not_authorize_session.text)
        status = "Session is not authenticated"
        assert status in str(
            add_record_post_request_with_do_not_authorize_session.text), "Answer text not " + status + " ; actual message : " + str(
            add_record_post_request_with_do_not_authorize_session.text)

#=======================================================================================================================
#=======================================================================================================================
#=======================================================================================================================

#=======================================================================================================================
#==================================================== Code 403 =========================================================
#=======================================================================================================================

#@allure.issue("https://trac.brightpattern.com/ticket/24588")
@pytest.mark.usefixtures("add_record_post_request_with_authorize_session_for_user_without_permission")
class Test_post_request_with_authorize_session_for_user_without_permission():
    @allure.epic("test_add_record")
    @allure.feature("answer code 403")
    @allure.step('test_check_status_code_post_request_with_authorize_session_for_user_without_permission')
    def test_check_status_code_post_request_with_authorize_session_for_user_without_permission(self,
                                                                                               add_record_post_request_with_authorize_session_for_user_without_permission):
        print("request_result_status_code : ", add_record_post_request_with_authorize_session_for_user_without_permission.status_code)
        assert "403" in str(
            add_record_post_request_with_authorize_session_for_user_without_permission.status_code), "Answer status not 403 ; actual status code : " + str(
            add_record_post_request_with_authorize_session_for_user_without_permission.status_code)

    @allure.epic("test_add_record")
    @allure.feature("answer code 403")
    @allure.step('test_check_answer_text_post_request_with_authorize_session_for_user_without_permission')
    def test_check_answer_text_post_request_with_authorize_session_for_user_without_permission(self,
                                                                                               add_record_post_request_with_authorize_session_for_user_without_permission):
        print("request_result_text : ", add_record_post_request_with_authorize_session_for_user_without_permission.text)
        status = "User authenticated but does not have sufficient privileges"
        assert status in str(
            add_record_post_request_with_authorize_session_for_user_without_permission.text), "Answer text not " + status + " ; actual message : " + str(
            add_record_post_request_with_authorize_session_for_user_without_permission.text)

#=======================================================================================================================
#=======================================================================================================================
#=======================================================================================================================

#=======================================================================================================================
#==================================================== Code 404 =========================================================
#=======================================================================================================================

@pytest.mark.usefixtures("add_record_post_request_to_the_non_existent_list")
class Test_post_request_to_the_non_existent_list():
    @allure.epic("test_add_record")
    @allure.feature("answer code 404")
    @allure.step('test_check_status_code_post_request_to_the_non_existent_list')
    def test_check_status_code_post_request_to_the_non_existent_list(self, add_record_post_request_to_the_non_existent_list):
        print("request_result_status_code : ", add_record_post_request_to_the_non_existent_list.status_code)
        assert "404" in str(
            add_record_post_request_to_the_non_existent_list.status_code), "Answer status not 404 ; actual status code : " + str(
            add_record_post_request_to_the_non_existent_list.status_code)

    @allure.epic("test_add_record")
    @allure.feature("answer code 404")
    @allure.step('test_check_answer_text_post_request_to_the_non_existent_list')
    def test_check_answer_text_post_request_to_the_non_existent_list(self, add_record_post_request_to_the_non_existent_list):
        print("request_result_text : ", add_record_post_request_to_the_non_existent_list.text)
        status = "calling list not found"
        assert status in str(
            add_record_post_request_to_the_non_existent_list.text), "Answer text not " + status + " ; actual message : " + str(
            add_record_post_request_to_the_non_existent_list.text)


@pytest.mark.usefixtures("add_record_post_request_with_invalid_url")
class Test_post_request_with_invalid_url():
    @allure.epic("test_add_record")
    @allure.feature("answer code 404")
    @allure.step('test_check_status_code_post_request_with_invalid_url')
    def test_check_status_code_post_request_with_invalid_url(self, add_record_post_request_with_invalid_url):
        print("request_result_status_code : ", add_record_post_request_with_invalid_url.status_code)
        assert "404" in str(
            add_record_post_request_with_invalid_url.status_code), "Answer status not 404 ; actual status code : " + str(
            add_record_post_request_with_invalid_url.status_code)

    @allure.epic("test_add_record")
    @allure.feature("answer code 404")
    @allure.step('test_check_answer_text_post_request_with_invalid_url')
    def test_check_answer_text_post_request_with_invalid_url(self, add_record_post_request_with_invalid_url):
        print("request_result_text : ", add_record_post_request_with_invalid_url.text)
        status = "HTTP 404 Not Found"
        assert status in str(
            add_record_post_request_with_invalid_url.text), "Answer text not " + status + " ; actual message : " + str(
            add_record_post_request_with_invalid_url.text)

#=======================================================================================================================
#=======================================================================================================================
#=======================================================================================================================

#=======================================================================================================================
#==================================================== Code 405 =========================================================
#=======================================================================================================================

#@allure.issue("https://trac.brightpattern.com/ticket/24265")
@pytest.mark.usefixtures("add_record_get_request_with_correct_body")
class Test_get_request_with_correct_body():
    @allure.epic("test_add_record")
    @allure.feature("answer code 405")
    @allure.step('test_check_status_code_get_request_with_correct_body')
    def test_check_status_code_get_request_with_correct_body(self, add_record_get_request_with_correct_body):
        print("request_result_status_code : ", add_record_get_request_with_correct_body.status_code)
        assert "405" in str(
            add_record_get_request_with_correct_body.status_code), "Answer status not 405 ; actual status code : " + str(
            add_record_get_request_with_correct_body.status_code)

    @allure.epic("test_add_record")
    @allure.feature("answer code 405")
    @allure.step('test_check_answer_text_get_request_with_correct_body')
    def test_check_answer_text_get_request_with_correct_body(self, add_record_get_request_with_correct_body):
        print("request_result_text : ", add_record_get_request_with_correct_body.text)
        status = "Method Not Allowed"
        assert status in str(
            add_record_get_request_with_correct_body.text), "Answer text not " + status + " ; actual message : " + str(
            add_record_get_request_with_correct_body.text)
        # assert len(str(get_request_with_correct_body.text)) == 0, "Answer text not empty ; actual message : " + str(get_request_with_correct_body.text)


#@allure.issue("https://trac.brightpattern.com/ticket/24265")
@pytest.mark.usefixtures("add_record_put_request_with_correct_body")
class Test_put_request_with_correct_body():
    @allure.epic("test_add_record")
    @allure.feature("answer code 405")
    @allure.step('test_check_status_code_put_request_with_correct_body')
    def test_check_status_code_put_request_with_correct_body(self, add_record_put_request_with_correct_body):
        print("request_result_status_code : ", add_record_put_request_with_correct_body.status_code)
        assert "405" in str(
            add_record_put_request_with_correct_body.status_code), "Answer status not 405 ; actual status code : " + str(
            add_record_put_request_with_correct_body.status_code)

    @allure.epic("test_add_record")
    @allure.feature("answer code 405")
    @allure.step('test_check_answer_text_put_request_with_correct_body')
    def test_check_answer_text_put_request_with_correct_body(self, add_record_put_request_with_correct_body):
        print("request_result_text : ", add_record_put_request_with_correct_body.text)
        status = "Method Not Allowed"
        assert status in str(
            add_record_put_request_with_correct_body.text), "Answer text not " + status + " ; actual message : " + str(
            add_record_put_request_with_correct_body.text)


#@allure.issue("https://trac.brightpattern.com/ticket/24265")
@pytest.mark.usefixtures("add_record_delete_request_with_correct_body")
class Test_delete_request_with_correct_body():
    @allure.epic("test_add_record")
    @allure.feature("answer code 405")
    @allure.step('test_check_status_code_delete_request_with_correct_body')
    def test_check_status_code_delete_request_with_correct_body(self, add_record_delete_request_with_correct_body):
        print("request_result_status_code : ", add_record_delete_request_with_correct_body.status_code)
        assert "405" in str(
            add_record_delete_request_with_correct_body.status_code), "Answer status not 405 ; actual status code : " + str(
            add_record_delete_request_with_correct_body.status_code)

    @allure.epic("test_add_record")
    @allure.feature("answer code 405")
    @allure.step('test_check_answer_text_delete_request_with_correct_body')
    def test_check_answer_text_delete_request_with_correct_body(self, add_record_delete_request_with_correct_body):
        print("request_result_text : ", add_record_delete_request_with_correct_body.text)
        status = "Method Not Allowed"
        assert status in str(
            add_record_delete_request_with_correct_body.text), "Answer text not " + status + " ; actual message : " + str(
            add_record_delete_request_with_correct_body.text)

#=======================================================================================================================
#=======================================================================================================================
#=======================================================================================================================