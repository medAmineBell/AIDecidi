from http.server import (
    HTTPServer, BaseHTTPRequestHandler
)

from urllib.parse import urlparse
import pickle
with open('model_bac_info', 'rb') as f:
    modelInfo = pickle.load(f)
with open('model_bac_science', 'rb') as f:
    modelScience = pickle.load(f)
with open('model_bac_math', 'rb') as f:
    modelMath = pickle.load(f)
with open('model_bac_eco', 'rb') as f:
    modelEco = pickle.load(f)
with open('model_bac_tech', 'rb') as f:
    modelTech = pickle.load(f)
with open('model_bac_lettre', 'rb') as f:
    modelLettre = pickle.load(f)
with open('model_bac_sport', 'rb') as f:
    modelSport = pickle.load(f)


class MySrv(BaseHTTPRequestHandler):
    print('server up and running...')

    def do_GET(self):
        query = urlparse(self.path).query
        query_components = dict(qc.split("=") for qc in query.split("&"))
        bac = query_components["BAC"]
        print(bac)

        if float(bac) == 1 :
            Moyenne = query_components["Moyenne"]
            BD = query_components["BD"]
            TIC = query_components["TIC"]
            Algo = query_components["Algo"]
            Math = query_components["Math"]
            Physique = query_components["Physique"]
            Francais = query_components["Francais"]
            Arabe = query_components["Arabe"]
            Anglais = query_components["Anglais"]
            Philo = query_components["Philo"]
            Sport = query_components["Sport"]
            Option = query_components["Option"]
            res = modelInfo.predict([[1,float(Moyenne),float(BD),float(TIC),float(Algo),float(Math),float(Physique),float(Francais),float(Arabe),float(Anglais),float(Philo),float(Sport),float(Option)]])
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            body = str(res)
            self.wfile.write(body.encode("utf-8"))
            self.wfile.close()
        
        if float(bac) == 2 :
            Moyenne = query_components["Moyenne"]
            Math = query_components["Math"]
            Physique = query_components["Physique"]
            Science = query_components["Science"]
            Anglais = query_components["Anglais"]
            Francais = query_components["Francais"]
            Arabe = query_components["Arabe"]
            Philo = query_components["Philo"]
            Info = query_components["Info"]
            Sport = query_components["Sport"]
            Option = query_components["Option"]
            res = modelMath.predict([[2,float(Moyenne),float(Math),float(Physique),float(Science),float(Anglais),float(Francais),float(Arabe),float(Philo),float(Info),float(Sport),float(Option)]])
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            body = str(res)
            self.wfile.write(body.encode("utf-8"))
            self.wfile.close()
        
        if float(bac) == 3 :
            Moyenne = query_components["Moyenne"]
            Economie = query_components["Economie"]
            Gestion = query_components["Gestion"]
            Math = query_components["Math"]
            HistoireGeographie = query_components["HistoireGeographie"]
            Anglais = query_components["Anglais"]
            Francais = query_components["Francais"]
            Arabe = query_components["Arabe"]
            Philo = query_components["Philo"]
            Info = query_components["Info"]
            Sport = query_components["Sport"]
            Option = query_components["Option"]
            res = modelEco.predict([[3,float(Moyenne),float(Economie),float(Gestion),float(Math),float(HistoireGeographie),float(Anglais),float(Francais),float(Arabe),float(Philo),float(Info),float(Sport),float(Option)]])
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            body = str(res)
            self.wfile.write(body.encode("utf-8"))
            self.wfile.close()
        
        if float(bac) == 4 :
            Moyenne = query_components["Moyenne"]
            Physique = query_components["Physique"]
            Science = query_components["Science"]
            Math = query_components["Math"]
            Anglais = query_components["Anglais"]
            Francais = query_components["Francais"]
            Arabe = query_components["Arabe"]
            Philo = query_components["Philo"]
            Info = query_components["Info"]
            Sport = query_components["Sport"]
            Option = query_components["Option"]
            res = modelScience.predict([[4,float(Moyenne),float(Physique),float(Science),float(Math),float(Anglais),float(Francais),float(Arabe),float(Philo),float(Info),float(Sport),float(Option)]])
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            body = str(res)
            self.wfile.write(body.encode("utf-8"))
            self.wfile.close()

        if float(bac) == 5 :
            Moyenne = query_components["Moyenne"]
            SpecialiteSport = query_components["SpecialiteSport"]
            Sport = query_components["Sport"]
            Science = query_components["Science"]
            Physique = query_components["Physique"]
            Math = query_components["Math"]
            Anglais = query_components["Anglais"]
            Francais = query_components["Francais"]
            Arabe = query_components["Arabe"]
            Philo = query_components["Philo"]
            Info = query_components["Info"]
            res = modelSport.predict([[5,float(Moyenne),float(SpecialiteSport),float(Sport),float(Science),float(Physique),float(Math),float(Anglais),float(Francais),float(Arabe),float(Philo),float(Info)]])
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            body = str(res)
            self.wfile.write(body.encode("utf-8"))
            self.wfile.close()
        
        if float(bac) == 6 :
            Moyenne = query_components["Moyenne"]
            ElectriqueMecanique = query_components["ElectriqueMecanique"]
            Math = query_components["Math"]
            Physique = query_components["Physique"]
            Anglais = query_components["Anglais"]
            Francais = query_components["Francais"]
            Arabe = query_components["Arabe"]
            Philo = query_components["Philo"]
            Info = query_components["Info"]
            TechnologieAppliquee = query_components["TechnologieAppliquee"]
            Sport = query_components["Sport"]
            Option = query_components["Option"]
            res = modelTech.predict([[6,float(Moyenne),float(ElectriqueMecanique),float(Math),float(Physique),float(Anglais),float(Francais),float(Arabe),float(Philo),float(Info),float(TechnologieAppliquee),float(Sport),float(Option)]])
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            body = str(res)
            self.wfile.write(body.encode("utf-8"))
            self.wfile.close()

        if float(bac) == 7 :
            Moyenne = query_components["Moyenne"]
            Philo = query_components["Philo"]
            Option = query_components["Option"]
            Arabe = query_components["Arabe"]
            HistoireGeographie = query_components["HistoireGeographie"]
            Anglais = query_components["Anglais"]
            Francais = query_components["Francais"]
            PhiloIslamique = query_components["PhiloIslamique"]
            Info = query_components["Info"]
            Sport = query_components["Sport"]
            res = modelLettre.predict([[7,float(Moyenne),float(Philo),float(Option),float(Arabe),float(HistoireGeographie),float(Anglais),float(Francais),float(PhiloIslamique),float(Info),float(Sport)]])
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            body = str(res)
            self.wfile.write(body.encode("utf-8"))
            self.wfile.close()

        

server = HTTPServer(('localhost', 2220), MySrv)
server.serve_forever()