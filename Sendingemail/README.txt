
TO-DO LIST:
-----------
- Create a working basic two page web app   =============DONE============
- Add a navbar to include home, Emails Sent, register, login and logout ============DONE=============
- Use base.html and extend to declutter your main html files ==========DONE=============
- Create a working registration form ========DONE===========
- Create a working login page and logout button ==========DONE===========
- Making the Emails Sent page login required ===========DONE=============
- Create an admin panel/superuser to add user manually ================DONE================
- Improve the navbar with formatting and having logout appear only when logged in
- Create a working SentEmail page with Mailgun API
- Use bootstrap in order to have a better design for the web app
- Sending emails with email address, user's name, email title, content...
- Sending emails to a target audience automatically ==========ON-HOLD========
- Create a category to sement users ==========ON-HOLD===========
- Send emails to a specific user category ========ON-HOLD=======
- Create a contact feature =========ON-HOLD===========


-------------------------------------------------------------------------------------------------------
Project idea:
-------------
Automate the process of sending emails with some customized features based on business requirements. You can have a list of email addresses and their respective names. Then you can modify the message and send emails to the target audience automatically.

-------------------------------------------------------------------------------------------------------

Solutions
---------

Djando documentation
Sending email => https://docs.djangoproject.com/en/3.0/topics/email/

https://documentation.mailgun.com/en/latest/quickstart-sending.html#verify-your-domain

Steps to send emails
1. Follow the tutorial https://data-flair.training/blogs/django-send-email/
2. Create a from with extra fields (body, subject...)
3. Create the view
4. Create the model

-------------------------------------------------------------------------------------------------------

App models
----------

- User model


- Email model


- Contact model

