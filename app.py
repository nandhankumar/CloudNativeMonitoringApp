import psutil
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    cpu_percent = psutil.cpu_percent()
    mem_percent = psutil.virtual_memory().percent
    Message = None
    if cpu_percent > 80 or mem_percent > 80:
        Message = "High CPU or Memory Detected, scale up!!!"
    #eturn render_template("index.html", cpu_metric=cpu_metric, mem_metric=mem_metric, message=Message)
    return f"CPU Utilization: {cpu_percent} and Memory Utilization:{mem-percent}"

if __name__=='__main__':
    app.run(debug=True, host = '0.0.0.0')