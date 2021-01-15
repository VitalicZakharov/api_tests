import pytest
import allure

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