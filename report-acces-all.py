import pandas as pd
import mysql.connector
import datetime


# Conexión con la base de datos
cnx = mysql.connector.connect(user='****', password='***',
                              host='***.***.***.**',
                              database='*******')

# Crea un cursor
cursor = cnx.cursor()

# Consulta SQL
query = """
SELECT distinct
	u.username AS usuario, 
	u.firstname AS nombre, 
	u.lastname AS apellido, 
	u.email,
	c.fullname AS nombre_curso,
    g.name AS nombre_grupo,
	r.shortname AS rol, 
	FROM_UNIXTIME(UNIX_TIMESTAMP(FROM_UNIXTIME((ula.timeaccess)))) AS ultimo_acceso_al_curso,
	u.suspended AS suspendido
FROM mdl_enrol AS er
INNER JOIN mdl_user_enrolments AS ue ON er.id=ue.enrolid
INNER JOIN mdl_course AS c ON er.courseid=c.id
INNER JOIN mdl_user AS u ON ue.userid=u.id
LEFT JOIN mdl_user_lastaccess AS ula ON u.id=ula.userid and c.id=ula.courseid
INNER JOIN mdl_role_assignments AS ra ON u.id=ra.userid
INNER JOIN mdl_role AS r ON r.id=ra.roleid
LEFT JOIN mdl_groups_members gm ON gm.userid = u.id
LEFT JOIN mdl_groups g ON g.id = gm.groupid AND g.courseid = c.id
WHERE r.id = 5 AND u.suspended=0 AND (YEAR(FROM_UNIXTIME(ula.timeaccess)) = 2024 OR ula.timeaccess IS NULL);


"""

cursor.execute(query)

# Resultados
results = cursor.fetchall()

# Convierte los resultados en un DataFrame de pandas
df = pd.DataFrame(results, columns=['Usuario', 'Nombre', 'Apellido', 'Email', 'Materia', 'Grupo','rol', 'Ãšltimo acceso', 'Suspendido'])

# Obtiene la fecha actual
now = datetime.datetime.now()

# Formatea la fecha como una cadena
date_str = now.strftime("%Y-%m-%d")

# Guarda en la carpeta "Reportes" el DataFrame en un archivo Excel.
df.to_excel(f'Reportes/reporte-acces-{date_str}.xlsx', index=False)

# Cierra la conexión
cnx.close()
