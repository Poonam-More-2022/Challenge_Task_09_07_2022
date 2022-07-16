import logging
logging.basicConfig(filename='course_task.log', level=logging.DEBUG, format='%(levelname)s %(asctime)s %(name)s %(message)s')


class DataScience:
    category="Data Science"


class DataAnalytics:
    category = "Data Analytics"


class FreeCourses:
    Fees="Free"

#---------------------------Multiple inheritence--------------------


class FreeCoursesDS(DataScience,FreeCourses):
    def MLDL(self):
        ''' This function returns info about MLDL course'''
        __courseName = "ML and DL Foundations"
        mentor = "Shridhar Mankar"
        logging.info("You are in MLDL public member function")
        try:
            logging.info("You are executing MLDL of course module")
            return "\tCourse Name : {}\n\tMentor : {}\n\tCategory : {}\n\tFees : {}".format(__courseName, mentor,FreeCoursesDS.category, FreeCoursesDS.Fees)
        except Exception as e:
            logging.error(e)
            logging.exception(e)
            return e

    def DeepLearning(self):
        ''' This function returns info about Deep Learning course'''
        _courseName="Deep Learning Foundations"
        mentor = "Krish Naik"
        logging.info("You are in DeepLearning public member function")
        try:
            logging.info("You are executing DeepLearning of course module")
            return "\tCourse Name : {}\n\tMentor : {}\n\tCategory : {}\n\tFees : {}".format(_courseName, mentor,
                                                                                            FreeCoursesDS.category,
                                                                                            FreeCoursesDS.Fees)
        except Exception as e:
            logging.error(e)
            logging.exception(e)
            return e


class FreeCoursesDA(DataAnalytics,FreeCourses):
    def PowerBI(self):
        ''' This function returns info about Power BI course'''
        _courseName = "PowerBI Foundation"
        mentor = "Amit Base"
        logging.info("You are in PowerBI public member function")
        try:
            logging.info("You are executing PowerBI of course module")
            return "\tCourse Name : {}\n\tMentor : {}\n\tCategory : {}\n\tFees : {}".format(_courseName, mentor,
                                                                                            FreeCoursesDA.category,
                                                                                            FreeCoursesDA.Fees)
        except Exception as e:
            logging.error(e)
            logging.exception(e)
            return e

#------------------------------------single inheritance----------------


class PaidCoursesDS(DataScience):
    def __init__(self):
        self.__Fees=17700.00


    def MLDL(self):
        ''' This function returns info about paid MLDL course'''
        _courseName = "Full Stack Data Science Bootcamp"
        mentor = "Sunny Chandra,Krish Naik, Sudhanshu Kumar "
        logging.info("You are in MLDL public member function")
        try:
            logging.info("You are executing MLDL of course module")
            return "\tCourse Name : {}\n\tMentor : {}\n\tCategory : {}\n\tFees : {}".format(_courseName, mentor,
                                                                                            PaidCoursesDS.category,
                                                                                            self.__Fees)
        except Exception as e:
            logging.error(e)
            logging.exception(e)
            return e

    def DeepLearning(self):
        ''' This function returns the info about paid Deep Learning course '''
        _courseName="Deep Learning Computer Vision Masters"
        mentor = "Krish Naik, Sudhanshu Kumar"
        self.__Fees= 7080.00
        logging.info("You are in DeepLearning public member function")
        try:
            logging.info("You are executing DeepLearning of course module")
            return "\tCourse Name : {}\n\tMentor : {}\n\tCategory : {}\n\tFees : {}".format(_courseName, mentor,
                                                                                            PaidCoursesDS.category,
                                                                                            self.__Fees)
        except Exception as e:
            logging.error(e)
            logging.exception(e)
            return e


class PaidCoursesDA(DataAnalytics):
    __Fees = 7080.00
    def PowerBI(self):
        ''' This function returns info about Power BI course'''
        _courseName = "PowerBI Foundation"
        mentor = "Jayant Topnani"

        logging.info("You are in PowerBI public member function")
        try:
            logging.info("You are executing PowerBI of course module")
            return "\tCourse Name : {}\n\tMentor : {}\n\tCategory : {}\n\tFees : {}".format(_courseName, mentor,
                                                                                            PaidCoursesDA.category,
                                                                                            PaidCoursesDA.__Fees)
        except Exception as e:
            logging.error(e)
            logging.exception(e)
            return e


#--------------------Multi-label inheritances-----------


#1.
class FreeinternshipDS(FreeCoursesDS):
    pass


#2.
class PaidinternshipDS(PaidCoursesDS):
    pass


#3.
class FreeinternshipDA(FreeCoursesDA):
    pass


#4.
class PaidinternshipDA(PaidCoursesDA):
    pass



#------Polymorphism--------

#1.
def ineuroncoursesds(a):
     return "Details for ML:\n{}\n Details for Deep Learning :\n{}".format(a.MLDL(), a.DeepLearning())
    #a.DeepLeraning()

#2.
def ineuroncoursesDA(a):
    return"Details of PowerBI course : \n{}".format(a.PowerBI())




i=FreeCoursesDS()
j=FreeCoursesDA()
k=PaidCoursesDS()
l=PaidCoursesDA()
print(ineuroncoursesds(i))
print(ineuroncoursesds(k))
print(ineuroncoursesDA(j))
print(ineuroncoursesDA(l))

m=FreeinternshipDA()
print("Free Internship details in DA\n",m.PowerBI())
#ineuroncoursesds(i)
#i.MLDL()
#print(i.MLDL())

#print(isinstance(PaidCoursesDA(),DataAnalytics))

#print(type(k))
#print(type(ineuroncoursesds(i)))
#help(l.PowerBI())


