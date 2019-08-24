from flask import Flask, jsonify, request
import os
import json
import requests

app = Flask(__name__)

@app.route('/')
def index():
    a=os.environ['Authorization']
    return a

@app.route("/webhook", methods=['POST'])
def webhook():
    if request.method == 'POST':
        return "OK"

@app.route('/callback', methods=['POST'])
def callback():
    json_line = request.get_json()
    json_line = json.dumps(json_line)
    decoded = json.loads(json_line)
    user = decoded['originalDetectIntentRequest']['payload']['data']['replyToken']
    userText = decoded['queryResult']['intent']['displayName']
    #sendText(user,userText)
    if (userText == '1') :
        sendText(user,'ความหมายอาเซียน อาเซียน เกิดจากการรวมตัวกันของ 10 ประเทศ อันได้แก่ มาเลเซีย, พม่า, กัมพูชา, ลาว, ไทย, สิงคโปร์, เวียดนาม, บรูไนดารุส-ซาลาม, ฟิลิปปินส์ และอินโดนีเซีย
    ซึ่งรายนามประเทศเหล่านี้เป็นประเทศที่ตั้งอยู่ในทวีปเอเชียตะวันออกเฉียงใต้ทั้งสิ้น โดยอาเซียน มีชื่อเรียกเต็มๆ ว่า
    "Association of Southeast Asian Nations" หรือ สมาคมประชาชาติแห่งเอเชียตะวันออกเฉียงใต้')
    elif (userText == '2') :
        sendText(user,'ประวัติของอาเซียน')
    elif (userText == '3') :
        sendText(user,'ผู้ก่อตั้ง')
    elif (userText == '4') :
        sendText(user,'คำขวัญอาเซียน')
    elif (userText == '5') :
        sendText(user,'สัญลักษณ์ของอาเซียน')
    elif (userText == '6') :
        sendText(user,'กฎบัตรอาเซียน')
    elif (userText == '7') :
        sendText(user,'ความรู้เกี่ยวกับประเทศสมาชิกอาเซียน')
    elif (userText == '8') :
        sendText(user,'วันสำคัญในอาเซียน')
    elif (userText == '9') :
        sendText(user,'เนื้อเพลงประจำอาเซียน “The ASEAN Way”')
    elif (userText == '10') :
        sendText(user,'ความรู้เพิ่มเติมเกี่ยวกับอาเซียน')
    
    return '',200

def sendText(user, text):
  LINE_API = 'https://api.line.me/v2/bot/message/reply'
  headers = {
    'Content-Type': 'application/json; charset=UTF-8',
    'Authorization': os.environ['Authorization']    # ตั้ง Config vars ใน heroku พร้อมค่า Access token
  }
  data = json.dumps({
    "replyToken":user,
    "messages":[{"type":"text","text":text}]
  })
  r = requests.post(LINE_API, headers=headers, data=data) # ส่งข้อมูล

if __name__ == '__main__':
    app.run()
