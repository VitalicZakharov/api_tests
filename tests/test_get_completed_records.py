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


@pytest.mark.usefixtures("get_completed_records_post_request_with_a_non_existent_query_parameter")
class Test_post_request_with_a_non_existent_query_parameter():
    @allure.epic("test_get_completed_records")
    @allure.feature("answer code 400")
    @allure.step('test_check_status_code_post_request_with_a_non_existent_query_parameter')
    def test_check_status_code_post_request_with_a_non_existent_query_parameter(self, get_completed_records_post_request_with_a_non_existent_query_parameter):
        print("request_result_status_code : ", get_completed_records_post_request_with_a_non_existent_query_parameter.status_code)
        assert "400" in str(
            get_completed_records_post_request_with_a_non_existent_query_parameter.status_code), "Answer status not 400 ; actual status code : " + str(
            get_completed_records_post_request_with_a_non_existent_query_parameter.status_code)

    @allure.epic("test_get_completed_records")
    @allure.feature("answer code 400")
    @allure.step('test_check_answer_text_post_request_with_a_non_existent_query_parameter')
    def test_check_answer_text_post_request_with_a_non_existent_query_parameter(self, get_completed_records_post_request_with_a_non_existent_query_parameter):
        print("request_result_text : ", get_completed_records_post_request_with_a_non_existent_query_parameter.text)
        status = 'invalid parameters'
        assert status in str(
            get_completed_records_post_request_with_a_non_existent_query_parameter.text), "Answer text not " + status + " ; actual message : " + str(
            get_completed_records_post_request_with_a_non_existent_query_parameter.text)


@pytest.mark.usefixtures("get_completed_records_post_request_with_a_wrong_fromtime_format")
class Test_post_request_with_a_wrong_fromtime_format():
    @allure.epic("test_get_completed_records")
    @allure.feature("answer code 400")
    @allure.step('test_check_status_code_post_request_with_a_wrong_fromtime_format')
    def test_check_status_code_post_request_with_a_wrong_fromtime_format(self, get_completed_records_post_request_with_a_wrong_fromtime_format):
        print("request_result_status_code : ", get_completed_records_post_request_with_a_wrong_fromtime_format.status_code)
        assert "400" in str(
            get_completed_records_post_request_with_a_wrong_fromtime_format.status_code), "Answer status not 400 ; actual status code : " + str(
            get_completed_records_post_request_with_a_wrong_fromtime_format.status_code)

    @allure.epic("test_get_completed_records")
    @allure.feature("answer code 400")
    @allure.step('test_check_answer_text_post_request_with_a_wrong_fromtime_format')
    def test_check_answer_text_post_request_with_a_wrong_fromtime_format(self, get_completed_records_post_request_with_a_wrong_fromtime_format):
        print("request_result_text : ", get_completed_records_post_request_with_a_wrong_fromtime_format.text)
        status = 'Unparseable date: "2003-03-03:15:06.456"'
        assert status in str(
            get_completed_records_post_request_with_a_wrong_fromtime_format.text), "Answer text not " + status + " ; actual message : " + str(
            get_completed_records_post_request_with_a_wrong_fromtime_format.text)


@pytest.mark.usefixtures("get_completed_records_post_request_with_maxsize_set_to_1000")
class Test_post_request_with_maxsize_set_to_1000():
    @allure.epic("test_get_completed_records")
    @allure.feature("answer code 200")
    @allure.step('test_check_status_code_post_request_with_maxsize_set_to_1000')
    def test_check_status_code_post_request_with_maxsize_set_to_1000(self, get_completed_records_post_request_with_maxsize_set_to_1000):
        print("request_result_status_code : ", get_completed_records_post_request_with_maxsize_set_to_1000.status_code)
        assert "200" in str(
            get_completed_records_post_request_with_maxsize_set_to_1000.status_code), "Answer status not 200 ; actual status code : " + str(
            get_completed_records_post_request_with_maxsize_set_to_1000.status_code)

    @allure.epic("test_get_completed_records")
    @allure.feature("answer code 200")
    @allure.step('test_check_answer_text_post_request_with_maxsize_set_to_1000')
    def test_check_answer_text_post_request_with_maxsize_set_to_1000(self, get_completed_records_post_request_with_maxsize_set_to_1000):
        print("request_result_text : ", get_completed_records_post_request_with_maxsize_set_to_1000.text)
        status = 'something'
        assert status in str(
            get_completed_records_post_request_with_maxsize_set_to_1000.text), "Answer text not " + status + " ; actual message : " + str(
            get_completed_records_post_request_with_maxsize_set_to_1000.text)


