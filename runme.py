# python program for a simple voting application
# participant can make proposals, and after all proposals are in can vote 

from flask import Flask,request,jsonify

import datetime

lieblingsseiten = {}
abgestimmt = []
voting=False


app = Flask(__name__)

# @route("/master")
# def handle_master():

@app.route("/resetlist")
def reset_list():
   lieblingsseiten = {}
   return ""

@app.route("/allentered",methods=['PUT'])
def all_entered():
   voting=True
   open("favorites" + datetime.datetime.now() + ".log","w").write(lieblingsseiten)
   return ""

@app.route("/meinelieblingsseite",methods=['PUT'])
def addpage():
  client_ip = request.remote_addr
  site = request.form["seite"]
  lieblingsseiten[client_ip] = (site,0)
  return ""


@app.route("/stimmeab",methods=['PUT'])
def vote():
  client_ip = request.remote_addr
  if client_ip in abgestimmt:
    return
  abgestimmt.append(client_ip)
  site = request.form["seite"]
  for it in lieblingsseiten.items():
    if it[1][0] == site:
     lieblingsseiten[it[0]][1] += 1
  return ""

@app.route("/resultat",methods=['GET'])
def ergebnis():
   return jsonify(lieblingsseiten.items())


