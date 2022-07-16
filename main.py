import logging
logging.basicConfig(filename='task_09_07_22.log', level=logging.DEBUG, format='%(levelname)s %(asctime)s %(name)s %(message)s')
import details
import change_details
import affiliate
import course
import jobs

import sys
import traceback



def YesNoException(Exception):
    pass
#ineuron affiliate examples
print("\n------------------------ineuron affiliate ----------------------------")


print("Hey, I'm iNeuron... I'm here to help you... Will you spare some time to fill some details about you, so that I can help you in best way I can?")
details_obj=details.stud_details()
name=details_obj.name_details()
surname=details_obj.surname_details()
email_id=details_obj.email_details()
aff_obj=affiliate.ineuron_affiliate_data(name, surname,email_id)
new_details_obj=change_details.stud_details()

try:
    print("Please give me a quick confirmation regarding the details you have entered just now...")
    print("Your name: {}\nYour surname: {}\nYour Email address : {}".format(aff_obj.stud_name, aff_obj._stud_surname, aff_obj._ineuron_affiliate_data__emailId))
    while True:
        while True:
            try:
                a = input("Is there anything that you would wish to change about your details? (Y/N)")
                if a.lower() not in 'yn':
                    raise YesNoException("Enter 'Y' if you wish to change details otherwise enter 'N'")
                print(a)
                break
            except:
                logging.error(traceback.format_exc())
                #logging.exception(traceback.format_exc())
                print(traceback.format_exc())
        if a.lower() == 'y':
            c=int(input("Press 1 for changing name\nPress 2 for changing surname\nPress 3 for changing email address"))
            if c==1:
                aff_obj.stud_name=new_details_obj.name_details()                 #updating the public data from ineuron_affiliate_data of affiliate module
                # Accessing the updated public data from ineuron_affiliate_data of affiliate module
                print("You have updated '{}' as your name".format(aff_obj.stud_name))

            elif c==2:
                aff_obj._stud_surname=new_details_obj.surname_details()         #updating the protected data from ineuron_affiliate_data of affiliate module
                # Accessing the updated protected data from ineuron_affiliate_data of affiliate module
                print("You have updated '{}' as your surname".format(aff_obj._stud_surname))
            elif c==3:
                aff_obj.stud_email_change(new_details_obj.email_details())      #updating the private data from ineuron_affiliate_data of affiliate module
                # Accessing the updated private data from ineuron_affiliate_data of affiliate module
                print("You have updated '{}' as your email address".format(aff_obj._ineuron_affiliate_data__emailId))
            else:
                pass
            continue
        else:
            break
except Exception as e:
    logging.error(e)
    logging.exception(e)
    print(e)