@pytest.mark.usefixtures("get_completed_records_post_request_maxSize_set_to_greater_than_1000")
class Test_post_request_maxSize_set_to_greater_than_1000():
    @allure.epic("test_get_completed_records")
    @allure.feature("answer code 400")
    @allure.step('test_check_status_code_post_request_maxSize_set_to_greater_than_1000')
    def test_check_status_code_post_request_maxSize_set_to_greater_than_1000(self, get_completed_records_post_request_maxSize_set_to_greater_than_1000):
        print("request_result_status_code : ", get_completed_records_post_request_maxSize_set_to_greater_than_1000.status_code)
        assert "400" in str(
            get_completed_records_post_request_maxSize_set_to_greater_than_1000.status_code), "Answer status not 400 ; actual status code : " + str(
            get_completed_records_post_request_maxSize_set_to_greater_than_1000.status_code)

    @allure.epic("test_get_completed_records")
    @allure.feature("answer code 400")
    @allure.step('test_check_answer_text_post_request_maxSize_set_to_greater_than_1000')
    def test_check_answer_text_post_request_maxSize_set_to_greater_than_1000(self, get_completed_records_post_request_maxSize_set_to_greater_than_1000):
        print("request_result_text : ", get_completed_records_post_request_maxSize_set_to_greater_than_1000.text)
        status = 'maxSize is too large (no more than 1000)'
        assert status in str(
            get_completed_records_post_request_maxSize_set_to_greater_than_1000.text), "Answer text not " + status + " ; actual message : " + str(
            get_completed_records_post_request_maxSize_set_to_greater_than_1000.text)


@pytest.mark.usefixtures("get_completed_records_post_request_with_do_not_authorize_session")
class Test_post_request_with_do_not_authorize_session():
    @allure.epic("test_get_completed_records")
    @allure.feature("answer code 401")
    @allure.step('test_check_status_code_post_request_with_do_not_authorize_session')
    def test_check_status_code_post_request_with_do_not_authorize_session(self,
                                                                          get_completed_records_post_request_with_do_not_authorize_session):
        print("request_result_status_code : ", get_completed_records_post_request_with_do_not_authorize_session.status_code)
        assert "401" in str(
            get_completed_records_post_request_with_do_not_authorize_session.status_code), "Answer status not 401 ; actual status code : " + str(
            get_completed_records_post_request_with_do_not_authorize_session.status_code)

    @allure.epic("test_get_completed_records")
    @allure.feature("answer code 401")
    @allure.step('test_check_answer_text_post_request_with_do_not_authorize_session')
    def test_check_answer_text_post_request_with_do_not_authorize_session(self,
                                                                          get_completed_records_post_request_with_do_not_authorize_session):
        print("request_result_text : ", get_completed_records_post_request_with_do_not_authorize_session.text)
        status = "Session is not authenticated"
        assert status in str(
            get_completed_records_post_request_with_do_not_authorize_session.text), "Answer text not " + status + " ; actual message : " + str(
            get_completed_records_post_request_with_do_not_authorize_session.text)


@pytest.mark.usefixtures("get_completed_records_post_request_with_invalid_url")
class Test_post_request_with_invalid_url():
    @allure.epic("test_get_completed_records")
    @allure.feature("answer code 404")
    @allure.step('test_check_status_code_post_request_with_invalid_url')
    def test_check_status_code_post_request_with_invalid_url(self, get_completed_records_post_request_with_invalid_url):
        print("request_result_status_code : ", get_completed_records_post_request_with_invalid_url.status_code)
        assert "404" in str(
            get_completed_records_post_request_with_invalid_url.status_code), "Answer status not 404 ; actual status code : " + str(
            get_completed_records_post_request_with_invalid_url.status_code)

    @allure.epic("test_get_completed_records")
    @allure.feature("answer code 404")
    @allure.step('test_check_answer_text_post_request_with_invalid_url')
    def test_check_answer_text_post_request_with_invalid_url(self, get_completed_records_post_request_with_invalid_url):
        print("request_result_text : ", get_completed_records_post_request_with_invalid_url.text)
        status = "HTTP 404 Not Found"
        assert status in str(
            get_completed_records_post_request_with_invalid_url.text), "Answer text not " + status + " ; actual message : " + str(
            get_completed_records_post_request_with_invalid_url.text)


