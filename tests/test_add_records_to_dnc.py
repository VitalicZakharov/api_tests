import pytest
import allure

@allure.issue("https://trac.brightpattern.com/ticket/24443")
@pytest.mark.usefixtures("add_records_to_dnc_post_request_to_any_non_existent_dnc_list")
class Test_post_request_to_any_non_existent_dnc_list():
    @allure.epic("test_add_records_to_dnc")
    @allure.feature("answer code 404")
    @allure.step('test_check_status_code_post_request_to_any_non_existent_dnc_list')
    def test_check_status_code_post_request_to_any_non_existent_dnc_list(self, add_records_to_dnc_post_request_to_any_non_existent_dnc_list):
        print("request_result_status_code : ", add_records_to_dnc_post_request_to_any_non_existent_dnc_list.status_code)
        assert "404" in str(
            add_records_to_dnc_post_request_to_any_non_existent_dnc_list.status_code), "Answer status not 404 ; actual status code : " + str(
            add_records_to_dnc_post_request_to_any_non_existent_dnc_list.status_code)

    @allure.epic("test_add_records_to_dnc")
    @allure.feature("answer code 404")
    @allure.step('test_check_answer_text_post_request_to_any_non_existent_dnc_list')
    def test_check_answer_text_post_request_to_any_non_existent_dnc_list(self, add_records_to_dnc_post_request_to_any_non_existent_dnc_list):
        print("request_result_text : ", add_records_to_dnc_post_request_to_any_non_existent_dnc_list.text)
        status = "Object does not exist"
        assert status in add_records_to_dnc_post_request_to_any_non_existent_dnc_list.text, "Answer text not " + status + " ; actual message : " + str(
            add_records_to_dnc_post_request_to_any_non_existent_dnc_list.text)


@allure.issue("https://trac.brightpattern.com/ticket/24443")
@pytest.mark.usefixtures("add_records_to_dnc_post_request_containing_correctly_formatted_numbers_to_dnc_of_type_internal_duplicates_and_not")
class Test_post_request_containing_correctly_formatted_numbers_to_dnc_of_type_internal_duplicates_and_not():
    @allure.epic("test_add_records_to_dnc")
    @allure.feature("answer code 200")
    @allure.step('test_check_status_code_post_request_containing_correctly_formatted_numbers_to_dnc_of_type_internal_duplicates_and_not')
    def test_check_status_code_post_request_containing_correctly_formatted_numbers_to_dnc_of_type_internal_duplicates_and_not(self, add_records_to_dnc_post_request_containing_correctly_formatted_numbers_to_dnc_of_type_internal_duplicates_and_not):
        print("request_result_status_code : ", add_records_to_dnc_post_request_containing_correctly_formatted_numbers_to_dnc_of_type_internal_duplicates_and_not.status_code)
        assert "200" in str(
            add_records_to_dnc_post_request_containing_correctly_formatted_numbers_to_dnc_of_type_internal_duplicates_and_not.status_code), "Answer status not 200 ; actual status code : " + str(
            add_records_to_dnc_post_request_containing_correctly_formatted_numbers_to_dnc_of_type_internal_duplicates_and_not.status_code)

    @allure.epic("test_add_records_to_dnc")
    @allure.feature("answer code 200")
    @allure.step('test_check_answer_text_post_request_containing_correctly_formatted_numbers_to_dnc_of_type_internal_duplicates_and_not')
    def test_check_answer_text_post_request_containing_correctly_formatted_numbers_to_dnc_of_type_internal_duplicates_and_not(self, add_records_to_dnc_post_request_containing_correctly_formatted_numbers_to_dnc_of_type_internal_duplicates_and_not):
        print("request_result_text : ", add_records_to_dnc_post_request_containing_correctly_formatted_numbers_to_dnc_of_type_internal_duplicates_and_not.text)
        status = "{\"added\":2}"
        assert status in add_records_to_dnc_post_request_containing_correctly_formatted_numbers_to_dnc_of_type_internal_duplicates_and_not.text, "Answer text not " + status + " ; actual message : " + str(
            add_records_to_dnc_post_request_containing_correctly_formatted_numbers_to_dnc_of_type_internal_duplicates_and_not.text)


