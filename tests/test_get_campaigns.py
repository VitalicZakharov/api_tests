import pytest
import allure

#=======================================================================================================================
#==================================================== Code 200 =========================================================
#=======================================================================================================================

# @allure.issue("https://trac.brightpattern.com/ticket/24242")
@pytest.mark.usefixtures("get_campaigns_get_request_to_get_campaigns_info")
class Test_get_request_to_get_campaigns_info():
    @allure.epic("test_get_campaigns")
    @allure.feature("answer code 200")
    @allure.step('test_check_status_code_get_request_to_get_campaigns_info')
    def test_check_status_code_get_request_to_get_campaigns_info(self, get_campaigns_get_request_to_get_campaigns_info):
        print("request_result_status_code : ", get_campaigns_get_request_to_get_campaigns_info.status_code)
        assert "200" in str(
            get_campaigns_get_request_to_get_campaigns_info.status_code), "Answer status not 200 ; actual status code : " + str(
            get_campaigns_get_request_to_get_campaigns_info.status_code)

    @allure.epic("test_get_campaigns")
    @allure.feature("answer code 200")
    @allure.step('test_check_answer_text_get_request_to_get_campaigns_info')
    def test_check_answer_text_get_request_to_get_campaigns_info(self, get_campaigns_get_request_to_get_campaigns_info):
        print("request_result_text : ", get_campaigns_get_request_to_get_campaigns_info.text)
        status = '[{"name":"Camp","state":"STOPPED","lists":["List_9_3x.txt"]},{"name":"Camp_1","state":"RUNNING","lists":["List_1.txt","List_1000.csv","List_2.txt","List_Completed.txt","List_Delete1.txt","List_Delete2.txt"]},{"name":"Camp_2","state":"RUNNING","lists":[]}]'
        assert status in str(
            get_campaigns_get_request_to_get_campaigns_info.text), "Answer text not " + status + " ; actual message : " + str(
            get_campaigns_get_request_to_get_campaigns_info.text)


@pytest.mark.usefixtures("get_campaigns_get_request_all_campaigns_disabled")
class Test_get_request_all_campaigns_disabled():
    @allure.epic("test_get_campaigns")
    @allure.feature("answer code 200")
    @allure.step('test_check_status_code_get_request_all_campaigns_disabled')
    def test_check_status_code_get_request_all_campaigns_disabled(self, get_campaigns_get_request_all_campaigns_disabled):
        print("request_result_status_code : ", get_campaigns_get_request_all_campaigns_disabled.status_code)
        assert "200" in str(
            get_campaigns_get_request_all_campaigns_disabled.status_code), "Answer status not 200 ; actual status code : " + str(
            get_campaigns_get_request_all_campaigns_disabled.status_code)

    @allure.epic("test_get_campaigns")
    @allure.feature("answer code 200")
    @allure.step('test_check_answer_text_get_request_all_campaigns_disabled')
    def test_check_answer_text_get_request_all_campaigns_disabled(self, get_campaigns_get_request_all_campaigns_disabled):
        print("request_result_text : ", get_campaigns_get_request_all_campaigns_disabled.text)
        status = '[]'
        assert status in str(
            get_campaigns_get_request_all_campaigns_disabled.text), "Answer text not " + status + " ; actual message : " + str(
            get_campaigns_get_request_all_campaigns_disabled.text)


