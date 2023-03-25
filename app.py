from flask import Flask, render_template, jsonify
from database import load_jobs_from_db
app = Flask(__name__)



@app.route("/")
def hello_aashrith():
  jobs = load_jobs_from_db()
  return render_template('home.html',
                         jobs = jobs,
                         company_name = 'Aashrith')

@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)

# database: aashrithcareers
# username: h4ibdffeaghmm74jtjzx
# host: ap-south.connect.psdb.cloud
# password: pscale_pw_cZKx9trcnjvYZjL2Pxgv3KcNx3hIjbqwjIRsRXsM3rH

if __name__ == "__main__":
  app.run(host = '0.0.0.0', debug = True)