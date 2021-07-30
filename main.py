import os
from flask import Flask, request, render_template
from flaskwebgui import FlaskUI



app = Flask(__name__)
#ui=FlaskUI(app)


# routes
@app.route("/", methods=['GET', 'POST'])
def main():
	return render_template("index.html")


@app.route("/submit", methods = ['GET', 'POST'])
def get_output():
    if request.method == 'POST':
        img = request.files['my_image']
        img_path = "static/" + img.filename
        img.save("static/im2.jpg")


        command = "python yolov5/detect.py --weights yolov5/best.pt --img 416 --conf 0.4 --source static/im2.jpg"
        os.system(command)


        f = open("yolov5/count.txt", "r")
        count=f.read()
        print(count)
        empty=count.split(' ')[1]
        occupied = count.split(' ')[3]
        p='hi'

    return render_template("index.html", prediction = p, img_path = img_path,empty1=empty,occupied1=occupied)


if __name__ == "__main__":
    app.run(debug=True)
    #ui.run()

