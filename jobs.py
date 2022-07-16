import logging
logging.basicConfig(filename='job_task.log', level=logging.DEBUG, format='%(levelname)s %(asctime)s %(name)s %(message)s')

class Contract:
    jobtype = "Contract"


class FullTime:
    jobtype = "Full time"


class PartTime:
    jobtype = "Part time"


class Remote:
    location = "Remote"

class Office:
    location = "Bengaluru, Karnataka, India"

class Experienced:
    exp='4-5 years'


class Fresher:
    exp=0

class DataAnalytics:
    skillset='''
            1.  To teach 90-120 mins dedicatedly on weekdays/weekends.
            2. Strong Command and knowledge over the languages/technologies/frameworks
            3. Must be highly dedicated and passionate to teach and help students learn the course using real-life examples and ready to build their practical knowledge via live online classes.
            4. Must be able to take the initiative to frame and simplify the course structure.'''

class DAQualification:
    qual='''
            1. Bachelors degree in Analytics, Computer Science, IT, Finance, Economics, Marketing, Business Administration, related field, or equivalent work experience, preferred(For exceptional candidates Degree is not required).
            2.  3-6 years of business intelligence experience, preferred
            3.  Excellent verbal, written, and interpersonal skills
            4. Proficient in Excel, SQL, Tableau, and Alteryx or equivalent, preferred
            5. Experience with data query, visualization, dashboard and/or scorecard tools preferred
            6. Self-motivated and willingness to teach and access
            7. Must have an “Ideate, Implement and learn” attitude.
            8. Should possess good communication skills, pleasant personality, and high initiative.
            9. Able to work with minimum supervision, self-driven and willing to work extra mile.'''


class WriterRequirement:
    role_resp= '''  
                    1. Write for different verticals like the website, social media, blog, article, title, and description.
                    2. Write and proofread copy for all content.
                    3. Ability to understand the brief and deliver within stipulated timelines.
                    4. Coordinate with designers to complement text with images and graphics.
                    5. Ideate and come up with meaningful content.
                    6. Produce creative and meaningful content — everything from social media posts, videos, blog posts, and articles'''
    skillset='''
                1. Proven content writing or copywriting experience.
                2. Working knowledge of content management systems.
                3. Proficient in all Microsoft Office applications.
                4. The ability to work in a fast-paced environment..
                5. Effective communication skills'''

class DATeachingAssistanceReq:
    resp='''
            1. Planning doubt-clearing sessions and making sure that students get the most out of live lessons, quizzes, and tests for Data Analytics course.
            2. Create technical feedback for all students and assist low performers in improving their performance.
            3. Examine the live classes and content, and give feedback to the content staff on the pre-reads and other materials.
            4. Provide feedback on the assignments that the students have submitted.
            5. Provide counsel to students to ensure that the maximum number of students achieve the course's objectives.'''

    req= '''
            1. Interpersonal, communication, and teamwork abilities are exceptional.
            2. Genuine desire to assist anyone interested in pursuing a career as a Data Analyst.
            3. Proficient in any business intelligence tool like Power BI, Tableau, etc.
            4. Interest in teaching and assessing.
            5. It is desired, but not required, that you have one year of experience as a Data Analyst.
            6. Prior teaching or teaching assistant experience in a Data Analytics course is recommended but not required.'''

#---------------------------Multiple inheritence--------------------


class DAInstructor(Remote,Contract,Experienced,DataAnalytics,DAQualification):
    def details(self):
        ''' THis function returns Job Description for Data Analyst Instructor/Mentor'''
        logging.info("You are in details public member function of DAInstructor class")
        try:
            logging.info("You are executing details public member function of DAInstructor class")
            return "Job Description for Data Analyst Instructor/Mentor\n\tJob Type: {}\n\t" \
                   "Job Location: {}\n\tYear of Experience : {}\n\tSkills Required: : {}\n\t" \
                   "Educational Qualification : {}".format(Contract.jobtype,Remote.location,Experienced.exp,
                                                           DataAnalytics.skillset, DAQualification.qual)
        except Exception as e:
            logging.error(e)
            logging.exception(e)
            return e


class ContentWriter(Office,FullTime,Experienced,WriterRequirement):
    def details(self):
        ''' THis function returns Job Description for Data Analyst Instructor/Mentor'''
        logging.info("You are in details public member function of ContentWriter class")
        try:
            logging.info("You are executing details public member function of ContentWriter class")
            return "Job Description for Content Writer\n\tJob Type: {}\n\t" \
                   "Job Location: {}\n\tYear of Experience : {}\n\tSkills Required: : {}\n\t" \
                   "Roles and Responsibilities: {}".format(FullTime.jobtype,Office.location,Experienced.exp,
                                                           WriterRequirement.skillset,WriterRequirement.role_resp)
        except Exception as e:
            logging.error(e)
            logging.exception(e)
            return e


class DATeachingAssistance(Remote,PartTime,Fresher,DATeachingAssistanceReq):
    def details(self):
        ''' THis function returns Job Description for Data Analyst Instructor/Mentor'''
        logging.info("You are in details public member function of DATeachingAssistance class")
        try:
            logging.info("You are executing details public member function of DATeachingAssistance class")
            return "Job Description for Data Analyst Teaching Assistance\n\tJob Type: {}\n\t" \
                   "Job Location: {}\n\tYear of Experience : {}\n\tSkills Required: : {}\n\t" \
                   "Roles and Responsibilities: {}".format(PartTime.jobtype,Remote.location,Fresher.exp,
                                                           DATeachingAssistanceReq.req,DATeachingAssistanceReq.resp)
        except Exception as e:
            logging.error(e)
            logging.exception(e)
            return e


#------Polymorphism--------

def jobdescribtion(a):
    return "{}".format(a.details())

i=DAInstructor()
j=DATeachingAssistance()
print(jobdescribtion(i))











