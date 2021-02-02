import pytest
import allure
import json

#=======================================================================================================================
#==================================================== Code 200 =========================================================
#=======================================================================================================================

# @allure.issue("https://trac.brightpattern.com/ticket/24242")
@pytest.mark.usefixtures("get_updated_records_post_request_with_valid_list_campaign_fromtime_and_maxsize_3")
class Test_post_request_with_valid_list_campaign_fromtime_and_maxsize_3():
    @allure.epic("test_get_updated_records")
    @allure.feature("answer code 200")
    @allure.step('test_check_status_code_post_request_with_valid_list_campaign_fromtime_and_maxsize_3')
    def test_check_status_code_post_request_with_valid_list_campaign_fromtime_and_maxsize_3(self, get_updated_records_post_request_with_valid_list_campaign_fromtime_and_maxsize_3):
        print("request_result_status_code : ", get_updated_records_post_request_with_valid_list_campaign_fromtime_and_maxsize_3.status_code)
        assert "200" in str(
            get_updated_records_post_request_with_valid_list_campaign_fromtime_and_maxsize_3.status_code), "Answer status not 200 ; actual status code : " + str(
            get_updated_records_post_request_with_valid_list_campaign_fromtime_and_maxsize_3.status_code)

    @allure.epic("test_get_updated_records")
    @allure.feature("answer code 200")
    @allure.step('test_check_answer_text_post_request_with_valid_list_campaign_fromtime_and_maxsize_3')
    def test_check_answer_text_post_request_with_valid_list_campaign_fromtime_and_maxsize_3(self, get_updated_records_post_request_with_valid_list_campaign_fromtime_and_maxsize_3):
        print("request_result_text : ", get_updated_records_post_request_with_valid_list_campaign_fromtime_and_maxsize_3.text)
        status = '[{"lastname":"Name_Last_C1","firstname":"Name_First_C1","agentid":"Test.C1","phone2":"8005","date/time":"07-07-2071","callerid":"101","integer":"1","phone1":"7005"},{"lastname":"Name_Last_C2","firstname":"Name_First_C2","agentid":"Test.C2","phone2":"8006","date/time":"07-07-2072","callerid":"102","integer":"2","phone1":"7006"},{"lastname":"Name_Last_C3","firstname":"Name_First_C3","agentid":"Test.C3","phone2":"8007","date/time":"07-07-2073","callerid":"103","integer":"3","phone1":"7007"}]'
        assert status in str(
            get_updated_records_post_request_with_valid_list_campaign_fromtime_and_maxsize_3.text), "Answer text not " + status + " ; actual message : " + str(
            get_updated_records_post_request_with_valid_list_campaign_fromtime_and_maxsize_3.text)


@pytest.mark.usefixtures("get_updated_records_post_request_with_valid_list_campaign_fromtime_and_maxsize_1")
class Test_post_request_with_valid_list_campaign_fromtime_and_maxsize_1():
    @allure.epic("test_get_updated_records")
    @allure.feature("answer code 200")
    @allure.step('test_check_status_code_post_request_with_valid_list_campaign_fromtime_and_maxsize_1')
    def test_check_status_code_post_request_with_valid_list_campaign_fromtime_and_maxsize_1(self, get_updated_records_post_request_with_valid_list_campaign_fromtime_and_maxsize_1):
        print("request_result_status_code : ", get_updated_records_post_request_with_valid_list_campaign_fromtime_and_maxsize_1.status_code)
        assert "200" in str(
            get_updated_records_post_request_with_valid_list_campaign_fromtime_and_maxsize_1.status_code), "Answer status not 200 ; actual status code : " + str(
            get_updated_records_post_request_with_valid_list_campaign_fromtime_and_maxsize_1.status_code)

    @allure.epic("test_get_updated_records")
    @allure.feature("answer code 200")
    @allure.step('test_check_answer_text_post_request_with_valid_list_campaign_fromtime_and_maxsize_1')
    def test_check_answer_text_post_request_with_valid_list_campaign_fromtime_and_maxsize_1(self, get_updated_records_post_request_with_valid_list_campaign_fromtime_and_maxsize_1):
        print("request_result_text : ", get_updated_records_post_request_with_valid_list_campaign_fromtime_and_maxsize_1.text)
        status = '[{"lastname":"Name_Last_C1","firstname":"Name_First_C1","agentid":"Test.C1","phone2":"8005","date/time":"07-07-2071","callerid":"101","integer":"1","phone1":"7005"}]'
        assert status in str(
            get_updated_records_post_request_with_valid_list_campaign_fromtime_and_maxsize_1.text), "Answer text not " + status + " ; actual message : " + str(
            get_updated_records_post_request_with_valid_list_campaign_fromtime_and_maxsize_1.text)


