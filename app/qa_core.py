# Core que contiene las herramientas basicas para la ejecucion de tests de QA.
import logging

# Clase basica que encapsula un test. 
# Es solo un contenedor, el test en si es un objeto recibido en el argumento testAction y que posteriormente será ejecutado.
class Test:
    testName = ""
    def __init__(self, testName, testAction):
        logging.info("New test", testName, "created.")
        self.testName = testName
        self.command = testAction
    
    def run (self) -> str:
        return self.command.run()

# Clase que contendra una coleccion de tests que puedan ser ejecutados
class TestSuit:
    tests = []
    def __init__(self, name) -> None:
        self.name = name

    def addTest(self, test):
        #Agrego un test al test suit
        logging.info(f"TestSuit - Se agrego el test {test.testName}")
        self.tests.append(test)

    def listTests(self):
        #Lista todos los tests que hayan sido agregados
        pass

    def run (self):
        # Recorrer la lista de tests con un for loop
        logging.info(f"TestSuit - Se van a ejecutar {len(TestSuit.tests)} test.")
        for obj in TestSuit.tests:
            # Verificar si el objeto es de tipo "Test"
            if isinstance(obj, Test):
                # Ejecutar el método "run"
                logging.info(f"TestSuit - Ejecutando test {obj.testName}")
                result = obj.run()
                logging.info(f"TestSuit - Resultado de {obj.testName} - {result}")
            else:
                logging.error (obj, "No es un test válido.")