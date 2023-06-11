from flask import Flask,render_template,request,url_for,redirect
import qrcode
from io import BytesIO
from base64 import b64encode

app=Flask(__name__)


@app.route('/')
def login():
    return render_template("login.html")

@app.route('/signup')
def signup():
    return render_template("signup.html")

@app.route('/index')
def index():
    return redirect("index.html")

@app.route('/',methods=["POST"])
def geberateQR():
    memory=BytesIO()
    data=request.form.get("link")
    img=qrcode.make(data)
    img.save(memory)
    memory.seek(0)

    base64_img="data:image/png;base64," + \
        b64encode(memory.getvalue()).decode('ascii')
    return render_template('index.html',data=base64_img)

    
if __name__ =='__main__':
    app.run(debug=True) 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # @app.route("/signup")
# def signup():
#     return render_template("signup.html")

# @app.route("/login")
# def login():
#     return render_template("login.html")

# @app.route("/qr")
# def qr():
#     return render_template("index.html")