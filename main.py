"""
Bot creador de plantilla de vale azul para comprobación de
gastos no deducibles personalizable en pdf.
    Este archivo tiene todas las funciones privadas y el bot que se debe llamar es:
        CreadorValePlantilla()

Gibran Valle
Revisión final: 11/03/2020
"""
from reportlab.lib.colors import magenta, pink, blue, green, black, white, red, transparent
from reportlab.lib.units import inch, cm
from reportlab.pdfgen import canvas
from constantes_variables import *


# ------------------------------- BOT PARA PROYECTO FINAL ---------------------------------------------
def CrearPlantillaVale(num_subvales, num_conceptos_vale_a, num_conceptos_vale_b):
    """Crear una plantilla de vale personalizada para el proyectofinal

    :param num_subvales: 1 para vales simple, 2 para vale doble
    :param num_conceptos_vale_a: los conceptos en el vale simple o primer subvale
    :param num_conceptos_vale_b: los conceptos en el subvale 2, aplicable solo en vale doble
    :return: guarda la plantilla en la raiz con el nombre: vale.pdf
    Gibran Valle
    Revisión final: 11/03/2020
    """
    debug = 1
    # 1) INICIAR EL CANVAS
    cvs = canvas.Canvas('plantilla_vale.pdf', bottomup=0)
    cvs.setPageSize(letter)

    # ELEGIR EL COLOR DE CANVAS
    cvs.setStrokeColorRGB(0.7, 0.7, 0.7)  # choose your line color

    # CREAR LOS STRINGS
    creadorPlantilla(num_subvales, num_conceptos_vale_a, num_conceptos_vale_b, cvs)

    # CREAR LAS FORMAS DINAMICAS
    forma(cvs, num_subvales, num_conceptos_vale_a, num_conceptos_vale_b)

    # FINALIZAR GUARDANDO EL DOCUMENTO, SOLO SE PUEDE GUARDAR UNA VEZ
    cvs.save()
    if debug:
        print("margen superior: {:.2f}".format(margen_y_calculado / cm))
        print("margen inferior: {:.2f}".format(margen_y_final / cm))
        print("Vale creado correctamente")


# -------------------------------FUNCIONES PRIVADAS PARA PROYECTO FINAL ---------------------------------------------
def roundedBox(canvas, x0=4.5 * cm, y0=2.5 * cm, width=12.5 * cm, heigh=1.63 * cm, linewidth=1.5, radius=0.25 * cm):
    canvas.setLineWidth(linewidth)
    canvas.roundRect(x0, y0, width, heigh, radius)


def rectInterna(canvas, x0, x1, y0, renglones, altura_renglon, linewidth=0.5, title=0):
    canvas.setLineWidth(linewidth)
    # escalar x1 razon desconocida
    x1 *= 1.355
    # empezar en x0, y0+altura renglon
    for i in range(1, renglones):
        canvas.setLineWidth(linewidth * 2.3) if (title == 1 and i == 1) else canvas.setLineWidth(linewidth)
        # x0,y0,x1,y1
        canvas.line(x0, y0 + altura_renglon * i, x1, y0 + altura_renglon * i)