@pytest.mark.usefixtures("get_updated_records_post_request_with_maxsize_set_to_1000")
class Test_post_request_with_maxsize_set_to_1000():
    @allure.epic("test_get_updated_records")
    @allure.feature("answer code 200")
    @allure.step('test_check_status_code_post_request_with_maxsize_set_to_1000')
    def test_check_status_code_post_request_with_maxsize_set_to_1000(self, get_updated_records_post_request_with_maxsize_set_to_1000):
        print("request_result_status_code : ", get_updated_records_post_request_with_maxsize_set_to_1000.status_code)
        assert "200" in str(
            get_updated_records_post_request_with_maxsize_set_to_1000.status_code), "Answer status not 200 ; actual status code : " + str(
            get_updated_records_post_request_with_maxsize_set_to_1000.status_code)

    @allure.epic("test_get_updated_records")
    @allure.feature("answer code 200")
    @allure.step('test_check_answer_text_post_request_with_maxsize_set_to_1000')
    def test_check_answer_text_post_request_with_maxsize_set_to_1000(self, get_updated_records_post_request_with_maxsize_set_to_1000):
        print("request_result_text : ", get_updated_records_post_request_with_maxsize_set_to_1000.text)
        status = len(json.loads(get_updated_records_post_request_with_maxsize_set_to_1000.text))
        print("status_length : ", status)
        assert status == 1000, "Answer text length not 1000 ; actual message length : " + str(status)


@pytest.mark.usefixtures("get_updated_records_post_request_with_valid_url_and_change_maxsize_and_fromtime_future_date")
class Test_post_request_with_valid_url_and_change_maxsize_and_fromtime_future_date():
    @allure.epic("test_get_updated_records")
    @allure.feature("answer code 200")
    @allure.step('test_check_status_code_post_request_with_valid_url_and_change_maxsize_and_fromtime_future_date')
    def test_check_status_code_post_request_with_valid_url_and_change_maxsize_and_fromtime_future_date(self, get_updated_records_post_request_with_valid_url_and_change_maxsize_and_fromtime_future_date):
        print("request_result_status_code : ", get_updated_records_post_request_with_valid_url_and_change_maxsize_and_fromtime_future_date.status_code)
        assert "200" in str(
            get_updated_records_post_request_with_valid_url_and_change_maxsize_and_fromtime_future_date.status_code), "Answer status not 200 ; actual status code : " + str(
            get_updated_records_post_request_with_valid_url_and_change_maxsize_and_fromtime_future_date.status_code)

    @allure.epic("test_get_updated_records")
    @allure.feature("answer code 200")
    @allure.step('test_check_answer_text_post_request_with_valid_url_and_change_maxsize_and_fromtime_future_date')
    def test_check_answer_text_post_request_with_valid_url_and_change_maxsize_and_fromtime_future_date(self, get_updated_records_post_request_with_valid_url_and_change_maxsize_and_fromtime_future_date):
        print("request_result_text : ", get_updated_records_post_request_with_valid_url_and_change_maxsize_and_fromtime_future_date.text)
        status = '[]'
        assert status in str(
            get_updated_records_post_request_with_valid_url_and_change_maxsize_and_fromtime_future_date.text), "Answer text not " + status + " ; actual message : " + str(
            get_updated_records_post_request_with_valid_url_and_change_maxsize_and_fromtime_future_date.text)


#=======================================================================================================================
#=======================================================================================================================
#=======================================================================================================================

