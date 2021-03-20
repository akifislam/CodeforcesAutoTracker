from bs4 import BeautifulSoup
import requests
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time
import datetime



def update_sheet(source_link, sheet_name):
    today = datetime.datetime.no[iw()
    yesterday_full_Date = (today - datetime.timedelta(1)).strftime("%d %B, %Y")
    today_time_format = today.strftime("%b/%d/%Y %H:%M")
    yesterday_dayno = (today - datetime.timedelta(1)).strftime("%d")


    print("Today is ", today_time_format)

    scrapper_end_time = (today - datetime.timedelta(1)).strftime("%b/%d/%Y 21:00")
    scrapper_start_time = (today - datetime.timedelta(2)).strftime("%b/%d/%Y 21:00")
    #
    # print("Start Time : ", scrapper_start_time)
    # print("End Time : ", scrapper_end_time)

    print()
    print("----- Start -----")
    print()
    # Test
    # todays_month = 'Sep'
    # todays_day = '15'
    # Test


    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("CodeforcesAutoTracker-b2030a7afa6c.json", scope);
    client = gspread.authorize(creds)

    sheet = client.open("Codeforces Auto Tracker - Akif Islam").worksheet(sheet_name)
    data = sheet.get_all_records()
    # pprint(data)
    date_column = sheet.col_values(1)
    no_of_total_submission_column = sheet.col_values(2)
    no_of_total_accepted_column = sheet.col_values(3)

    source = requests.get(source_link).text
    soup = BeautifulSoup(source, "lxml").find('table', class_="status-frame-datatable")

    submission_time = []

    # 1. Collecting all dates from 50 submission of First Page of Codeforces Submission
    for data in soup.findAll('span', class_="format-time"):
        datetime_object = datetime.datetime.strptime(data.text, "%b/%d/%Y %H:%M")
        submission_time.append(datetime_object.strftime("%b/%d/%Y %H:%M"))


    print(" ALL OK !")

    print()

    # Execution
    submission_count = int(0)
    total_accepted = []
    accepted_count = int(0)
    accpeted_nonduplicate_set = []

    # Total Accepted Count from 50s :
    for data in soup.findAll('span', class_="submissionVerdictWrapper"):
        total_accepted.append(data.text)

    # print(total_accepted)
    # print("Found: ",len(total_accepted))
    # print("Found : ",len(submission_time))
    # print(total_accepted)

    #Total Submission Count
    for i in range(0,len(submission_time),1):
        if submission_time[i]>scrapper_start_time and submission_time[i]<scrapper_end_time:
            submission_count += 1

            if(total_accepted[i]== "Accepted" or total_accepted[i].__contains__("Pretest Passed")):
                str = get_problemlist(source_link)[i] + "  Accepted"
                accpeted_nonduplicate_set.append(str)



        # Total Submission Count
    accpeted_nonduplicate_set = set(accpeted_nonduplicate_set)
    # print("Accepted List : ",accpeted_nonduplicate_set)

    accepted_count = len(accpeted_nonduplicate_set)
    print("Total Submission : ", submission_count)
    print("Total Accepted : ", accepted_count)
    insert_list = [yesterday_full_Date, submission_count, accepted_count]
    # print(insert_list)
    previous_date = sheet.cell(len(date_column), 1).value[0:2]

    if previous_date != yesterday_dayno:
        sheet.insert_row(insert_list, (len(date_column) + 1))

    else:
        print("Duplicate Date Found ! ")


    print(sheet_name + " data checked successfully !")
    print("----- Finished !-----")
    print()


def get_problemlist(source_link):
    source2 = requests.get(source_link).text
    soup2 = BeautifulSoup(source2, "lxml").find('table', class_="status-frame-datatable")

    problem_names = []

    for data in soup2.findAll('a'):
        splitted_text = str(data.text).strip()
        if (len(splitted_text) > 2 and splitted_text.__contains__(" - ")):
            # print(splitted_text)
            problem_names.append(splitted_text)

    return problem_names



Farhan = "https://codeforces.com/submissions/Farhan132"
Akif = "https://codeforces.com/submissions/__SHERLOCK__"

Sagor = "https://codeforces.com/submissions/Shoriful_Islam"

Kamol = "https://codeforces.com/submissions/__iago__"
Mhamuda= "https://codeforces.com/submissions/Mhamuda"
Fahim = "https://codeforces.com/submissions/LUMBERJACK__"
Pranto = "https://codeforces.com/submissions/Ashiq_Uddin_Pranto"

update_sheet(Pranto,"Pranto")
update_sheet(Akif,"Akif")
update_sheet(Farhan,"Farhan")

update_sheet(Mhamuda,"Mhamuda")
update_sheet(Sagor,"Sagor")

update_sheet(Kamol,"Kamol")
update_sheet(Fahim,"Fahim")

