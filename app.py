from flask import Flask, request, redirect, render_template, url_for
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def home():
    return render_template('base.html')

@app.route("/images", methods = ['POST'])
def search_images():

    try:
        search_string = request.form['keyword'].replace(" ", "+")
        print("-------Search string is----- ", search_string)
        response = requests.get(f"https://www.google.com/search?rlz=1C1CHBD_enIN988IN989&sxsrf=AB5stBhuB-seuI3iBYly3oIRB8iVaEunIA:1691468106035&q={search_string}&tbm=isch&source=lnms&sa=X&sqi=2&ved=2ahUKEwiOtO_cmcyAAxVF-TgGHSjWDJEQ0pQJegQIChAB&biw=1422&bih=632&dpr=1.35")
        soup = BeautifulSoup(response.content)
        images_list = soup.find_all('img')
        images_list.pop(0)

        # appending images url in a list 'images_src'
        images_src = []
        for img_tag in images_list:
            src = img_tag['src']
            images_src.append(src)

        return render_template('index.html', images_src=images_src)

    except:
        print("error encountered!")


if __name__ == "__main__":
    app.run(debug=True)