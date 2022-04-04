from flask import Flask, render_template


app = Flask(__name__)





@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/about_us')
def about_us():
    return render_template('about-us.html')





if __name__ == '__main__':
    app.run(debug=True)
    
    
    