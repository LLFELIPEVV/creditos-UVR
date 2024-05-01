from django.shortcuts import render

# Create your views here.
# Calcula el valor de la cuota mensual del crédito UVR.
def calcular_cuota(monto_credito, tasa_uvr, plazo_credito, periodicidad_pagos):
    
    # Calcula el factor de capitalización, que representa el efecto de la tasa de interés sobre el monto del crédito
    """Se refiere a los intereses mensuales
        tasa_uvr == 0.012 que seria el 1,2% por eso se le suma el 1 que ya cuenta como el 100%
        y quedaria como 101,2%"""
    factor_capitalizacion = (1 + tasa_uvr) ** periodicidad_pagos
    # Calcula el factor de amortización, que representa el efecto de la tasa de interés sobre el plazo del crédito
    """Da el procentaje del total de la cuota que se descuenta del total del credito"""
    factor_amortizacion = 1 - (1 + tasa_uvr) ** (-plazo_credito * periodicidad_pagos)
    # Calcula la cuota mensual del crédito UVR utilizando los factores de capitalización y amortización
    cuota = monto_credito * factor_capitalizacion * tasa_uvr / factor_amortizacion
    
    return cuota

def simulador(request):
    if request.method == 'POST':
        # Monto del crédito en pesos colombianos.
        monto_credito = float(request.POST.get('monto_credito'))
        # Tasa de interés UVR mensual.
        tasa_uvr = float(request.POST.get('tasa_uvr'))
        # Plazo del crédito en meses.
        plazo_credito = int(request.POST.get('plazo_credito'))
        # Periodicidad de los pagos (mensual).
        periodicidad_pagos = int(request.POST.get('periodicidad_pagos'))

        cuota_mensual = calcular_cuota(monto_credito, tasa_uvr, plazo_credito, periodicidad_pagos)

        pago_actual = 0
        saldo_actual = monto_credito
        interes_pagado = 0
        pagos_data = []

        for mes in range(1, plazo_credito + 1):
            pago_actual += cuota_mensual
            interes_pagado_mes = saldo_actual * tasa_uvr
            saldo_actual = saldo_actual - cuota_mensual + interes_pagado_mes
            interes_pagado += interes_pagado_mes

            pagos_data.append({
                "Mes": mes,
                "Pago": round(cuota_mensual, 2),
                "Saldo": round(saldo_actual, 2),
                "Interes_pagado": round(interes_pagado_mes, 2)
            })

        context = {
            'cuota_mensual': cuota_mensual,
            'pagos_data': pagos_data,
        }
        return render(request, 'tu_app/tu_plantilla.html', context)

    return render(request, 'tu_app/tu_plantilla.html')