#=======================================================================================================================
#==================================================== Code 400 =========================================================
#=======================================================================================================================

@pytest.mark.usefixtures("get_updated_records_post_request_with_valid_list_campaign_and_maxsize_without_fromtime")
class Test_post_request_with_valid_list_campaign_and_maxsize_without_fromtime():
    @allure.epic("test_get_updated_records")
    @allure.feature("answer code 400")
    @allure.step('test_check_status_code_post_request_with_valid_list_campaign_and_maxsize_without_fromtime')
    def test_check_status_code_post_request_with_valid_list_campaign_and_maxsize_without_fromtime(self, get_updated_records_post_request_with_valid_list_campaign_and_maxsize_without_fromtime):
        print("request_result_status_code : ", get_updated_records_post_request_with_valid_list_campaign_and_maxsize_without_fromtime.status_code)
        assert "400" in str(
            get_updated_records_post_request_with_valid_list_campaign_and_maxsize_without_fromtime.status_code), "Answer status not 400 ; actual status code : " + str(
            get_updated_records_post_request_with_valid_list_campaign_and_maxsize_without_fromtime.status_code)

    @allure.epic("test_get_updated_records")
    @allure.feature("answer code 400")
    @allure.step('test_check_answer_text_post_request_with_valid_list_campaign_and_maxsize_without_fromtime')
    def test_check_answer_text_post_request_with_valid_list_campaign_and_maxsize_without_fromtime(self, get_updated_records_post_request_with_valid_list_campaign_and_maxsize_without_fromtime):
        print("request_result_text : ", get_updated_records_post_request_with_valid_list_campaign_and_maxsize_without_fromtime.text)
        status = 'invalid parameters'
        assert status in str(
            get_updated_records_post_request_with_valid_list_campaign_and_maxsize_without_fromtime.text), "Answer text not " + status + " ; actual message : " + str(
            get_updated_records_post_request_with_valid_list_campaign_and_maxsize_without_fromtime.text)


@pytest.mark.usefixtures("get_updated_records_post_request_with_valid_list_campaign_and_fromtime_without_maxsize")
class Test_post_request_with_valid_list_campaign_and_fromtime_without_maxsize():
    @allure.epic("test_get_updated_records")
    @allure.feature("answer code 400")
    @allure.step('test_check_status_code_post_request_with_valid_list_campaign_and_fromtime_without_maxsize')
    def test_check_status_code_post_request_with_valid_list_campaign_and_fromtime_without_maxsize(self, get_updated_records_post_request_with_valid_list_campaign_and_fromtime_without_maxsize):
        print("request_result_status_code : ", get_updated_records_post_request_with_valid_list_campaign_and_fromtime_without_maxsize.status_code)
        assert "400" in str(
            get_updated_records_post_request_with_valid_list_campaign_and_fromtime_without_maxsize.status_code), "Answer status not 400 ; actual status code : " + str(
            get_updated_records_post_request_with_valid_list_campaign_and_fromtime_without_maxsize.status_code)

    @allure.epic("test_get_updated_records")
    @allure.feature("answer code 400")
    @allure.step('test_check_answer_text_post_request_with_valid_list_campaign_and_fromtime_without_maxsize')
    def test_check_answer_text_post_request_with_valid_list_campaign_and_fromtime_without_maxsize(self, get_updated_records_post_request_with_valid_list_campaign_and_fromtime_without_maxsize):
        print("request_result_text : ", get_updated_records_post_request_with_valid_list_campaign_and_fromtime_without_maxsize.text)
        status = 'invalid parameters'
        assert status in str(
            get_updated_records_post_request_with_valid_list_campaign_and_fromtime_without_maxsize.text), "Answer text not " + status + " ; actual message : " + str(
            get_updated_records_post_request_with_valid_list_campaign_and_fromtime_without_maxsize.text)


