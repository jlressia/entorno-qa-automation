#Aqui se ejecutan los diferentes pruebas 
import logging
import traceback
from qa_core import TestSuit
from qa_mcd_tasks import McdDMB
#from qa_core import TestSuit

#-------- MCD --------
#LEER PRECIO
def mbMcdReadPrice ():
    logging.info("{} - McdDMB reading price.".format(mbMcdReadPrice.__name__))
    try:
        miTestsuit = TestSuit("Tests de MCD")
        # 1er test que se agrega al testSuit
        miTest1 = McdDMB("Read MCD Test 1", "", 1)
        miTestsuit.addTest(miTest1)
        # 2do test que se agrega al testSuit
        miTest2 = McdDMB("Read MCD Test 2", "", 2)
        miTestsuit.addTest(miTest2)        
        # Ejecuto el test suit
        readTest = miTestsuit.run()
    except Exception as e:
        miError = traceback.format_exc()
        readTest = f"UPSS! - {e} {miError}"
        logging.error(f"{mbMcdReadPrice.__name__} - McdDMB reading price. \n {miError}")
    return readTest

#MODIFICAR PRECIO
def mbMcdModifyPrice ():
    logging.info("{} - McdDMB modifing price.".format(mbMcdModifyPrice.__name__))
    readTest = McdDMB("Modify MCD Test",2).run()
    return readTest

#-------- ALSEA --------
#LEER PRECIO

#MODIFICAR PRECIO
