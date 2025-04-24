import smtplib,ssl
import csv


sender="hackoclock.gdg@gmail.com"
password="vkjx liwb swqe ofbk"

count=0

context=ssl.create_default_context()
connection=smtplib.SMTP_SSL("smtp.gmail.com",465,context=context)
connection.login(sender,password)

f=open("test.csv","r")
data=csv.reader(f)

for i in data:
    
    teamName=i[2]
    memberName=i[0]
    receiver=i[1]
    securityCode=i[3]
    
    subject="🚨 Final Team Guidelines for Hack O'Clock – Don't Miss These Essentials!"
    body=f'''Dear {memberName} of Team {teamName},  

Hope you're doing great!  

We’re thrilled to have your teams on board for Hack O'Clock! Please carefully go through the following important guidelines to ensure a smooth and successful experience:

1. Team Login & App Access:  
   Each team will receive a unique ID: {securityCode} to log into our official app along with their registered email to which this email has been sent. The app will be used exclusively for check-in, check-out, and accessing meal schedules. Make sure all team members are familiar with the app before the event.

2. Team Composition:  
   It is mandatory to have exactly four members in each team. Teams with less than four members will be disqualified from the competition, so please ensure your team meets this requirement without fail.

3. No Hardware Allowed:
   Please note that Hack O'Clock is a software-only hackathon. The use of any hardware components is not permitted. All project development should be strictly software-based.

4. ID Verification:
   All participants are required to bring a valid government-issued ID and their college ID for on-site verification. Entry will not be permitted without both IDs.

If you have any questions or need further assistance, feel free to reach out. We're looking forward to hosting you and witnessing some incredible innovations!

Best regards,  
Piyush Pattanayak  
Team GDG IILM  
Hack O'Clock Coordinator

'''
    
    message = f"""From: {sender}
To: {receiver}
Subject: {subject}
MIME-Version: 1.0
Content-Type: text/plain; charset=utf-8

{body}
"""
    
    
    connection.sendmail(sender,receiver,message.encode('utf-8'))
    print("Mail",count," sent to",i[0])
    count+=1
    
    f1=open("devFolioDone.csv","a+")
    csvwriter=csv.writer(f1,delimiter=",")
    csvwriter.writerow(i)
    f1.close()
    
    
    
    
f.close()
connection.close()