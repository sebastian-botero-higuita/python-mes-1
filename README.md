# 🐍 Python 180 Días - De Cero a Mid Backend v3.0 BLINDADO
Plan intensivo de 180 días enfocado en buenas prácticas, arquitectura limpia y código de producción listo para el mercado laboral.

**Stack Objetivo:** Python 3 + FastAPI + PostgreSQL + Docker + Pytest + Git

---

## 🗺️ PLAN 180 DÍAS v3.0 BLINDADO
**Meta:** Ofertas laborales antes del 25 Noviembre 2026  
**Filosofía:** Código de producción > tutoriales. Cada día = commit + README + test real

### FASE 1: FUNDAMENTOS BLINDADOS DÍA 1-30
**Objetivo:** Base inquebrantable. Si fallas aquí, todo el backend se cae.

| Día | Tema | Blindaje Auditor | Entregable GitHub |
| :--- | :--- | :--- | :--- |
| 1-3 | Variables, tipos, input/output | Validación de tipos + manejo de `ValueError` | `dia1-3.py` con tests |
| 4-5 | Condicionales, loops | Lógica defensiva + `while True` con break seguro | Ejercicios con casos borde |
| 6 | `*args, **kwargs` | Documentar cuándo usar vs listas/dicts | `dia6.py` + output terminal |
| **7** | **Decoradores @** | **`@wraps` obligatorio + regla `return resultado`** | `dia7.py` blindado ✅ |
| 8 | `yield` y Generadores | Manejo `StopIteration` + memoria vs listas | Consumo de archivos grandes |
| 9-10 | Manejo de Errores | `try/except/else/finally` + excepciones custom | Sistema de logging básico |
| 11-15 | Módulos + Paquetes | `__init__.py` + imports relativos vs absolutos | Proyecto modular |
| 16-20 | POO Básico | Encapsulamiento + `@property` + `__str__` | Sistema de usuarios |
| 21-25 | POO Avanzado | Herencia múltiple + MRO + `super()` | Sistema bancario |
| 26-30 | Testing con Pytest | `assert` + fixtures + coverage >80% | `test_*.py` blindados |

*Blindaje Fase 1: Todo código debe pasar linter + tener docstrings + 3 casos de prueba mínimo.*

### FASE 2: BACKEND REAL DÍA 31-90
**Objetivo:** Construir APIs que no se caigan en producción

| Día | Tema | Blindaje Auditor | Entregable GitHub |
| :--- | :--- | :--- | :--- |
| 31-40 | FastAPI Fundamentos | Validación Pydantic + códigos HTTP correctos | API REST básica |
| 41-50 | SQL + PostgreSQL | SQL Injection prevention + transacciones ACID | CRUD completo |
| 51-60 | ORM SQLAlchemy | Migraciones Alembic + relaciones N:N | Base de datos real |
| 61-70 | Autenticación JWT | Hash bcrypt + refresh tokens + roles | Sistema login seguro |
| 71-80 | Docker | `Dockerfile` multicapa + `.dockerignore` | Container deployable |
| 81-90 | Deploy Cloud | Variables entorno + logs + health checks | API en Render/Railway |

*Blindaje Fase 2: Cada API debe tener documentación interactiva + Postman collection + manejo de errores 400/500.*

### FASE 3: ALGORITMOS + SYSTEM DESIGN DÍA 91-150
**Objetivo:** Pasar entrevistas técnicas sin sudar

| Día | Tema | Blindaje Auditor | Entregable GitHub |
| :--- | :--- | :--- | :--- |
| 91-110 | LeetCode Blind 75 | Complejidad O(n) documentada + casos borde | 30 problemas resueltos |
| 111-130 | Estructuras de Datos | Implementar desde cero: HashMap, Árbol, Grafo | Librería propia |
| 131-150 | System Design | Diseño escalable + cuellos de botella + caching | 3 diseños documentados |

*Blindaje Fase 3: Cada solución incluye: diagrama + complejidad + trade-offs.*

### FASE 4: PROYECTO CAPSTONE + EMPLEO DÍA 151-180
**Objetivo:** Portafolio que vende + CV que pasa ATS

| Día | Tema | Blindaje Auditor | Entregable GitHub |
| :--- | :--- | :--- | :--- |
| 151-165 | Proyecto Fintech/AI | Arquitectura hexagonal + tests + CI/CD | Repo estrella ⭐ |
| 166-170 | LinkedIn + CV | Keywords ATS + métricas cuantificables | Perfil optimizado |
| 171-175 | Entrevistas Mock | STAR method + preguntas sistema | 5 simulacros grabados |
| 176-180 | Aplicar + Negociar | 5 a 10 aplicaciones de alto impacto/día + follow up | Primera oferta |

*Blindaje Fase 4: Proyecto con README que incluye: problema, solución, arquitectura, demo video.*

---