@pytest.mark.usefixtures("get_updated_records_post_request_with_maxsize_set_to_greater_than_1000")
class Test_post_request_with_maxsize_set_to_greater_than_1000():
    @allure.epic("test_get_updated_records")
    @allure.feature("answer code 400")
    @allure.step('test_check_status_code_post_request_with_maxsize_set_to_greater_than_1000')
    def test_check_status_code_post_request_with_maxsize_set_to_greater_than_1000(self, get_updated_records_post_request_with_maxsize_set_to_greater_than_1000):
        print("request_result_status_code : ", get_updated_records_post_request_with_maxsize_set_to_greater_than_1000.status_code)
        assert "400" in str(
            get_updated_records_post_request_with_maxsize_set_to_greater_than_1000.status_code), "Answer status not 400 ; actual status code : " + str(
            get_updated_records_post_request_with_maxsize_set_to_greater_than_1000.status_code)

    @allure.epic("test_get_updated_records")
    @allure.feature("answer code 400")
    @allure.step('test_check_answer_text_post_request_with_maxsize_set_to_greater_than_1000')
    def test_check_answer_text_post_request_with_maxsize_set_to_greater_than_1000(self, get_updated_records_post_request_with_maxsize_set_to_greater_than_1000):
        print("request_result_text : ", get_updated_records_post_request_with_maxsize_set_to_greater_than_1000.text)
        status = 'maxSize is too large (no more than 1000)'
        assert status in str(
            get_updated_records_post_request_with_maxsize_set_to_greater_than_1000.text), "Answer text not " + status + " ; actual message : " + str(
            get_updated_records_post_request_with_maxsize_set_to_greater_than_1000.text)


@pytest.mark.usefixtures("get_updated_records_post_request_with_invalid_fromtime_value_fromtime_alphabetical")
class Test_post_request_with_invalid_fromtime_value_fromtime_alphabetical():
    @allure.epic("test_get_updated_records")
    @allure.feature("answer code 400")
    @allure.step('test_check_status_code_post_request_with_invalid_fromtime_value_fromtime_alphabetical')
    def test_check_status_code_post_request_with_invalid_fromtime_value_fromtime_alphabetical(self, get_updated_records_post_request_with_invalid_fromtime_value_fromtime_alphabetical):
        print("request_result_status_code : ", get_updated_records_post_request_with_invalid_fromtime_value_fromtime_alphabetical.status_code)
        assert "400" in str(
            get_updated_records_post_request_with_invalid_fromtime_value_fromtime_alphabetical.status_code), "Answer status not 400 ; actual status code : " + str(
            get_updated_records_post_request_with_invalid_fromtime_value_fromtime_alphabetical.status_code)

    @allure.epic("test_get_updated_records")
    @allure.feature("answer code 400")
    @allure.step('test_check_answer_text_post_request_with_invalid_fromtime_value_fromtime_alphabetical')
    def test_check_answer_text_post_request_with_invalid_fromtime_value_fromtime_alphabetical(self, get_updated_records_post_request_with_invalid_fromtime_value_fromtime_alphabetical):
        print("request_result_text : ", get_updated_records_post_request_with_invalid_fromtime_value_fromtime_alphabetical.text)
        status = 'Unparseable date: "abc"'
        assert status in str(
            get_updated_records_post_request_with_invalid_fromtime_value_fromtime_alphabetical.text), "Answer text not " + status + " ; actual message : " + str(
            get_updated_records_post_request_with_invalid_fromtime_value_fromtime_alphabetical.text)


