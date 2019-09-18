#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import json as js
import re
import requests


# In[ ]:


def get_coupon_info(long_str_lst,ticket_lst):
    data_df = pd.DataFrame(columns =['Ticket ID',
                                     'Submitted By',
                                     'Submitted On',
                                     'Branch',
                                     'Branch Id',
                                     'Association',
                                     'Association Id',
                                     'Do I need a proof before my order is mailed?',
                                     'Type of Request- I am submitting',
                                     'Assessment Start Date',
                                     'Assessment End Date',
                                     'Billing Frequency',
                                     'Billing Method',
                                     'Additional Details',
                                     'Charge Type',
                                     'Total Per Cycle Billing Amount',
                                     'Total Unit Count',
                                     'Number',
                                     'Unit Type',
                                     'Assessment Amount',
                                     'NO. of Units',
                                     'Paid by Direct Debit?',
                                     'Total'])
    for i in range(len(long_str_lst)):
        request_content = long_str_lst[i]['request_history']['item']
        for k, v in request_content.items():
            if len(v['tNote']) > 1000:
                html_table = v['tNote']
        sub_str = re.findall(r'<tr>(.*?)<\/tr>',html_table)
        value_list = []
        type_str_lst = []
        for n in sub_str:
            ht_value = re.findall(r'<td style="min-width:100px;padding-left:10px;">(.*?)</td>',n)
            bf_value = re.findall(r'<td style="padding-bottom:10px;">(.*?)</td>',n)
            value_list.append(bf_value)
            value_list.append(ht_value)
            value_list = [e for e in value_list if e]
        for a in sub_str:
            type_value = re.findall(r'<td style="min-width:25px;border-right:1px solid #E0E0E0;padding:0px 2px 0px 2px;">(.*?)</td>',a)
            type_str_lst.append(type_value)
            type_str_lst = [e for e in type_str_lst if e]
        del type_str_lst[0]
        if len(value_list)  == 15 :
            for b in range(len(type_str_lst)):
                data_df = data_df.append({'Ticket ID':ticket_lst[i],
                                          'Submitted By':value_list[0][0], 
                                          'Submitted On':value_list[1][0],
                                          'Branch':value_list[2][0],
                                          'Branch Id':value_list[3][0],
                                          'Association':value_list[4][0],
                                          'Association Id':value_list[5][0],
                                          'Do I need a proof before my order is mailed?':value_list[6][0],
                                          'Type of Request- I am submitting':value_list[7][0],
                                          'Assessment Start Date':value_list[8][0], 
                                          'Assessment End Date':value_list[9][0],
                                          'Billing Frequency':value_list[10][0],
                                          'Billing Method':value_list[11][0],
                                          'Additional Details':value_list[12][0], 
                                          'Charge Type':" ",
                                          'Total Per Cycle Billing Amount':value_list[13][0],
                                          'Total Unit Count':value_list[14][0],
                                          'Number':type_str_lst[b][0],
                                          'Unit Type':type_str_lst[b][1],
                                          'Assessment Amount':type_str_lst[b][2],
                                          'NO. of Units':type_str_lst[b][3],
                                          'Paid by Direct Debit?':type_str_lst[b][4],
                                          'Charge Type':type_str_lst[b][5],
                                          'Total':type_str_lst[b][6]},ignore_index = True)
        else:
            for n in range(len(ticket_lst)):
                data_df = data_df.append({'Ticket ID':ticket_lst[i],
                                          'Submitted By':value_list[0][0], 
                                          'Submitted On':value_list[1][0],
                                          'Branch':value_list[2][0],
                                          'Branch Id':value_list[3][0],
                                          'Association':value_list[4][0],
                                          'Association Id':value_list[5][0],
                                          'Do I need a proof before my order is mailed?':value_list[6][0],
                                          'Type of Request- I am submitting':value_list[7][0],
                                          'Assessment Start Date':value_list[8][0], 
                                          'Assessment End Date':value_list[9][0],
                                          'Billing Frequency':value_list[10][0], 
                                          'Billing Method':value_list[11][0],
                                          'Additional Details':value_list[12][0], 
                                          'Charge Type':value_list[13][0],
                                          'Total Per Cycle Billing Amount':value_list[14][0],
                                          'Total Unit Count':value_list[15][0],
                                          'Number':" ",
                                          'Unit Type':type_str_lst[n][0],
                                          'Assessment Amount':type_str_lst[n][1],
                                          'NO. of Units':type_str_lst[n][2],
                                          'Paid by Direct Debit?':type_str_lst[n][3],
                                          'Total':type_str_lst[n][4]},ignore_index = True)
    return(data_df)                       


# In[ ]:


def pull_ticket_info():
    http_lst = [] 
    ticket_lst = []
    request_lst = []
    HS_Json_lst =[]
    api_url = r'***'
    para = {"xFilter":***}
    request = requests.get(api_url, auth=('***', '***'),params = para)
    ticket_str = request.text
    HS_Json = js.loads(ticket_str)
    HS_Json = HS_Json['request']
    for i in range(len(HS_Json)):
        Ticket_id = HS_Json[i]['xRequest']
        ticket_lst.append(Ticket_id)
    for i in range(len(ticket_lst)):
        http_str = '***'+str(ticket_lst[i]) + '&output=json'
        http_lst.append(http_str)
    for i in http_lst:
        request = requests.get(i, auth=('***', '***'))
        ticket_str = request.text
        request_lst.append(ticket_str)
    for i in request_lst:
        HS_Json = js.loads(i)
        HS_Json_lst.append(HS_Json)
    return(HS_Json_lst,ticket_lst)


# In[ ]:


pull_ticket_info()[0]


# In[ ]:


get_coupon_info(pull_ticket_info()[0],pull_ticket_info()[1]).to_csv(r'***', index = False)

