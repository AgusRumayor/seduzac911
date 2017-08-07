import config
from terminaltables import AsciiTable
from collections import defaultdict

client = config.client

#total escuelas
preescolar_escuelas_total = client.query('select count(clave) from Plantel where motivo = "" and nivel in ["preescolar", "ipreescolar"]',1)[0].count
primaria_escuelas_total = client.query('select count(clave) from Plantel where motivo = "" and nivel = "primaria"',1)[0].count
secundaria_escuelas_total = client.query('select count(clave) from Plantel where motivo = "" and nivel = "secundaria"',1)[0].count

#aulas existentes
preescolar_aulas_existentes = client.query('select sum(V534, V408) from (select sum(V534) as V534, sum(V408) as V408 from (select expand(out("Resultado")) from Plantel where motivo = "" and nivel in ["preescolar", "ipreescolar"]))',1)[0].sum
primaria_aulas_existentes = client.query('select sum(V895) from (select expand(out(Resultado)) from Plantel where motivo = "" and nivel = "primaria")',1)[0].sum
secundaria_aulas_existentes = client.query('select sum(V717) from (select expand(out(Resultado)) from Plantel where motivo = "" and nivel = "secundaria")',1)[0].sum

#aulas uso
preescolar_aulas_uso = 0
primaria_aulas_uso = client.query('select sum(V903) from (select expand(out(Resultado)) from Plantel where motivo = "" and nivel = "primaria")',1)[0].sum
secundaria_aulas_uso = client.query('select sum(V722) from (select expand(out(Resultado)) from Plantel where motivo = "" and nivel = "secundaria")',1)[0].sum

#total grupos
preescolar_grupos_total = 0
primaria_grupos_general = client.query('select sum(V348) from (select expand(out(Resultado)) from Plantel where motivo = "" and nivel = "primaria" and subnivel = "general")',1)[0].sum
primaria_grupos_comunitaria = client.query('select sum(V408) from (select expand(out(Resultado)) from Plantel where motivo = "" and nivel = "primaria" and subnivel = "comunitaria")',1)[0].sum
primaria_grupos_total = primaria_grupos_general + primaria_grupos_comunitaria
secundaria_grupos_total = client.query('select sum(sum, sum2) from (select sum(V165), sum(V757) from (select expand(out(Resultado)) from Plantel where motivo = "" and nivel = "secundaria"))',1)[0].sum
#alumnos
preescolar_alumnos_hombres = 0
primaria_alumnos_hombres_comunitaria = client.query('select sum(V339) from (select expand(out(Resultado)) from Plantel where motivo = "" and nivel = "primaria" and subnivel = "comunitaria")',1)[0].sum
primaria_alumnos_hombres_general = client.query('select sum(V301, V312) from (select sum(V301) as V301, sum(V312) as V312 from (select expand(out(Resultado)) from Plantel where motivo = "" and nivel = "primaria" and subnivel = "general"))',1)[0].sum
primaria_alumnos_hombres = primaria_alumnos_hombres_comunitaria + primaria_alumnos_hombres_general

