import pandas as pd
import mysql.connector

# Conexion con la base de datos
cnx = mysql.connector.connect(user='*****', password='******',
                              host='******',
                              database='******')

# Crea un cursor
cursor = cnx.cursor()

# Consulta SQL
query = """
#SELECT username, firstname, lastname, city, FROM_UNIXTIME(lastaccess) AS last_access
#FROM mdl_user
#WHERE (city = 'city1' OR city = 'city2')
#  AND lastaccess > UNIX_TIMESTAMP(DATE_SUB(NOW(), INTERVAL 30 DAY));

"""
cursor.execute(query)

# Resultados
results = cursor.fetchall()

# Convierte los resultados en un DataFrame de pandas
df = pd.DataFrame(results, columns=['username', 'firstname', 'lastname', 'city', 'last_access'])

# Guarda en la carpeta "Reportes" el DataFrame en un archivo Excel.
df.to_excel('Reportes/reporte-last-acces.xlsx', index=False)


# Cierra la conexiÃ³n
cnx.close()