@allure.issue("https://trac.brightpattern.com/ticket/24717")
@pytest.mark.usefixtures("get_updated_records_post_request_with_invalid_maxsize_value_maxsize_alphabetical")
class Test_post_request_with_invalid_maxsize_value_maxsize_alphabetical():
    @allure.epic("test_get_updated_records")
    @allure.feature("answer code 400")
    @allure.step('test_check_status_code_post_request_with_invalid_maxsize_value_maxsize_alphabetical')
    def test_check_status_code_post_request_with_invalid_maxsize_value_maxsize_alphabetical(self, get_updated_records_post_request_with_invalid_maxsize_value_maxsize_alphabetical):
        print("request_result_status_code : ", get_updated_records_post_request_with_invalid_maxsize_value_maxsize_alphabetical.status_code)
        assert "400" in str(
            get_updated_records_post_request_with_invalid_maxsize_value_maxsize_alphabetical.status_code), "Answer status not 400 ; actual status code : " + str(
            get_updated_records_post_request_with_invalid_maxsize_value_maxsize_alphabetical.status_code)

    @allure.epic("test_get_updated_records")
    @allure.feature("answer code 400")
    @allure.step('test_check_answer_text_post_request_with_invalid_maxsize_value_maxsize_alphabetical')
    def test_check_answer_text_post_request_with_invalid_maxsize_value_maxsize_alphabetical(self, get_updated_records_post_request_with_invalid_maxsize_value_maxsize_alphabetical):
        print("request_result_text : ", get_updated_records_post_request_with_invalid_maxsize_value_maxsize_alphabetical.text)
        status = '<Fill this response>'
        assert status in str(
            get_updated_records_post_request_with_invalid_maxsize_value_maxsize_alphabetical.text), "Answer text not " + status + " ; actual message : " + str(
            get_updated_records_post_request_with_invalid_maxsize_value_maxsize_alphabetical.text)


@allure.issue("https://trac.brightpattern.com/ticket/24716")
@pytest.mark.usefixtures("get_updated_records_post_request_with_incorrect_body_format_typization")
class Test_post_request_with_incorrect_body_format_typization():
    @allure.epic("test_get_updated_records")
    @allure.feature("answer code 400")
    @allure.step('test_check_status_code_post_request_with_incorrect_body_format_typization')
    def test_check_status_code_post_request_with_incorrect_body_format_typization(self,
                                                                                  get_updated_records_post_request_with_incorrect_body_format_typization):
        print("request_result_status_code : ", get_updated_records_post_request_with_incorrect_body_format_typization.status_code)
        assert "400" in str(
            get_updated_records_post_request_with_incorrect_body_format_typization.status_code), "Answer status not 400 ; actual status code : " + str(
            get_updated_records_post_request_with_incorrect_body_format_typization.status_code)

    @allure.epic("test_get_updated_records")
    @allure.feature("answer code 400")
    @allure.step('test_check_answer_text_post_request_with_incorrect_body_format_typization')
    def test_check_answer_text_post_request_with_incorrect_body_format_typization(self,
                                                                                  get_updated_records_post_request_with_incorrect_body_format_typization):
        print("request_result_text : ", get_updated_records_post_request_with_incorrect_body_format_typization.text)
        status = "Expected BEGIN_OBJECT but was STRING at line 1 column 1 path $"
        assert status in str(
            get_updated_records_post_request_with_incorrect_body_format_typization.text), "Answer text not " + status + " ; actual message : " + str(
            get_updated_records_post_request_with_incorrect_body_format_typization.text)


@pytest.mark.usefixtures("get_updated_records_post_request_with_wrong_fromtime_format")
class Test_post_request_with_wrong_fromtime_format():
    @allure.epic("test_get_updated_records")
    @allure.feature("answer code 400")
    @allure.step('test_check_status_code_post_request_with_wrong_fromtime_format')
    def test_check_status_code_post_request_with_wrong_fromtime_format(self, get_updated_records_post_request_with_wrong_fromtime_format):
        print("request_result_status_code : ", get_updated_records_post_request_with_wrong_fromtime_format.status_code)
        assert "400" in str(
            get_updated_records_post_request_with_wrong_fromtime_format.status_code), "Answer status not 400 ; actual status code : " + str(
            get_updated_records_post_request_with_wrong_fromtime_format.status_code)

    @allure.epic("test_get_updated_records")
    @allure.feature("answer code 400")
    @allure.step('test_check_answer_text_post_request_with_wrong_fromtime_format')
    def test_check_answer_text_post_request_with_wrong_fromtime_format(self, get_updated_records_post_request_with_wrong_fromtime_format):
        print("request_result_text : ", get_updated_records_post_request_with_wrong_fromtime_format.text)
        status = 'Unparseable date: "2003-03-0:15:06.456"'
        assert status in str(
            get_updated_records_post_request_with_wrong_fromtime_format.text), "Answer text not " + status + " ; actual message : " + str(
            get_updated_records_post_request_with_wrong_fromtime_format.text)