@allure.issue("https://trac.brightpattern.com/ticket/22859")
@allure.issue("https://trac.brightpattern.com/ticket/24443")
@pytest.mark.usefixtures("add_records_to_dnc_post_request_containing_both_correctly_and_incorrectly_formatted_numbers_to_dnc_of_type_internal")
class Test_post_request_containing_both_correctly_and_incorrectly_formatted_numbers_to_dnc_of_type_internal():
    @allure.epic("test_add_records_to_dnc")
    @allure.feature("answer code 200")
    @allure.step('test_check_status_code_post_request_containing_both_correctly_and_incorrectly_formatted_numbers_to_dnc_of_type_internal')
    def test_check_status_code_post_request_containing_both_correctly_and_incorrectly_formatted_numbers_to_dnc_of_type_internal(self, add_records_to_dnc_post_request_containing_both_correctly_and_incorrectly_formatted_numbers_to_dnc_of_type_internal):
        print("request_result_status_code : ", add_records_to_dnc_post_request_containing_both_correctly_and_incorrectly_formatted_numbers_to_dnc_of_type_internal.status_code)
        assert "200" in str(
            add_records_to_dnc_post_request_containing_both_correctly_and_incorrectly_formatted_numbers_to_dnc_of_type_internal.status_code), "Answer status not 200 ; actual status code : " + str(
            add_records_to_dnc_post_request_containing_both_correctly_and_incorrectly_formatted_numbers_to_dnc_of_type_internal.status_code)

    @allure.epic("test_add_records_to_dnc")
    @allure.feature("answer code 200")
    @allure.step('test_check_answer_text_post_request_containing_both_correctly_and_incorrectly_formatted_numbers_to_dnc_of_type_internal')
    def test_check_answer_text_post_request_containing_both_correctly_and_incorrectly_formatted_numbers_to_dnc_of_type_internal(self, add_records_to_dnc_post_request_containing_both_correctly_and_incorrectly_formatted_numbers_to_dnc_of_type_internal):
        print("request_result_text : ", add_records_to_dnc_post_request_containing_both_correctly_and_incorrectly_formatted_numbers_to_dnc_of_type_internal.text)
        status = "{\"added\":3}"
        assert status in add_records_to_dnc_post_request_containing_both_correctly_and_incorrectly_formatted_numbers_to_dnc_of_type_internal.text, "Answer text not " + status + " ; actual message : " + str(
            add_records_to_dnc_post_request_containing_both_correctly_and_incorrectly_formatted_numbers_to_dnc_of_type_internal.text)


@allure.issue("https://trac.brightpattern.com/ticket/24443")
@pytest.mark.usefixtures("add_records_to_dnc_post_request_containing_a_correctly_formatted_number_and_a_comment_to_dnc_of_type_internal_comment_not_correspond_any_existing_campaigns")
class Test_post_request_containing_a_correctly_formatted_number_and_a_comment_to_dnc_of_type_internal_comment_not_correspond_any_existing_campaigns():
    @allure.epic("test_add_records_to_dnc")
    @allure.feature("answer code 200")
    @allure.step('test_check_status_code_post_request_containing_a_correctly_formatted_number_and_a_comment_to_dnc_of_type_internal_comment_not_correspond_any_existing_campaigns')
    def test_check_status_code_post_request_containing_a_correctly_formatted_number_and_a_comment_to_dnc_of_type_internal_comment_not_correspond_any_existing_campaigns(self, add_records_to_dnc_post_request_containing_a_correctly_formatted_number_and_a_comment_to_dnc_of_type_internal_comment_not_correspond_any_existing_campaigns):
        print("request_result_status_code : ", add_records_to_dnc_post_request_containing_a_correctly_formatted_number_and_a_comment_to_dnc_of_type_internal_comment_not_correspond_any_existing_campaigns.status_code)
        assert "200" in str(
            add_records_to_dnc_post_request_containing_a_correctly_formatted_number_and_a_comment_to_dnc_of_type_internal_comment_not_correspond_any_existing_campaigns.status_code), "Answer status not 200 ; actual status code : " + str(
            add_records_to_dnc_post_request_containing_a_correctly_formatted_number_and_a_comment_to_dnc_of_type_internal_comment_not_correspond_any_existing_campaigns.status_code)

    @allure.epic("test_add_records_to_dnc")
    @allure.feature("answer code 200")
    @allure.step('test_check_answer_text_post_request_containing_a_correctly_formatted_number_and_a_comment_to_dnc_of_type_internal_comment_not_correspond_any_existing_campaigns')
    def test_check_answer_text_post_request_containing_a_correctly_formatted_number_and_a_comment_to_dnc_of_type_internal_comment_not_correspond_any_existing_campaigns(self, add_records_to_dnc_post_request_containing_a_correctly_formatted_number_and_a_comment_to_dnc_of_type_internal_comment_not_correspond_any_existing_campaigns):
        print("request_result_text : ", add_records_to_dnc_post_request_containing_a_correctly_formatted_number_and_a_comment_to_dnc_of_type_internal_comment_not_correspond_any_existing_campaigns.text)
        status = "{\"added\":2}"
        assert status in add_records_to_dnc_post_request_containing_a_correctly_formatted_number_and_a_comment_to_dnc_of_type_internal_comment_not_correspond_any_existing_campaigns.text, "Answer text not " + status + " ; actual message : " + str(
            add_records_to_dnc_post_request_containing_a_correctly_formatted_number_and_a_comment_to_dnc_of_type_internal_comment_not_correspond_any_existing_campaigns.text)


