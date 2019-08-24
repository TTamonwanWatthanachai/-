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
        sendText(user,'ความหมายอาเซียน อาเซียน เกิดจากการรวมตัวกันของ 10 ประเทศ อันได้แก่ มาเลเซีย พม่า กัมพูชา ลาว ไทย สิงคโปร์ เวียดนาม บรูไนดารุส-ซาลาม ฟิลิปปินส์ และอินโดนีเซีย ซึ่งรายนามประเทศเหล่านี้เป็นประเทศที่ตั้งอยู่ในทวีปเอเชียตะวันออกเฉียงใต้ทั้งสิ้น โดยอาเซียน มีชื่อเรียกเต็มๆ ว่า Association of Southeast Asian Nations หรือ สมาคมประชาชาติแห่งเอเชียตะวันออกเฉียงใต้')
    elif (userText == '2') :
        sendText(user,'ประวัติของอาเซียน  เป็นการพัฒนามาจากการเป็น สมาคมประชาชาติแห่งเอเชียตะวันออกเฉียงใต้ ก่อตั้งขึ้นตามปฏิญญากรุงเทพฯ  เมื่อ 8 สิงหาคม 2510 โดยมีประเทศผู้ก่อตั้งแรกเริ่ม 5 ประเทศ คือ อินโดนีเซีย มาเลเซีย ฟิลิปปินส์ สิงคโปร์ และไทย ต่อมาในปี 2527 บรูไน ก็ได้เข้าเป็นสมาชิก ตามด้วย 2538 เวียดนาม ก็เข้าร่วมเป็นสมาชิก ต่อมา 2540 ลาวและพม่า เข้าร่วม และปี 2542 กัมพูชาก็ได้เข้าร่วมเป็นสมาชิกลำดับที่ 10 ทำให้ปัจจุบันอาเซียนเป็นกลุ่มเศรษฐกิจภูมิภาคขนาดใหญ่ มีประชากร รวมกันเกือบ 500 ล้านคน จากนั้นในการประชุมสุดยอดอาเซียนครั้งที่  9 ที่อินโดนีเซีย เมื่อ 7 ต.ค.  2546  ผู้นำประเทศสมาชิกอาเซียนได้ตกลงกันที่จะจัดตั้งประชาคมอาเซียน ซึ่งประกอบด้วย 3 เสาหลัก คือ 1.ประชาคมเศรษฐกิจอาเซียน 2.ประชาคมสังคมและวัฒนธรรมอาเซียน 3.ประชาคมความมั่นคงอาเซียน')
    elif (userText == '3') :
        sendText(user,'ผู้ก่อตั้ง ผู้แทนทั้ง 5 ประเทศ ประกอบด้วย 1.นายอาดัม มาลิก(รัฐมนตรีต่างประเทศอินโดนีเซีย) 2.นายตุน อับดุล ราชัก บิน ฮุสเซน(รองนายกรัฐมนตรี รัฐมนตรีกลาโหมและรัฐมนตรีกระทรวงพัฒนาการแห่งชาติมาเลเซีย)  3.นายนาซิโซ รามอส (รัฐมนตรีต่างประเทศฟิลิปปินส์) 4.นายเอส ราชารัตนัม (รัฐมนตรีต่างประเทศสิงค์โปร์)  5.พันเอก(พิเศษ)ถนัด คอมันตร์ (รัฐมนตรีว่าการกระทรวงการต่างประเทศของไทย)')
    elif (userText == '4') :
        sendText(user,'คำขวัญอาเซียน คือ หนึ่งวิสัยทัศน์ หนึ่งเอกลักษณ์ หนึ่งประชาคม หรือ One Vision One Identity One Community')
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
