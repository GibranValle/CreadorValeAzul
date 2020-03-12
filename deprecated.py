# ------------------------------- PROTOTIPOS ---------------------------------------------
def gridInterno(canvas, x0, x1, y0, renglones, altura_renglon, linewidth=0.5):
    x1 *= 1.355
    canvas.setLineWidth(linewidth)
    p = canvas.beginPath()
    # empezar en el origine x0, y0+altura renglon
    for i in range(1, renglones):
        p.moveTo(x0, y0 + altura_renglon * i)
        p.lineTo(x1, y0 + altura_renglon * i)
    p.close()
    canvas.drawPath(p)


def star(canvas, title="Title Here", aka="Comment here.", xcenter=None, ycenter=None, nvertices=5):
    from math import pi
    from reportlab.lib.units import inch
    radius = inch / 3.0
    if xcenter is None: xcenter = 2.75 * inch
    if ycenter is None: ycenter = 1.5 * inch
    canvas.drawCentredString(xcenter, ycenter + 1.3 * radius, title)
    canvas.drawCentredString(xcenter, ycenter - 1.4 * radius, aka)
    p = canvas.beginPath()
    p.moveTo(xcenter, ycenter + radius)
    from math import pi, cos, sin
    angle = (2 * pi) * 2 / 5.0
    startangle = pi / 2.0
    for vertex in range(nvertices - 1):
        nextangle = angle * (vertex + 1) + startangle
        x = xcenter + radius * cos(nextangle)
        y = ycenter + radius * sin(nextangle)
        p.lineTo(x, y)
    if nvertices == 5:
        p.close()
    canvas.drawPath(p)


def joins(canvas):
    # make lines big
    canvas.setLineWidth(5)
    canvas.setLineJoin(1)
    star(canvas, "Round join", "1: rounded")


def borde_curvo(canvas):
    canvas.setLineWidth(5)

    #  "Default: mitered join"
    #  "Round join", "1: rounded"
    #  "Bevelled join", "2: square"
    canvas.setLineJoin(1)

    letra_alto = 1.63 * cm
    espacio = 0.33 * cm

    x0_letra = 4.5 * cm
    x1_letra = letter_width - x0_letra

    y0_letra = 2.5 * cm
    y1_letra = y0_letra + letra_alto

    p = canvas.beginPath()
    p.moveTo(x0_letra, y0_letra)
    p.lineTo(x0_letra, y1_letra)
    p.lineTo(x1_letra, y1_letra)
    p.lineTo(x1_letra, y0_letra)
    p.close()
    canvas.drawPath(p)


def botCreadorFormaSimple():
    # FUNCIONANDO OK
    c = canvas.Canvas('../simple_form.pdf')

    # c.rect(15, 625, 250, 125, fill=0)

    c.setFont("Courier", 20)
    c.drawCentredString(300, 700, 'Employment Form')
    c.setFont("Courier", 14)
    form = c.acroForm

    c.drawString(10, 650, 'First Name:')
    form.textfield(name='fname', tooltip='First Name',
                   x=110, y=635, borderStyle='inset',
                   borderColor=magenta, fillColor=pink,
                   width=300,
                   textColor=blue, forceBorder=True)

    c.drawString(10, 600, 'Last Name:')
    form.textfield(name='lname', tooltip='Last Name',
                   x=110, y=585, borderStyle='inset',
                   borderColor=green, fillColor=magenta,
                   width=300,
                   textColor=blue, forceBorder=True)

    c.drawString(10, 550, 'Address:')
    form.textfield(name='address', tooltip='Address',
                   x=110, y=535, borderStyle='inset',
                   width=400, forceBorder=True)

    c.drawString(10, 500, 'City:')
    form.textfield(name='city', tooltip='City',
                   x=110, y=485, borderStyle='inset',
                   forceBorder=True)

    c.drawString(250, 500, 'State:')
    form.textfield(name="state", tooltip="State", x=350, y=485, borderStyle="inset", forceBorder=True)

    c.drawString(10, 450, 'Zip Code:')
    form.textfield(name='zip_code', tooltip='Zip Code',
                   x=110, y=435, borderStyle='inset',
                   forceBorder=True)

    c.save()

