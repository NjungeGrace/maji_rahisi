#import necessary libraries
from flask import Flask, request, Response

#instantiating flask
app = Flask(__name__)

#defining the necessary helper functions
def gen_homepage():
        return "\n".join([
            "CON Choose Language / Chagua lugha",
            "1.English",
            "2.Kiswahili",
            "3.Sheng"
        ])
        
def eng_homepage():
    return "\n".join([
        "CON Welcome to Maji Rahisi!",
        "1.Check water prices",
        "2.Report an issue",
        "3.Find water locations near you",
        "4.About Maji rahisi",
        "00. Homepage"  
    ])
def kis_homepage():
     return "\n".join([
        "CON Karibu Maji Rahisi!",
        "1. Angalia bei za maji",
        "2. Ripoti tatizo",
        "3. Pata maeneo ya maji yaliyo karibu nawe",
        "4. Kuhusu Maji Rahisi",
        "00. Homepage"
     ])

def sheng_homepage():
     return "\n".join([
        "CON Karibu Maji Rahisi!",
        "1. Cheki how much maji inauzwa",
        "2. Tuma noma",
        "3. Pata spot za maji karibu na wewe",
        "4. Story ya Maji Rahisi",
        "00. Homepage"
     ])

def prices(price_intro):
    return "\n".join([
        price_intro,
        "Mosque Road: 15/-",
        "Kwa Njenga: 16/-",
        "Kwa Reuben: 13/-",
        "Viwandani: 18/-",
        "0.return"
    ])

def eng_issue():
     return"\n".join([
        "CON 1.Poor quality water",
        "2.Water is unavailable",
        "3.extremely high prices",
        "0.return"
     ])
def kis_issue():
     return"\n".join([
        "CON 1. Maji yana ubora duni",
        "2. Maji hayapatikani",
        "3. Bei ni za juu sana",
        "0. Rudi"
     ])
def sheng_issue():
     return"\n".join([
       "CON 1. Maji ni trash kabisa",
        "2. Maji hakuna ata kidogo",
        "3. Bei ni crazy juu",
        "0. Rudi nyuma"
     ])
def locations():
     return "\n".join([
         "CON Mosque road",
         "Kwa Reuben",
         "Kwa Njenga",
         "Viwandani",
         "0.Return"
     ])

def eng_about():
     return "END Maji rahisi is an app that helps you locate reliable water sources near you and find the best prices in real time."  
def kis_about():
     return "END Maji Rahisi ni app inayokusaidia kupata vyanzo vya maji vinavyoaminika karibu nawe na kujua bei nafuu kwa wakati halisi."
def sheng_about():
     return"END Maji Rahisi ni app inakuonyesha spot legit za maji karibu na wewe na kukusaidia kupata bei poa real time."
def issue_confirmation(issue_message):
     return issue_message

#setting up the routes
@app.route("/ussd", methods = ["POST"])

#main function containing the logic
def maji_main():
    text = request.form.get("text", "")
    if text == "":
        return gen_homepage()
    elif text == "1":
        return eng_homepage()
    elif text == "1*1":
        return prices("CON The prices listed below are for a 20l jerican")
    elif text == "1*2":
        return eng_issue()
    elif text in ["1*2*1", "1*2*2", "1*2*3"]:
        return issue_confirmation("END issue reported, it will be resolved soon")
    elif text in ["1*3", "2*3", "3*3"]:
        return locations()
    elif text == "1*4":
        return eng_about()
    elif text in ["1*1*0", "1*2*0", "1*3*0", "1*4*0"]:
        return eng_homepage()
    elif text == "2":
        return kis_homepage()
    elif text == "2*1":
        return prices("CON Bei zilizo hapa chini ni za jerikani la lita 20.")
    elif text == "2*2":
        return kis_issue()
    elif text in ["2*2*1", "2*2*2", "2*2*3"]:
        return issue_confirmation(
            "END tumepokea malalamiko yako na tunaendelea kuyashughulikia kwa haraka."
        )
    elif text == "2*4":
        return kis_about()
    elif text in ["2*1*0", "2*2*0", "2*3*0", "2*4*0"]:
        return kis_homepage()
    elif text == "3":
        return sheng_homepage()
    elif text == "3*1":
        return prices("END Hizi bei ni za jerican ya 20L tu, usichanganye.")
    elif text == "3*2":
        return sheng_issue()
    elif text in ["3*2*1", "3*2*2", "3*2*3"]:
        return issue_confirmation(
            "END Issue yako imeshika, iko kwa system na tunashughulikia mbio"
        )
    elif text == "3*4":
        return sheng_about()
    elif text in ["3*1*0", "3*2*0", "3*3*0", "3*4*0"]:
        return sheng_homepage()
    elif text == "00":
        return gen_homepage()
    else:
        return "\n".join([
            "CON Invalid choice",
            gen_homepage().replace("CON ", "")
        ])

    
#run the flask app
if __name__ == "__main__":
    app.run(port = 5000)