@allure.issue("https://trac.brightpattern.com/ticket/22851")
@allure.issue("https://trac.brightpattern.com/ticket/24443")
@pytest.mark.usefixtures("add_records_to_dnc_post_request_containing_a_correctly_spelled_us_state_to_a_dnc_of_type_geographic")
class Test_post_request_containing_a_correctly_spelled_us_state_to_a_dnc_of_type_geographic():
    @allure.epic("test_add_records_to_dnc")
    @allure.feature("answer code 403")
    @allure.step('test_check_status_code_post_request_containing_a_correctly_spelled_us_state_to_a_dnc_of_type_geographic')
    def test_check_status_code_post_request_containing_a_correctly_spelled_us_state_to_a_dnc_of_type_geographic(self, add_records_to_dnc_post_request_containing_a_correctly_spelled_us_state_to_a_dnc_of_type_geographic):
        print("request_result_status_code : ", add_records_to_dnc_post_request_containing_a_correctly_spelled_us_state_to_a_dnc_of_type_geographic.status_code)
        assert "403" in str(
            add_records_to_dnc_post_request_containing_a_correctly_spelled_us_state_to_a_dnc_of_type_geographic.status_code), "Answer status not 403 ; actual status code : " + str(
            add_records_to_dnc_post_request_containing_a_correctly_spelled_us_state_to_a_dnc_of_type_geographic.status_code)

    @allure.epic("test_add_records_to_dnc")
    @allure.feature("answer code 403")
    @allure.step('test_check_answer_text_post_request_containing_a_correctly_spelled_us_state_to_a_dnc_of_type_geographic')
    def test_check_answer_text_post_request_containing_a_correctly_spelled_us_state_to_a_dnc_of_type_geographic(self, add_records_to_dnc_post_request_containing_a_correctly_spelled_us_state_to_a_dnc_of_type_geographic):
        print("request_result_text : ", add_records_to_dnc_post_request_containing_a_correctly_spelled_us_state_to_a_dnc_of_type_geographic.text)
        status = "this type of list is not supported by the API"
        assert status in add_records_to_dnc_post_request_containing_a_correctly_spelled_us_state_to_a_dnc_of_type_geographic.text, "Answer text not " + status + " ; actual message : " + str(
            add_records_to_dnc_post_request_containing_a_correctly_spelled_us_state_to_a_dnc_of_type_geographic.text)


@allure.issue("https://trac.brightpattern.com/ticket/22859")
@allure.issue("https://trac.brightpattern.com/ticket/24443")
@pytest.mark.usefixtures("add_records_to_dnc_post_request_containing_a_free_text_to_a_dnc_of_type_record_exclusion")
class Test_post_request_containing_a_free_text_to_a_dnc_of_type_record_exclusion():
    @allure.epic("test_add_records_to_dnc")
    @allure.feature("answer code 200")
    @allure.step('test_check_status_code_post_request_containing_a_free_text_to_a_dnc_of_type_record_exclusion')
    def test_check_status_code_post_request_containing_a_free_text_to_a_dnc_of_type_record_exclusion(self, add_records_to_dnc_post_request_containing_a_free_text_to_a_dnc_of_type_record_exclusion):
        print("request_result_status_code : ", add_records_to_dnc_post_request_containing_a_free_text_to_a_dnc_of_type_record_exclusion.status_code)
        assert "200" in str(
            add_records_to_dnc_post_request_containing_a_free_text_to_a_dnc_of_type_record_exclusion.status_code), "Answer status not 200 ; actual status code : " + str(
            add_records_to_dnc_post_request_containing_a_free_text_to_a_dnc_of_type_record_exclusion.status_code)

    @allure.epic("test_add_records_to_dnc")
    @allure.feature("answer code 200")
    @allure.step('test_check_answer_text_post_request_containing_a_free_text_to_a_dnc_of_type_record_exclusion')
    def test_check_answer_text_post_request_containing_a_free_text_to_a_dnc_of_type_record_exclusion(self, add_records_to_dnc_post_request_containing_a_free_text_to_a_dnc_of_type_record_exclusion):
        print("request_result_text : ", add_records_to_dnc_post_request_containing_a_free_text_to_a_dnc_of_type_record_exclusion.text)
        status = "{\"added\":1}"
        assert status in add_records_to_dnc_post_request_containing_a_free_text_to_a_dnc_of_type_record_exclusion.text, "Answer text not " + status + " ; actual message : " + str(
            add_records_to_dnc_post_request_containing_a_free_text_to_a_dnc_of_type_record_exclusion.text)


@allure.issue("https://trac.brightpattern.com/ticket/24443")
@pytest.mark.usefixtures("add_records_to_dnc_post_request_add_a_new_and_an_existing_records_containing_a_valid_us_postal_code_to_a_dnc_of_type_geographic_and_free_text")
class Test_post_request_add_a_new_and_an_existing_records_containing_a_valid_us_postal_code_to_a_dnc_of_type_geographic_and_free_text():
    @allure.epic("test_add_records_to_dnc")
    @allure.feature("answer code 200")
    @allure.step('test_check_status_code_post_request_add_a_new_and_an_existing_records_containing_a_valid_us_postal_code_to_a_dnc_of_type_geographic_and_free_text')
    def test_check_status_code_post_request_add_a_new_and_an_existing_records_containing_a_valid_us_postal_code_to_a_dnc_of_type_geographic_and_free_text(self, add_records_to_dnc_post_request_add_a_new_and_an_existing_records_containing_a_valid_us_postal_code_to_a_dnc_of_type_geographic_and_free_text):
        print("request_result_status_code : ", add_records_to_dnc_post_request_add_a_new_and_an_existing_records_containing_a_valid_us_postal_code_to_a_dnc_of_type_geographic_and_free_text.status_code)
        assert "200" in str(
            add_records_to_dnc_post_request_add_a_new_and_an_existing_records_containing_a_valid_us_postal_code_to_a_dnc_of_type_geographic_and_free_text.status_code), "Answer status not 200 ; actual status code : " + str(
            add_records_to_dnc_post_request_add_a_new_and_an_existing_records_containing_a_valid_us_postal_code_to_a_dnc_of_type_geographic_and_free_text.status_code)

    @allure.epic("test_add_records_to_dnc")
    @allure.feature("answer code 200")
    @allure.step('test_check_answer_text_post_request_add_a_new_and_an_existing_records_containing_a_valid_us_postal_code_to_a_dnc_of_type_geographic_and_free_text')
    def test_check_answer_text_post_request_add_a_new_and_an_existing_records_containing_a_valid_us_postal_code_to_a_dnc_of_type_geographic_and_free_text(self, add_records_to_dnc_post_request_add_a_new_and_an_existing_records_containing_a_valid_us_postal_code_to_a_dnc_of_type_geographic_and_free_text):
        print("request_result_text : ", add_records_to_dnc_post_request_add_a_new_and_an_existing_records_containing_a_valid_us_postal_code_to_a_dnc_of_type_geographic_and_free_text.text)
        status = "{\"added\":1}"
        assert status in add_records_to_dnc_post_request_add_a_new_and_an_existing_records_containing_a_valid_us_postal_code_to_a_dnc_of_type_geographic_and_free_text.text, "Answer text not " + status + " ; actual message : " + str(
            add_records_to_dnc_post_request_add_a_new_and_an_existing_records_containing_a_valid_us_postal_code_to_a_dnc_of_type_geographic_and_free_text.text)


