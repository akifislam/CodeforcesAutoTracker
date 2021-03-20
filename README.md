# Codeforces-AutoTracker

In brief, This application tracks your everyday's Codeforces submission and write on your personal GoogleSheet like this :
- My GoogleSheet Link
https://docs.google.com/spreadsheets/d/1VVjA379F-L5pBTLMOGf1BjluZxyJBHikzAuyOs6Ai3w/edit?usp=sharing
- Github Repository of Codeforces AutoTracker 
https://github.com/akifislam/CodeforcesAutoTracker

## Why I made Codeforces AutoTracker?

When I started my CS journey, I really loved to make different kinds of projects to satisfy my thirst rather than solving problem on online judges. Besides, it was our (most of the Asian) university-culture to participate in competitive programming or to practise problem-solving on different kinds of online judge. But I did not get any interest on this stuff. So, I read many blogs, watched many videos on the internet to keep myself focused on a new habit. Then I found the best advice from a NasDaily video which says : 
   ### "Commitment is the one and only way to get success."
 
So, I commited to myself that I atleast solve 1 easy problem each day I will do it for 30 days. Then I realized I am so lazy to track my solve count eachday. Even I had no coder friend to ask me everyday how much problem I solved. S

So I made my own friend titled 'Codeforces AutoTracker' which will check my Codeforces submission each day and write it on GoogleSheet. This is the story behind this tracker.

## Do I have to run this program every single day?
The answer is 'Yes'. But you don't need to run this program everyday on the terminal. At first I used Heroku (A Free Hosting Platform) to host my program. With free account, it hosted my python program for 500 hours. Then they kicked me and asked for money. 

So, I made a better plan which works fine for me for FREE. I usually turn on my laptop every single day for coding or watching YouTube or checking mail. So I set this 'Codeforces AutoTracker' script to run as startup application. But it is always a better idea to host it somewhere else if you can afford.

## Disclaimer
- This app is not totally bug free. Even sometimes it cannot count properly if someone hacks your problem on Codeforces.
- This app is fully dependent on Codeforces website. So if it is down then the program may crash.

- Please use the clock.py file to host on server. Use the codeforces_autotrackerscript.py to run on local machine.
- In this app, I used 'GoogleSheetAPI' to connect with GoogleSheet. So, use your own API key to connect with GoogleSheet. You can also use it without API if you change the code slightly by using PANDAs in python.

- You must have to install dependencies of python packages to run this script.

- Check the requirement.txt to get details.


## How to Setup Your Codeforces AutoTracker 


##### Step 0 - Install Python and Download this Repository
##### Step 1 - Install Dependencies
  1) gspread : *pip install gspread*
  2) oauth2client : *pip install oauth2client*
  3) requests : *pip install requests*
  4) beautifulsoup4 : *pip install beautifulsoup4*
  5) lxml : *pip install lxml*
##### Step 2 - Get your own GoogleSheet API Key
To write or edit your personal GoogleSheet, you need to have your own Google API key. A quick Google search may help you to get the key (JSON file). Otherwise this video might help you : 
(Link)

After that, rename your downloaded json file and match the name on the code. Suppose for me, my JSON file name was 'CodeforcesAutoTracker-b2030a7afa6c.json', So I wrote this title in my code. 

##### Step 3 - Put Codeforces ID to track on GoogleSheet.
Add your friends name on the GoogleSheet as well as in the program. On this part, you have to be careful about the link and the new GoogleSheet tab name. Check the picture to get idea.


##### Step 4 - Run the program
Now run codeforcesAutoTrackerscript.py.  You can use the clock.py to host this program on Heroku or other hosting server. This clock.py uses Advance Python Scheduler (APScheduler) which helps to run this program once a day.



## Support & Contact
If you want to thank me or give any suggestion, feel free to mail here : 
iamakifislam@gmail.com
