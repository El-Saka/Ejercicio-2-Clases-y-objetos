class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    
    def imprimir_informacion(self):
        print("Nombre del alumno: ", self.nombre)
        print("Nota del alumno: ", self.nota)
    
    def evaluar_aprobacion(self):
        if self.nota >= 5:
            print("El alumno", self.nombre, "ha aprobado")
        else:
            print("El alumno", self.nombre, "ha suspendido")

# Ejemplo de uso
alumno1 = Alumno(" David", 7)
alumno1.imprimir_informacion()
alumno1.evaluar_aprobacion()

alumno2 = Alumno("Maria", 4)
alumno2.imprimir_informacion()
alumno2.evaluar_aprobacion()
