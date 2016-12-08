import doctor



def CheckIn():
    print("Please enter username: ")
    return False

def CheckA():
    print("b")
    doctor1 = doctor.Doctor("Marko", "sifra")
    print(doctor1.name)

# listaDoktora = ucitajFajlDoktora() //

isLoginSuccess = CheckIn()
if isLoginSuccess == True:
    print("uspesno")
else:
    exit(0)

print("sss")



