#if

edad = 20
if edad < 13:
    print("eres un niño")
elif edad < 18:
    print("eres un adolecente")
else: 
    print("eres adulto")

edad = 17
tiene_permiso = True

if edad >= 18: 
    print("puedes entrar")
else:
    if tiene_permiso:
        print("puede entrar con permiso") 
    else:
        print("no puede entrar")

