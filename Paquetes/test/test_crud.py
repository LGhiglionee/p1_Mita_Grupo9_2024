from Paquetes import validar_mail, validar_fecha_nacimiento #1er test
 

def  test_LoginMailT(): #testeo del login x mail
    login_pass = validar_mail('mailgenerico@gmail.com')
    login_pass1 = validar_mail('mailgegmail.com')
    assert login_pass == True
    assert login_pass1 == False


def test_LoginFecha ():
    login_pass = validar_fecha_nacimiento('11/10/2020')
    login_pass1 = validar_fecha_nacimiento('90/1/20')
    assert login_pass == True
    assert login_pass1 == False