def creadorPlantilla(num_subvales, num_conceptos_vale_a, num_conceptos_vale_b, canvas):
    debug = 0
    # COMPROBAR TOTAL DE CONCEPTOS
    if num_conceptos_vale_a + num_conceptos_vale_b > 8:
        print("ERROR: VALE DEMASIADO GRANDE")
        return

        # 2) EMPEZAR A CALCULAR LA POSICION DE LOS BORDES
    for i in range(1, num_subvales + 1):
        if i == 2:
            num_conceptos = num_conceptos_vale_b
            y0 += SALTO_VALE
            print("creando segundo subvale") if debug else 0
        else:
            num_conceptos = num_conceptos_vale_a
            if num_subvales == 1:
                y0 = margen_y_calculado
            elif num_subvales == 2:
                y0 = margen_y_calculado
            print("creando primer subvale") if debug else 0
        # BORDE 1: IMPORTE_LETRA
        x0 = margen_x
        renglones = 2
        alto_borde = ALTURA_RENGLON * renglones
        roundedBox(canvas, x0=x0, y0=y0, width=LARGO_RENGLON, heigh=alto_borde)
        # HACER EL GRID INTERNO
        rectInterna(canvas, x0=x0, x1=LARGO_RENGLON, y0=y0, renglones=renglones, altura_renglon=ALTURA_RENGLON)
        # moverse 9cm y 10cm en x, para hacer 2 lineas verticales de y0 a y1
        canvas.line(x0 + 9 * cm, y0, x0 + 9 * cm, y0 + ALTURA_RENGLON)
        canvas.line(x0 + 10 * cm, y0, x0 + 10 * cm, y0 + ALTURA_RENGLON)

        # BORDE 2: CONCEPTO
        # editar y0
        y0 += alto_borde + ESPACIO
        renglones = 1 + num_conceptos
        alto_borde = ALTURA_RENGLON * renglones
        roundedBox(canvas, x0=x0, y0=y0, width=LARGO_RENGLON, heigh=alto_borde)
        # HACER EL GRID INTERNO
        rectInterna(canvas, x0=x0, x1=LARGO_RENGLON, y0=y0, renglones=renglones, altura_renglon=ALTURA_RENGLON, title=1)

        # BORDE 3: CARGUESE A
        # sólo editar y0
        y0 += alto_borde + ESPACIO * 2
        renglones = 4
        alto_borde = ALTURA_RENGLON * renglones
        roundedBox(canvas, x0=x0, y0=y0, width=LARGO_RENGLON, heigh=alto_borde)
        # HACER EL GRID INTERNO
        rectInterna(canvas, x0=x0, x1=LARGO_RENGLON, y0=y0, renglones=renglones, altura_renglon=ALTURA_RENGLON, title=1)
        # moverse 9cm y 10cm en x, para hacer 2 lineas verticales de y0 a y1
        canvas.line(x0 + X1, y0, x0 + X1, y0 + alto_borde)
        canvas.line(x0 + X2, y0, x0 + X2, y0 + alto_borde)

        # BORDE 4: FECHA Y FIRMA
        # sólo editar y0
        y0 += alto_borde + ESPACIO
        renglones = 2
        alto_borde = ALTURA_RENGLON * renglones
        roundedBox(canvas, x0=x0, y0=y0, width=LARGO_RENGLON, heigh=alto_borde)
        # HACER EL GRID INTERNO
        rectInterna(canvas, x0=x0, x1=LARGO_RENGLON, y0=y0, renglones=renglones, altura_renglon=ALTURA_RENGLON)
        # moverse 9cm y 10cm en x, para hacer 2 lineas verticales de y0 a y1
        canvas.line(x0 + X1, y0, x0 + X1, y0 + alto_borde)
        canvas.line(x0 + X2, y0, x0 + X2, y0 + alto_borde)


