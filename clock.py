import codeforces_autotracker_script
from apscheduler.schedulers.blocking import BlockingScheduler

#Link Source :

Akif = "https://codeforces.com/submissions/__SHERLOCK__"

Sagor = "https://codeforces.com/submissions/Shoriful_Islam"

Kamol = "https://codeforces.com/submissions/IncubatorMan"


def run () :
    codeforces_autotracker_script.update_sheet(Akif, "Akif")

    codeforces_autotracker_script.update_sheet(Sagor, "Sagor")

    codeforces_autotracker_script.update_sheet(Kamol, "Kamol")

try :
    run()
    print("Running Perfectly!")
except :
    print("Cannot Extract Data Right Now !")

print("Updated Instantly !")
sched = BlockingScheduler()

print('Waiting for Schedule Update !')

@sched.scheduled_job('interval', minutes=360)
def sched_function():
    try:
        run()
        print("Running Perfectly!")
    except:
        print("Cannot Extract Data Right Now !")

sched.start()

print('Scheduler Finished')