### 🔑 REGLAS DE ORO BLINDADAS (Aplica todos los días)
* **Git:** Commit diario con mensaje descriptivo. Nada de "update".
* **README:** Cada día documentado con qué aprendiste + output real de consola.
* **Testing:** Si no hay test, no existe el código (Fase 1 corporativa).
* **Debugging:** Todo error crítico se documenta. El aprendizaje del wrapper es ley.
* **Código Limpio:** Formateo y orden estructural antes de cada push.
* **Producción:** Pregúntate siempre "¿Esto aguantaría 10k usuarios concurrentes?".

---

### 🛡️ Día 9: Arquitectura Defensiva (`try/except/else/finally`) y Sistemas de Logging
**Archivo:** `dia9.py` | **Logs:** `log.txt`  
**Fecha:** 1 Junio 2026

**Qué aprendí hoy:**
* **Flujo Defensivo Completo:** Implementé la estructura de control de excepciones de Python. Utilicé `else` para ejecutar operaciones lógicas de éxito exclusivo y `finally` como bloque de cierre mandatorio para flujos de auditoría del sistema.
* **Excepciones de Dominio Personalizadas:** Creé clases de error específicas heredando de `Exception` para interceptar de forma aislada las violaciones lógicas de las reglas de negocio (como las alertas de rachas insuficientes) sin mezclar fallos sintácticos de entrada de datos.
* **Persistencia de Eventos de Servidor (Logging):** Diseñé un motor básico de logging persistente en disco utilizando el modo de apertura `"a"` (append) y codificación `utf-8`, asignando niveles semánticos de criticidad (`INFO`, `WARNING`, `DEBUG`) a cada acción del flujo.

**Formato de auditoría registrado en el sistema:**
```text
[2026-06-01 17:30:44] [INFO] Iniciando validacion
[2026-06-01 17:30:52] [WARNING] racha 5 insuficiente
[2026-06-01 17:30:52] [DEBUG] proceso terminado

---
```
## 📈 Progreso Actual: Día 8/180 ✅


### ⚡ Día 8: Iteradores y Generadores (`yield`) - Optimización de Memoria
**Archivo:** `dia8.py`  
**Fecha:** 31 Mayo 2026

**Qué aprendí hoy:**
* **Evaluación Perezosa (Lazy Evaluation):** Los generadores no calculan ni almacenan colecciones masivas en memoria. Producen un elemento a la vez bajo demanda, reduciendo el consumo de RAM a una escala constante $O(1)$ (bajé de 8.06 MB a solo 208 bytes).
* **Mecanismo de Pausa (`yield`):** Entendí que `yield` actúa como un retorno temporal que congela el estado completo de la función (variables locales y puntero de ejecución), permitiendo revivirla en el mismo punto exacto.
* **Protocolo de Iteración y `StopIteration`:** Aprendí que el consumo manual se ejecuta con la función nativa `next()` y que Python avisa de forma estructural que el flujo se quedó sin datos levantando la excepción `StopIteration`.
* **Flujos Infinitos Controlados:** Diseñé un generador infinito con un ciclo `while True` continuo, comprendiendo cómo consumir datos ilimitados de forma segura mediante peticiones dosificadas sin bloquear los núcleos de la CPU.

**Output verificado en consola:**
```text
📦 Lista completa : 8.06 MB
=== PRUEBA stopIteration ===
Elemento 1: 0
Elemento 2: 1
StopIteration atrapada: El generador se quedo sin datos

=== PRUEBA INFINITO CONTROLADO ===
1
3
5
7
... y paramos antes de que la mac llore
Generador: 208 bytes. Misma info, RAM constante 0(1)

```
---

## 📈 Progreso Actual: Día 7/180 ✅

### 🛠️ Día 7: Decoradores (`@`) - Closures y Envolturas Estructurales
**Archivo:** `dia7.py`  
**Fecha:** 30 Mayo 2026

**Qué aprendí hoy:**
* **Decoradores = Azúcar Sintáctica:** Entendí que la sintaxis `@decorador` es una reasignación automática equivalente a escribir `mi_funcion = decorador(mi_funcion)`.
* **Patrón Wrapper:** Creación de una función interna que intercepta el flujo para ejecutar código antes y después de la función principal sin modificar su código original.
* **Preservación de Metadatos:** Uso de `@wraps(func)` de la librería nativa `functools` para evitar que la función pierda su nombre (`__name__`) y su documentación original dentro del sistema.
* **Control de Acceso Básico:** Intercepción estructural de payloads dinámicos (`**kwargs`) para validar roles y credenciales antes de permitir la ejecución de procesos críticos en el backend.
* **Regla de Oro Backend:** Todo decorador debe almacenar el retorno con `resultado = func()` y devolverlo con `return resultado`, de lo contrario romperás el flujo de datos del servidor.
* **Bug Clásico de Junior:** Comprender la diferencia crítica entre `return wrapper()` (que ejecuta la función antes de tiempo) y `return wrapper` (que devuelve la función envuelta lista para ser usada después).

---

### 📈 Progreso Actual: Día 6/180 ✅

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