import pytest
import allure

@pytest.mark.usefixtures("delete_all_records_post_request_with_a_valid_list_assigned_to_multiple_campaigns")
class Test_post_request_with_a_valid_list_assigned_to_multiple_campaigns():
    @allure.epic("test_delete_all_records")
    @allure.feature("answer code 200")
    @allure.step('test_check_status_code_post_request_with_a_valid_list_assigned_to_multiple_campaigns')
    def test_check_status_code_post_request_with_a_valid_list_assigned_to_multiple_campaigns(self, delete_all_records_post_request_with_a_valid_list_assigned_to_multiple_campaigns):
        print("request_result_status_code : ", delete_all_records_post_request_with_a_valid_list_assigned_to_multiple_campaigns.status_code)
        assert "200" in str(
            delete_all_records_post_request_with_a_valid_list_assigned_to_multiple_campaigns.status_code), "Answer status not 200 ; actual status code : " + str(
            delete_all_records_post_request_with_a_valid_list_assigned_to_multiple_campaigns.status_code)

    @allure.epic("test_delete_all_records")
    @allure.feature("answer code 200")
    @allure.step('test_check_answer_text_post_request_with_a_valid_list_assigned_to_multiple_campaigns')
    def test_check_answer_text_post_request_with_a_valid_list_assigned_to_multiple_campaigns(self, delete_all_records_post_request_with_a_valid_list_assigned_to_multiple_campaigns):
        print("request_result_text : ", delete_all_records_post_request_with_a_valid_list_assigned_to_multiple_campaigns.text)
        assert len(str(
            delete_all_records_post_request_with_a_valid_list_assigned_to_multiple_campaigns.text)) == 0, "Answer text not empty ; actual message : " + str(
            delete_all_records_post_request_with_a_valid_list_assigned_to_multiple_campaigns.text)