#@pytest.mark.usefixtures("get_completed_records_post_request_to_the_non_existent_list")
#class Test_post_request_to_the_non_existent_list():
#    @allure.epic("test_get_completed_records")
#    @allure.feature("answer code 404")
#    @allure.step('test_check_status_code_post_request_to_the_non_existent_list')
#    def test_check_status_code_post_request_to_the_non_existent_list(self, get_completed_records_post_request_to_the_non_existent_list):
#        print("request_result_status_code : ", get_completed_records_post_request_to_the_non_existent_list.status_code)
#        assert "404" in str(
#            get_completed_records_post_request_to_the_non_existent_list.status_code), "Answer status not 404 ; actual status code : " + str(
#            get_completed_records_post_request_to_the_non_existent_list.status_code)
#
#    @allure.epic("test_get_completed_records")
#    @allure.feature("answer code 404")
#    @allure.step('test_check_answer_text_post_request_to_the_non_existent_list')
#    def test_check_answer_text_post_request_to_the_non_existent_list(self, get_completed_records_post_request_to_the_non_existent_list):
#        print("request_result_text : ", get_completed_records_post_request_to_the_non_existent_list.text)
#        status = "calling list not found"
#        assert status in str(
#            get_completed_records_post_request_to_the_non_existent_list.text), "Answer text not " + status + " ; actual message : " + str(
#            get_completed_records_post_request_to_the_non_existent_list.text)


#@allure.issue("https://trac.brightpattern.com/ticket/22720")
@pytest.mark.usefixtures("get_completed_records_post_request_with_invalid_fromtime_value_fromtime_alphabetical")
class Test_post_request_with_invalid_fromtime_value_fromtime_alphabetical():
    @allure.epic("test_get_completed_records")
    @allure.feature("answer code 400")
    @allure.step('test_check_status_code_post_request_with_invalid_fromtime_value_fromtime_alphabetical')
    def test_check_status_code_post_request_with_invalid_fromtime_value_fromtime_alphabetical(self, get_completed_records_post_request_with_invalid_fromtime_value_fromtime_alphabetical):
        print("request_result_status_code : ", get_completed_records_post_request_with_invalid_fromtime_value_fromtime_alphabetical.status_code)
        assert "400" in str(
            get_completed_records_post_request_with_invalid_fromtime_value_fromtime_alphabetical.status_code), "Answer status not 400 ; actual status code : " + str(
            get_completed_records_post_request_with_invalid_fromtime_value_fromtime_alphabetical.status_code)

    @allure.epic("test_get_completed_records")
    @allure.feature("answer code 400")
    @allure.step('test_check_answer_text_post_request_with_invalid_fromtime_value_fromtime_alphabetical')
    def test_check_answer_text_post_request_with_invalid_fromtime_value_fromtime_alphabetical(self, get_completed_records_post_request_with_invalid_fromtime_value_fromtime_alphabetical):
        print("request_result_text : ", get_completed_records_post_request_with_invalid_fromtime_value_fromtime_alphabetical.text)
        status = 'Unparseable date: "ab"'
        assert status in str(
            get_completed_records_post_request_with_invalid_fromtime_value_fromtime_alphabetical.text), "Answer text not " + status + " ; actual message : " + str(
            get_completed_records_post_request_with_invalid_fromtime_value_fromtime_alphabetical.text)


