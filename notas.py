"""""""""
    # ultima parte
    nombre = "Fecha" if i == 1 else "Fecha2"
    form.textfield(name=nombre, tooltip='', x=margen_x,
                   y=y + offset - altura_renglon * n,
                   width=largo_cuenta, borderWidth=0, height=altura_renglon, fillColor=transparent,
                   textColor=black,
                   forceBorder=False)

    nombre = "Autorizado" if i == 1 else "Autorizado2"
    form.textfield(name=nombre, tooltip='', x=margen_x + x1,
                   y=y + offset - altura_renglon * n,
                   width=largo_nombre, borderWidth=0, height=altura_renglon, fillColor=transparent,
                   textColor=black,
                   forceBorder=False)

    nombre = "Recibido" if i == 1 else "Recibido2"
    form.textfield(name=nombre, tooltip='', x=margen_x + x2,
                   y=y + offset - altura_renglon * n,
                   width=largo_importe, borderWidth=0, height=altura_renglon, fillColor=transparent,
                   textColor=black,
                   forceBorder=False)

"""""""""""