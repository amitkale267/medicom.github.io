from flask import Flask , render_template , request
app = Flask(__name__)
import pickle

# open a file, where you stored the pickled data
file = open('model.pkl', 'rb')

clf = pickle.load(file)

file.close()

@app.route('/', methods=["GET","POST"])
def hello_world():
    
    if request.method == "POST" :
        myDict = request.form
        fever = int(myDict['fever'])
        pain = int(myDict['pain'])
        runnyNose = int(myDict['runnyNose'])
        diffBreath = int(myDict['diffBreath'])
        age = int(myDict['age'])
        
         #code for inference
        inputFeatures = [fever, pain, age, runnyNose, diffBreath]
        infProb = clf.predict_proba([inputFeatures])[0][1]
        print(infProb)
        return render_template('show.html',inf=round(infProb*100))
    return render_template('index.html')

@app.route("/add")
def add():
    return render_template('add.html')

@app.route("/a")
def a():
    return render_template('a.php')


    #app.run(host='192.168.43.224 ', threaded=True , debug=True)