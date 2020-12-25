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


@pytest.mark.usefixtures("delete_all_records_post_request_with_an_invalid_list")
class Test_post_request_with_an_invalid_list():
    @allure.epic("test_delete_all_records")
    @allure.feature("answer code 404")
    @allure.step('test_check_status_code_post_request_with_an_invalid_list')
    def test_check_status_code_post_request_with_an_invalid_list(self, delete_all_records_post_request_with_an_invalid_list):
        print("request_result_status_code : ", delete_all_records_post_request_with_an_invalid_list.status_code)
        assert "404" in str(
            delete_all_records_post_request_with_an_invalid_list.status_code), "Answer status not 404 ; actual status code : " + str(
            delete_all_records_post_request_with_an_invalid_list.status_code)

    @allure.epic("test_delete_all_records")
    @allure.feature("answer code 404")
    @allure.step('test_check_answer_text_post_request_with_an_invalid_list')
    def test_check_answer_text_post_request_with_an_invalid_list(self, delete_all_records_post_request_with_an_invalid_list):
        print("request_result_text : ", delete_all_records_post_request_with_an_invalid_list.text)
        status = 'calling list not found'
        assert status in str(
            delete_all_records_post_request_with_an_invalid_list.text), "Answer text not " + status + " ; actual message : " + str(
            delete_all_records_post_request_with_an_invalid_list.text)


@pytest.mark.usefixtures("delete_all_records_post_request_with_do_not_authorize_session")
class Test_post_request_with_do_not_authorize_session():
    @allure.epic("test_delete_all_records")
    @allure.feature("answer code 401")
    @allure.step('test_check_status_code_post_request_with_do_not_authorize_session')
    def test_check_status_code_post_request_with_do_not_authorize_session(self,
                                                                          delete_all_records_post_request_with_do_not_authorize_session):
        print("request_result_status_code : ", delete_all_records_post_request_with_do_not_authorize_session.status_code)
        assert "401" in str(
            delete_all_records_post_request_with_do_not_authorize_session.status_code), "Answer status not 401 ; actual status code : " + str(
            delete_all_records_post_request_with_do_not_authorize_session.status_code)

    @allure.epic("test_delete_all_records")
    @allure.feature("answer code 401")
    @allure.step('test_check_answer_text_post_request_with_do_not_authorize_session')
    def test_check_answer_text_post_request_with_do_not_authorize_session(self,
                                                                          delete_all_records_post_request_with_do_not_authorize_session):
        print("request_result_text : ", delete_all_records_post_request_with_do_not_authorize_session.text)
        status = "Session is not authenticated"
        assert status in str(
            delete_all_records_post_request_with_do_not_authorize_session.text), "Answer text not " + status + " ; actual message : " + str(
            delete_all_records_post_request_with_do_not_authorize_session.text)


@pytest.mark.usefixtures("delete_all_records_post_request_with_authorize_session_for_user_without_permission")
class Test_post_request_with_authorize_session_for_user_without_permission():
    @allure.epic("test_delete_all_records")
    @allure.feature("answer code 403")
    @allure.step('test_check_status_code_post_request_with_authorize_session_for_user_without_permission')
    def test_check_status_code_post_request_with_authorize_session_for_user_without_permission(self,
                                                                                               delete_all_records_post_request_with_authorize_session_for_user_without_permission):
        print("request_result_status_code : ", delete_all_records_post_request_with_authorize_session_for_user_without_permission.status_code)
        assert "403" in str(
            delete_all_records_post_request_with_authorize_session_for_user_without_permission.status_code), "Answer status not 403 ; actual status code : " + str(
            delete_all_records_post_request_with_authorize_session_for_user_without_permission.status_code)

    @allure.epic("test_delete_all_records")
    @allure.feature("answer code 403")
    @allure.step('test_check_answer_text_post_request_with_authorize_session_for_user_without_permission')
    def test_check_answer_text_post_request_with_authorize_session_for_user_without_permission(self,
                                                                                               delete_all_records_post_request_with_authorize_session_for_user_without_permission):
        print("request_result_text : ", delete_all_records_post_request_with_authorize_session_for_user_without_permission.text)
        status = "Access denied deleteAll"
        assert status in str(
            delete_all_records_post_request_with_authorize_session_for_user_without_permission.text), "Answer text not " + status + " ; actual message : " + str(
            delete_all_records_post_request_with_authorize_session_for_user_without_permission.text)


