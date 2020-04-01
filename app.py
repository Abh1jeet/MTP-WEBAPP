#working on "flaskuse" env

#imports
from flask import Flask,render_template,request,session,redirect
import pickle

with open("model/pickle_model.pkl", 'rb') as file:
    modelsvm = pickle.load(file)

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def home():
    # greeting = "thankyou"
    # alert =False
    if (request.method == 'POST'):
        text1 = request.form.get('text1')
        print(text1)
        value = func1(text1)
        return render_template('index.html',text1=value,alert=True)
    else:
        return render_template('index.html')


def func1(text):
	test_str=[text]
	predicted=modelsvm.predict(test_str)
	test_res=predicted[0]
	print(test_res)
	return test_res


app.run(debug=True)