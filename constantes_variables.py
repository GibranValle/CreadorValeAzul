from reportlab.lib.units import cm
from reportlab.lib.pagesizes import letter


# PARAMETROS PARA EDITAR
VALES_POR_HOJA = 2
CONCEPTOS_EN_VALE_A = 3
CONCEPTOS_EN_VALE_B = 3


# ------------------------------------------- CONSTANTES ------------------------------------------------------------
# tamaños de hoja carta en cm
letter_width, letter_height = letter
# rayas perpendiculares
X1 = 4.25 * cm  # raya vertical 1
X2 = 9 * cm  # raya vertical 2
X3 = 10 * cm  # raya vertical 3
CENTRO_TITLE = 9 * cm
CENTRO_LABEL = 5.7 * cm
CENTRO_SYMBOL = 14 * cm
CENTRO_CONCEPTOS = 11 * cm
CENTRO_CUENTA = 6.5 * cm
CENTRO_NOMBRE = 11 * cm
CENTRO_IMPORTE = 15.6 * cm
# dimensiones
ALTURA_RENGLON = 0.7 * cm
LARGO_RENGLON = 12.5 * cm
ESPACIO = 0.5 * cm
SALTO_VALE = 3 * cm
# ajuste desconocido
AJUSTE = 0.2 * cm
# font size
SIZE_TITLE = 16
SIZE_TEXT = 13
SIZE_LABEL = 11

# VARIABLES
largo_cuenta = X1
largo_nombre = X2 - X1
largo_importe = LARGO_RENGLON - X2
largo_suma_importe = LARGO_RENGLON - X3
# margenes
margen_x = (letter_width - LARGO_RENGLON) / 2
# para calcular el margen automatico
altura_vale_a = ESPACIO * 4 + ALTURA_RENGLON * (7 + CONCEPTOS_EN_VALE_A)
altura_vale_b = ESPACIO * 4 + ALTURA_RENGLON * (7 + CONCEPTOS_EN_VALE_B)
altura_vales = altura_vale_b + altura_vale_b + SALTO_VALE * 1.5
margen_y_calculado = (letter_height - altura_vales) / 2
margen_y_final = letter_height - altura_vales - margen_y_calculado