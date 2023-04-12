# Importação da biblioteca

from django.http import JsonResponse

def calculator(consumption: list, distributor_tax: float, tax_type: str) -> tuple:
    """
    returns a tuple of floats contained anual savings, monthly savings, applied_discount and coverage
    """
    annual_savings = 0
    monthly_savings = 0
    applied_discount = 0
    coverage = 0

    # your code here #

    # Colocando os campos de entrada (Consumo dos últimos 3 meses, valor da tarifa e tipo da tarifa)
    consumo1 = float(request.GET.get('consumo1', 0))
    consumo2 = float(request.GET.get('consumo2', 0))
    consumo3 = float(request.GET.get('consumo3', 0))
    tarifa = float(request.GET.get('tarifa', 0))
    tipo_tarifa = request.GET.get('tipo_tarifa', '')

    # Calcula o consumo médio mensal
    consumo_medio = (consumo1 + consumo2 + consumo3) / 3

        # Calcula o desconto aplicado com base no tipo de tarifa e no consumo médio
    if consumo_medio < 10000:
        if tipo_tarifa == 'Residencial':
            desconto = 0.18
        elif tipo_tarifa == 'Comercial':
            desconto = 0.16
        elif tipo_tarifa == 'Industrial':
            desconto = 0.12
    elif consumo_medio <= 20000:
        if tipo_tarifa == 'Residencial':
            desconto = 0.22
        elif tipo_tarifa == 'Comercial':
            desconto = 0.18
        elif tipo_tarifa == 'Industrial':
            desconto = 0.15
    else:
        if tipo_tarifa == 'Residencial':
            desconto = 0.25
        elif tipo_tarifa == 'Comercial':
            desconto = 0.22
        elif tipo_tarifa == 'Industrial':
            desconto = 0.18
    
    # Calcula a economia mensal e anual com base no consumo médio, tarifa e desconto aplicado
    economia_mensal = consumo_medio * tarifa * desconto
    economia_anual = economia_mensal * 12

    # Calcula a cobertura com base no consumo médio
    if consumo_medio < 10000:
        cobertura = 0.9
    elif consumo_medio <= 20000:
        cobertura = 0.95
    else:
        cobertura = 0.99


  # Retorna os resultados em formato JSON
    return JsonResponse({
        'economia_anual': economia_anual,
        'economia_mensal': economia_mensal,
        'desconto_aplicado': desconto,
        'cobertura': cobertura
    })


if __name__ == "__main__":
    print("Testing...")

    assert calculator([1518, 1071, 968], 0.95871974, "Industrial") == (
        1473.19,
        122.77,
        0.12,
        0.9,
    )

    assert calculator([1000, 1054, 1100], 1.12307169, "Residencial") == (
        2295.32,
        191.28,
        0.18,
        0.9,
    )

    assert calculator([973, 629, 726], 1.04820025, "Comercial") == (
        1405.56,
        117.13,
        0.16,
        0.9,
    )

    assert calculator([15000, 14000, 16000], 0.95871974, "Industrial") == (
        24591.16,
        2049.26,
        0.15,
        0.95,
    )

    assert calculator([12000, 11000, 11400], 1.12307169, "Residencial") == (
        32297.74,
        2691.48,
        0.22,
        0.95,
    )

    assert calculator([17500, 16000, 16400], 1.04820025, "Comercial") == (
        35776.75,
        2981.40,
        0.18,
        0.95,
    )

    assert calculator([30000, 29000, 29500], 0.95871974, "Industrial") == (
        60478.73,
        5039.89,
        0.18,
        0.99,
    )

    assert calculator([22000, 21000, 21400], 1.12307169, "Residencial") == (
        71602.56,
        5966.88,
        0.25,
        0.99,
    )

    assert calculator([25500, 23000, 21400], 1.04820025, "Comercial") == (
        63832.12,
        5319.34,
        0.22,
        0.99,
    )

    print("Everything passed")