@allure.issue("https://trac.brightpattern.com/ticket/24443")
@pytest.mark.usefixtures("add_records_to_dnc_post_request_add_a_record_containing_a_valid_us_postal_code_to_a_dnc_of_type_geographic_and_free_text")
class Test_post_request_add_a_record_containing_a_valid_us_postal_code_to_a_dnc_of_type_geographic_and_free_text():
    @allure.epic("test_add_records_to_dnc")
    @allure.feature("answer code 200")
    @allure.step('test_check_status_code_post_request_add_a_record_containing_a_valid_us_postal_code_to_a_dnc_of_type_geographic_and_free_text')
    def test_check_status_code_post_request_add_a_record_containing_a_valid_us_postal_code_to_a_dnc_of_type_geographic_and_free_text(self, add_records_to_dnc_post_request_add_a_record_containing_a_valid_us_postal_code_to_a_dnc_of_type_geographic_and_free_text):
        print("request_result_status_code : ", add_records_to_dnc_post_request_add_a_record_containing_a_valid_us_postal_code_to_a_dnc_of_type_geographic_and_free_text.status_code)
        assert "200" in str(
            add_records_to_dnc_post_request_add_a_record_containing_a_valid_us_postal_code_to_a_dnc_of_type_geographic_and_free_text.status_code), "Answer status not 200 ; actual status code : " + str(
            add_records_to_dnc_post_request_add_a_record_containing_a_valid_us_postal_code_to_a_dnc_of_type_geographic_and_free_text.status_code)

    @allure.epic("test_add_records_to_dnc")
    @allure.feature("answer code 200")
    @allure.step('test_check_answer_text_post_request_add_a_record_containing_a_valid_us_postal_code_to_a_dnc_of_type_geographic_and_free_text')
    def test_check_answer_text_post_request_add_a_record_containing_a_valid_us_postal_code_to_a_dnc_of_type_geographic_and_free_text(self, add_records_to_dnc_post_request_add_a_record_containing_a_valid_us_postal_code_to_a_dnc_of_type_geographic_and_free_text):
        print("request_result_text : ", add_records_to_dnc_post_request_add_a_record_containing_a_valid_us_postal_code_to_a_dnc_of_type_geographic_and_free_text.text)
        status = "{\"added\":2}"
        assert status in add_records_to_dnc_post_request_add_a_record_containing_a_valid_us_postal_code_to_a_dnc_of_type_geographic_and_free_text.text, "Answer text not " + status + " ; actual message : " + str(
            add_records_to_dnc_post_request_add_a_record_containing_a_valid_us_postal_code_to_a_dnc_of_type_geographic_and_free_text.text)


@allure.issue("https://trac.brightpattern.com/ticket/24443")
@pytest.mark.usefixtures("add_records_to_dnc_post_request_add_2_records_containing_a_special_symbols_postal_code_to_a_dnc_of_type_geographic_and_free_text")
class Test_post_request_add_2_records_containing_a_special_symbols_postal_code_to_a_dnc_of_type_geographic_and_free_text():
    @allure.epic("test_add_records_to_dnc")
    @allure.feature("answer code 200")
    @allure.step('test_check_status_code_post_request_add_2_records_containing_a_special_symbols_postal_code_to_a_dnc_of_type_geographic_and_free_text')
    def test_check_status_code_post_request_add_2_records_containing_a_special_symbols_postal_code_to_a_dnc_of_type_geographic_and_free_text(self, add_records_to_dnc_post_request_add_2_records_containing_a_special_symbols_postal_code_to_a_dnc_of_type_geographic_and_free_text):
        print("request_result_status_code : ", add_records_to_dnc_post_request_add_2_records_containing_a_special_symbols_postal_code_to_a_dnc_of_type_geographic_and_free_text.status_code)
        assert "200" in str(
            add_records_to_dnc_post_request_add_2_records_containing_a_special_symbols_postal_code_to_a_dnc_of_type_geographic_and_free_text.status_code), "Answer status not 200 ; actual status code : " + str(
            add_records_to_dnc_post_request_add_2_records_containing_a_special_symbols_postal_code_to_a_dnc_of_type_geographic_and_free_text.status_code)

    @allure.epic("test_add_records_to_dnc")
    @allure.feature("answer code 200")
    @allure.step('test_check_answer_text_post_request_add_2_records_containing_a_special_symbols_postal_code_to_a_dnc_of_type_geographic_and_free_text')
    def test_check_answer_text_post_request_add_2_records_containing_a_special_symbols_postal_code_to_a_dnc_of_type_geographic_and_free_text(self, add_records_to_dnc_post_request_add_2_records_containing_a_special_symbols_postal_code_to_a_dnc_of_type_geographic_and_free_text):
        print("request_result_text : ", add_records_to_dnc_post_request_add_2_records_containing_a_special_symbols_postal_code_to_a_dnc_of_type_geographic_and_free_text.text)
        status = "{\"added\":2}"
        assert status in add_records_to_dnc_post_request_add_2_records_containing_a_special_symbols_postal_code_to_a_dnc_of_type_geographic_and_free_text.text, "Answer text not " + status + " ; actual message : " + str(
            add_records_to_dnc_post_request_add_2_records_containing_a_special_symbols_postal_code_to_a_dnc_of_type_geographic_and_free_text.text)


