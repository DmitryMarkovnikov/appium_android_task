from screens.welcome_screen import WelcomeScreen


class TestSmoke:
    def test_positive_make_offer(self, get_registered_accounts_from_yml):
        sign_up_screen = WelcomeScreen(self.driver).use_email_to_enter()
        login_screen = sign_up_screen.switch_to_login()
        main_screen = login_screen.login(get_registered_accounts_from_yml['test_user_1'])
        cars_category = main_screen.open_category('cars')  # TODO fails time to time on this step
        car = cars_category.open_detailed_item_by_index(0)
        offer = car.buy_product()
        chat = offer.go_chating()
        chat.verify_made_offer()  # assertion part
        chat.clenup_offer()
