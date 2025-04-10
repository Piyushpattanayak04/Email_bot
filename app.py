import smtplib,ssl
import csv


sender="lolachoda22@gmail.com"
password="jifb hniw lbdi vkpx"



context=ssl.create_default_context()
connection=smtplib.SMTP_SSL("smtp.gmail.com",465,context=context)
connection.login(sender,password)

f=open("contacts.csv")
data=csv.reader(f)
for i in data:
    
    comp_name=i[0]
    
    receiver=i[3]
    
    subject="Sponsorship Opportunity: 24-Hour Hackathon at IILM University by GDG Club"
    body=f'''Dear Team {comp_name},

I hope this message finds you well!

I am writing on behalf of the *GDG Club of IILM University* since we are hosting a thrilling *24-hour Hackathon—an event that has already received more than **1200+ registrations, with **300+ students* likely to be attending on the last day. This will provide an excellent chance for {comp_name}, to interact with a very engaged and technology-friendly audience.

We would be more than happy to have *{comp_name}*, as one of our main sponsors!

By collaborating with us, {comp_name},would enjoy *considerable exposure and brand visibility* through:

- *Direct interaction with 300+ students* on the event day
- *Branding on-site opportunities*: Flyers, banners, and posters
- *Social media promotion: We will post and share **specific reels and shoutouts* on our Instagram and LinkedIn accounts
- Your *prominent logo* on all event-related documents, including flyers, posters, and digital advertising

We think your platform fits in beautifully with the developer-first ethos of the event, and we'd love to introduce your brand to a crowd of future engineers, developers, and tech leaders.

Looking forward to the chance to work together. Let us know if you'd be interested in chatting more about this—we'd be delighted to provide more information and sponsorship options.

Warm regards,
Tanmay Jain
Sponsorship Lead
Google Developers Group IILM University
📞 +91 8266009496
Chapter Link | LinkedIn | Instagram

FIND THE BROCHURE BY CLICKING THIS LINK FOR MORE DETALS : https://drive.google.com/file/d/1iz8fIK0FNNvi98brzOnhYHon9eqUe1xY/view?usp=sharing

'''
    
    message = f"""From: {sender}
To: {receiver}
Subject: {subject}
MIME-Version: 1.0
Content-Type: text/plain; charset=utf-8

{body}
"""
    
    
    connection.sendmail(sender,receiver,message.encode('utf-8'))
    print("Mail sent to",i[0],i[1])
    
    
    
    
f.close()
connection.close()