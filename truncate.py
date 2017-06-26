import pyorient
import config

client = config.client

#DELETING ALL RECORDS
client.command("TRUNCATE CLASS Institucion UNSAFE")
client.command("TRUNCATE CLASS Empleado UNSAFE")
client.command("TRUNCATE CLASS Responsable UNSAFE")
client.command("TRUNCATE CLASS Direccion UNSAFE")
client.command("TRUNCATE CLASS Resultados911 UNSAFE")
client.command("TRUNCATE CLASS Plantel UNSAFE")
client.command("TRUNCATE CLASS Pertenece_a UNSAFE")
client.command("TRUNCATE CLASS Alumno UNSAFE")
client.command("TRUNCATE CLASS Carrera UNSAFE")
client.command("TRUNCATE CLASS Resultado UNSAFE")
client.command("TRUNCATE CLASS Ofrece UNSAFE")
#DELETING ALL RECORDS
