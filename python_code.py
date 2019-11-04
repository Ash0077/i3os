import urllib
import sys
import re
sys.setrecursionlimit(1000)
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
import json,os
import pymongo
import pandas as pd


from pymongo import MongoClient
client = MongoClient('mongodb://Test:9319262642@1gen-shard-00-00-cyllg.mongodb.net:27017,1gen-shard-00-01-cyllg.mongodb.net:27017,1gen-shard-00-02-cyllg.mongodb.net:27017/test?ssl=true&replicaSet=1Gen-shard-0&authSource=admin&retryWrites=true&w=majority')
db = client.get_database('1Gen_Database')
cm = db.client_master
# webapp = Flask(__name__)
# api = Api(webapp)
# @api.resource('/', methods=['GET'])
app = Flask(__name__)
@app.route("/")
# class Allget(Resource):
def post1():
    client_master = [{
            'client_id': 1,
            'client_name': 'Inner Explorer',
        },
        {
            'client_id': 2,
            'client_name': 'NoTube',
        },
    {
            'client_id': 3,
            'client_name':'Voice4Change' ,
        },
        {
            'client_id': 4,
            'client_name':'Youth4Planet' ,
        },
        {
            'client_id': 5,
            'client_name':'Bioskop' ,
        },
        {
            'client_id': 6,
            'client_name':'Origin' ,
        },
        {
            'client_id': 7,
            'client_name':'Indian Documentary Foundation' ,
        },
        {
            'client_id': 8,
            'client_name':'Help Heal' ,
        },
        {
            'client_id': 9,
            'client_name':'World Food Program' ,
        },
        {
            'client_id': 10,
            'client_name':'Saksham' ,
        },
        {
            'client_id': 11,
            'client_name':'Udham' ,
        },
        {
            'client_id': 12,
            'client_name':'Meet For Meat' ,
        },
        {
            'client_id': 13,
            'client_name':'Alpha' ,
        },
        {
            'client_id': 14,
            'client_name':'Synergy' ,
        },
        {
            'client_id': 15,
            'client_name':'Kind Hours' ,
        },
        {
            'client_id': 16,
            'client_name':'i3OS' ,
        },
        {
            'client_id': 17,
            'client_name':'Infinity' ,
        },
        {
            'client_id': 18,
            'client_name':'Connect+' ,
        },
        {
            'client_id': 19,
            'client_name':'O2' ,
        }
    ]

    cm.insert_many(client_master)

    sdg = db.sdg_master

    sdg_master = [
        {
            'sdg_id': 1,
            'sdg_name': 'No Poverty',
        },
    {
            'sdg_id': 2,
            'sdg_name': 'Zero Hunger',
        },
        {
            'sdg_id': 3,
            'sdg_name': 'Good Health And Well-Being',
        },
        {
            'sdg_id': 4,
            'sdg_name': 'Quality Education',
        },
        {
            'sdg_id': 5,
            'sdg_name': 'Gender Equality',
        },
        {
            'sdg_id': 6,
            'sdg_name': 'Clean Water And Sanitation',
        },
        {
            'sdg_id': 7,
            'sdg_name': 'Affordable And Clean Energy',
        },
        {
            'sdg_id': 8,
            'sdg_name': 'Decent Work And Economic Growth',
        },
        {
            'sdg_id': 9,
            'sdg_name': 'Industry,Innovation And Infrastructure',
        },
        {
            'sdg_id': 10,
            'sdg_name': 'Reduced Inequalites',
        },
        {
            'sdg_id': 11,
            'sdg_name': 'Sustainable Cities And Communities',
        },
        {
            'sdg_id': 12,
            'sdg_name': 'Responsible Consumption And Production',
        },
        {
            'sdg_id': 13,
            'sdg_name': 'Climate Action',
        },
        {
            'sdg_id': 14,
            'sdg_name': 'Life Below Water',
        },
        {
            'sdg_id': 15,
            'sdg_name': 'Life On Land',
        },
        {
            'sdg_id': 16,
            'sdg_name': 'Peace,Justice And Strong Institutions',
        },
        {
            'sdg_id': 17,
            'sdg_name': 'Partnership For The Goals',
        }
    ]

    sdg.insert_many(sdg_master)

    mongo_docs= list(sdg_master)

    mongo_docs2=list(client_master)

    dfsdg = pd.DataFrame(mongo_docs)

    dfcm = pd.DataFrame(mongo_docs2)

    info_m=db.client_info_master

    client_info_master = [{
            'info_id': 1,
            'client_name': 'Inner Explorer',
            'info': 'https://innerexplorer.org/#abUs'
        },
        {
            'info_id': 2,
            'client_name': 'NoTube',
            'info': 'https://notube.com/'
        },
    {
            'info_id': 3,
            'client_name':'Voice4Change' ,
            'info': 'http://www.voice4change-england.co.uk/'
        },
        {
            'info_id': 4,
            'client_name':'Youth4Planet' ,
            'info': 'https://youth4planet.com/'
        },
        {
            'info_id': 5,
            'client_name':'Bioskop' ,
            'info': 'https://www.origin.1gen.io/'
        },
        {
            'info_id': 6,
            'client_name':'Origin' ,
            'info': 'https://www.origin.1gen.io/'
        },
        {
            'info_id': 7,
            'client_name':'Indian Documentary Foundation' ,
            'info': 'http://www.indiandocumentaryfoundation.org/'
        },
        {
            'info_id': 8,
            'client_name':'Help Heal' ,
            'info': 'https://www.origin.1gen.io/'
        },
        {
            'info_id': 9,
            'client_name':'World Food Program' ,
            'info': 'https://www.wfp.org/'
        },
        {
            'info_id': 10,
            'client_name':'Saksham' ,
            'info': 'https://www.origin.1gen.io/'
        },
        {
            'info_id': 11,
            'client_name':'Udham' ,
            'info': 'https://www.origin.1gen.io/'
        },
        {
            'info_id': 12,
            'client_name':'Meet For Meat' ,
            'info': 'https://www.origin.1gen.io/'
        },
        {
            'info_id': 13,
            'client_name':'Alpha' ,
            'info': 'https://www.origin.1gen.io/'
        },
        {
            'info_id': 14,
            'client_name':'Synergy' ,
            'info': 'https://www.origin.1gen.io/'
        },
        {
            'info_id': 15,
            'client_name':'Kind Hours' ,
            'info': 'https://www.origin.1gen.io/'
        },
        {
            'info_id': 16,
            'client_name':'i3OS' ,
            'info': 'https://www.origin.1gen.io/'
        },
        {
            'info_id': 17,
            'client_name':'Infinity' ,
            'info': 'https://www.origin.1gen.io/'
        },
        {
            'info_id': 18,
            'client_name':'Connect+' ,
            'info': 'https://www.origin.1gen.io/'
        },
        {
            'info_id': 19,
            'client_name':'O2' ,
            'info': 'https://www.origin.1gen.io/'
        }
    ]

    info_m.insert_many(client_info_master)

    mongo_docs3=list(client_info_master)

    dfcim= pd.DataFrame(mongo_docs3)

    dfsdg[['sdg_id','sdg_name']]

    csm=db.client_sdg_master2

    client_sdg_master2 = [{
            'client_id': 1,
            'client_name': 'Inner Explorer',
            "SDG":"Good Health and Well-being"
                        },
        {
            'client_id': 1,
            'client_name': 'Inner Explorer',
            "SDG":"Quality Education"
        },{
            'client_id': 1,
            'client_name': 'Inner Explorer',
            "SDG":"Reduced Inequality"
                        },
        {
            'client_id': 1,
            'client_name': 'Inner Explorer',
            "SDG":"Peace and Justice Strong Institutions"
                        },
        
        {
            'client_id': 2,
            'client_name': 'NoTube',
            'SDG': 'Good Health and Well-being'
        },
    {
            'client_id': 3,
            'client_name':'Voice4Change' ,
            'SDG': 'Peace and Justice Strong Institutions'
        },
        {
            'client_id': 3,
            'client_name':'Voice4Change' ,
            'SDG': 'Gender Equality'
        },
        {
            'client_id': 4,
            'client_name':'Youth4Planet' ,
            'SDG': 'No Poverty'
        },
        {
            'client_id': 4,
            'client_name':'Youth4Planet' ,
            'SDG': 'Zero Hunger'
        },
        {
            'client_id': 4,
            'client_name':'Youth4Planet' ,
            'SDG': 'Good Health and Well-being'
        },
        {
            'client_id': 4,
            'client_name':'Youth4Planet' ,
            'SDG': 'Quality Education'
        },
        {
            'client_id': 4,
            'client_name':'Youth4Planet' ,
            'SDG': 'Gender Equality'
        },
        {
            'client_id': 4,
            'client_name':'Youth4Planet' ,
            'SDG': 'Clean Water and Sanitation'
        },
        {
            'client_id': 4,
            'client_name':'Youth4Planet' ,
            'SDG': 'Affordable and Clean Energy'
        },
        {
            'client_id': 4,
            'client_name':'Youth4Planet' ,
            'SDG': 'Decent Work and Economic Growth'
        },
        {
            'client_id': 4,
            'client_name':'Youth4Planet' ,
            'SDG': 'Industry, Innovation and Infrastructure'
        },
        {
            'client_id': 4,
            'client_name':'Youth4Planet' ,
            'SDG': 'Reduced Inequality'
        },
        {
            'client_id': 4,
            'client_name':'Youth4Planet' ,
            'SDG': 'Sustainable Cities and Communities'
        },
        {
            'client_id': 4,
            'client_name':'Youth4Planet' ,
            'SDG': 'Responsible Consumption and Production'
        },
        {
            'client_id': 4,
            'client_name':'Youth4Planet' ,
            'SDG': 'Climate Action'
        },
        {
            'client_id': 4,
            'client_name':'Youth4Planet' ,
            'SDG': 'Life Below Water'
        },
        {
            'client_id': 4,
            'client_name':'Youth4Planet' ,
            'SDG': 'Life on Land'
        },
        {
            'client_id': 4,
            'client_name':'Youth4Planet' ,
            'SDG': 'Peace and Justice Strong Institutions'
        },
        {
            'client_id': 4,
            'client_name':'Youth4Planet' ,
            'SDG': 'Partnerships to achieve the Goal'
        },
        {
            'client_id': 5,
            'client_name':'Bioskop' ,
            'SDG': 'PARTNERSHIPS FOR THE GOALS'
        },
        {
            'client_id': 5,
            'client_name':'Bioskop' ,
            'SDG': 'CLIMATE ACTION'
        },
        {
            'client_id': 6,
            'client_name':'Origin' ,
            'SDG': 'QUALITY EDUCATION'
        },
        {
            'client_id': 6,
            'client_name':'Origin' ,
            'SDG': 'Gender Equality'
        },
        {
            'client_id': 6,
            'client_name':'Origin' ,
            'SDG': 'GOOD HEALTH AND WELL-BEING'
        },
        {
            'client_id': 6,
            'client_name':'Origin' ,
            'SDG': 'PARTNERSHIPS FOR THE GOALS'
        },
        {
            'client_id': 6,
            'client_name':'Origin' ,
            'SDG': 'Decent  work and Economic growth'
        },
        {
            'client_id': 7,
            'client_name':'Indian Documentary Foundation' ,
            'SDG': 'No Poverty'
        },
        {
            'client_id': 7,
            'client_name':'Indian Documentary Foundation' ,
            'SDG': 'Zero Hunger'
        },
        {
            'client_id': 7,
            'client_name':'Indian Documentary Foundation' ,
            'SDG': 'Good Health and Well-being'
        },
        {
            'client_id': 7,
            'client_name':'Indian Documentary Foundation' ,
            'SDG': 'Quality Education'
        },
        {
            'client_id': 7,
            'client_name':'Indian Documentary Foundation' ,
            'SDG': 'Gender Equality'
        },
        {
            'client_id': 7,
            'client_name':'Indian Documentary Foundation' ,
            'SDG': 'Clean Water and Sanitation'
        },
        {
            'client_id': 7,
            'client_name':'Indian Documentary Foundation' ,
            'SDG': 'Affordable and Clean Energy'
        },
        {
            'client_id': 7,
            'client_name':'Indian Documentary Foundation' ,
            'SDG': 'Decent Work and Economic Growth'
        },
        {
            'client_id': 7,
            'client_name':'Indian Documentary Foundation' ,
            'SDG': 'Industry, Innovation and Infrastructure'
        },
        {
            'client_id': 7,
            'client_name':'Indian Documentary Foundation' ,
            'SDG': 'Reduced Inequality'
        },
        {
            'client_id': 7,
            'client_name':'Indian Documentary Foundation' ,
            'SDG': 'Sustainable Cities and Communities'
        },
        {
            'client_id': 7,
            'client_name':'Indian Documentary Foundation' ,
            'SDG': 'Responsible Consumption and Production'
        },
        {
            'client_id': 7,
            'client_name':'Indian Documentary Foundation' ,
            'SDG': 'Climate Action'
        },
        {
            'client_id': 7,
            'client_name':'Indian Documentary Foundation' ,
            'SDG': 'Life Below Water'
        },
        {
            'client_id': 7,
            'client_name':'Indian Documentary Foundation' ,
            'SDG': 'Life on Land'
        },
        {
            'client_id': 7,
            'client_name':'Indian Documentary Foundation' ,
            'SDG': 'Peace and Justice Strong Institutions'
        },
        {
            'client_id': 7,
            'client_name':'Indian Documentary Foundation' ,
            'SDG': 'Partnerships to achieve the Goal'
        },
        {
            'client_id': 8,
            'client_name':'Help Heal' ,
            'SDG': 'Good Health and Well-being'
        },
        {
            'client_id': 9,
            'client_name':'World Food Program' ,
            'SDG': 'Zero Hunger'
        },
        {
            'client_id': 10,
            'client_name':'Saksham' ,
            'SDG': 'Reduced Inequality'
        },
        {
            'client_id': 11,
            'client_name':'Udham' ,
            'SDG': 'Good Health and Well-being'
        },
        {
            'client_id': 12,
            'client_name':'Meet For Meat' ,
            'SDG': 'Zero Hunger'
        },
        {
            'client_id': 12,
            'client_name':'Meet For Meat' ,
            'SDG': 'Climate Action'
        },
        {
            'client_id': 13,
            'client_name':'Alpha' ,
            'SDG': 'Reduced Inequality'
        },
        {
            'client_id': 13,
            'client_name':'Alpha' ,
            'SDG': 'Good Health and Well-being'
        },
        {
            'client_id': 14,
            'client_name':'Synergy' ,
            'SDG': 'Zero Hunger '
        },
        {
            'client_id': 15,
            'client_name':'Kind Hours' ,
            'SDG': 'Partnerships to achieve the Goal'
        },
        {
            'client_id': 15,
            'client_name':'Kind Hours' ,
            'SDG': 'Decent Work and Economic Growth'
        },
        {
            'client_id': 16,
            'client_name':'i3OS' ,
            'SDG': 'Partnerships to achieve the Goal'
        },
        {
            'client_id': 17,
            'client_name':'Infinity' ,
            'SDG': 'Partnerships to achieve the Goal'
        },
        {
            'client_id': 18,
            'client_name':'Connect+' ,
            'SDG': 'Partnerships to achieve the Goal'
        },
        {
            'client_id': 19,
            'client_name':'O2' ,
            'SDG': 'Partnerships to achieve the Goal'
        }
    ]

    csm.insert_many(client_sdg_master2)

    mongo_docs4=list(client_sdg_master2)

    dfcsm= pd.DataFrame(mongo_docs4)

    dfcsm

    mongo_docs2=list(client_master)

    mongo_docs3=list(client_info_master)
    dfcim= pd.DataFrame(mongo_docs3)
    dfcim[['client_name', 'info',]]
    temp_dict={}
    temp_dict={"name": "1Gen","children":[] }
    for i in dfcm['client_name']:
        temp_dict['children'].append({'name':i,'children':[]})

    temp_dict

    temp_dict['children'][0]['children']

    ie_sdg=dfcsm[dfcsm['client_name']=='Inner Explorer']
    ie_sdg

    for i in ie_sdg['SDG']:
        temp_dict['children'][0]['children'].append({'name':i,'children':[]})

    NoTube_sdg=dfcsm[dfcsm['client_name']=='NoTube']
    NoTube_sdg

    for i in NoTube_sdg['SDG']:
        temp_dict['children'][1]['children'].append({'name':i,'children':[]})

    Voice4Change_sdg=dfcsm[dfcsm['client_name']=='Voice4Change']
    Voice4Change_sdg

    for i in Voice4Change_sdg['SDG']:
        temp_dict['children'][2]['children'].append({'name':i,'children':[]})

    Youth4Planet_sdg=dfcsm[dfcsm['client_name']=='Youth4Planet']
    Youth4Planet_sdg

    for i in Youth4Planet_sdg['SDG']:
        temp_dict['children'][3]['children'].append({'name':i,'children':[]})

    Bioskop_sdg=dfcsm[dfcsm['client_name']=='Bioskop']
    Bioskop_sdg

    for i in Bioskop_sdg['SDG']:
        temp_dict['children'][4]['children'].append({'name':i,'children':[]})

    Origin_sdg=dfcsm[dfcsm['client_name']=='Origin']
    Origin_sdg

    for i in Origin_sdg['SDG']:
        temp_dict['children'][5]['children'].append({'name':i,'children':[]})

    idf_sdg=dfcsm[dfcsm['client_name']=='Indian Documentary Foundation']
    idf_sdg
    for i in idf_sdg['SDG']:
        temp_dict['children'][6]['children'].append({'name':i,'children':[]})
    Help_Heal_sdg=dfcsm[dfcsm['client_name']=='Help Heal']
    Help_Heal_sdg
    for i in Help_Heal_sdg['SDG']:
        temp_dict['children'][7]['children'].append({'name':i,'children':[]})
    wfp_sdg=dfcsm[dfcsm['client_name']=='World Food Program']
    wfp_sdg
    for i in wfp_sdg['SDG']:
        temp_dict['children'][8]['children'].append({'name':i,'children':[]})
    Saksham_sdg=dfcsm[dfcsm['client_name']=='Saksham']
    Saksham_sdg
    for i in Saksham_sdg['SDG']:
        temp_dict['children'][9]['children'].append({'name':i,'children':[]})
    Udham_sdg=dfcsm[dfcsm['client_name']=='Udham']
    Udham_sdg
    for i in Udham_sdg['SDG']:
        temp_dict['children'][10]['children'].append({'name':i,'children':[]})
    mfm_sdg=dfcsm[dfcsm['client_name']=='Meet For Meat']
    mfm_sdg
    for i in mfm_sdg['SDG']:
        temp_dict['children'][11]['children'].append({'name':i,'children':[]})
    Alpha_sdg=dfcsm[dfcsm['client_name']=='Alpha']
    Alpha_sdg
    for i in Alpha_sdg['SDG']:
        temp_dict['children'][12]['children'].append({'name':i,'children':[]})
    Synergy_sdg=dfcsm[dfcsm['client_name']=='Synergy']
    Synergy_sdg
    for i in Synergy_sdg['SDG']:
        temp_dict['children'][13]['children'].append({'name':i,'children':[]})
    Kind_Hours_sdg=dfcsm[dfcsm['client_name']=='Kind Hours']
    Kind_Hours_sdg
    for i in Kind_Hours_sdg['SDG']:
        temp_dict['children'][14]['children'].append({'name':i,'children':[]})
    i3OS_sdg=dfcsm[dfcsm['client_name']=='i3OS']
    i3OS_sdg
    for i in i3OS_sdg['SDG']:
        temp_dict['children'][15]['children'].append({'name':i,'children':[]})
    Infinity_sdg=dfcsm[dfcsm['client_name']=='Infinity']
    Infinity_sdg
    for i in Infinity_sdg['SDG']:
        temp_dict['children'][16]['children'].append({'name':i,'children':[]})
    Connect_sdg=dfcsm[dfcsm['client_name']=='Connect+']
    Connect_sdg
    for i in Connect_sdg['SDG']:
        temp_dict['children'][17]['children'].append({'name':i,'children':[]})
    O2_sdg=Connect_sdg=dfcsm[dfcsm['client_name']=='O2']
    O2_sdg
    for i in O2_sdg['SDG']:
        temp_dict['children'][18]['children'].append({'name':i,'children':[]})
    return(jsonify(temp_dict))
# if __name__ == "__main__":
#     app.run(host='192.168.1.7')
# if __name__ == '__main__':
#    webapp.secret_key = os.urandom(24)
#    port = int(os.environ.get('PORT',5001))
#    webapp.run(host='192.168.1.7', port = port)
if __name__ == "__main__":
    app.run()