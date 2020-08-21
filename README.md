# mutual-fund-daily-report-generator
The code generates daily report on your mutual fund portfolio and sends  report to your gmail.



# Libraries used:(as mentioned in requirements.txt file)

1. Pandas(to process the data and prepare it in proper format)
2. mftools (getting nav data for mutual funds)
3. smls( to deploy this job using seamless cloud)

# Workflow:

-- this job get the nav data for mutual funds from mftools library and calculate the investment data in daily basis and send you a report of your current situation of portfolio in your gmail.

-- you have to get the scheme code of your funds from internet and put it in the code and the allocated asset for each fund.(the part is pointed in the code at function.py)

-- after that we will use python package to send a mail of that report at your gamil account. To send mail you have to configure 2-way- authentication in your mailbox. Detailed explanation given below.

-- Now our full codebase is ready we will serve it in Seamless cloud and automate it to run at particular moment every day.


# Setting up Gmail
We are going to use Gmail account to send emails. For security reasons, user's Gmail password cannot be used in Python script. Also, we are not going to turn on the Less Secure App Access instead, we will enable 2-Step Verification and create an app password.

1.Navigate to https://myaccount.google.com/ and open the Security tab. Then, enable 2-Step Verification and click App passwords.

![Result](https://github.com/seamless-io/templates/blob/master/images/send_daily_email_yfinance/myaccount.png)

2.In the dropdown menu, select Other (Custom name) option and name your application, for example mutual fund tracker.

![Result](https://github.com/seamless-io/templates/blob/master/images/send_daily_email_yfinance/apps.png)

3.Paste somewhere the generated password (to be 100% clear, you will have a different password from the one you see on the screenshot). We are going to use this password in our Python script.(in .env file)

![Result](https://github.com/seamless-io/templates/blob/master/images/send_daily_email_yfinance/password.png)

# Setting up SeamlessCloud
Create a free account at http://seamlesscloud.io. Since you already have a Gmail account you will be able to sign up and then log in with your Gmail account.
Seamless Sign Up

![Result](https://github.com/seamless-io/templates/blob/master/images/smls-signup.png)

# Running the script
Follow instructions to run and publish your first test job. Seamless Sign Up

![Result](https://github.com/seamless-io/templates/blob/master/images/seamless_no_jobs_screen.png)

You can also check out the Quick Start Guide. When you will be done with testing, copy/paste files from this folder to yours. Additionally, create .env file where we are going to store our Gmail credentials (check .env file for the reference). Since we are going to send an email to yourself, SENDER and RECIPIENT should be the same unless you want to send an email to other recipients. PASSWORD is a password from the Setting up Gmail step.

The next step is to install requirements: pip install -r requirements. Please, remember, SeamlessCloud requires Python>=3.6, so you may need to use pip3.

We are almost there! Run our script on the SeamlessCloud: smls run. If you set up everything correctly, you will receive an email mutual fund daily report. And finally, let's deploy our script to execute it on schedule, say 9 AM every day (UTC): smls publish --name "Mutual fund daily report" --schedule "0 9 * * *". If you are new to cron schedule, check this service https://crontab.guru.

# Files:

1. function.py: It conatines the core functional code. Please use the main function otherwise seamless cloud will not work.
2. send-mail.py: contains code for sending mail.
3. .env : it contains the mail id and passowrd. To provide more secure way we have used this file with dot-env library.


# Further playing:

You can play further with the code if you want more information included in the report. Another thing you have to do manually is that each time you do new investment or you have SIP you have to manually change this part:

    units_own=[1.905,127.465,140.809,27.217]  # add units owned by you for various mutual funds
    scheme_code=[133810,120465,119781,118759]  # add scheme code  for various mutual funds owned by you (order should be same as above)
    total_investment=17499                     # total investment done by you

If someone find a way automate this process also kudos. Please create a pull request I will happily add that functionality. Anyway after changing the code, to re-deploy the job into seamless code you can use the smls publish command with same job name, if you want to change scheduling part also same process.

# Example of mail with generated report:

![Result](https://github.com/Escanor1996/mutual-fund-daily-report-generator/blob/master/mail-report.PNG)