#=======================================================================================================================
#=======================================================================================================================
#=======================================================================================================================

#=======================================================================================================================
#==================================================== Code 404 =========================================================
#=======================================================================================================================

@allure.issue("https://trac.brightpattern.com/ticket/22717")
@pytest.mark.usefixtures("get_updated_records_post_request_with_valid_list_and_campaign_that_are_not_associated")
class Test_post_request_with_valid_list_and_campaign_that_are_not_associated():
    @allure.epic("test_get_updated_records")
    @allure.feature("answer code 404")
    @allure.step('test_check_status_code_post_request_with_valid_list_and_campaign_that_are_not_associated')
    def test_check_status_code_post_request_with_valid_list_and_campaign_that_are_not_associated(self, get_updated_records_post_request_with_valid_list_and_campaign_that_are_not_associated):
        print("request_result_status_code : ", get_updated_records_post_request_with_valid_list_and_campaign_that_are_not_associated.status_code)
        assert "404" in str(
            get_updated_records_post_request_with_valid_list_and_campaign_that_are_not_associated.status_code), "Answer status not 404 ; actual status code : " + str(
            get_updated_records_post_request_with_valid_list_and_campaign_that_are_not_associated.status_code)

    @allure.epic("test_get_updated_records")
    @allure.feature("answer code 404")
    @allure.step('test_check_answer_text_post_request_with_valid_list_and_campaign_that_are_not_associated')
    def test_check_answer_text_post_request_with_valid_list_and_campaign_that_are_not_associated(self, get_updated_records_post_request_with_valid_list_and_campaign_that_are_not_associated):
        print("request_result_text : ", get_updated_records_post_request_with_valid_list_and_campaign_that_are_not_associated.text)
        status = 'campaign is not found'
        assert status in str(
            get_updated_records_post_request_with_valid_list_and_campaign_that_are_not_associated.text), "Answer text not " + status + " ; actual message : " + str(
            get_updated_records_post_request_with_valid_list_and_campaign_that_are_not_associated.text)


@pytest.mark.usefixtures("get_updated_records_post_request_to_the_non_existent_list")
class Test_post_request_to_the_non_existent_list():
    @allure.epic("test_get_updated_records")
    @allure.feature("answer code 404")
    @allure.step('test_check_status_code_post_request_to_the_non_existent_list')
    def test_check_status_code_post_request_to_the_non_existent_list(self, get_updated_records_post_request_to_the_non_existent_list):
        print("request_result_status_code : ", get_updated_records_post_request_to_the_non_existent_list.status_code)
        assert "404" in str(
            get_updated_records_post_request_to_the_non_existent_list.status_code), "Answer status not 404 ; actual status code : " + str(
            get_updated_records_post_request_to_the_non_existent_list.status_code)

    @allure.epic("test_get_updated_records")
    @allure.feature("answer code 404")
    @allure.step('test_check_answer_text_post_request_to_the_non_existent_list')
    def test_check_answer_text_post_request_to_the_non_existent_list(self, get_updated_records_post_request_to_the_non_existent_list):
        print("request_result_text : ", get_updated_records_post_request_to_the_non_existent_list.text)
        status = 'calling list not found'
        assert status in str(
            get_updated_records_post_request_to_the_non_existent_list.text), "Answer text not " + status + " ; actual message : " + str(
            get_updated_records_post_request_to_the_non_existent_list.text)


@pytest.mark.usefixtures("get_updated_records_post_request_with_invalid_url")
class Test_post_request_with_invalid_url():
    @allure.epic("test_get_updated_records")
    @allure.feature("answer code 404")
    @allure.step('test_check_status_code_post_request_with_invalid_url')
    def test_check_status_code_post_request_with_invalid_url(self, get_updated_records_post_request_with_invalid_url):
        print("request_result_status_code : ", get_updated_records_post_request_with_invalid_url.status_code)
        assert "404" in str(
            get_updated_records_post_request_with_invalid_url.status_code), "Answer status not 404 ; actual status code : " + str(
            get_updated_records_post_request_with_invalid_url.status_code)

    @allure.epic("test_get_updated_records")
    @allure.feature("answer code 404")
    @allure.step('test_check_answer_text_post_request_with_invalid_url')
    def test_check_answer_text_post_request_with_invalid_url(self, get_updated_records_post_request_with_invalid_url):
        print("request_result_text : ", get_updated_records_post_request_with_invalid_url.text)
        status = 'HTTP 404 Not Found'
        assert status in str(
            get_updated_records_post_request_with_invalid_url.text), "Answer text not " + status + " ; actual message : " + str(
            get_updated_records_post_request_with_invalid_url.text)

