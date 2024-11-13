from Paquetes import validar_mail, validar_fecha_nacimiento #1er test
 

def  test_LoginMailT(): #testeo del login x mail
    login_pass = validar_mail('mailgenerico@gmail.com')
    assert login_pass == True


def test_LoginFecha ():
    login_pass = validar_fecha_nacimiento('11/10/2020')
    assert login_pass == True