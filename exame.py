class IR:
    def __init__(self):
        self.tranches = [0,30000, 50000, 60000, 80000, 180000]
        self.tauxIR = [0,10, 20, 30, 34, 38]

    def geIR(self,salaire):
        salaireAnnuel = salaire * 12
        for i in range(5,-1,-1):
            if salaireAnnuel > self.tranches[i]:
                return  self.tauxIR[i] / 100
from abc import ABC, abstractmethod
class IEmploye(ABC):
    @abstractmethod
    def age(self):
        pass 
    @abstractmethod
    def anciennete(self):
        pass
    @abstractmethod
    def dateRetrait(self,ageRetrait):
        pass

class Formature(IEmploye):
    def __init__(self, mtle, nom, dateNaissance, dateEmbuche, salaireBase, heurSup):
        super().__init__(mtle, nom, dateNaissance, dateEmbuche, salaireBase)
        self.heurSup = heurSup
        self.tariSup = 70

    @property
    def heurSup(self):
        return self.heurSup
    @heurSup.setter
    def heurSup(self,h):
        self.heurSup = h

    @property
    def tarifSup(self):
        return self.tarifSup

    def __str__(self):
        return f"{self.__str__()} - {self.heurSup} - {self.tarifSup}"

    def salaireAPayer(self):
        salaireNet = (self.salaireBase + self.heurSup * self.tarifSup ) * (1-self.geIR(self.salaireBase))
        return salaireNet
from abc import ABC, abstractmethod
from datetime import datetime

class Employe(IEmploye,IR,ABC):
    count = 0
    def __init__(self, mtle, nom, dateNaissance, dateEmbuche, salaireBase):
        count += 1
        self.mtle = mtle
        self.nom = nom

        d = datetime.strptime(dateNaissance)
        self.dateNaissance = d
        
        d = datetime.strptime(dateEmbuche)
        self.dateEmbuche = d
        self.salaireBase = salaireBase
    
    @property
    def mtle(self):
        return self.mtle 
    
    @property
    def nom(self):
        return self.nom 
    @nom.setter
    def nom(self,nom):
        self.nom= nom

    @property
    def dateNaissance(self):
        return self.dateNaissance 
    @dateNaissance.setter
    def dateNaissance(self,dateNaissance):
        self.dateNaissance= dateNaissance

    @property
    def dateEmbuche(self):
        return self.dateEmbuche 
    @dateEmbuche.setter
    def dateEmbuche(self,dateEmbuche):
        self.dateEmbuche= dateEmbuche

    @property
    def salaireBase(self):
        return self.salaireBase 
    @salaireBase.setter
    def salaireBase(self,salaireBase):
        self.salaireBase= salaireBase

    def age(self):
        todayDate = datetime.date.today()
        age = todayDate.year - self.dateNaissance.year
        return age
    
    def dateRetrait(self, ageRetrait):
        return self.dateNaissance - datetime.strptime(ageRetrait+"/01/"+"01")
        
    def anciennete(self):
        todayDate = datetime.date.today()
        anc = todayDate.year - self.dateEmbuche.year
        return anc
    def isAncienneteGreaterthan20year(self):
        if self.anciennete() > 20:
            return True
        else:
            return False
    
    def __str__(self):
        return f"{self.mtle} - {self.nom} - {self.dateNaissance} - {self.dateEmbuche} - {self.salaireBase} "

    def __eq__(self,e):
        if self.mtle == e.mtle:
            return True
        else :
            return False
        
    @abstractmethod
    def salaireAPayer():
        pass     
class Agent(Employe):
    def __init__(self, mtle, nom, dateNaissance, dateEmbuche, salaireBase, primeRespo):
        super().__init__(mtle, nom, dateNaissance, dateEmbuche, salaireBase)
        self.primeRespo = primeRespo

    def salaireAPayer(self):
        salaireNet = (self.salaireBase + self.primeRespo) * (1 - self.geIR(self.salaireBase))
        return salaireNet                        