#=======================================================================================================================
#=======================================================================================================================
#=======================================================================================================================

#=======================================================================================================================
#==================================================== Code 403 =========================================================
#=======================================================================================================================

@pytest.mark.usefixtures("get_updated_records_post_request_with_authorize_session_for_user_without_permission")
class Test_post_request_with_authorize_session_for_user_without_permission():
    @allure.epic("test_get_updated_records")
    @allure.feature("answer code 403")
    @allure.step('test_check_status_code_post_request_with_authorize_session_for_user_without_permission')
    def test_check_status_code_post_request_with_authorize_session_for_user_without_permission(self,
                                                                                               get_updated_records_post_request_with_authorize_session_for_user_without_permission):
        print("request_result_status_code : ", get_updated_records_post_request_with_authorize_session_for_user_without_permission.status_code)
        assert "403" in str(
            get_updated_records_post_request_with_authorize_session_for_user_without_permission.status_code), "Answer status not 403 ; actual status code : " + str(
            get_updated_records_post_request_with_authorize_session_for_user_without_permission.status_code)

    @allure.epic("test_get_updated_records")
    @allure.feature("answer code 403")
    @allure.step('test_check_answer_text_post_request_with_authorize_session_for_user_without_permission')
    def test_check_answer_text_post_request_with_authorize_session_for_user_without_permission(self,
                                                                                               get_updated_records_post_request_with_authorize_session_for_user_without_permission):
        print("request_result_text : ", get_updated_records_post_request_with_authorize_session_for_user_without_permission.text)
        status = "User authenticated but does not have sufficient privileges"
        assert status in str(
            get_updated_records_post_request_with_authorize_session_for_user_without_permission.text), "Answer text not " + status + " ; actual message : " + str(
            get_updated_records_post_request_with_authorize_session_for_user_without_permission.text)

#=======================================================================================================================
#=======================================================================================================================
#=======================================================================================================================

#=======================================================================================================================
#==================================================== Code 401 =========================================================
#=======================================================================================================================

@pytest.mark.usefixtures("get_updated_records_post_request_with_do_not_authorize_session")
class Test_post_request_with_do_not_authorize_session():
    @allure.epic("test_get_updated_records")
    @allure.feature("answer code 401")
    @allure.step('test_check_status_code_post_request_with_do_not_authorize_session')
    def test_check_status_code_post_request_with_do_not_authorize_session(self,
                                                                          get_updated_records_post_request_with_do_not_authorize_session):
        print("request_result_status_code : ", get_updated_records_post_request_with_do_not_authorize_session.status_code)
        assert "401" in str(
            get_updated_records_post_request_with_do_not_authorize_session.status_code), "Answer status not 401 ; actual status code : " + str(
            get_updated_records_post_request_with_do_not_authorize_session.status_code)

    @allure.epic("test_get_updated_records")
    @allure.feature("answer code 401")
    @allure.step('test_check_answer_text_post_request_with_do_not_authorize_session')
    def test_check_answer_text_post_request_with_do_not_authorize_session(self,
                                                                          get_updated_records_post_request_with_do_not_authorize_session):
        print("request_result_text : ", get_updated_records_post_request_with_do_not_authorize_session.text)
        status = "Session is not authenticated"
        assert status in str(
            get_updated_records_post_request_with_do_not_authorize_session.text), "Answer text not " + status + " ; actual message : " + str(
            get_updated_records_post_request_with_do_not_authorize_session.text)

#=======================================================================================================================
#=======================================================================================================================
#=======================================================================================================================

#=======================================================================================================================
#==================================================== Code 405 =========================================================
#=======================================================================================================================

