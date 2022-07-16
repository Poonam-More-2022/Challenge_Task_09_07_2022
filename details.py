import logging
logging.basicConfig(filename='details_task.log', level=logging.DEBUG, format='%(levelname)s %(asctime)s %(name)s %(message)s')


class stud_details:
#-----------------------------Public Member Functions--------------------------------
    def name_details(self):
        '''' This function will take and return name of user'''
        logging.info("You are in name_details public member function")
        try:
            logging.info("You are executing name_details of details module")
            name = input("What's your first name? :")
            return name
        except Exception as e:
            logging.error(e)
            logging.exception(e)
            return e

    def surname_details(self):
        '''' This function will take and return surname of user'''
        logging.info("You are in surname_details public member function")
        try:
            logging.info("You are executing surname_details of details module")
            surname = input("I would love to know your surname as well.. :)  :")
            return surname
        except Exception as e:
            logging.error(e)
            logging.exception(e)
            return e

    def email_details(self):
        '''' This function will take and return email address of user'''
        logging.info("You are in email_details public member function")
        try:
            logging.info("You are executing email_details of details module")
            email_id = input("Let me know your email address so that I can assist you in better way : ")
            return email_id
        except Exception as e:
            logging.error(e)
            logging.exception(e)
            return e