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


@pytest.mark.usefixtures("delete_all_records_post_request_with_a_valid_list_assigned_to_multiple_campaigns_empty_body")
class Test_post_request_with_a_valid_list_assigned_to_multiple_campaigns_empty_body():
    @allure.epic("test_delete_all_records")
    @allure.feature("answer code 200")
    @allure.step('test_check_status_code_post_request_with_a_valid_list_assigned_to_multiple_campaigns_empty_body')
    def test_check_status_code_post_request_with_a_valid_list_assigned_to_multiple_campaigns_empty_body(self, delete_all_records_post_request_with_a_valid_list_assigned_to_multiple_campaigns_empty_body):
        print("request_result_status_code : ", delete_all_records_post_request_with_a_valid_list_assigned_to_multiple_campaigns_empty_body.status_code)
        assert "200" in str(
            delete_all_records_post_request_with_a_valid_list_assigned_to_multiple_campaigns_empty_body.status_code), "Answer status not 200 ; actual status code : " + str(
            delete_all_records_post_request_with_a_valid_list_assigned_to_multiple_campaigns_empty_body.status_code)

    @allure.epic("test_delete_all_records")
    @allure.feature("answer code 200")
    @allure.step('test_check_answer_text_post_request_with_a_valid_list_assigned_to_multiple_campaigns_empty_body')
    def test_check_answer_text_post_request_with_a_valid_list_assigned_to_multiple_campaigns_empty_body(self, delete_all_records_post_request_with_a_valid_list_assigned_to_multiple_campaigns_empty_body):
        print("request_result_text : ", delete_all_records_post_request_with_a_valid_list_assigned_to_multiple_campaigns_empty_body.text)
        assert len(str(
            delete_all_records_post_request_with_a_valid_list_assigned_to_multiple_campaigns_empty_body.text)) == 0, "Answer text not empty ; actual message : " + str(
            delete_all_records_post_request_with_a_valid_list_assigned_to_multiple_campaigns_empty_body.text)


@pytest.mark.usefixtures("delete_all_records_post_request_with_a_valid_list_assigned_to_multiple_campaigns_empty_body_and_list_without_records")
class Test_post_request_with_a_valid_list_assigned_to_multiple_campaigns_empty_body_and_list_without_records():
    @allure.epic("test_delete_all_records")
    @allure.feature("answer code 200")
    @allure.step('test_check_status_code_post_request_with_a_valid_list_assigned_to_multiple_campaigns_empty_body_and_list_without_records')
    def test_check_status_code_post_request_with_a_valid_list_assigned_to_multiple_campaigns_empty_body_and_list_without_records(self, delete_all_records_post_request_with_a_valid_list_assigned_to_multiple_campaigns_empty_body_and_list_without_records):
        print("request_result_status_code : ", delete_all_records_post_request_with_a_valid_list_assigned_to_multiple_campaigns_empty_body_and_list_without_records.status_code)
        assert "200" in str(
            delete_all_records_post_request_with_a_valid_list_assigned_to_multiple_campaigns_empty_body_and_list_without_records.status_code), "Answer status not 200 ; actual status code : " + str(
            delete_all_records_post_request_with_a_valid_list_assigned_to_multiple_campaigns_empty_body_and_list_without_records.status_code)

    @allure.epic("test_delete_all_records")
    @allure.feature("answer code 200")
    @allure.step('test_check_answer_text_post_request_with_a_valid_list_assigned_to_multiple_campaigns_empty_body_and_list_without_records')
    def test_check_answer_text_post_request_with_a_valid_list_assigned_to_multiple_campaigns_empty_body_and_list_without_records(self, delete_all_records_post_request_with_a_valid_list_assigned_to_multiple_campaigns_empty_body_and_list_without_records):
        print("request_result_text : ", delete_all_records_post_request_with_a_valid_list_assigned_to_multiple_campaigns_empty_body_and_list_without_records.text)
        assert len(str(
            delete_all_records_post_request_with_a_valid_list_assigned_to_multiple_campaigns_empty_body_and_list_without_records.text)) == 0, "Answer text not empty ; actual message : " + str(
            delete_all_records_post_request_with_a_valid_list_assigned_to_multiple_campaigns_empty_body_and_list_without_records.text)