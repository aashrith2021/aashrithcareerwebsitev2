from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru',
    'salary': '1200000'
  },
  {
    'id': 2,
    'title': 'Data Engineer',
    'location': 'Noida',
    'salary': '2500000'
  },
  {
    'id': 3,
    'title': 'Data Scientist',
    'location': 'Hyderabad',
    
  },
]

@app.route("/")
def hello_world():
    return render_template('home.html', jobs = JOBS, company_name = 'Aashrith')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
  

if __name__ == "__main__":
  app.run(host = '0.0.0.0', debug = True)