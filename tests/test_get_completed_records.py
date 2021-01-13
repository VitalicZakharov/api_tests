import pytest
import allure


# @allure.issue("https://trac.brightpattern.com/ticket/24242")
@pytest.mark.usefixtures("get_completed_records_post_request_with_valid_list_campaign_fromtime_and_maxsize_2")
class Test_post_request_with_valid_list_campaign_fromtime_and_maxsize_2():
    @allure.epic("test_get_completed_records")
    @allure.feature("answer code 200")
    @allure.step('test_check_status_code_post_request_with_valid_list_campaign_fromtime_and_maxsize_2')
    def test_check_status_code_post_request_with_valid_list_campaign_fromtime_and_maxsize_2(self, get_completed_records_post_request_with_valid_list_campaign_fromtime_and_maxsize_2):
        print("request_result_status_code : ", get_completed_records_post_request_with_valid_list_campaign_fromtime_and_maxsize_2.status_code)
        assert "200" in str(
            get_completed_records_post_request_with_valid_list_campaign_fromtime_and_maxsize_2.status_code), "Answer status not 200 ; actual status code : " + str(
            get_completed_records_post_request_with_valid_list_campaign_fromtime_and_maxsize_2.status_code)

    @allure.epic("test_get_completed_records")
    @allure.feature("answer code 200")
    @allure.step('test_check_answer_text_post_request_with_valid_list_campaign_fromtime_and_maxsize_2')
    def test_check_answer_text_post_request_with_valid_list_campaign_fromtime_and_maxsize_2(self, get_completed_records_post_request_with_valid_list_campaign_fromtime_and_maxsize_2):
        print("request_result_text : ", get_completed_records_post_request_with_valid_list_campaign_fromtime_and_maxsize_2.text)
        status = '[{"lastname":"Name_Last_C1","firstname":"Name_First_C1","agentid":"Test.C1","phone2":"8005","date/time":"07-07-2071","callerid":"101","integer":"1","phone1":"7005"},{"lastname":"Name_Last_C2","firstname":"Name_First_C2","agentid":"Test.C2","phone2":"8006","date/time":"07-07-2072","callerid":"102","integer":"2","phone1":"7006"}]'
        assert status in str(
            get_completed_records_post_request_with_valid_list_campaign_fromtime_and_maxsize_2.text), "Answer text not " + status + " ; actual message : " + str(
            get_completed_records_post_request_with_valid_list_campaign_fromtime_and_maxsize_2.text)


@pytest.mark.usefixtures("get_completed_records_post_request_with_valid_list_campaign_fromtime_and_maxsize_3")
class Test_post_request_with_valid_list_campaign_fromtime_and_maxsize_3():
    @allure.epic("test_get_completed_records")
    @allure.feature("answer code 200")
    @allure.step('test_check_status_code_post_request_with_valid_list_campaign_fromtime_and_maxsize_3')
    def test_check_status_code_post_request_with_valid_list_campaign_fromtime_and_maxsize_3(self, get_completed_records_post_request_with_valid_list_campaign_fromtime_and_maxsize_3):
        print("request_result_status_code : ", get_completed_records_post_request_with_valid_list_campaign_fromtime_and_maxsize_3.status_code)
        assert "200" in str(
            get_completed_records_post_request_with_valid_list_campaign_fromtime_and_maxsize_3.status_code), "Answer status not 200 ; actual status code : " + str(
            get_completed_records_post_request_with_valid_list_campaign_fromtime_and_maxsize_3.status_code)

    @allure.epic("test_get_completed_records")
    @allure.feature("answer code 200")
    @allure.step('test_check_answer_text_post_request_with_valid_list_campaign_fromtime_and_maxsize_3')
    def test_check_answer_text_post_request_with_valid_list_campaign_fromtime_and_maxsize_3(self, get_completed_records_post_request_with_valid_list_campaign_fromtime_and_maxsize_3):
        print("request_result_text : ", get_completed_records_post_request_with_valid_list_campaign_fromtime_and_maxsize_3.text)
        status = '[{"lastname":"Name_Last_C1","firstname":"Name_First_C1","agentid":"Test.C1","phone2":"8005","date/time":"07-07-2071","callerid":"101","integer":"1","phone1":"7005"},{"lastname":"Name_Last_C2","firstname":"Name_First_C2","agentid":"Test.C2","phone2":"8006","date/time":"07-07-2072","callerid":"102","integer":"2","phone1":"7006"},{"lastname":"Name_Last_C3","firstname":"Name_First_C3","agentid":"Test.C3","phone2":"8007","date/time":"07-07-2073","callerid":"103","integer":"3","phone1":"7007"}]'
        assert status in str(
            get_completed_records_post_request_with_valid_list_campaign_fromtime_and_maxsize_3.text), "Answer text not " + status + " ; actual message : " + str(
            get_completed_records_post_request_with_valid_list_campaign_fromtime_and_maxsize_3.text)


