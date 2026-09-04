from database.cuentas import obtener_cuentas

def main():
    
    cuentas = obtener_cuentas()
    
    for cuenta in cuentas:
        print(
            cuenta.nombre,
            cuenta.moneda.value,
            cuenta.proposito.value,
            cuenta.saldo
)

if __name__ == "__main__":
    main()