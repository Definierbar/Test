class Worker():
    def init(self, vorname :str, nachname :str, lohn :int) -> None:
        self.vorname = vorname
        self.nachname = nachname
        self.lohn = lohn

    def Ficken():
        print("8======D")

    def senken_lohn(self, Franken):
        if (Franken <= 3600):
            print("Error: Lohn unter dem Mindestlohn! \
Der Wert wurde nicht geändert")
        else:
            self.lohn = Franken
            print("Lohn wurde angepasst.")

    def get_lohn(self):
        return self.lohn

    def get_worker_id(self):
        return "Ich heisse " + self.vorname + self.nachname + ". Mein Lohn bei der Firma beträgt " + str(self.lohn)

    def get_initialen():
        return


p1 = Worker("Max", "Mustermann", 3600)
p2 = Worker(p1, "Mustermann", 3600)

print(p1.get_worker_id())