@allure.issue("https://trac.brightpattern.com/ticket/24443")
@pytest.mark.usefixtures("add_records_to_dnc_post_request_add_nothing_for_1_record_for_a_dnc_of_type_geographic")
class Test_post_request_add_nothing_for_1_record_for_a_dnc_of_type_geographic():
    @allure.epic("test_add_records_to_dnc")
    @allure.feature("answer code 200")
    @allure.step('test_check_status_code_post_request_add_nothing_for_1_record_for_a_dnc_of_type_geographic')
    def test_check_status_code_post_request_add_nothing_for_1_record_for_a_dnc_of_type_geographic(self, add_records_to_dnc_post_request_add_nothing_for_1_record_for_a_dnc_of_type_geographic):
        print("request_result_status_code : ", add_records_to_dnc_post_request_add_nothing_for_1_record_for_a_dnc_of_type_geographic.status_code)
        assert "200" in str(
            add_records_to_dnc_post_request_add_nothing_for_1_record_for_a_dnc_of_type_geographic.status_code), "Answer status not 200 ; actual status code : " + str(
            add_records_to_dnc_post_request_add_nothing_for_1_record_for_a_dnc_of_type_geographic.status_code)

    @allure.epic("test_add_records_to_dnc")
    @allure.feature("answer code 200")
    @allure.step('test_check_answer_text_post_request_add_nothing_for_1_record_for_a_dnc_of_type_geographic')
    def test_check_answer_text_post_request_add_nothing_for_1_record_for_a_dnc_of_type_geographic(self, add_records_to_dnc_post_request_add_nothing_for_1_record_for_a_dnc_of_type_geographic):
        print("request_result_text : ", add_records_to_dnc_post_request_add_nothing_for_1_record_for_a_dnc_of_type_geographic.text)
        status = "{\"added\":2}"
        assert status in add_records_to_dnc_post_request_add_nothing_for_1_record_for_a_dnc_of_type_geographic.text, "Answer text not " + status + " ; actual message : " + str(
            add_records_to_dnc_post_request_add_nothing_for_1_record_for_a_dnc_of_type_geographic.text)


@allure.issue("https://trac.brightpattern.com/ticket/24443")
@allure.issue("https://trac.brightpattern.com/ticket/22859")
@pytest.mark.usefixtures("add_records_to_dnc_post_request_add_only_1_record_with_a_comment_for_a_dnc_of_type_geographic")
class Test_post_request_add_only_1_record_with_a_comment_for_a_dnc_of_type_geographic():
    @allure.epic("test_add_records_to_dnc")
    @allure.feature("answer code 200")
    @allure.step('test_check_status_code_post_request_add_only_1_record_with_a_comment_for_a_dnc_of_type_geographic')
    def test_check_status_code_post_request_add_only_1_record_with_a_comment_for_a_dnc_of_type_geographic(self, add_records_to_dnc_post_request_add_only_1_record_with_a_comment_for_a_dnc_of_type_geographic):
        print("request_result_status_code : ", add_records_to_dnc_post_request_add_only_1_record_with_a_comment_for_a_dnc_of_type_geographic.status_code)
        assert "200" in str(
            add_records_to_dnc_post_request_add_only_1_record_with_a_comment_for_a_dnc_of_type_geographic.status_code), "Answer status not 200 ; actual status code : " + str(
            add_records_to_dnc_post_request_add_only_1_record_with_a_comment_for_a_dnc_of_type_geographic.status_code)

    @allure.epic("test_add_records_to_dnc")
    @allure.feature("answer code 200")
    @allure.step('test_check_answer_text_post_request_add_only_1_record_with_a_comment_for_a_dnc_of_type_geographic')
    def test_check_answer_text_post_request_add_only_1_record_with_a_comment_for_a_dnc_of_type_geographic(self, add_records_to_dnc_post_request_add_only_1_record_with_a_comment_for_a_dnc_of_type_geographic):
        print("request_result_text : ", add_records_to_dnc_post_request_add_only_1_record_with_a_comment_for_a_dnc_of_type_geographic.text)
        status = "{\"added\":1}"
        assert status in add_records_to_dnc_post_request_add_only_1_record_with_a_comment_for_a_dnc_of_type_geographic.text, "Answer text not " + status + " ; actual message : " + str(
            add_records_to_dnc_post_request_add_only_1_record_with_a_comment_for_a_dnc_of_type_geographic.text)