secundaria_alumnos_hombres = client.query('select sum(sum, sum2) from (select sum(V130), sum(V138) from (select expand(out(Resultado)) from Plantel where motivo = "" and nivel = "secundaria"))',1)[0].sum
preescolar_alumnos_mujeres = 0
primaria_alumnos_mujeres_general = client.query('select sum(V324, V335) from (select sum(V324) as V324, sum(V335) as V335 from (select expand(out(Resultado)) from Plantel where motivo = "" and nivel = "primaria" and subnivel = "general"))',1)[0].sum
primaria_alumnos_mujeres_comunitaria = client.query('select sum(V351) from (select expand(out(Resultado)) from Plantel where motivo = "" and nivel = "primaria" and subnivel = "comunitaria")',1)[0].sum
primaria_alumnos_mujeres = primaria_alumnos_mujeres_general + primaria_alumnos_mujeres_comunitaria
secundaria_alumnos_mujeres = client.query('select sum(sum, sum2) from (select sum(V147), sum(V155) from (select expand(out(Resultado)) from Plantel where motivo = "" and nivel = "secundaria"))',1)[0].sum
primaria_alumnos_general = client.query('select sum(V347) from (select expand(out(Resultado)) from Plantel where motivo = "" and nivel = "primaria" and subnivel = "general")',1)[0].sum
primaria_alumnos_comunitaria = client.query('select sum(V363) from (select expand(out(Resultado)) from Plantel where motivo = "" and nivel = "primaria" and subnivel = "comunitaria")',1)[0].sum
preescolar_alumnos_total = 0
primaria_alumnos_total = primaria_alumnos_general + primaria_alumnos_comunitaria
secundaria_alumnos_total = client.query('select sum(V164) from (select expand(out(Resultado)) from Plantel where motivo = "" and nivel = "secundaria")',1)[0].sum
#personal
preescolar_personal_total = 0
primaria_personal_general = client.query('select sum(V836) from (select expand(out(Resultado)) from Plantel where motivo = "" and nivel = "primaria" and subnivel = "general")',1)[0].sum
primaria_personal_comunitaria = client.query('select sum(V408) from (select expand(out(Resultado)) from Plantel where motivo = "" and nivel = "primaria" and subnivel = "comunitaria")',1)[0].sum
primaria_personal_total = primaria_personal_general + primaria_personal_comunitaria
secundaria_personal_total = client.query('select sum(V619,V609,V611,V612,V613,V614,V615,V616,V617,V618,V610,V620,V621,V622,V974,V975,V976,V977,V1026,V1027,V757) from (select sum(V609) as V609, sum(V610) as V610, sum(V611) as V611, sum(V612) as V612, sum(V613) as V613, sum(V614) as V614, sum(V615) as V615, sum(V616) as V616, sum(V617) as V617, sum(V618) as V618, sum(V619) as V619, sum(V620) as V620, sum(V621) as V621, sum(V622) as V622, sum(V974) as V974, sum(V975) as V975, sum(V976) as V976, sum(V977) as V977, sum(V1026) as V1026, sum(V1027) as V1027, sum(V757) as V757  from (select expand(out(Resultado)) from Plantel where motivo = "" and nivel = "secundaria"))',1)[0].sum
preescolar_personal_docentes = 0
primaria_personal_docentes_general = client.query('select sum(V820, V821, V824, V825) from (select sum(V824) as V824, sum(V825) as V825, sum(V820) as V820, sum(V821) as V821 from (select expand(out(Resultado)) from Plantel where motivo = "" and nivel = "primaria" and subnivel = "general"))',1)[0].sum
primaria_personal_docentes_comunitaria = client.query('select sum(V408) from (select expand(out(Resultado)) from Plantel where motivo = "" and nivel = "primaria" and subnivel = "comunitaria")',1)[0].sum
primaria_personal_docentes = primaria_personal_docentes_general + primaria_personal_docentes_comunitaria
secundaria_personal_docentes = client.query('select sum(V619,V609,V613,V614,V615,V616,V617,V618,V610,V620,V1026,V1027,V757) from (select sum(V609) as V609, sum(V610) as V610, sum(V611) as V611, sum(V612) as V612, sum(V613) as V613, sum(V614) as V614, sum(V615) as V615, sum(V616) as V616, sum(V617) as V617, sum(V618) as V618, sum(V619) as V619, sum(V620) as V620, sum(V621) as V621, sum(V622) as V622, sum(V974) as V974, sum(V975) as V975, sum(V976) as V976, sum(V977) as V977, sum(V1026) as V1026, sum(V1027) as V1027, sum(V757) as V757  from (select expand(out(Resultado)) from Plantel where motivo = "" and nivel = "secundaria"))',1)[0].sum
preescolar_personal_dir_s_gpo = 0
primaria_personal_dir_s_gpo = client.query('select sum(V822, V823) from (select sum(V822) as V822, sum(V823) as V823 from (select expand(out(Resultado)) from Plantel where motivo = "" and nivel = "primaria" and subnivel = "general"))',1)[0].sum
secundaria_personal_dir_s_gpo = client.query('select sum(V612,V611) from (select sum(V611) as V611, sum(V612) as V612 from (select expand(out(Resultado)) from Plantel where motivo = "" and nivel = "secundaria"))',1)[0].sum
preescolar_personal_advo = 0
primaria_personal_advo = client.query('select sum(V834, V835, V1278, V1279, V1280, V1281) from (select sum(V834) as V834, sum(V835) as V835, sum(V1278) as V1278, sum(V1279) as V1279, sum(V1280) as V1280, sum(V1281) as V1281 from (select expand(out(Resultado)) from Plantel where motivo = "" and nivel = "primaria" and subnivel = "general"))',1)[0].sum
secundaria_personal_advo = client.query('select sum(V974,V975,V976,V977,V621,V622) from (select sum(V609) as V609, sum(V610) as V610, sum(V974) as V974, sum(V975) as V975, sum(V976) as V976, sum(V977) as V977, sum(V622) as V622, sum(V621) as V621 from (select expand(out(Resultado)) from Plantel where motivo = "" and nivel = "secundaria"))',1)[0].sum
preescolar_personal_especial = 0
primaria_personal_especial = client.query('select sum(V826, V827, V828, V829, V830, V831, V832, V833) from (select sum(V833) as V833, sum(V832) as V832, sum(V831) as V831, sum(V830) as V830, sum(V829) as V829, sum(V828) as V828, sum(V827) as V827, sum(V826) as V826 from (select expand(out(Resultado)) from Plantel where motivo = "" and nivel = "primaria" and subnivel = "general"))',1)[0].sum
secundaria_personal_especial = client.query('select sum(V615,V616,V617,V618,V619,V620,V1026,V1027) from (select sum(V615) as V615, sum(V616) as V616, sum(V617) as V617, sum(V618) as V618, sum(V619) as V619, sum(V620) as V620, sum(V1026) as V1026, sum(V1027) as V1027 from (select expand(out(Resultado)) from Plantel where motivo = "" and nivel = "secundaria"))',1)[0].sum

