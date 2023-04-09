class FortifyApi:
    def __init__(self, url, username = "", password = "", token = ""):
        self.url = url
        self.username = username
        self.password = password
        self.token = token

    def connectserver(self):
        if self.token == "":
            if self.username != "" and self.password != "":
                //basic auth base64
            else:
                //Authentification error . No credentials to connect to the server
        else:
            //FortifyTone auth

    def createToken(self, typeToken = "UnifiedToken"):
        if self.token == "":
            print("create token de type donné en paramètre")
        return tok["data"]

    def deleteToken(self, token_id):
        if self.token != "":
            print("delete token en  parametre")
        return ""