@pytest.mark.usefixtures("get_campaigns_get_request_started_predictive_campaign")
class Test_get_request_started_predictive_campaign():
    @allure.epic("test_get_campaigns")
    @allure.feature("answer code 200")
    @allure.step('test_check_status_code_get_request_started_predictive_campaign')
    def test_check_status_code_get_request_started_predictive_campaign(self, get_campaigns_get_request_started_predictive_campaign):
        print("request_result_status_code : ", get_campaigns_get_request_started_predictive_campaign.status_code)
        assert "200" in str(
            get_campaigns_get_request_started_predictive_campaign.status_code), "Answer status not 200 ; actual status code : " + str(
            get_campaigns_get_request_started_predictive_campaign.status_code)

    @allure.epic("test_get_campaigns")
    @allure.feature("answer code 200")
    @allure.step('test_check_answer_text_get_request_started_predictive_campaign')
    def test_check_answer_text_get_request_started_predictive_campaign(self, get_campaigns_get_request_started_predictive_campaign):
        print("request_result_text : ", get_campaigns_get_request_started_predictive_campaign.text)
        status = '[{"name":"Camp","state":"STOPPED","lists":["List_9_3x.txt"]},{"name":"Camp_1","state":"RUNNING","lists":["List_1.txt","List_1000.csv","List_2.txt","List_Completed.txt","List_Delete1.txt","List_Delete2.txt"]},{"name":"Camp_2","state":"RUNNING","lists":[]}]'
        assert status in str(
            get_campaigns_get_request_started_predictive_campaign.text), "Answer text not " + status + " ; actual message : " + str(
            get_campaigns_get_request_started_predictive_campaign.text)


@pytest.mark.usefixtures("get_campaigns_get_request_started_preview_campaign")
class Test_get_request_started_preview_campaign():
    @allure.epic("test_get_campaigns")
    @allure.feature("answer code 200")
    @allure.step('test_check_status_code_get_request_started_preview_campaign')
    def test_check_status_code_get_request_started_preview_campaign(self, get_campaigns_get_request_started_preview_campaign):
        print("request_result_status_code : ", get_campaigns_get_request_started_preview_campaign.status_code)
        assert "200" in str(
            get_campaigns_get_request_started_preview_campaign.status_code), "Answer status not 200 ; actual status code : " + str(
            get_campaigns_get_request_started_preview_campaign.status_code)

    @allure.epic("test_get_campaigns")
    @allure.feature("answer code 200")
    @allure.step('test_check_answer_text_get_request_started_preview_campaign')
    def test_check_answer_text_get_request_started_preview_campaign(self, get_campaigns_get_request_started_preview_campaign):
        print("request_result_text : ", get_campaigns_get_request_started_preview_campaign.text)
        status = '[{"name":"Camp","state":"STOPPED","lists":["List_9_3x.txt"]},{"name":"Camp_1","state":"RUNNING","lists":["List_1.txt","List_1000.csv","List_2.txt","List_Completed.txt","List_Delete1.txt","List_Delete2.txt"]},{"name":"Camp_2","state":"RUNNING","lists":[]}]'
        assert status in str(
            get_campaigns_get_request_started_preview_campaign.text), "Answer text not " + status + " ; actual message : " + str(
            get_campaigns_get_request_started_preview_campaign.text)

#=======================================================================================================================
#=======================================================================================================================
#=======================================================================================================================

#=======================================================================================================================
#==================================================== Code 401 =========================================================
#=======================================================================================================================

@pytest.mark.usefixtures("get_campaigns_get_request_with_do_not_authorize_session")
class Test_get_request_with_do_not_authorize_session():
    @allure.epic("test_get_campaigns")
    @allure.feature("answer code 401")
    @allure.step('test_check_status_code_get_request_with_do_not_authorize_session')
    def test_check_status_code_get_request_with_do_not_authorize_session(self,
                                                                          get_campaigns_get_request_with_do_not_authorize_session):
        print("request_result_status_code : ", get_campaigns_get_request_with_do_not_authorize_session.status_code)
        assert "401" in str(
            get_campaigns_get_request_with_do_not_authorize_session.status_code), "Answer status not 401 ; actual status code : " + str(
            get_campaigns_get_request_with_do_not_authorize_session.status_code)

    @allure.epic("test_get_campaigns")
    @allure.feature("answer code 401")
    @allure.step('test_check_answer_text_get_request_with_do_not_authorize_session')
    def test_check_answer_text_get_request_with_do_not_authorize_session(self,
                                                                          get_campaigns_get_request_with_do_not_authorize_session):
        print("request_result_text : ", get_campaigns_get_request_with_do_not_authorize_session.text)
        status = "Session is not authenticated"
        assert status in str(
            get_campaigns_get_request_with_do_not_authorize_session.text), "Answer text not " + status + " ; actual message : " + str(
            get_campaigns_get_request_with_do_not_authorize_session.text)

