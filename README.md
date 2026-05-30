# 🐍 Python 180 Días - De Cero a Mid Backend
Plan intensivo de 180 días enfocado en buenas prácticas, arquitectura limpia y código de producción listo para el mercado laboral.

**Stack Objetivo:** Python 3 + FastAPI + PostgreSQL + Docker + Pytest + Git

---

## 📈 Progreso Actual: Día 6/180 ✅

### 🛠️ Día 6: Operadores *args y \*\*kwargs`
**Archivo:** `dia6.py`

**Qué aprendi hoy:**
- `*args`: Permite que las funciones acepten infinitos argumentos posicionales, empaquetándolos en una **tupla inmutable**.
- `\*\*kwargs`: Permite que las funciones acepten argumentos dinámicos con nombre, empaquetándolos en un **diccionario** (clave para simular JSON en APIs).
- `sum()`, `len()`, `round()` para procesar colecciones de datos numéricos de forma nativa.
- `try/except` atrapando `TypeError` para blindar el código contra fallos por tipos de datos inválidos.
- `if __name__ == "__main__"` para estructurar la zona de pruebas automatizadas locales.

**Funciones creadas a mano:**
1. `sumar(*args)` - Suma dinámica de colecciones con retorno seguro.
2. `restar(*args)` - Resta secuencial usando *slicing* (`args[1:]`) para aislar la base.
3. `multiplicar(*args)` - Multiplicador flexible inicializado en base `1`.
4. `promedio(*notas)` - Calculadora estadística con redondeo a 2 decimales y control de división por cero.
5. `registrar_api_endpoint(\*\*kwargs)` - Simulación de recepción de payloads en backend usando `.get()` para evitar `KeyError`.

**Output verificado en terminal:**
```text
=== TEST 1: SUMAR *ARGS ===
sumar(5, 10, 15) = 30
sumar() = 0

=== TEST 2: RESTAR *ARGS ===
restar(20, 5, 3) = 12
restar() = 0

=== TEST 3: MULTIPLICAR *ARGS ===
multiplicar(2, 3, 4) = 24

=== TEST 4: PROMEDIO *ARGS ===
promedio(4.5, 3.0, 5.0) = 4.17
promedio vacío = 0

=== TEST 5: **KWARGS API ===

--- [API LOG] Payload Recibido ---
Tipo: <class 'dict'>
Datos: {'nombre': 'Sebas', 'rol': 'Backend Jr', 'pais': 'Colombia'}
Sistema: Registro exitoso para Sebas [Backend Jr]
```


### 🗺️ Roadmap de Carrera (v2.1 Blindado)
- **Fase 1 (Días 1-30):** Fundamentos Python Puro, Módulos, POO y Testing con Pytest.
- **Fase 2 (Días 31-90):** Backend con FastAPI, SQL + PostgreSQL, ORM, Docker y Deploy Cloud.
- **Fase 3 (Días 91-150):** Algoritmos LeetCode, Estructuras de Datos y System Design.
- **Fase 4 (Días 151-180):** Proyecto Capstone Fintech/AI, LinkedIn, CV y Entrevistas.

*Meta: Ofertas laborales antes del 25 de Noviembre de 2026.*

