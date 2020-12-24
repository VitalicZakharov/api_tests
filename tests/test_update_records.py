import pytest
import allure

# @allure.issue("https://trac.brightpattern.com/ticket/24242")
@pytest.mark.usefixtures("update_records_post_request_with_existent_record_key")
class Test_post_request_with_existent_record_key():
    @allure.epic("test_update_records")
    @allure.feature("answer code 200")
    @allure.step('test_check_status_code_post_request_with_existent_record_key')
    def test_check_status_code_post_request_with_existent_record_key(self, update_records_post_request_with_existent_record_key):
        print("request_result_status_code : ", update_records_post_request_with_existent_record_key.status_code)
        assert "200" in str(
            update_records_post_request_with_existent_record_key.status_code), "Answer status not 200 ; actual status code : " + str(
            update_records_post_request_with_existent_record_key.status_code)

    @allure.epic("test_update_records")
    @allure.feature("answer code 200")
    @allure.step('test_check_answer_text_post_request_with_existent_record_key')
    def test_check_answer_text_post_request_with_existent_record_key(self, update_records_post_request_with_existent_record_key):
        print("request_result_text : ", update_records_post_request_with_existent_record_key.text)
        assert len(str(
            update_records_post_request_with_existent_record_key.text)) == 0, "Answer text not empty ; actual message : " + str(
            update_records_post_request_with_existent_record_key.text)


@pytest.mark.usefixtures("update_records_post_request_with_a_non_existent_record_key")
class Test_post_request_with_a_non_existent_record_key():
    @allure.epic("test_update_records")
    @allure.feature("answer code 404")
    @allure.step('test_check_status_code_post_request_with_a_non_existent_record_key')
    def test_check_status_code_post_request_with_a_non_existent_record_key(self, update_records_post_request_with_a_non_existent_record_key):
        print("request_result_status_code : ", update_records_post_request_with_a_non_existent_record_key.status_code)
        assert "404" in str(
            update_records_post_request_with_a_non_existent_record_key.status_code), "Answer status not 404 ; actual status code : " + str(
            update_records_post_request_with_a_non_existent_record_key.status_code)

    @allure.epic("test_update_records")
    @allure.feature("answer code 404")
    @allure.step('test_check_answer_text_post_request_with_a_non_existent_record_key')
    def test_check_answer_text_post_request_with_a_non_existent_record_key(self, update_records_post_request_with_a_non_existent_record_key):
        print("request_result_text : ", update_records_post_request_with_a_non_existent_record_key.text)
        status = "record is not found"
        assert status in str(
            update_records_post_request_with_a_non_existent_record_key.text), "Answer text not " + status + " ; actual message : " + str(
            update_records_post_request_with_a_non_existent_record_key.text)