@allure.issue("https://trac.brightpattern.com/ticket/24443")
@pytest.mark.usefixtures("add_records_to_dnc_post_request_add_a_record_containing_a_valid_us_area_code_to_a_dnc_of_type_area_codes_and_free_text")
class Test_post_request_add_a_record_containing_a_valid_us_area_code_to_a_dnc_of_type_area_codes_and_free_text():
    @allure.epic("test_add_records_to_dnc")
    @allure.feature("answer code 200")
    @allure.step('test_check_status_code_post_request_add_a_record_containing_a_valid_us_area_code_to_a_dnc_of_type_area_codes_and_free_text')
    def test_check_status_code_post_request_add_a_record_containing_a_valid_us_area_code_to_a_dnc_of_type_area_codes_and_free_text(self, add_records_to_dnc_post_request_add_a_record_containing_a_valid_us_area_code_to_a_dnc_of_type_area_codes_and_free_text):
        print("request_result_status_code : ", add_records_to_dnc_post_request_add_a_record_containing_a_valid_us_area_code_to_a_dnc_of_type_area_codes_and_free_text.status_code)
        assert "200" in str(
            add_records_to_dnc_post_request_add_a_record_containing_a_valid_us_area_code_to_a_dnc_of_type_area_codes_and_free_text.status_code), "Answer status not 200 ; actual status code : " + str(
            add_records_to_dnc_post_request_add_a_record_containing_a_valid_us_area_code_to_a_dnc_of_type_area_codes_and_free_text.status_code)

    @allure.epic("test_add_records_to_dnc")
    @allure.feature("answer code 200")
    @allure.step('test_check_answer_text_post_request_add_a_record_containing_a_valid_us_area_code_to_a_dnc_of_type_area_codes_and_free_text')
    def test_check_answer_text_post_request_add_a_record_containing_a_valid_us_area_code_to_a_dnc_of_type_area_codes_and_free_text(self, add_records_to_dnc_post_request_add_a_record_containing_a_valid_us_area_code_to_a_dnc_of_type_area_codes_and_free_text):
        print("request_result_text : ", add_records_to_dnc_post_request_add_a_record_containing_a_valid_us_area_code_to_a_dnc_of_type_area_codes_and_free_text.text)
        status = "{\"added\":2}"
        assert status in add_records_to_dnc_post_request_add_a_record_containing_a_valid_us_area_code_to_a_dnc_of_type_area_codes_and_free_text.text, "Answer text not " + status + " ; actual message : " + str(
            add_records_to_dnc_post_request_add_a_record_containing_a_valid_us_area_code_to_a_dnc_of_type_area_codes_and_free_text.text)


@allure.issue("https://trac.brightpattern.com/ticket/24443")
@pytest.mark.usefixtures("add_records_to_dnc_post_request_add_a_record_containing_an_incorrectly_formatted_us_area_code_to_a_dnc_of_type_area_codes")
class Test_post_request_add_a_record_containing_an_incorrectly_formatted_us_area_code_to_a_dnc_of_type_area_codes():
    @allure.epic("test_add_records_to_dnc")
    @allure.feature("answer code 200")
    @allure.step('test_check_status_code_post_request_add_a_record_containing_an_incorrectly_formatted_us_area_code_to_a_dnc_of_type_area_codes')
    def test_check_status_code_post_request_add_a_record_containing_an_incorrectly_formatted_us_area_code_to_a_dnc_of_type_area_codes(self, add_records_to_dnc_post_request_add_a_record_containing_an_incorrectly_formatted_us_area_code_to_a_dnc_of_type_area_codes):
        print("request_result_status_code : ", add_records_to_dnc_post_request_add_a_record_containing_an_incorrectly_formatted_us_area_code_to_a_dnc_of_type_area_codes.status_code)
        assert "200" in str(
            add_records_to_dnc_post_request_add_a_record_containing_an_incorrectly_formatted_us_area_code_to_a_dnc_of_type_area_codes.status_code), "Answer status not 200 ; actual status code : " + str(
            add_records_to_dnc_post_request_add_a_record_containing_an_incorrectly_formatted_us_area_code_to_a_dnc_of_type_area_codes.status_code)

    @allure.epic("test_add_records_to_dnc")
    @allure.feature("answer code 200")
    @allure.step('test_check_answer_text_post_request_add_a_record_containing_an_incorrectly_formatted_us_area_code_to_a_dnc_of_type_area_codes')
    def test_check_answer_text_post_request_add_a_record_containing_an_incorrectly_formatted_us_area_code_to_a_dnc_of_type_area_codes(self, add_records_to_dnc_post_request_add_a_record_containing_an_incorrectly_formatted_us_area_code_to_a_dnc_of_type_area_codes):
        print("request_result_text : ", add_records_to_dnc_post_request_add_a_record_containing_an_incorrectly_formatted_us_area_code_to_a_dnc_of_type_area_codes.text)
        status = "{\"added\":3}"
        assert status in add_records_to_dnc_post_request_add_a_record_containing_an_incorrectly_formatted_us_area_code_to_a_dnc_of_type_area_codes.text, "Answer text not " + status + " ; actual message : " + str(
            add_records_to_dnc_post_request_add_a_record_containing_an_incorrectly_formatted_us_area_code_to_a_dnc_of_type_area_codes.text)