@allure.issue("https://trac.brightpattern.com/ticket/24692")
@pytest.mark.usefixtures("get_completed_records_post_request_with_invalid_maxsize_value_maxsize_alphabetical")
class Test_post_request_with_invalid_maxsize_value_maxsize_alphabetical():
    @allure.epic("test_get_completed_records")
    @allure.feature("answer code 400")
    @allure.step('test_check_status_code_post_request_with_invalid_maxsize_value_maxsize_alphabetical')
    def test_check_status_code_post_request_with_invalid_maxsize_value_maxsize_alphabetical(self, get_completed_records_post_request_with_invalid_maxsize_value_maxsize_alphabetical):
        print("request_result_status_code : ", get_completed_records_post_request_with_invalid_maxsize_value_maxsize_alphabetical.status_code)
        assert "400" in str(
            get_completed_records_post_request_with_invalid_maxsize_value_maxsize_alphabetical.status_code), "Answer status not 400 ; actual status code : " + str(
            get_completed_records_post_request_with_invalid_maxsize_value_maxsize_alphabetical.status_code)

    @allure.epic("test_get_completed_records")
    @allure.feature("answer code 400")
    @allure.step('test_check_answer_text_post_request_with_invalid_maxsize_value_maxsize_alphabetical')
    def test_check_answer_text_post_request_with_invalid_maxsize_value_maxsize_alphabetical(self, get_completed_records_post_request_with_invalid_maxsize_value_maxsize_alphabetical):
        print("request_result_text : ", get_completed_records_post_request_with_invalid_maxsize_value_maxsize_alphabetical.text)
        status = '<Fill this response>'
        assert status in str(
            get_completed_records_post_request_with_invalid_maxsize_value_maxsize_alphabetical.text), "Answer text not " + status + " ; actual message : " + str(
            get_completed_records_post_request_with_invalid_maxsize_value_maxsize_alphabetical.text)


@pytest.mark.usefixtures("get_completed_records_post_request_with_authorize_session_for_user_without_permission")
class Test_post_request_with_authorize_session_for_user_without_permission():
    @allure.epic("test_get_completed_records")
    @allure.feature("answer code 403")
    @allure.step('test_check_status_code_post_request_with_authorize_session_for_user_without_permission')
    def test_check_status_code_post_request_with_authorize_session_for_user_without_permission(self,
                                                                                               get_completed_records_post_request_with_authorize_session_for_user_without_permission):
        print("request_result_status_code : ", get_completed_records_post_request_with_authorize_session_for_user_without_permission.status_code)
        assert "403" in str(
            get_completed_records_post_request_with_authorize_session_for_user_without_permission.status_code), "Answer status not 403 ; actual status code : " + str(
            get_completed_records_post_request_with_authorize_session_for_user_without_permission.status_code)

    @allure.epic("test_get_completed_records")
    @allure.feature("answer code 403")
    @allure.step('test_check_answer_text_post_request_with_authorize_session_for_user_without_permission')
    def test_check_answer_text_post_request_with_authorize_session_for_user_without_permission(self,
                                                                                               get_completed_records_post_request_with_authorize_session_for_user_without_permission):
        print("request_result_text : ", get_completed_records_post_request_with_authorize_session_for_user_without_permission.text)
        status = "User authenticated but does not have sufficient privileges"
        assert status in str(
            get_completed_records_post_request_with_authorize_session_for_user_without_permission.text), "Answer text not " + status + " ; actual message : " + str(
            get_completed_records_post_request_with_authorize_session_for_user_without_permission.text)


@pytest.mark.usefixtures("get_completed_records_get_request_with_correct_body")
class Test_get_request_with_correct_body():
    @allure.epic("test_get_completed_records")
    @allure.feature("answer code 405")
    @allure.step('test_check_status_code_get_request_with_correct_body')
    def test_check_status_code_get_request_with_correct_body(self, get_completed_records_get_request_with_correct_body):
        print("request_result_status_code : ", get_completed_records_get_request_with_correct_body.status_code)
        assert "405" in str(
            get_completed_records_get_request_with_correct_body.status_code), "Answer status not 405 ; actual status code : " + str(
            get_completed_records_get_request_with_correct_body.status_code)

    @allure.epic("test_get_completed_records")
    @allure.feature("answer code 405")
    @allure.step('test_check_answer_text_get_request_with_correct_body')
    def test_check_answer_text_get_request_with_correct_body(self, get_completed_records_get_request_with_correct_body):
        print("request_result_text : ", get_completed_records_get_request_with_correct_body.text)
        status = "Method Not Allowed"
        assert status in str(
            get_completed_records_get_request_with_correct_body.text), "Answer text not " + status + " ; actual message : " + str(
            get_completed_records_get_request_with_correct_body.text)
        # assert len(str(get_request_with_correct_body.text)) == 0, "Answer text not empty ; actual message : " + str(get_request_with_correct_body.text)


