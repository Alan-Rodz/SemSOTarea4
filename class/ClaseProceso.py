class Proceso:
    id = 0
    tme = 0
    op = ""
    op1 = 0
    op2 = 0
    resultado = 0
    estado = "pendiente"
    tt = 0
    tr = 0
    numlote = 0
    error = False 

    def __init__(self, idProceso, tme, operacion, op1, op2):
        self.id = idProceso
        self.tme = tme
        self.op = operacion
        self.op1 = op1
        self.op2 = op2
        if self.op == "+":
            self.resultado = op1+op2
        elif self.op == "-":
            self.resultado = op1-op2
        elif self.op == "/":
            self.resultado = op1/op2
        elif self.op == "%":
            self.resultado = op1 % op2
        else:
            self.resultado = 0
        self.estado = "pendiente"
        self.tt = 0
        self.tr = tme
        self.numlote = 0
        self.error = False

    # Override print Process Object
    def __str__(self):
        if self.estado == "pendiente":
            return "(ID: {}, TME: {}, TT: {})".format(self.id, self.tme, self.tt)
        elif self.estado == "ejecucion":
            return ("ID: {}, OP: {}, TME: {}, TT: {}, TR: {}".format(self.id, self.op, self.tme, self.tt, self.tr))
        elif self.estado == "terminado" and self.error == False:
            return "(ID: {}, OP: {}, RESULTADO: {}, LOTE: {})".format(self.id, self.op, self.resultado, self.numlote)
        elif self.estado == "terminado" and self.error == True:
            return "(ID: {}, OP: {}, RESULTADO: ERROR, LOTE: {})".format(self.id, self.op, self.resultado, self.numlote)

    # Override list of this Object Type

    def __repr__(self):
        return str(self)