def forma(canvas, num_subvales, renglonesA, renglonesB):
    debug = 0
    # CREACION DE TEXTO ESTÁTICO
    espacio_entre_vales = margen_y_calculado + altura_vale_a + SALTO_VALE + AJUSTE
    print("espacio entre vales = {} o {}cm".format(espacio_entre_vales, espacio_entre_vales / cm)) if debug else 0
    form = canvas.acroForm
    for sub_vale in range(1, num_subvales + 1):
        if sub_vale == 1:
            if num_subvales == 1:
                # offset = margen_y + margen_y_simple
                offset = margen_y_calculado
            elif num_subvales == 2:
                offset = margen_y_calculado + AJUSTE
        elif sub_vale == 2:
            offset = espacio_entre_vales

        # posiciones fijas
        # PRIMER RENGLON FIJO
        canvas.setFont("Helvetica", SIZE_TITLE)
        xcentro = CENTRO_TITLE
        ycentro = offset + ALTURA_RENGLON / 2
        canvas.drawCentredString(xcentro, ycentro, "Comprobante de gastos")
        xcentro = CENTRO_SYMBOL
        canvas.drawCentredString(xcentro, ycentro, "$")
        # calcular salto de renglon (fija)
        sr = ALTURA_RENGLON * 2 + ESPACIO

        # SEGUNDO RENGLON FIJO
        xcentro = CENTRO_CONCEPTOS
        ycentro += sr
        canvas.setFont("Helvetica", SIZE_TEXT)
        canvas.drawCentredString(xcentro, ycentro, "Conceptos")
        sr = ALTURA_RENGLON * renglonesA + 1 + ESPACIO * 2

        # posiciones a calcular
        # EN FUNCION DE LOS CONCEPTOS QUE HAYAN
        ycentro += sr
        xcentro = CENTRO_LABEL
        canvas.setFont("Helvetica", SIZE_LABEL)
        canvas.drawCentredString(xcentro, ycentro, "Carguese a:")
        sr = ALTURA_RENGLON

        # TEXTOS FIJOS
        ycentro += sr
        canvas.setFont("Helvetica", SIZE_TEXT)
        xcentro = CENTRO_CUENTA
        canvas.drawCentredString(xcentro, ycentro, "No. de cuenta")
        xcentro = CENTRO_NOMBRE
        canvas.drawCentredString(xcentro, ycentro, "Nombre")
        xcentro = CENTRO_IMPORTE
        canvas.drawCentredString(xcentro, ycentro, "Importe")
        sr = ESPACIO + ALTURA_RENGLON * 4

        # TEXTO FIJO
        ycentro += sr
        xcentro = CENTRO_CUENTA
        canvas.setFont("Helvetica", SIZE_TEXT)
        canvas.drawCentredString(xcentro, ycentro, "Fecha")
        xcentro = CENTRO_NOMBRE
        canvas.drawCentredString(xcentro, ycentro, "Autorizado por:")
        xcentro = CENTRO_IMPORTE
        canvas.drawCentredString(xcentro, ycentro, "Recibido:")

        # ------------------------------------- FORMAS --------------------------------------------------------------
        nombre = "Importe" if sub_vale == 1 else "Importe2"
        print("offset: {}".format(offset / cm)) if debug else 0
        y0 = letter_height - ALTURA_RENGLON - offset + AJUSTE
        x0 = margen_x + LARGO_RENGLON - largo_suma_importe
        form.textfield(name=nombre, tooltip='$100.00', x=x0, y=y0,
                       width=largo_suma_importe, borderWidth=0, height=ALTURA_RENGLON, fillColor=transparent,
                       textColor=black, forceBorder=False)

        nombre = "ImporteLetra" if sub_vale == 1 else "ImporteLetra2"
        y0 -= ALTURA_RENGLON
        x0 = margen_x
        form.textfield(name=nombre, tooltip='cien pesos 00/100 m.n.', x=x0, y=y0,
                       width=LARGO_RENGLON, borderWidth=0, height=ALTURA_RENGLON, fillColor=transparent,
                       textColor=black,
                       forceBorder=False)
        y0 = y0 - ALTURA_RENGLON * 2 - ESPACIO
        print("posicion: {}".format(y0 / cm)) if debug else 0
        for num_concepto in range(1, renglonesA + 1):
            print("conceptos: {}".format(num_concepto)) if debug else 0
            # forma de conceto enesimo
            concepto = switch_concepto(num_concepto, sub_vale)
            print("nombre: {}".format(concepto)) if debug else 0
            form.textfield(name=concepto, tooltip='taxi hospital - terminal $50.00', x=x0, y=y0,
                           width=LARGO_RENGLON, borderWidth=0, height=ALTURA_RENGLON, fillColor=transparent,
                           textColor=black,
                           forceBorder=False)
            y0 -= ALTURA_RENGLON
        y0 -= ESPACIO * 2

        for renglon in range(1, 4):
            cuenta = switch_cuenta(renglon, sub_vale)
            y = y0 - ALTURA_RENGLON * renglon
            form.textfield(name=cuenta, tooltip='', x=margen_x,
                           y=y,
                           width=largo_cuenta, borderWidth=0, height=ALTURA_RENGLON, fillColor=transparent,
                           textColor=black,
                           forceBorder=False)

            nombre = switch_nombre(renglon, sub_vale)
            form.textfield(name=nombre, tooltip='', x=margen_x + X1,
                           y=y,
                           width=largo_nombre, borderWidth=0, height=ALTURA_RENGLON, fillColor=transparent,
                           textColor=black,
                           forceBorder=False)

            importe = switch_importe(renglon, sub_vale)
            form.textfield(name=importe, tooltip='', x=margen_x + X2,
                           y=y,
                           width=largo_importe, borderWidth=0, height=ALTURA_RENGLON, fillColor=transparent,
                           textColor=black,
                           forceBorder=False)
        y0 -= (ALTURA_RENGLON * 4 + ESPACIO)

        # ultima parte
        y = y0 - ALTURA_RENGLON
        nombre = "Fecha" if sub_vale == 1 else "Fecha2"
        form.textfield(name=nombre, tooltip='', x=margen_x,
                       y=y,
                       width=largo_cuenta, borderWidth=0, height=ALTURA_RENGLON, fillColor=transparent,
                       textColor=black,
                       forceBorder=False)

        nombre = "Autorizado" if sub_vale == 1 else "Autorizado2"
        form.textfield(name=nombre, tooltip='', x=margen_x + X1,
                       y=y,
                       width=largo_nombre, borderWidth=0, height=ALTURA_RENGLON, fillColor=transparent,
                       textColor=black,
                       forceBorder=False)

        nombre = "Recibido" if sub_vale == 1 else "Recibido2"
        form.textfield(name=nombre, tooltip='', x=margen_x + X2,
                       y=y,
                       width=largo_importe, borderWidth=0, height=ALTURA_RENGLON, fillColor=transparent,
                       textColor=black,
                       forceBorder=False)


