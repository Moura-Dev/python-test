from flask import request, jsonify
from flask_api import FlaskAPI, status, exceptions

app = FlaskAPI(__name__)

@app.route("/<cpfparameter>/", methods=['GET'])
def ConsultarCPF(cpfparameter):
    CpfUser = cpfparameter
    CpfUser = CpfUser[:3] + "." + CpfUser[3:6] + "." + CpfUser[6:9] + "-" + CpfUser[9:]
    cpf = open("blacklist.txt", "r+")
    for cc in cpf:
        if CpfUser in cc:
            return jsonify("BLOCK")
        else:
            return jsonify("FREE")
    cpf.close()

@app.route("/", methods=['GET'])

def ConsultarCPFVazio():
    return jsonify("Running")

@app.route("/delete/<cpfparameter>", methods=['DELETE'])


if __name__ == '__main__':
    app.run()