@pytest.mark.usefixtures("delete_all_records_post_request_with_invalid_url")
class Test_post_request_with_invalid_url():
    @allure.epic("test_delete_all_records")
    @allure.feature("answer code 404")
    @allure.step('test_check_status_code_post_request_with_invalid_url')
    def test_check_status_code_post_request_with_invalid_url(self, delete_all_records_post_request_with_invalid_url):
        print("request_result_status_code : ", delete_all_records_post_request_with_invalid_url.status_code)
        assert "404" in str(
            delete_all_records_post_request_with_invalid_url.status_code), "Answer status not 404 ; actual status code : " + str(
            delete_all_records_post_request_with_invalid_url.status_code)

    @allure.epic("test_delete_all_records")
    @allure.feature("answer code 404")
    @allure.step('test_check_answer_text_post_request_with_invalid_url')
    def test_check_answer_text_post_request_with_invalid_url(self, delete_all_records_post_request_with_invalid_url):
        print("request_result_text : ", delete_all_records_post_request_with_invalid_url.text)
        status = "HTTP 404 Not Found"
        assert status in str(
            delete_all_records_post_request_with_invalid_url.text), "Answer text not " + status + " ; actual message : " + str(
            delete_all_records_post_request_with_invalid_url.text)


@allure.issue("https://trac.brightpattern.com/ticket/24576")
@pytest.mark.usefixtures("delete_all_records_get_request_with_correct_body")
class Test_get_request_with_correct_body():
    @allure.epic("test_delete_all_records")
    @allure.feature("answer code 405")
    @allure.step('test_check_status_code_get_request_with_correct_body')
    def test_check_status_code_get_request_with_correct_body(self, delete_all_records_get_request_with_correct_body):
        print("request_result_status_code : ", delete_all_records_get_request_with_correct_body.status_code)
        assert "405" in str(
            delete_all_records_get_request_with_correct_body.status_code), "Answer status not 405 ; actual status code : " + str(
            delete_all_records_get_request_with_correct_body.status_code)

    @allure.epic("test_delete_all_records")
    @allure.feature("answer code 405")
    @allure.step('test_check_answer_text_get_request_with_correct_body')
    def test_check_answer_text_get_request_with_correct_body(self, delete_all_records_get_request_with_correct_body):
        print("request_result_text : ", delete_all_records_get_request_with_correct_body.text)
        status = "GET Method Not Allowed"
        assert status in str(
            delete_all_records_get_request_with_correct_body.text), "Answer text not " + status + " ; actual message : " + str(
            delete_all_records_get_request_with_correct_body.text)


@allure.issue("https://trac.brightpattern.com/ticket/24576")
@pytest.mark.usefixtures("delete_all_records_put_request_with_correct_body")
class Test_put_request_with_correct_body():
    @allure.epic("test_delete_all_records")
    @allure.feature("answer code 405")
    @allure.step('test_check_status_code_put_request_with_correct_body')
    def test_check_status_code_put_request_with_correct_body(self, delete_all_records_put_request_with_correct_body):
        print("request_result_status_code : ", delete_all_records_put_request_with_correct_body.status_code)
        assert "405" in str(
            delete_all_records_put_request_with_correct_body.status_code), "Answer status not 405 ; actual status code : " + str(
            delete_all_records_put_request_with_correct_body.status_code)

    @allure.epic("test_delete_all_records")
    @allure.feature("answer code 405")
    @allure.step('test_check_answer_text_put_request_with_correct_body')
    def test_check_answer_text_put_request_with_correct_body(self, delete_all_records_put_request_with_correct_body):
        print("request_result_text : ", delete_all_records_put_request_with_correct_body.text)
        status = "Method Not Allowed"
        assert status in str(
            delete_all_records_put_request_with_correct_body.text), "Answer text not " + status + " ; actual message : " + str(
            delete_all_records_put_request_with_correct_body.text)


