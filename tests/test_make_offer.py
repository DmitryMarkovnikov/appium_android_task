from screens.welcome_screen import WelcomeScreen

import logging

logger = logging.getLogger('tests')


class TestSmoke:
    def test_positive_make_offer(self, get_registered_accounts_from_yml):
        logger.info('Taping email to log in with registered user')
        sign_up_screen = WelcomeScreen(self.driver).use_email_to_enter()
        logger.info('Switching to login tab')
        login_screen = sign_up_screen.switch_to_login()
        logger.info('Login with already registered account')
        account = get_registered_accounts_from_yml['test_user_1']
        logger.debug('Account name: {0}, account password: {1}'.format(account['name'], account['password']))
        main_screen = login_screen.login(account)
        logger.info('Search and tap the category')
        cars_category = main_screen.open_category('cars')  # TODO fails time to time on this step
        logger.info('Open item by index')
        car = cars_category.open_detailed_item_by_index(0)
        logger.info('Going to making offer screen')
        offer = car.buy_product()
        logger.info('Make offer')
        chat = offer.go_chating()
        logger.info('Assert that offer was made')
        chat.verify_made_offer()  # assertion part
        logger.info('Apologize for user for made offer for testing purposes')
        chat.clenup_offer()
