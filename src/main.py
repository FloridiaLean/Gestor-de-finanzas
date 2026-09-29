from consultas.resumen import obtener_resumen_anual

def main():
    
    resumen = obtener_resumen_anual(2026)
    
    print("Año:", resumen["año"])
    
    for mes in resumen["meses"]:
        print(mes)
    
if __name__ == "__main__":
    main()