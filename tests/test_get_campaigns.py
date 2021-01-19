import pytest
import allure

#=======================================================================================================================
#==================================================== Code 200 =========================================================
#=======================================================================================================================

# @allure.issue("https://trac.brightpattern.com/ticket/24242")
@pytest.mark.usefixtures("get_campaigns_post_request_to_get_campaigns_info")
class Test_post_request_to_get_campaigns_info():
    @allure.epic("test_get_campaigns")
    @allure.feature("answer code 200")
    @allure.step('test_check_status_code_post_request_to_get_campaigns_info')
    def test_check_status_code_post_request_to_get_campaigns_info(self, get_campaigns_post_request_to_get_campaigns_info):
        print("request_result_status_code : ", get_campaigns_post_request_to_get_campaigns_info.status_code)
        assert "200" in str(
            get_campaigns_post_request_to_get_campaigns_info.status_code), "Answer status not 200 ; actual status code : " + str(
            get_campaigns_post_request_to_get_campaigns_info.status_code)

    @allure.epic("test_get_campaigns")
    @allure.feature("answer code 200")
    @allure.step('test_check_answer_text_post_request_to_get_campaigns_info')
    def test_check_answer_text_post_request_to_get_campaigns_info(self, get_campaigns_post_request_to_get_campaigns_info):
        print("request_result_text : ", get_campaigns_post_request_to_get_campaigns_info.text)
        status = '[{"name": "Camp_1", "state": "STOPPED", "lists": ["List_1.txt", "List_1000.csv", "List_2.txt", "List_Completed.txt", "List_Delete1.txt", "List_Delete2.txt"]}, {"name": "Camp_2", "state": "RUNNING", "lists": []}]'
        assert status in str(
            get_campaigns_post_request_to_get_campaigns_info.text), "Answer text not " + status + " ; actual message : " + str(
            get_campaigns_post_request_to_get_campaigns_info.text)

#=======================================================================================================================
#=======================================================================================================================
#=======================================================================================================================