@allure.issue("https://trac.brightpattern.com/ticket/24443")
@pytest.mark.usefixtures("add_records_to_dnc_post_request_with_do_not_authorize_session")
class Test_post_request_with_do_not_authorize_session():
    @allure.epic("test_add_records_to_dnc")
    @allure.feature("answer code 401")
    @allure.step('test_check_status_code_post_request_with_do_not_authorize_session')
    def test_check_status_code_post_request_with_do_not_authorize_session(self,
                                                                          add_records_to_dnc_post_request_with_do_not_authorize_session):
        print("request_result_status_code : ", add_records_to_dnc_post_request_with_do_not_authorize_session.status_code)
        assert "401" in str(
            add_records_to_dnc_post_request_with_do_not_authorize_session.status_code), "Answer status not 401 ; actual status code : " + str(
            add_records_to_dnc_post_request_with_do_not_authorize_session.status_code)

    @allure.epic("test_add_records_to_dnc")
    @allure.feature("answer code 401")
    @allure.step('test_check_answer_text_post_request_with_do_not_authorize_session')
    def test_check_answer_text_post_request_with_do_not_authorize_session(self,
                                                                          add_records_to_dnc_post_request_with_do_not_authorize_session):
        print("request_result_text : ", add_records_to_dnc_post_request_with_do_not_authorize_session.text)
        status = "Session is not authenticated"
        assert status in str(
            add_records_to_dnc_post_request_with_do_not_authorize_session.text), "Answer text not " + status + " ; actual message : " + str(
            add_records_to_dnc_post_request_with_do_not_authorize_session.text)


@allure.issue("https://trac.brightpattern.com/ticket/24443")
@allure.issue("https://trac.brightpattern.com/ticket/24588")
@pytest.mark.usefixtures("add_records_to_dnc_post_request_with_authorize_session_for_user_without_permission")
class Test_post_request_with_authorize_session_for_user_without_permission():
    @allure.epic("test_add_records_to_dnc")
    @allure.feature("answer code 403")
    @allure.step('test_check_status_code_post_request_with_authorize_session_for_user_without_permission')
    def test_check_status_code_post_request_with_authorize_session_for_user_without_permission(self,
                                                                                               add_records_to_dnc_post_request_with_authorize_session_for_user_without_permission):
        print("request_result_status_code : ", add_records_to_dnc_post_request_with_authorize_session_for_user_without_permission.status_code)
        assert "403" in str(
            add_records_to_dnc_post_request_with_authorize_session_for_user_without_permission.status_code), "Answer status not 403 ; actual status code : " + str(
            add_records_to_dnc_post_request_with_authorize_session_for_user_without_permission.status_code)

    @allure.epic("test_add_records_to_dnc")
    @allure.feature("answer code 403")
    @allure.step('test_check_answer_text_post_request_with_authorize_session_for_user_without_permission')
    def test_check_answer_text_post_request_with_authorize_session_for_user_without_permission(self,
                                                                                               add_records_to_dnc_post_request_with_authorize_session_for_user_without_permission):
        print("request_result_text : ", add_records_to_dnc_post_request_with_authorize_session_for_user_without_permission.text)
        status = "Access denied add"
        assert status in str(
            add_records_to_dnc_post_request_with_authorize_session_for_user_without_permission.text), "Answer text not " + status + " ; actual message : " + str(
            add_records_to_dnc_post_request_with_authorize_session_for_user_without_permission.text)


@allure.issue("https://trac.brightpattern.com/ticket/24445")
@allure.issue("https://trac.brightpattern.com/ticket/24443")
@pytest.mark.usefixtures("add_records_to_dnc_post_request_with_incorrect_body_format_typization")
class Test_post_request_with_incorrect_body_format_typization():
    @allure.epic("test_add_records_to_dnc")
    @allure.feature("answer code 400")
    @allure.step('test_check_status_code_post_request_with_incorrect_body_format_typization')
    def test_check_status_code_post_request_with_incorrect_body_format_typization(self,
                                                                                      add_records_to_dnc_post_request_with_incorrect_body_format_typization):
        print("request_result_status_code : ", add_records_to_dnc_post_request_with_incorrect_body_format_typization.status_code)
        assert "400" in str(
            add_records_to_dnc_post_request_with_incorrect_body_format_typization.status_code), "Answer status not 400 ; actual status code : " + str(
            add_records_to_dnc_post_request_with_incorrect_body_format_typization.status_code)

    @allure.epic("test_add_records_to_dnc")
    @allure.feature("answer code 400")
    @allure.step('test_check_answer_text_post_request_with_incorrect_body_format_typization')
    def test_check_answer_text_post_request_with_incorrect_body_format_typization(self,
                                                                                      add_records_to_dnc_post_request_with_incorrect_body_format_typization):
        print("request_result_text : ", add_records_to_dnc_post_request_with_incorrect_body_format_typization.text)
        status = "Expected BEGIN_OBJECT but was STRING at line 1 column 1 path $"
        assert status in str(
            add_records_to_dnc_post_request_with_incorrect_body_format_typization.text), "Answer text not " + status + " ; actual message : " + str(
            add_records_to_dnc_post_request_with_incorrect_body_format_typization.text)


