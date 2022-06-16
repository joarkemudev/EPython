
    
    userReply = input("Necesitas enviar un paquete? (Enter si o no) ")

if userReply == "si":
    print("Nosotros podemos ayudarte a enviar un paquete!")
else:
    print("Por favor vuelve cuando necesites ennviar un paquete. Gracias.")
    
    
userReply = input("Deseas comprar estampillas, comprar un sobre, o hacer una copia? (Digite estampillas, sobres, o copias) ")
if userReply.lower() == "estampillas":
    print("Tenemos diferentes diseños de espampilla para escoger.")
elif userReply.lower()  == "sobres":
    print("Tenemos varios diseños de sobres para escoger.")
elif userReply.lower() == "copias":
    copies = input("Cuantas copias necesitas? (Digite el numero) ")
    print("Here are {} copies.".format(copies))
else:
    print("Gracias, vuelva pronto.")    