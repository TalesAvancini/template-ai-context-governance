#!/usr/bin/env python3
"""
🕐 _tz_utils.py — Motor de Fuso Horário (Stdlib Only)
Padrão: America/Sao_Paulo (UTC-3). Configurável via env var CONTEXT_TIMEZONE.
"""
import os
from datetime import datetime, timezone, timedelta

# Dicionário de Timezones (Brasília offset fixo)
TZ_MAP = {
    "America/Sao_Paulo": timedelta(hours=-3),
    "America/Recife": timedelta(hours=-3),
    "America/Manaus": timedelta(hours=-4),
    "America/Los_Angeles": timedelta(hours=-8),
    "America/New_York": timedelta(hours=-5),
    "Europe/London": timedelta(hours=0),
    "Europe/Berlin": timedelta(hours=1),
    "Asia/Tokyo": timedelta(hours=9),
    "UTC": timedelta(hours=0),
}

def get_now_tz():
    """Retorna o datetime atual no timezone configurado."""
    tz_name = os.environ.get("CONTEXT_TIMEZONE", "America/Sao_Paulo")
    offset = TZ_MAP.get(tz_name, timedelta(hours=-3))
    return datetime.now(timezone(offset))

def format_ts(dt=None, fmt="%Y-%m-%d %H:%M"):
    """Formata o datetime para string legível."""
    if dt is None:
        dt = get_now_tz()
    return dt.strftime(fmt)

if __name__ == "__main__":
    # Teste isolado
    tz_env = os.environ.get("CONTEXT_TIMEZONE", "America/Sao_Paulo")
    print(f"[OK] Agora em {tz_env}: {format_ts()}")