@allure.issue("https://trac.brightpattern.com/ticket/24443")
#@allure.issue("https://trac.brightpattern.com/ticket/24437")
@pytest.mark.usefixtures("add_records_to_dnc_get_request_with_correct_body")
class Test_get_request_with_correct_body():
    @allure.epic("test_add_records_to_dnc")
    @allure.feature("answer code 405")
    @allure.step('test_check_status_code_get_request_with_correct_body')
    def test_check_status_code_get_request_with_correct_body(self, add_records_to_dnc_get_request_with_correct_body):
        print("request_result_status_code : ", add_records_to_dnc_get_request_with_correct_body.status_code)
        assert "405" in str(
            add_records_to_dnc_get_request_with_correct_body.status_code), "Answer status not 405 ; actual status code : " + str(
            add_records_to_dnc_get_request_with_correct_body.status_code)

    @allure.epic("test_add_records_to_dnc")
    @allure.feature("answer code 405")
    @allure.step('test_check_answer_text_get_request_with_correct_body')
    def test_check_answer_text_get_request_with_correct_body(self, add_records_to_dnc_get_request_with_correct_body):
        print("request_result_text : ", add_records_to_dnc_get_request_with_correct_body.text)
        status = "Method Not Allowed"
        assert status in str(
            add_records_to_dnc_get_request_with_correct_body.text), "Answer text not " + status + " ; actual message : " + str(
            add_records_to_dnc_get_request_with_correct_body.text)


@allure.issue("https://trac.brightpattern.com/ticket/24443")
#@allure.issue("https://trac.brightpattern.com/ticket/24437")
@pytest.mark.usefixtures("add_records_to_dnc_put_request_with_correct_body")
class Test_put_request_with_correct_body():
    @allure.epic("test_add_records_to_dnc")
    @allure.feature("answer code 405")
    @allure.step('test_check_status_code_put_request_with_correct_body')
    def test_check_status_code_put_request_with_correct_body(self, add_records_to_dnc_put_request_with_correct_body):
        print("request_result_status_code : ", add_records_to_dnc_put_request_with_correct_body.status_code)
        assert "405" in str(
            add_records_to_dnc_put_request_with_correct_body.status_code), "Answer status not 405 ; actual status code : " + str(
            add_records_to_dnc_put_request_with_correct_body.status_code)

    @allure.epic("test_add_records_to_dnc")
    @allure.feature("answer code 405")
    @allure.step('test_check_answer_text_put_request_with_correct_body')
    def test_check_answer_text_put_request_with_correct_body(self, add_records_to_dnc_put_request_with_correct_body):
        print("request_result_text : ", add_records_to_dnc_put_request_with_correct_body.text)
        status = "Method Not Allowed"
        assert status in str(
            add_records_to_dnc_put_request_with_correct_body.text), "Answer text not " + status + " ; actual message : " + str(
            add_records_to_dnc_put_request_with_correct_body.text)


@allure.issue("https://trac.brightpattern.com/ticket/24443")
#@allure.issue("https://trac.brightpattern.com/ticket/24437")
@pytest.mark.usefixtures("add_records_to_dnc_delete_request_with_correct_body")
class Test_delete_request_with_correct_body():
    @allure.epic("test_add_records_to_dnc")
    @allure.feature("answer code 405")
    @allure.step('test_check_status_code_delete_request_with_correct_body')
    def test_check_status_code_delete_request_with_correct_body(self, add_records_to_dnc_delete_request_with_correct_body):
        print("request_result_status_code : ", add_records_to_dnc_delete_request_with_correct_body.status_code)
        assert "405" in str(
            add_records_to_dnc_delete_request_with_correct_body.status_code), "Answer status not 405 ; actual status code : " + str(
            add_records_to_dnc_delete_request_with_correct_body.status_code)

    @allure.epic("test_add_records_to_dnc")
    @allure.feature("answer code 405")
    @allure.step('test_check_answer_text_delete_request_with_correct_body')
    def test_check_answer_text_delete_request_with_correct_body(self, add_records_to_dnc_delete_request_with_correct_body):
        print("request_result_text : ", add_records_to_dnc_delete_request_with_correct_body.text)
        status = "Method Not Allowed"
        assert status in str(
            add_records_to_dnc_delete_request_with_correct_body.text), "Answer text not " + status + " ; actual message : " + str(
            add_records_to_dnc_delete_request_with_correct_body.text)


#@allure.issue("https://trac.brightpattern.com/ticket/24443")
#@pytest.mark.usefixtures("add_records_to_dnc_post_request_with_body_from_other_list")
#class Test_post_request_with_body_from_other_list():
#    @allure.epic("test_add_records_to_dnc")
#    @allure.feature("answer code 400")
#    @allure.step('test_check_status_code_post_request_with_body_from_other_list')
#    def test_check_status_code_post_request_with_body_from_other_list(self, add_records_to_dnc_post_request_with_body_from_other_list):
#        print("request_result_status_code : ", add_records_to_dnc_post_request_with_body_from_other_list.status_code)
#        assert "400" in str(
#            add_records_to_dnc_post_request_with_body_from_other_list.status_code), "Answer status not 400 ; actual status code : " + str(
#            add_records_to_dnc_post_request_with_body_from_other_list.status_code)

#    @allure.epic("test_add_records_to_dnc")
#    @allure.feature("answer code 400")
#    @allure.step('test_check_answer_text_post_request_with_body_from_other_list')
#    def test_check_answer_text_post_request_with_body_from_other_list(self, add_records_to_dnc_post_request_with_body_from_other_list):
#        print("request_result_text : ", add_records_to_dnc_post_request_with_body_from_other_list.text)
#        status = "Some valid message"
#        assert status in str(
#            add_records_to_dnc_post_request_with_body_from_other_list.text), "Answer text not " + status + " ; actual message : " + str(
#            add_records_to_dnc_post_request_with_body_from_other_list.text)
