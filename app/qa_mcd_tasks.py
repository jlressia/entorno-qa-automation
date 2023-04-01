#Tareas relacionadas con el MB de MCD
import logging
from qa_core import Test

class McdDMB(Test):
    __opciones = {}
    __testNumber = 0
    def __init__(self, testName, testCommand, testNumber):
        logging.info(f"New test {testName} and test num. ", testNumber, "created.")
        # Inicializo variables del objeto padre
        super().__init__(testName, testCommand)
        self.__testNumber = testNumber

    def run(self) -> str:
        #Ejecuta la opcion seleccionada
        logging.info(f"RUN {self.testName} Test Num. {self.__testNumber} - OPS {len(self.__opciones)}")
        if self.__testNumber > 0 and len(self.__opciones) >= self.__testNumber:
            result = self.__opciones[self.__testNumber]()
        else:
            result = "El test solicitado no existe"
        return result
        
    
    # TAREAS A REALIZAR
    def funcion1():
        return("Se ha seleccionado la opción 1.")

    def funcion2():
        return("Se ha seleccionado la opción 2.")

    def funcion3():
        return("Se ha seleccionado la opción 3.")

    # Diccionario de funcionalidades que podran ser invocadas desde RUN
    __opciones = {
        1: funcion1,
        2: funcion2,
        3: funcion3
    }