# implementación de un switch en python
def switch_concepto(num_concepto, sub_vale):
    sufijo = "" if sub_vale == 1 else "2"
    switcher = {
        1: "ConceptoA" + sufijo,
        2: "ConceptoB" + sufijo,
        3: "ConceptoC" + sufijo,
        4: "ConceptoD" + sufijo,
        5: "ConceptoE" + sufijo,
        6: "ConceptoF" + sufijo,
        7: "ConceptoG" + sufijo,
        8: "ConceptoH" + sufijo,
    }
    return switcher.get(num_concepto, "concepto invalido")


def switch_cuenta(num_cuenta, sub_vale):
    sufijo = "" if sub_vale == 1 else "2"
    switcher = {
        1: "No de Cuenta A" + sufijo,
        2: "No de Cuenta B" + sufijo,
        3: "No de Cuenta C" + sufijo,
    }
    return switcher.get(num_cuenta, "cuenta invalida")


def switch_nombre(num_nombre, sub_vale):
    sufijo = "" if sub_vale == 1 else "2"
    switcher = {
        1: "NombreA" + sufijo,
        2: "NombreB" + sufijo,
        3: "NombreC" + sufijo,
    }
    return switcher.get(num_nombre, "cuenta invalida")


def switch_importe(num_importe, sub_vale):
    sufijo = "" if sub_vale == 1 else "2"
    switcher = {
        1: "ImporteA" + sufijo,
        2: "ImporteB" + sufijo,
        3: "ImporteC" + sufijo,
    }
    return switcher.get(num_importe, "cuenta invalida")

# ----------------------------------------- PRUEBA DE BOT ---------------------------------------------
CrearPlantillaVale(VALES_POR_HOJA, CONCEPTOS_EN_VALE_A, CONCEPTOS_EN_VALE_B)