#=======================================================================================================================
#=======================================================================================================================
#=======================================================================================================================

#=======================================================================================================================
#==================================================== Code 403 =========================================================
#=======================================================================================================================

#@allure.issue("https://trac.brightpattern.com/ticket/24588")
@pytest.mark.usefixtures("get_campaigns_get_request_with_authorize_session_for_user_without_permission")
class Test_get_request_with_authorize_session_for_user_without_permission():
    @allure.epic("test_get_campaigns")
    @allure.feature("answer code 403")
    @allure.step('test_check_status_code_get_request_with_authorize_session_for_user_without_permission')
    def test_check_status_code_get_request_with_authorize_session_for_user_without_permission(self,
                                                                                               get_campaigns_get_request_with_authorize_session_for_user_without_permission):
        print("request_result_status_code : ", get_campaigns_get_request_with_authorize_session_for_user_without_permission.status_code)
        assert "403" in str(
            get_campaigns_get_request_with_authorize_session_for_user_without_permission.status_code), "Answer status not 403 ; actual status code : " + str(
            get_campaigns_get_request_with_authorize_session_for_user_without_permission.status_code)

    @allure.epic("test_get_campaigns")
    @allure.feature("answer code 403")
    @allure.step('test_check_answer_text_get_request_with_authorize_session_for_user_without_permission')
    def test_check_answer_text_get_request_with_authorize_session_for_user_without_permission(self,
                                                                                               get_campaigns_get_request_with_authorize_session_for_user_without_permission):
        print("request_result_text : ", get_campaigns_get_request_with_authorize_session_for_user_without_permission.text)
        status = "User authenticated but does not have sufficient privileges"
        assert status in str(
            get_campaigns_get_request_with_authorize_session_for_user_without_permission.text), "Answer text not " + status + " ; actual message : " + str(
            get_campaigns_get_request_with_authorize_session_for_user_without_permission.text)

#=======================================================================================================================
#=======================================================================================================================
#=======================================================================================================================

#=======================================================================================================================
#==================================================== Code 405 =========================================================
#=======================================================================================================================

#@allure.issue("https://trac.brightpattern.com/ticket/24265")
@pytest.mark.usefixtures("get_campaigns_post_request_with_correct_body")
class Test_post_request_with_correct_body():
    @allure.epic("test_get_campaigns")
    @allure.feature("answer code 405")
    @allure.step('test_check_status_code_post_request_with_correct_body')
    def test_check_status_code_post_request_with_correct_body(self, get_campaigns_post_request_with_correct_body):
        print("request_result_status_code : ", get_campaigns_post_request_with_correct_body.status_code)
        assert "405" in str(
            get_campaigns_post_request_with_correct_body.status_code), "Answer status not 405 ; actual status code : " + str(
            get_campaigns_post_request_with_correct_body.status_code)

    @allure.epic("test_get_campaigns")
    @allure.feature("answer code 405")
    @allure.step('test_check_answer_text_post_request_with_correct_body')
    def test_check_answer_text_post_request_with_correct_body(self, get_campaigns_post_request_with_correct_body):
        print("request_result_text : ", get_campaigns_post_request_with_correct_body.text)
        status = "Method Not Allowed"
        assert status in str(
            get_campaigns_post_request_with_correct_body.text), "Answer text not " + status + " ; actual message : " + str(
            get_campaigns_post_request_with_correct_body.text)
        # assert len(str(get_request_with_correct_body.text)) == 0, "Answer text not empty ; actual message : " + str(get_request_with_correct_body.text)