table_data = [
    ['Nivel', 'Escuelas', 'Aulas Ex', 'Aulas Uso', 'Grupos', 'Alumnos_H', 'Alumnos_M', 'Alumnos', 'Docentes', 'Dir s/gpo', 'Advos', 'Especial', 'Personal'],
    #['Inicial', consultas['inicial']['escuelas']['total'], inicial_aulas_existentes],
    ['Preescolar', preescolar_escuelas_total, preescolar_aulas_existentes, preescolar_aulas_uso, preescolar_grupos_total, preescolar_alumnos_hombres, preescolar_alumnos_mujeres, preescolar_alumnos_total, preescolar_personal_docentes, preescolar_personal_dir_s_gpo, preescolar_personal_advo, preescolar_personal_especial, preescolar_personal_total],
    ['Primaria', primaria_escuelas_total, primaria_aulas_existentes, primaria_aulas_uso, primaria_grupos_total, primaria_alumnos_hombres, primaria_alumnos_mujeres, primaria_alumnos_total, primaria_personal_docentes, primaria_personal_dir_s_gpo, primaria_personal_advo, primaria_personal_especial, primaria_personal_total],
    ['Secundaria', secundaria_escuelas_total, secundaria_aulas_existentes, secundaria_aulas_uso, secundaria_grupos_total, secundaria_alumnos_hombres, secundaria_alumnos_mujeres, secundaria_alumnos_total, secundaria_personal_docentes, secundaria_personal_dir_s_gpo, secundaria_personal_advo, secundaria_personal_especial, secundaria_personal_total],
    #['Media', media_escuelas_total, media_aulas_existentes],
    #['Superior', superior_escuelas_total, superior_aulas_existentes],
]
table = AsciiTable(table_data)
print table.table