@pytest.mark.usefixtures("get_completed_records_post_request_with_valid_list_campaign_maxsize_and_fromtime_in_the_future")
class Test_post_request_with_valid_list_campaign_maxsize_and_fromtime_in_the_future():
    @allure.epic("test_get_completed_records")
    @allure.feature("answer code 200")
    @allure.step('test_check_status_code_post_request_with_valid_list_campaign_maxsize_and_fromtime_in_the_future')
    def test_check_status_code_post_request_with_valid_list_campaign_maxsize_and_fromtime_in_the_future(self, get_completed_records_post_request_with_valid_list_campaign_maxsize_and_fromtime_in_the_future):
        print("request_result_status_code : ", get_completed_records_post_request_with_valid_list_campaign_maxsize_and_fromtime_in_the_future.status_code)
        assert "200" in str(
            get_completed_records_post_request_with_valid_list_campaign_maxsize_and_fromtime_in_the_future.status_code), "Answer status not 200 ; actual status code : " + str(
            get_completed_records_post_request_with_valid_list_campaign_maxsize_and_fromtime_in_the_future.status_code)

    @allure.epic("test_get_completed_records")
    @allure.feature("answer code 200")
    @allure.step('test_check_answer_text_post_request_with_valid_list_campaign_maxsize_and_fromtime_in_the_future')
    def test_check_answer_text_post_request_with_valid_list_campaign_maxsize_and_fromtime_in_the_future(self, get_completed_records_post_request_with_valid_list_campaign_maxsize_and_fromtime_in_the_future):
        print("request_result_text : ", get_completed_records_post_request_with_valid_list_campaign_maxsize_and_fromtime_in_the_future.text)
        status = '[]'
        assert status in str(
            get_completed_records_post_request_with_valid_list_campaign_maxsize_and_fromtime_in_the_future.text), "Answer text not " + status + " ; actual message : " + str(
            get_completed_records_post_request_with_valid_list_campaign_maxsize_and_fromtime_in_the_future.text)


@pytest.mark.usefixtures("get_completed_records_post_request_with_valid_list_campaign_maxsize_but_without_fromtime")
class Test_post_request_with_valid_list_campaign_maxsize_but_without_fromtime():
    @allure.epic("test_get_completed_records")
    @allure.feature("answer code 400")
    @allure.step('test_check_status_code_post_request_with_valid_list_campaign_maxsize_but_without_fromtime')
    def test_check_status_code_post_request_with_valid_list_campaign_maxsize_but_without_fromtime(self, get_completed_records_post_request_with_valid_list_campaign_maxsize_but_without_fromtime):
        print("request_result_status_code : ", get_completed_records_post_request_with_valid_list_campaign_maxsize_but_without_fromtime.status_code)
        assert "400" in str(
            get_completed_records_post_request_with_valid_list_campaign_maxsize_but_without_fromtime.status_code), "Answer status not 400 ; actual status code : " + str(
            get_completed_records_post_request_with_valid_list_campaign_maxsize_but_without_fromtime.status_code)

    @allure.epic("test_get_completed_records")
    @allure.feature("answer code 400")
    @allure.step('test_check_answer_text_post_request_with_valid_list_campaign_maxsize_but_without_fromtime')
    def test_check_answer_text_post_request_with_valid_list_campaign_maxsize_but_without_fromtime(self, get_completed_records_post_request_with_valid_list_campaign_maxsize_but_without_fromtime):
        print("request_result_text : ", get_completed_records_post_request_with_valid_list_campaign_maxsize_but_without_fromtime.text)
        status = 'invalid parameters'
        assert status in str(
            get_completed_records_post_request_with_valid_list_campaign_maxsize_but_without_fromtime.text), "Answer text not " + status + " ; actual message : " + str(
            get_completed_records_post_request_with_valid_list_campaign_maxsize_but_without_fromtime.text)


