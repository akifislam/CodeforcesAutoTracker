from bs4 import BeautifulSoup
import requests
import test
import gspread
from oauth2client.service_account import ServiceAccountCredentials

import datetime

def update_inRange():
    print("Today's Date : ",datetime.date.today())
    today = datetime.date.today() - datetime.timedelta(1)

    yesterday_month = today.strftime("%b")
    yesterday_dayno = today.strftime("%d")
    yesterday_full_Date = today.strftime("%d %B, %Y")
    compareable_date = today.strftime("%b/%d")
    print(compareable_date)

    print()
    print("----- Start -----")
    print()
    # Test
    # todays_month = 'Sep'
    # todays_day = '15'
    # Test
    print("Yesterday was : ",yesterday_full_Date)

    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("CodeforcesAutoTracker-b2030a7afa6c.json", scope);
    client = gspread.authorize(creds)

    sheet = client.open("Codeforces Auto Tracker - Akif Islam").worksheet('Sheet2')
    data = sheet.get_all_records()
    # pprint(data)
    date_column = sheet.col_values(1)
    no_of_total_submission_column = sheet.col_values(2)
    no_of_total_accepted_column = sheet.col_values(3)

    source_link = "https://codeforces.com/submissions/miss.progga"
    source = requests.get(source_link).text
    soup = BeautifulSoup(source, "lxml").find('table', class_="status-frame-datatable")

    submission_time = []

    # 1. Collecting all dates from 50 submission of First Page of Codeforces Submission
    for data in soup.findAll('span', class_="format-time"):
        submission_time.append(data.text[0:6])

    print("Submission's Time : ", submission_time)

    print("OK !")

    print()

    # Execution
    submission_count = int(0)
    total_accepted = []
    accepted_count = int(0)
    accpeted_nonduplicate_set = []

    # Total Accepted Count from 50s :
    for data in soup.findAll('span', class_="submissionVerdictWrapper"):
        total_accepted.append(data.text)

    print(total_accepted)
    print(len(total_accepted))
    print(len(submission_time))

    #Total Submission Count
    for i in range(0,len(submission_time),1):
        if submission_time[i][0:3] == yesterday_month and submission_time[i][4:6] == yesterday_dayno:
            submission_count += 1

            if(total_accepted[i]== "Accepted"):
                str = test.get_problemlist()[i] + "  Accepted"
                accpeted_nonduplicate_set.append(str)



        # Total Submission Count
    accpeted_nonduplicate_set = set(accpeted_nonduplicate_set)
    print("Accepted List : ",accpeted_nonduplicate_set)

    accepted_count = len(accpeted_nonduplicate_set)
    print("Total Submission : ", submission_count)
    print("Total Accepted : ", accepted_count)
    insert_list = [yesterday_full_Date, submission_count, accepted_count]
    print(insert_list)
    previous_date = sheet.cell(len(date_column), 1).value[0:2]

    # if sheet.cell(len(date_column),1)[0:1] != todays_day :
    if previous_date != yesterday_dayno:
        sheet.insert_row(insert_list, (len(date_column) + 1))

    else:
        print("Duplicate Date Found ! ")


    print()
    print("----- Finished !-----")
    print()

update_inRange()