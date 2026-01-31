import random

def generate_volatility():
    """
    Simulates market volatility (VIX-like index)
    """
    return round(random.uniform(10, 80), 2)


def generate_exposure():
    """
    Simulates portfolio exposure percentage
    """
    return round(random.uniform(50, 150), 2)


def calculate_risk(volatility, exposure):
    """
    Core risk calculation logic
    """
    return round((volatility * exposure) / 100, 2)
def hedge_exposure(exposure):
    """
    Simulates hedging by reducing exposure
    """
    reduced = exposure * 0.8  # reduce by 20%
    return round(reduced, 2)
