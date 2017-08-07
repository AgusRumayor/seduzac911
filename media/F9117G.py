from dbfread import DBF
import re
import datetime
import config

client = config.client
nivel = "media"
table = DBF('F9117G.dbf', load=True, encoding="latin-1")
#print table.field_names
#print table.records[0]
r = re.compile("MS\d")
fields = filter(r.match, table.field_names)
#print fields
info_general = ['PLANTEL', 'NOMPLANTEL', 'ESTATUS', 'INMUEBLE']
ubicacion = ['ENTIDAD', 'NOMENTIDAD', 'MUNICIPIO', 'NOMMUNICI', 'LOCALIDAD', 'NOMLOCALI', 'DOMICILIO']
sostenimiento = ['SOSTENIMIE', 'NOMBRESOS']
dependencia_normativa = ['DEPNORMTVA', 'NOMBREDEP']
grupos = ['GRUPO1', 'GRUPO2', 'GRUPO3', 'GRUPO4']
direccion = ['NOMBREDIR', 'APDIR', 'APDIR2']
resultados911 = ['CAPTURA', 'OBSERVACIO', 'RESPLLENA', 'FECHA', 'CORREORESP', 'PUESTORESP']
biblioteca = ['CCTBIBLIO']
control = ['CONTROL', 'SUBCONTROL']
renombres = {u'PLANTEL':'clave', u'NOMPLANTEL':'nombre', u'TURNO':'turno', u'ENTIDAD':'entidad', u'NOMENTIDAD':'nombre_entidad', 
u'MUNICIPIO':'municipio', u'NOMMUNICI':'nombre_municipio', u'LOCALIDAD':'localidad', u'NOMLOCALI':'nombre_localidad', u'DOMICILIO':'domicilio', 
u'DEPADMVA':'depadva', u'DEPNORMTVA':'dependencia_normativa', u'ZONAESCOLA':'zona_escolar', u'SECTOR':'sector', u'DIRSERVREG':'dirservreg', 
u'SOSTENIMIE':'sosteimiento', u'SERVICIO':'servicio', u'UNIDADRESP':'unidadresp', u'PROGRAMA':'programa', u'SUBPROG':'subprog', u'RENGLON':'renglon',
 u'N_RENGLON':'nombre_renglon', u'PERIODO':'periodo', u'MOTIVO':'motivo', u'DISPON':'dispon', u'CONTROL':'control', u'CAPTURA':'captura',
 u'GRUPO3':'3', u'GRUPO2':'2', u'FECHA':'fecha', u'INMUEBLE':'inmueble', u'APDIR2':'segundo_apellido', u'APDIR':'primer_apellido', u'GRUPO4':'4', 
u'RESPLLENA':'responasable_llenado', u'NOMBREDEP':'nombre', u'NOMBRESOS':'nombre', u'CCTBIBLIO':'clave', u'SUBCONTROL':'subcontrol',
 u'CORREORESP':'correo', u'GRUPO1':'1', u'NOMBREDIR':'nombre', u'PUESTORESP':'puesto', u'OBSERVACIO':'observaciones', u'ESTATUS':'estatus'}
#print len(table.field_names)
total_f = info_general+ubicacion+sostenimiento+dependencia_normativa+fields+resultados911+grupos+control+biblioteca+direccion
#print len(total_f)
print (set(total_f) - set(table.field_names))
print (set(table.field_names) - set(total_f))
records = table.records
#records = table.records[1:3]
print len(table.records)
exit(0)
for record in records:
	q='CREATE VERTEX Plantel CONTENT {'
	q=q+'"nivel":"'+nivel+'",'
	#Informacion general
	for field in info_general:
		value = record[field]
		if type(value) == unicode:
			value = value.replace('"', '\\"')
		q=q+'"%s":"%s",'%(renombres[field], value)
	q=q+'ubicacion:{'
	for field in ubicacion:
		value = record[field]
                if type(value) == unicode:
                        value = value.replace('"', '\\"')
		q=q+'"%s":"%s",'%(renombres[field], value)
	q=q[:-1]
	q=q+'}, '
	q=q+'direccion:{'
	for field in direccion:
                value = record[field]
                if type(value) == unicode:
                        value = value.replace('"', '\\"')
                q=q+'"%s":"%s",'%(renombres[field], value)
        q=q[:-1]
	q=q+'},'
	q=q+'sostenimiento:{'
        for field in sostenimiento:
                value = record[field]
                if type(value) == unicode:
                        value = value.replace('"', '\\"')
                q=q+'"%s":"%s",'%(renombres[field], value)
        q=q[:-1]
        q=q+'},'
	q=q+'dependencia_normativa:{'
        for field in dependencia_normativa:
                value = record[field]
                if type(value) == unicode:
                        value = value.replace('"', '\\"')
                q=q+'"%s":"%s",'%(renombres[field], value)
        q=q[:-1]
        q=q+'},'
	q=q+'grupos:{'
        for field in grupos:
                value = record[field]
                if type(value) == unicode:
                        value = value.replace('"', '\\"')
                q=q+'"%s":"%s",'%(renombres[field], value)
        q=q[:-1]
        q=q+'},'
	q=q+'control:{'
        for field in control:
                value = record[field]
                if type(value) == unicode:
                        value = value.replace('"', '\\"')
                q=q+'"%s":"%s",'%(renombres[field], value)
        q=q[:-1]
        q=q+'},'
	q=q+'biblioteca:{'
        for field in biblioteca:
                value = record[field]
                if type(value) == unicode:
                        value = value.replace('"', '\\"')
                q=q+'"%s":"%s",'%(renombres[field], value)
        q=q[:-1]
        q=q+'}'
	q=q+'}'
	rid_plantel = client.command(q)[0]._rid
	#print q
	q='CREATE VERTEX Resultados911 CONTENT {'
	for field in fields:
		value = record[field]
		#print value
		#print type(value)
                if type(value) == unicode:
                        value = value.replace('"', '\\"')
                	q=q+'"%s":"%s",'%(field, value)
		elif type(value) == datetime.date:
			q=q+'"%s":"%s",'%(field, value) 
		elif type(value) == int:
			q=q+'"%s":%i,'%(field, value)
		else:
			print "Data error @:"+rid_plantel
	for field in resultados911:
                value = record[field]
                if type(value) == unicode:
                        value = value.replace('"', '\\"')
			value = value.replace('\n', '')
			value = value.replace('\r', '')
                q=q+'"%s":"%s",'%(renombres[field], value)
        q=q[:-1]
	q=q+'}'
	#print q
	rid_911 = client.command(q)[0]._rid
	if rid_911:
                q= 'CREATE EDGE Resultado FROM %s TO %s'%(rid_plantel, rid_911)
                client.command(q)

