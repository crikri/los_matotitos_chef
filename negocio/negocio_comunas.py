from datos.conexion import conectar_db
from prettytable import PrettyTable

def listado_comunas(tabla: PrettyTable):
    db = conectar_db()
    db.connect()
    query = "SELECT * FROM comunas"
    cursor = db.execute_sql(query)
    for row in cursor.fetchall():
        tabla.add_row(row)
    db.close()
    
