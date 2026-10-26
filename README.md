# agentforge-sandbox-demo (mailcheck)

Repositorio privado y desechable para validar la lectura mediante la GitHub App de AgentForge (Fase 7, Paso 2) y la primera ejecución gobernada sobre un repositorio real. Nada se publica desde AgentForge.

## Tarea

Implementar `validate_email(address: str) -> bool` en `src/mailcheck/validator.py`
y añadir pruebas unitarias propias en `tests/test_validator.py`.
Las pruebas de aceptación de `tests/test_acceptance.py` definen el comportamiento
exigido y no se modifican.

## Reglas

1. Exactamente un `@`; parte local y dominio no vacíos.
2. Longitud total máxima 254 caracteres; parte local máxima 64.
3. Parte local: letras ASCII, dígitos y los símbolos `. _ % + -`; sin punto
   inicial ni final; sin dos puntos consecutivos.
4. Dominio: al menos dos etiquetas separadas por `.`; cada etiqueta de 1 a 63
   caracteres entre letras ASCII, dígitos y guion, sin guion inicial ni final.
5. La última etiqueta (TLD) contiene solo letras y al menos dos.
6. Sin espacios en blanco en ninguna posición. Mayúsculas y minúsculas se admiten.
7. Si `address` no es `str`, lanzar `TypeError`.

Sin dependencias externas. Debe pasar `ruff check`, `ruff format --check` y `pytest`
con la configuración de `pyproject.toml`.