#@allure.issue("https://trac.brightpattern.com/ticket/24265")
@pytest.mark.usefixtures("get_campaigns_put_request_with_correct_body")
class Test_put_request_with_correct_body():
    @allure.epic("test_get_campaigns")
    @allure.feature("answer code 405")
    @allure.step('test_check_status_code_put_request_with_correct_body')
    def test_check_status_code_put_request_with_correct_body(self, get_campaigns_put_request_with_correct_body):
        print("request_result_status_code : ", get_campaigns_put_request_with_correct_body.status_code)
        assert "405" in str(
            get_campaigns_put_request_with_correct_body.status_code), "Answer status not 405 ; actual status code : " + str(
            get_campaigns_put_request_with_correct_body.status_code)

    @allure.epic("test_get_campaigns")
    @allure.feature("answer code 405")
    @allure.step('test_check_answer_text_put_request_with_correct_body')
    def test_check_answer_text_put_request_with_correct_body(self, get_campaigns_put_request_with_correct_body):
        print("request_result_text : ", get_campaigns_put_request_with_correct_body.text)
        status = "Method Not Allowed"
        assert status in str(
            get_campaigns_put_request_with_correct_body.text), "Answer text not " + status + " ; actual message : " + str(
            get_campaigns_put_request_with_correct_body.text)


#@allure.issue("https://trac.brightpattern.com/ticket/24265")
@pytest.mark.usefixtures("get_campaigns_delete_request_with_correct_body")
class Test_delete_request_with_correct_body():
    @allure.epic("test_get_campaigns")
    @allure.feature("answer code 405")
    @allure.step('test_check_status_code_delete_request_with_correct_body')
    def test_check_status_code_delete_request_with_correct_body(self, get_campaigns_delete_request_with_correct_body):
        print("request_result_status_code : ", get_campaigns_delete_request_with_correct_body.status_code)
        assert "405" in str(
            get_campaigns_delete_request_with_correct_body.status_code), "Answer status not 405 ; actual status code : " + str(
            get_campaigns_delete_request_with_correct_body.status_code)

    @allure.epic("test_get_campaigns")
    @allure.feature("answer code 405")
    @allure.step('test_check_answer_text_delete_request_with_correct_body')
    def test_check_answer_text_delete_request_with_correct_body(self, get_campaigns_delete_request_with_correct_body):
        print("request_result_text : ", get_campaigns_delete_request_with_correct_body.text)
        status = "Method Not Allowed"
        assert status in str(
            get_campaigns_delete_request_with_correct_body.text), "Answer text not " + status + " ; actual message : " + str(
            get_campaigns_delete_request_with_correct_body.text)

#=======================================================================================================================
#=======================================================================================================================
#=======================================================================================================================

#=======================================================================================================================
#==================================================== Code 404 =========================================================
#=======================================================================================================================

@pytest.mark.usefixtures("get_campaigns_get_request_with_invalid_url")
class Test_get_request_with_invalid_url():
    @allure.epic("test_get_campaigns")
    @allure.feature("answer code 404")
    @allure.step('test_check_status_code_get_request_with_invalid_url')
    def test_check_status_code_get_request_with_invalid_url(self, get_campaigns_get_request_with_invalid_url):
        print("request_result_status_code : ", get_campaigns_get_request_with_invalid_url.status_code)
        assert "404" in str(
            get_campaigns_get_request_with_invalid_url.status_code), "Answer status not 404 ; actual status code : " + str(
            get_campaigns_get_request_with_invalid_url.status_code)

    @allure.epic("test_get_campaigns")
    @allure.feature("answer code 404")
    @allure.step('test_check_answer_text_get_request_with_invalid_url')
    def test_check_answer_text_get_request_with_invalid_url(self, get_campaigns_get_request_with_invalid_url):
        print("request_result_text : ", get_campaigns_get_request_with_invalid_url.text)
        status = "HTTP 404 Not Found"
        assert status in str(
            get_campaigns_get_request_with_invalid_url.text), "Answer text not " + status + " ; actual message : " + str(
            get_campaigns_get_request_with_invalid_url.text)

#=======================================================================================================================
#=======================================================================================================================
#=======================================================================================================================