@allure.issue("https://trac.brightpattern.com/ticket/24576")
@pytest.mark.usefixtures("delete_all_records_delete_request_with_correct_body")
class Test_delete_request_with_correct_body():
    @allure.epic("test_delete_all_records")
    @allure.feature("answer code 405")
    @allure.step('test_check_status_code_delete_request_with_correct_body')
    def test_check_status_code_delete_request_with_correct_body(self, delete_all_records_delete_request_with_correct_body):
        print("request_result_status_code : ", delete_all_records_delete_request_with_correct_body.status_code)
        assert "405" in str(
            delete_all_records_delete_request_with_correct_body.status_code), "Answer status not 405 ; actual status code : " + str(
            delete_all_records_delete_request_with_correct_body.status_code)

    @allure.epic("test_delete_all_records")
    @allure.feature("answer code 405")
    @allure.step('test_check_answer_text_delete_request_with_correct_body')
    def test_check_answer_text_delete_request_with_correct_body(self, delete_all_records_delete_request_with_correct_body):
        print("request_result_text : ", delete_all_records_delete_request_with_correct_body.text)
        status = "Method Not Allowed"
        assert status in str(
            delete_all_records_delete_request_with_correct_body.text), "Answer text not " + status + " ; actual message : " + str(
            delete_all_records_delete_request_with_correct_body.text)


@allure.issue("https://trac.brightpattern.com/ticket/24577")
@pytest.mark.usefixtures("delete_all_records_post_request_with_incorrect_body_format_typization")
class Test_post_request_with_incorrect_body_format_typization():
    @allure.epic("test_delete_all_records")
    @allure.feature("answer code 400")
    @allure.step('test_check_status_code_post_request_with_incorrect_body_format_typization')
    def test_check_status_code_post_request_with_incorrect_body_format_typization(self,
                                                                                  delete_all_records_post_request_with_incorrect_body_format_typization):
        print("request_result_status_code : ", delete_all_records_post_request_with_incorrect_body_format_typization.status_code)
        assert "400" in str(
            delete_all_records_post_request_with_incorrect_body_format_typization.status_code), "Answer status not 400 ; actual status code : " + str(
            delete_all_records_post_request_with_incorrect_body_format_typization.status_code)

    @allure.epic("test_delete_all_records")
    @allure.feature("answer code 400")
    @allure.step('test_check_answer_text_post_request_with_incorrect_body_format_typization')
    def test_check_answer_text_post_request_with_incorrect_body_format_typization(self,
                                                                                  delete_all_records_post_request_with_incorrect_body_format_typization):
        print("request_result_text : ", delete_all_records_post_request_with_incorrect_body_format_typization.text)
        status = "Expected BEGIN_OBJECT but was STRING at line 1 column 1 path $"
        assert status in str(
            delete_all_records_post_request_with_incorrect_body_format_typization.text), "Answer text not " + status + " ; actual message : " + str(
            delete_all_records_post_request_with_incorrect_body_format_typization.text)


@pytest.mark.usefixtures("delete_all_records_post_request_with_csv_list_format")
class Test_post_request_with_csv_list_format():
    @allure.epic("test_delete_all_records")
    @allure.feature("answer code 200")
    @allure.step('test_check_status_code_post_request_with_csv_list_format')
    def test_check_status_code_post_request_with_csv_list_format(self, delete_all_records_post_request_with_csv_list_format):
        print("request_result_status_code : ", delete_all_records_post_request_with_csv_list_format.status_code)
        assert "200" in str(
            delete_all_records_post_request_with_csv_list_format.status_code), "Answer status not 200 ; actual status code : " + str(
            delete_all_records_post_request_with_csv_list_format.status_code)

    @allure.epic("test_delete_all_records")
    @allure.feature("answer code 200")
    @allure.step('test_check_answer_text_post_request_with_csv_list_format')
    def test_check_answer_text_post_request_with_csv_list_format(self, delete_all_records_post_request_with_csv_list_format):
        print("request_result_text : ", delete_all_records_post_request_with_csv_list_format.text)
        assert len(str(
            delete_all_records_post_request_with_csv_list_format.text)) == 0, "Answer text not empty ; actual message : " + str(
            delete_all_records_post_request_with_csv_list_format.text)

