from flask import Flask,render_template,request
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

app = Flask(__name__)

@app.route('/main', methods = ["GET","POST"])
def main():
    if request.method == "POST":

        number = request.form.get("track")
        num = phonenumbers.parse(number)
        country = geocoder.description_for_number(num,"en")

        num1 = phonenumbers.parse(number)
        sim = carrier.name_for_number(num1,"en")
        # print(carrier.name_for_number(num1,"en"))

        return render_template ("main.html", box = country, bag = sim)
    return render_template ("main.html")

@app.route('/', methods = ["GET","POST"])
def home():
    if request.method == "POST":

        code = request.form.get("code")
        return render_template ("home.html",code = code)
    return render_template ("home.html")


if __name__ == "__main__":
    app.run(debug=True)
      