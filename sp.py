from browser import document, alert

def calcular_numero_mersenne(p):
    return (2 ** p) - 1

def es_primo(n, k=7):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
 
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    
    for _ in range(k):
        a = 2 + _  
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def mostrar_informacion(event):
    document["boton-informacion"].style.display = "none"
    document["boton-calculadora-mersenne"].style.display = "none"
    document["seccion-informacion"].style.display = "block"


def mostrar_calculadora_mersenne(event):
    document["boton-informacion"].style.display = "none"
    document["boton-calculadora-mersenne"].style.display = "none"
    document["seccion-calculadora-mersenne"].style.display = "block"


def mostrar_resultado_mersenne(event):
    entrada_potencia = document["potencia"]
    potencia = int(entrada_potencia.value)
    if potencia < 0:
        alert("Inserta una cantidad positiva")
        return
    div_resultado = document["resultado"]
    numero_mersenne = calcular_numero_mersenne(potencia)
    div_resultado.text = f"M_{potencia} = 2^{potencia} - 1\n\n{numero_mersenne}\n\n"
    if es_primo(numero_mersenne):
        div_resultado.text += "Es un número primo."
    else:
        div_resultado.text += "No es un número primo."


def volver_desde_calculadora(event):
    document["boton-informacion"].style.display = "inline-block"
    document["boton-calculadora-mersenne"].style.display = "inline-block"
    document["seccion-calculadora-mersenne"].style.display = "none"
    document["resultado"].text = ""


def volver_desde_informacion(event):
    document["boton-informacion"].style.display = "inline-block"
    document["boton-calculadora-mersenne"].style.display = "inline-block"
    document["seccion-informacion"].style.display = "none"


document["boton-informacion"].bind("click", mostrar_informacion)
document["boton-calculadora-mersenne"].bind("click", mostrar_calculadora_mersenne)
document["boton-calcular"].bind("click", mostrar_resultado_mersenne)
document["boton-volver"].bind("click", volver_desde_calculadora)
document["boton-volver-informacion"].bind("click", volver_desde_informacion)