@pytest.mark.usefixtures("get_updated_records_get_request_with_correct_body")
class Test_get_request_with_correct_body():
    @allure.epic("test_get_updated_records")
    @allure.feature("answer code 405")
    @allure.step('test_check_status_code_get_request_with_correct_body')
    def test_check_status_code_get_request_with_correct_body(self, get_updated_records_get_request_with_correct_body):
        print("request_result_status_code : ", get_updated_records_get_request_with_correct_body.status_code)
        assert "405" in str(
            get_updated_records_get_request_with_correct_body.status_code), "Answer status not 405 ; actual status code : " + str(
            get_updated_records_get_request_with_correct_body.status_code)

    @allure.epic("test_get_updated_records")
    @allure.feature("answer code 405")
    @allure.step('test_check_answer_text_get_request_with_correct_body')
    def test_check_answer_text_get_request_with_correct_body(self, get_updated_records_get_request_with_correct_body):
        print("request_result_text : ", get_updated_records_get_request_with_correct_body.text)
        status = "Method Not Allowed"
        assert status in str(
            get_updated_records_get_request_with_correct_body.text), "Answer text not " + status + " ; actual message : " + str(
            get_updated_records_get_request_with_correct_body.text)
        # assert len(str(get_request_with_correct_body.text)) == 0, "Answer text not empty ; actual message : " + str(get_request_with_correct_body.text)


#@allure.issue("https://trac.brightpattern.com/ticket/24265")
@pytest.mark.usefixtures("get_updated_records_put_request_with_correct_body")
class Test_put_request_with_correct_body():
    @allure.epic("test_get_updated_records")
    @allure.feature("answer code 405")
    @allure.step('test_check_status_code_put_request_with_correct_body')
    def test_check_status_code_put_request_with_correct_body(self, get_updated_records_put_request_with_correct_body):
        print("request_result_status_code : ", get_updated_records_put_request_with_correct_body.status_code)
        assert "405" in str(
            get_updated_records_put_request_with_correct_body.status_code), "Answer status not 405 ; actual status code : " + str(
            get_updated_records_put_request_with_correct_body.status_code)

    @allure.epic("test_get_updated_records")
    @allure.feature("answer code 405")
    @allure.step('test_check_answer_text_put_request_with_correct_body')
    def test_check_answer_text_put_request_with_correct_body(self, get_updated_records_put_request_with_correct_body):
        print("request_result_text : ", get_updated_records_put_request_with_correct_body.text)
        status = "Method Not Allowed"
        assert status in str(
            get_updated_records_put_request_with_correct_body.text), "Answer text not " + status + " ; actual message : " + str(
            get_updated_records_put_request_with_correct_body.text)


#@allure.issue("https://trac.brightpattern.com/ticket/24265")
@pytest.mark.usefixtures("get_updated_records_delete_request_with_correct_body")
class Test_delete_request_with_correct_body():
    @allure.epic("test_get_updated_records")
    @allure.feature("answer code 405")
    @allure.step('test_check_status_code_delete_request_with_correct_body')
    def test_check_status_code_delete_request_with_correct_body(self, get_updated_records_delete_request_with_correct_body):
        print("request_result_status_code : ", get_updated_records_delete_request_with_correct_body.status_code)
        assert "405" in str(
            get_updated_records_delete_request_with_correct_body.status_code), "Answer status not 405 ; actual status code : " + str(
            get_updated_records_delete_request_with_correct_body.status_code)

    @allure.epic("test_get_updated_records")
    @allure.feature("answer code 405")
    @allure.step('test_check_answer_text_delete_request_with_correct_body')
    def test_check_answer_text_delete_request_with_correct_body(self, get_updated_records_delete_request_with_correct_body):
        print("request_result_text : ", get_updated_records_delete_request_with_correct_body.text)
        status = "Method Not Allowed"
        assert status in str(
            get_updated_records_delete_request_with_correct_body.text), "Answer text not " + status + " ; actual message : " + str(
            get_updated_records_delete_request_with_correct_body.text)

#=======================================================================================================================
#=======================================================================================================================
#=======================================================================================================================