@pytest.mark.usefixtures("get_completed_records_post_request_with_valid_list_campaign_fromtime_but_without_maxsize")
class Test_post_request_with_valid_list_campaign_fromtime_but_without_maxsize():
    @allure.epic("test_get_completed_records")
    @allure.feature("answer code 400")
    @allure.step('test_check_status_code_post_request_with_valid_list_campaign_fromtime_but_without_maxsize')
    def test_check_status_code_post_request_with_valid_list_campaign_fromtime_but_without_maxsize(self, get_completed_records_post_request_with_valid_list_campaign_fromtime_but_without_maxsize):
        print("request_result_status_code : ", get_completed_records_post_request_with_valid_list_campaign_fromtime_but_without_maxsize.status_code)
        assert "400" in str(
            get_completed_records_post_request_with_valid_list_campaign_fromtime_but_without_maxsize.status_code), "Answer status not 400 ; actual status code : " + str(
            get_completed_records_post_request_with_valid_list_campaign_fromtime_but_without_maxsize.status_code)

    @allure.epic("test_get_completed_records")
    @allure.feature("answer code 400")
    @allure.step('test_check_answer_text_post_request_with_valid_list_campaign_fromtime_but_without_maxsize')
    def test_check_answer_text_post_request_with_valid_list_campaign_fromtime_but_without_maxsize(self, get_completed_records_post_request_with_valid_list_campaign_fromtime_but_without_maxsize):
        print("request_result_text : ", get_completed_records_post_request_with_valid_list_campaign_fromtime_but_without_maxsize.text)
        status = 'invalid parameters'
        assert status in str(
            get_completed_records_post_request_with_valid_list_campaign_fromtime_but_without_maxsize.text), "Answer text not " + status + " ; actual message : " + str(
            get_completed_records_post_request_with_valid_list_campaign_fromtime_but_without_maxsize.text)


@pytest.mark.usefixtures("get_completed_records_post_request_with_valid_list_and_campaign_that_are_not_associated")
class Test_post_request_with_valid_list_and_campaign_that_are_not_associated():
    @allure.epic("test_get_completed_records")
    @allure.feature("answer code 404")
    @allure.step('test_check_status_code_post_request_with_valid_list_and_campaign_that_are_not_associated')
    def test_check_status_code_post_request_with_valid_list_and_campaign_that_are_not_associated(self, get_completed_records_post_request_with_valid_list_and_campaign_that_are_not_associated):
        print("request_result_status_code : ", get_completed_records_post_request_with_valid_list_and_campaign_that_are_not_associated.status_code)
        assert "404" in str(
            get_completed_records_post_request_with_valid_list_and_campaign_that_are_not_associated.status_code), "Answer status not 404 ; actual status code : " + str(
            get_completed_records_post_request_with_valid_list_and_campaign_that_are_not_associated.status_code)

    @allure.epic("test_get_completed_records")
    @allure.feature("answer code 404")
    @allure.step('test_check_answer_text_post_request_with_valid_list_and_campaign_that_are_not_associated')
    def test_check_answer_text_post_request_with_valid_list_and_campaign_that_are_not_associated(self, get_completed_records_post_request_with_valid_list_and_campaign_that_are_not_associated):
        print("request_result_text : ", get_completed_records_post_request_with_valid_list_and_campaign_that_are_not_associated.text)
        status = 'campaign is not found'
        assert status in str(
            get_completed_records_post_request_with_valid_list_and_campaign_that_are_not_associated.text), "Answer text not " + status + " ; actual message : " + str(
            get_completed_records_post_request_with_valid_list_and_campaign_that_are_not_associated.text)


@pytest.mark.usefixtures("get_completed_records_post_request_with_an_invalid_list_and_valid_campaign")
class Test_post_request_with_an_invalid_list_and_valid_campaign():
    @allure.epic("test_get_completed_records")
    @allure.feature("answer code 404")
    @allure.step('test_check_status_code_post_request_with_an_invalid_list_and_valid_campaign')
    def test_check_status_code_post_request_with_an_invalid_list_and_valid_campaign(self, get_completed_records_post_request_with_an_invalid_list_and_valid_campaign):
        print("request_result_status_code : ", get_completed_records_post_request_with_an_invalid_list_and_valid_campaign.status_code)
        assert "404" in str(
            get_completed_records_post_request_with_an_invalid_list_and_valid_campaign.status_code), "Answer status not 404 ; actual status code : " + str(
            get_completed_records_post_request_with_an_invalid_list_and_valid_campaign.status_code)

    @allure.epic("test_get_completed_records")
    @allure.feature("answer code 404")
    @allure.step('test_check_answer_text_post_request_with_an_invalid_list_and_valid_campaign')
    def test_check_answer_text_post_request_with_an_invalid_list_and_valid_campaign(self, get_completed_records_post_request_with_an_invalid_list_and_valid_campaign):
        print("request_result_text : ", get_completed_records_post_request_with_an_invalid_list_and_valid_campaign.text)
        status = 'calling list not found'
        assert status in str(
            get_completed_records_post_request_with_an_invalid_list_and_valid_campaign.text), "Answer text not " + status + " ; actual message : " + str(
            get_completed_records_post_request_with_an_invalid_list_and_valid_campaign.text)
