from flask import Flask, jsonify, render_template, request
import scanner, subdomain

app = Flask(__name__)

@app.route('/',methods=["GET", "POST"])
def home():
    return render_template('index.html')

@app.route('/portscanner',methods=["GET", "POST"])
def portScanner():
    if request.method == "POST":
        ip = request.form["ipAddress"]
        port = request.form["portNumbers"]
        ans = scanner.scan(ip, int(port))
        return render_template('portScanner.html', ans=ans, ip=ip)
    return render_template('portScanner.html')


@app.route('/subdomain',methods=["GET", "POST"])
def subDomain():
    if request.method == "POST":
        domain = request.form["domainName"]
        with open('subDomain.txt','r') as file:
            name = file.read()
            sub_dom = name.splitlines()
         
        urls = subdomain.domain_scanner(domain,sub_dom)
        return render_template('subDomain.html', urls=urls, domain=domain)
    return render_template('subDomain.html')


if __name__ == "__main__":
    app.run(debug=True, port=3000)