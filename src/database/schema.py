from database.database import obtener_conexion

def crear_tabla_cuentas():
    
    conexion = obtener_conexion()
    
    conexion.execute("""
        CREATE TABLE IF NOT EXISTS cuentas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            moneda TEXT NOT NULL,
            proposito TEXT NOT NULL,
            saldo REAL NOT NULL
            )
    """)
    
    conexion.commit()
    conexion.close()

def crear_tabla_categorias():
    
    conexion = obtener_conexion()
    
    conexion.execute("""
        CREATE TABLE IF NOT EXISTS categorias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            activa INTEGER NOT NULL DEFAULT 1
            )
    """)
    
    conexion.commit()
    conexion.close()

def crear_tabla_operaciones():
    
    conexion = obtener_conexion()
    
    conexion.execute("""
        CREATE TABLE IF NOT EXISTS operaciones (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha TEXT NOT NULL,
            tipo TEXT NOT NULL,
            categoria_id INTEGER,
            descripcion TEXT NOT NULL,
            monto REAL NOT NULL,
            cuenta_origen_id INTEGER,
            cuenta_destino_id INTEGER,
            precio_conversion REAL,
            subtipo_conversion TEXT,
            
            FOREIGN KEY (categoria_id) REFERENCES categorias(id),
            FOREIGN KEY (cuenta_origen_id) REFERENCES cuentas(id),
            FOREIGN KEY (cuenta_destino_id) REFERENCES cuentas(id)
            )
    """)
    
    conexion.commit()
    conexion.close()
