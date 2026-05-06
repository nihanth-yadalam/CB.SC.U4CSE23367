from pydantic import BaseModel
import httpx

class Log(BaseModel):
    stack: str
    level: str
    package: str
    message: str

    
    def logdata(self):

        vstack = ["backend","frontend"]
        vlevel = ["debug","info","warn","error","fatal"]
        vpackage = ["cache","controller","cron_job","db","domain","handler","repository","route","service",
                "auth","config","middleware","utils"]
        
        self.stack = self.stack.lower()
        self.level = self.level.lower()
        self.package = self.package.lower()
        self.message = self.message.lower()

        if self.stack not in vstack:
            raise ValueError("invalid input for stack")
        elif self.level not in vlevel:
            raise ValueError("invalid input for level")
        elif self.package not in vpackage:
            raise ValueError("invalid input for package")

        return {
            "stack": self.stack,
            "level": self.level,
            "package": self.package,
            "message": self.message,
        }

    def send(self):

        url = "http://20.207.122.201/evaluation-service/logs"
        payload = self.logdata()

        with httpx.Client() as client:
            response = client.post(url, json=payload)
            response.raise_for_status()

        return response.json()
        

