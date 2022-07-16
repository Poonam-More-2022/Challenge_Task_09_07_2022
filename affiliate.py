import logging
logging.basicConfig(filename='affiliate_task.log', level=logging.DEBUG, format='%(levelname)s %(asctime)s %(name)s %(message)s')

class ineuron_affiliate_data:
    __course1="OneNeuron (OTT platform for Education)"          #data abstraction, private data
    __course2="Full stack data science course (Job guaranteed)" #data abstraction, private data
    __webpage="https://ineuron.ai/"                             #data abstraction, private data

    def __init__(self, stud_name, stud_surname, emailid):       #constructor
        self.stud_name=stud_name                                #public data
        self._stud_surname=stud_surname                         #protected data
        self.__emailId=emailid                                  #data abstraction, private data

#------------------------------Functions for updating protected data values------------------------------
    # updating self.__emaiID
    def stud_email_change(self, new_value):
        ''' This function will update students email address which is protected data'''
        self.__emailId=new_value

    # updating __course1
    def UpdateCourse1(self, new_value):
        ''' This function will update course1 which is protected data'''
        ineuron_affiliate_data.__course1 = new_value

    # updating __course2
    def UpdateCourse2(self, new_value):
        ''' This function will update course2 which is protected data'''
        ineuron_affiliate_data.__course2 = new_value

    # updating __webpage
    def UpdateWebpage(self, new_value):
        ''' This function will update webpage which is protected data'''
        ineuron_affiliate_data.__webpage = new_value

#----------------------------Public Member Functions----------------------------------
#1.
    def how_to_start(self):                                     #public member function
        ''' This function returns about how to start affiliation program'''
        logging.info("You are in how_to_start public member function")
        try:
            logging.info("You are executing how_to_start of affiliation module")
            return "Dear {},Register by clicking on this link and follow the procedure".format(self.stud_name)
        except Exception as e:
            logging.error(e)
            logging.exception(e)
            return e

#2.
    def where_to_promote(self):                                  #public member function
        ''' This function returns information about where to promote'''
        logging.info(" You are in where_to_promote public member function")
        try:
            logging.info("You are executing where_to_promote of affiliation module")
            return "Dear {} {}, you have complete liberty of promoting your affiliate link as per your will, word of mouth, social media or door to door sales. The choice is yours.".format(self.stud_name, self._stud_surname)
        except Exception as e:
            logging.error(e)
            logging.exception(e)
            return e

#3.
    def which_products(self):                                   #public member function
        ''' This function returns information about which products can be promoted'''
        logging.info(" You are in which_products public member function")
        try:
            logging.info("You are executing which_products of affiliation module")
            return "Dear {}, you can do the promotion for \nA) {} \nB) {}".format(self.stud_name,ineuron_affiliate_data.__course1, ineuron_affiliate_data.__course2)
        except Exception as e:
            logging.error(e)
            logging.exception(e)
            return e

#4.
    def referral_earnings(self):                                   #public member function
        ''' This function returns information about referral earnings'''
        logging.info(" You are in referral_earnings public member function")
        try:
            logging.info("You are executing referral_earnings of affiliation module")
            return "Yes, dear {}, there is no minimum limit to earn commission in this affiliate program.".format(self.stud_name)
        except Exception as e:
            logging.error(e)
            logging.exception(e)
            return e

#5.
    def Max_referral_earnings(self):                                   #public member function
        ''' This function returns information about maximum limit for referral earnings'''
        logging.info(" You are in Max_referral_earnings public member function")
        try:
            logging.info("You are executing Max_referral_earnings of affiliation module")
            return "Dear {}, there is no maximum limit,You can earn as much as you want.. :D".format(self.stud_name)
        except Exception as e:
            logging.error(e)
            logging.exception(e)
            return e

#6.
    def commission(self):                                   #public member function
        ''' This function returns information about commission earning for referrals'''
        logging.info(" You are in commission public member function")
        try:
            logging.info("You are executing commission of affiliation module")
            return "Dear {}, It seems impossible! The commission will only be given for the first transaction made.".format(self.stud_name)
        except Exception as e:
            logging.error(e)
            logging.exception(e)
            return e

#7.
    def bonus(self):                                   #public member function
        ''' This function returns information about bonus earning for referrals'''
        logging.info(" You are in bonus public member function")
        try:
            logging.info("You are executing bonus of affiliation module")
            return "Dear {}, If you cross the bonus limit defined, you will be eligible for earning the bonus... Yuhoo!!!".format(self.stud_name)
        except Exception as e:
            logging.error(e)
            logging.exception(e)
            return e