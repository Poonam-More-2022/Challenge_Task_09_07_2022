import logging
logging.basicConfig(filename='change_details_task.log', level=logging.DEBUG, format='%(levelname)s %(asctime)s %(name)s %(message)s')


class stud_details:

#-----------------------------Public Member Functions for changing students details---------------
    def name_details(self):
        '''' This function will take and return updated name of user'''
        logging.info("You are in name_details public member function")
        try:
            logging.info("You are executing name_details of change_details module")
            name = input("Update name :")
            return name
        except Exception as e:
            logging.error(e)
            logging.exception(e)
            return e

    def surname_details(self):
        '''' This function will take and return updated surname of user'''
        logging.info("You are in surname_details public member function")
        try:
            logging.info("You are executing surname_details of change_details module")
            surname = input("Update your surname :")
            return surname
        except Exception as e:
            logging.error(e)
            logging.exception(e)
            return e

    def email_details(self):
        '''' This function will take and return updated email address of user'''
        logging.info("You are in email_details public member function")
        try:
            logging.info("You are executing email_details of change_details module")
            email_id = input("Update your email address : ")
            return email_id
        except Exception as e:
            logging.error(e)
            logging.exception(e)
            return e