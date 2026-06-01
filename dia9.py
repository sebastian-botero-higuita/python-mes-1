from datetime import datetime

class ErrorRachaRota(Exception):
    pass
def log(mensaje, nivel="INFO"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(f"{timestamp} {nivel} {mensaje}\n")

def validar_racha():
            log("Iniciando validacion", "INFO")
            try:
                entrada = input("Dias de Racha:")
                racha = int(entrada)
                if racha < 9:
                    raise ErrorRachaRota(f"racha {racha} insuficiente")
            except ValueError:
                print("Error: solo numeros")
                log(f"valuerror: {entrada}", "ERROR")
            except ErrorRachaRota as e:
                print(f"Alerta: {e}")
                log(str(e), "WARNING")
            else:
                print(f"OK: {racha} dias")
                log(f"Racha OK: {racha}", "INFO")
            finally:
                log("proceso terminado", "DEBUG")

validar_racha()