print("\nHere I'm sharing some FAQs for you regarding our affiliation program, hope it will serve your need\n")
try:
    print("#1. How to start affiliation program? : ", aff_obj.how_to_start())
    print("#2. Where can I promote affiliate link? : ", aff_obj.where_to_promote())
    print("#3. Which products of iNeuron can I earn a referral commission from? : ", aff_obj.which_products())
    print("#4. Will I get referral earnings even if I make only 1 sale? : ", aff_obj.referral_earnings())
    print("#5. Is there any maximum limit for referral earning? : ", aff_obj.Max_referral_earnings())
    print("#6. If someone enrolls for a yearly subscription will I get the commission every year? : ", aff_obj.commission())
    print("#7. How do I earn a bonus? : ", aff_obj.bonus())

    # Updating products of iNeuron used for referral commission
    print("----------Updating the course names and webpage (private data) from affiliate module---------")
    print("iNeuron Products used for referral commission are\nCourse1 : {}\nCourse2 : {}".format(aff_obj._ineuron_affiliate_data__course1,aff_obj._ineuron_affiliate_data__course2))
    while True:
        while True:
            try:
                a = input("Do you wish to update any course name from above list? (Y/N)")
                if a.lower() not in 'yn':
                    raise YesNoException("Enter 'Y' if you wish to change details otherwise enter 'N'")
                print(a)
                break
            except:
                logging.error(traceback.format_exc())
                #logging.exception(traceback.format_exc())
                print(traceback.format_exc())

        if a.lower()=='y':
            c= int(input("Which course name you wish to update from above list? \n For Course1 press 1\n For Course1 press 2 : "))
            if c==1:
                aff_obj.UpdateCourse1(input("Enter the New Course Name for Course 1: ")) #updating the private data from ineuron_affiliate_data of affiliate module
                # Accessing the private data from ineuron_affiliate_data of affiliate module
                print("Here is the updated list of the courses: \n Course1 : {}\nCourse2 : {}".format(aff_obj._ineuron_affiliate_data__course1,aff_obj._ineuron_affiliate_data__course2))
            elif a==2:
                aff_obj.UpdateCourse2(input("Enter the New Course Name for Course 2: ")) #updating the private data from ineuron_affiliate_data of affiliate module
                # Accessing the updated private data from ineuron_affiliate_data of affiliate module
                print("Here is the updated list of the courses: \n Course1 : {}\nCourse2 : {}".format(aff_obj._ineuron_affiliate_data__course1, aff_obj._ineuron_affiliate_data__course2))
            else:
                pass
            continue
        else:
            break

    print("The current webpage for affiliation is '{}'".format(aff_obj._ineuron_affiliate_data__webpage))
    while True:
        try:
            a = input("Do you wish to update webpage link? (Y/N)")
            if a.lower() not in 'yn':
                raise YesNoException("Enter 'Y' if you wish to change details otherwise enter 'N'")
            print(a)
            break
        except:
            logging.error(traceback.format_exc())
            # logging.exception(traceback.format_exc())
            print(traceback.format_exc())
    if a.lower() == 'y':
        aff_obj.UpdateWebpage(input("Enter the new link for affiliation webpage : ")) #updating the private data from ineuron_affiliate_data of affiliate module
                # Accessing the updated private data from ineuron_affiliate_data of affiliate module
        print("The updated webpage for affiliation is '{}'".format(aff_obj._ineuron_affiliate_data__webpage))
    else:
        pass
except Exception as e:
    logging.error(e)
    logging.exception(e)
    print(e)

print("\n --------------------------------iNeuron Courses and Internships---------------------------------\n ")
print("Here are the details of courses offered by iNeuron")
# Declaring objects for different classes of course module
PaidDS_obj=course.PaidCoursesDS()
FreeDS_obj=course.FreeCoursesDS()
FreeDA_obj=course.FreeCoursesDA()
PaidDA_obj=course.PaidCoursesDA()
FreeInternDA_obj=course.FreeinternshipDA()
FreeInternDS_obj=course.FreeinternshipDS()
PaidinternDA_obj=course.PaidinternshipDA()
PaidinternDS_obj=course.PaidinternshipDS()

try:
    logging.info("Executing the methods from course module")
    print("Free Internship details offered by iNeuron\n\t{}\n\n\t{}\n\n".format(course.ineuroncoursesDA(FreeInternDA_obj),
                                                                                course.ineuroncoursesds(FreeInternDS_obj)))
    print("Free courses offered by iNeuron\n\t{}\n\n\t{}\n\n".format(course.ineuroncoursesDA(FreeDA_obj),
                                                                     course.ineuroncoursesds(FreeDS_obj)))
    print("Paid Internship details offered by iNeuron\n\t{}\n\n\t{}\n\n".format(course.ineuroncoursesDA(PaidinternDA_obj),
                                                                                course.ineuroncoursesds(PaidinternDS_obj)))
    print("Paid courses offered by iNeuron\n\t{}\n\n\t{}\n\n".format(course.ineuroncoursesDA(PaidDA_obj),
                                                                     course.ineuroncoursesds(PaidDS_obj)))

except Exception as e:
    logging.error(e)
    logging.exception(e)
    print(e)
#--------------------------------iNeuron Jobs-------------------------------------------

print("\nHere are some details about Job opportunities in iNeuron\n")
# Declaring objects for different classes of jobs module
DA_obj=jobs.DAInstructor()
DATeachAsst_obj=jobs.DATeachingAssistance()
ConWrt_obj=jobs.ContentWriter()
try:
    logging.info("Executing the methods from jobs module")
    print("\n",jobs.jobdescribtion(DA_obj))
    print("\n",jobs.jobdescribtion(DATeachAsst_obj))
    print("\n",jobs.jobdescribtion(ConWrt_obj))

except Exception as e:
    logging.error(e)
    logging.exception(e)
    print(e)
