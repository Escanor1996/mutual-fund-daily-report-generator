import os
from dotenv import load_dotenv, find_dotenv
import requests
import pandas as pd
from send_mail import send_mail
from mftool import Mftool
import json
mf = Mftool()

load_dotenv(find_dotenv())

def main():
    df_final=pd.DataFrame(columns=['fund-name', 'date', 'nav', 'price', '1-day-diff', '1-day-percentage'])

    units_own=[1.905,127.465,140.809,27.217]  # add units owned by you for various mutual funds
    scheme_code=[133810,120465,119781,118759]  # add scheme code  for various mutual funds owned by you (order should be same as above)
    total_investment=17499                     # total investment done by you


    for units,scheme in zip(units_own,scheme_code):
        dict=mf.get_scheme_quote(scheme)
        dict.pop('scheme_code',None)
        dict.pop('scheme_name',None)
        dict['date']=dict.pop('last_updated')
        dict['nav']=dict.pop('nav')
        result=mf.get_scheme_historical_nav(scheme,as_json=True)
        result=json.loads(result)
        result=result['data'][0]
        data1=pd.DataFrame(dict,index=[0])
        data2=pd.DataFrame(result,index=[0])
        df=pd.concat([data1,data2])
        df['price']=df['nav'].astype('float')*units
        df['1-day-diff']=df['price'].diff(-1)
        df=df[:1]
        df['1-day-percentage']=(df['1-day-diff']/(df['price']-df['1-day-diff']))*100
        df['fund-name']=mf.get_scheme_quote(scheme)['scheme_name']
        df.set_index(df.columns[-1], inplace=True)
        df.reset_index(inplace=True)
        df_final=pd.concat([df_final,df])

    total_portfolio=df_final['price'].sum()
    one_day_total_portfolio_diff=df_final['1-day-diff'].sum()
    gain=total_portfolio-total_investment
    return_percentage=(gain/total_investment)*100

    table = df_final.to_html()
    body=f'<h1>mutual fund report</h1>{table}<h2>current value: {total_portfolio}</h2><h2>gain: {gain}</h2><h2>return: {return_percentage}%</h2><h2>1 day difference: {one_day_total_portfolio_diff}</h2>'


    sender = os.getenv('SENDER')
    recipient = os.getenv('RECIPIENT')
    password = os.getenv('PASSWORD')
    subject = 'Mutual fund Daily Report'

    send_mail(sender, recipient, subject, body, password)
    print("Mail sent successfully")
