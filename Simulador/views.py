from django.shortcuts import render
from .forms import SimuladorForm

# Create your views here.
# Calcula el valor de la cuota mensual del crédito UVR.
def calcular_cuota(monto_credito, tasa_anual, plazo_credito, mes_pago):
    # Lista para almacenar los detalles de cada mes
    pagos_data = []
    # Interes mensual
    r = (tasa_anual / 12) / 100
    print(f'r: {r}')
    # Monto total del credito
    pv = monto_credito
    print(f'pv: {pv}')
    # Numero total de pagos
    n = plazo_credito
    print(f'n: {n}')
    # Tasa de inflacion mensual
    i = 0.01
    # Numero de la cuota
    m = mes_pago
    print(f'm: {m}')
    
    saldo = pv
    
    pagos_data.append({
        'Mes': 0,
        'Cuota': 0,
        'Intereses': 0,
        'Inflacion': 0,
        'Abono': 0,
        'Saldo': monto_credito
    })
    
    for x in range(1, n+1):
        cuota_mensual = round(((r * pv) / (1 - (1 + r) ** -n)) * (1 + i) ** (x - 1), 3)
        # La cantidad de intereses que se pagan en la cuota
        intereses = round(saldo * r, 3)
        # La cantidad de inflacion que se paga en la cuota
        inflacion = round(cuota_mensual - (cuota_mensual / ((i + 1) ** (x - 1))), 3)
        print(f'inflacion: {inflacion}')
        # La cantidad de dinero real que se va a pagar el saldo del prestamo
        abono = round(cuota_mensual - (intereses + inflacion), 3)
        
        saldo = round(saldo - abono, 4)
        
        if x == m:
            cuota_mes = cuota_mensual
        
        pagos_data.append({
            'Mes': x,
            'Cuota': cuota_mensual,
            'Intereses': intereses,
            'Inflacion': inflacion,
            'Abono': abono,
            'Saldo': saldo
        })
    
    print(f'Cuota: {cuota_mes}')
    
    return cuota_mes, pagos_data

def simulador(request):
    if request.method == 'POST':
        form = SimuladorForm(request.POST)
        if form.is_valid():
            # Monto del crédito en pesos colombianos.
            monto_credito = float(request.POST.get('monto_credito'))
            # Tasa de interés UVR mensual.
            tasa_anual = float(request.POST.get('tasa_anual'))
            # Plazo del crédito en meses.
            plazo_credito = int(request.POST.get('plazo_credito'))
            # Periodicidad de los pagos (mensual).
            mes_pago = int(request.POST.get('mes_pago'))

            cuota_mes, pagos_data = calcular_cuota(monto_credito, tasa_anual, plazo_credito, mes_pago)

            context = {
                'form': form,
                'cuota_mes': cuota_mes,
                'numero_mes': mes_pago,
                'pagos_data': pagos_data,
            }
            
            return render(request, 'simulador.html', context)
    else:
        form = SimuladorForm()
    return render(request, 'simulador.html', {'form': form})