#@allure.issue("https://trac.brightpattern.com/ticket/24265")
@pytest.mark.usefixtures("get_completed_records_put_request_with_correct_body")
class Test_put_request_with_correct_body():
    @allure.epic("test_get_completed_records")
    @allure.feature("answer code 405")
    @allure.step('test_check_status_code_put_request_with_correct_body')
    def test_check_status_code_put_request_with_correct_body(self, get_completed_records_put_request_with_correct_body):
        print("request_result_status_code : ", get_completed_records_put_request_with_correct_body.status_code)
        assert "405" in str(
            get_completed_records_put_request_with_correct_body.status_code), "Answer status not 405 ; actual status code : " + str(
            get_completed_records_put_request_with_correct_body.status_code)

    @allure.epic("test_get_completed_records")
    @allure.feature("answer code 405")
    @allure.step('test_check_answer_text_put_request_with_correct_body')
    def test_check_answer_text_put_request_with_correct_body(self, get_completed_records_put_request_with_correct_body):
        print("request_result_text : ", get_completed_records_put_request_with_correct_body.text)
        status = "Method Not Allowed"
        assert status in str(
            get_completed_records_put_request_with_correct_body.text), "Answer text not " + status + " ; actual message : " + str(
            get_completed_records_put_request_with_correct_body.text)


#@allure.issue("https://trac.brightpattern.com/ticket/24265")
@pytest.mark.usefixtures("get_completed_records_delete_request_with_correct_body")
class Test_delete_request_with_correct_body():
    @allure.epic("test_get_completed_records")
    @allure.feature("answer code 405")
    @allure.step('test_check_status_code_delete_request_with_correct_body')
    def test_check_status_code_delete_request_with_correct_body(self, get_completed_records_delete_request_with_correct_body):
        print("request_result_status_code : ", get_completed_records_delete_request_with_correct_body.status_code)
        assert "405" in str(
            get_completed_records_delete_request_with_correct_body.status_code), "Answer status not 405 ; actual status code : " + str(
            get_completed_records_delete_request_with_correct_body.status_code)

    @allure.epic("test_get_completed_records")
    @allure.feature("answer code 405")
    @allure.step('test_check_answer_text_delete_request_with_correct_body')
    def test_check_answer_text_delete_request_with_correct_body(self, get_completed_records_delete_request_with_correct_body):
        print("request_result_text : ", get_completed_records_delete_request_with_correct_body.text)
        status = "Method Not Allowed"
        assert status in str(
            get_completed_records_delete_request_with_correct_body.text), "Answer text not " + status + " ; actual message : " + str(
            get_completed_records_delete_request_with_correct_body.text)


@allure.issue("https://trac.brightpattern.com/ticket/24691")
@pytest.mark.usefixtures("get_completed_records_post_request_with_incorrect_body_format_typization")
class Test_post_request_with_incorrect_body_format_typization():
    @allure.epic("test_get_completed_records")
    @allure.feature("answer code 400")
    @allure.step('test_check_status_code_post_request_with_incorrect_body_format_typization')
    def test_check_status_code_post_request_with_incorrect_body_format_typization(self,
                                                                                  get_completed_records_post_request_with_incorrect_body_format_typization):
        print("request_result_status_code : ", get_completed_records_post_request_with_incorrect_body_format_typization.status_code)
        assert "400" in str(
            get_completed_records_post_request_with_incorrect_body_format_typization.status_code), "Answer status not 400 ; actual status code : " + str(
            get_completed_records_post_request_with_incorrect_body_format_typization.status_code)

    @allure.epic("test_get_completed_records")
    @allure.feature("answer code 400")
    @allure.step('test_check_answer_text_post_request_with_incorrect_body_format_typization')
    def test_check_answer_text_post_request_with_incorrect_body_format_typization(self,
                                                                                  get_completed_records_post_request_with_incorrect_body_format_typization):
        print("request_result_text : ", get_completed_records_post_request_with_incorrect_body_format_typization.text)
        status = "Expected BEGIN_OBJECT but was STRING at line 1 column 1 path $"
        assert status in str(
            get_completed_records_post_request_with_incorrect_body_format_typization.text), "Answer text not " + status + " ; actual message : " + str(
            get_completed_records_post_request_with_incorrect_body_format_typization.text)