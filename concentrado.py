import config
from terminaltables import AsciiTable
from collections import defaultdict

client = config.client

#total escuelas
inicial_escuelas_total = client.query('select count(clave) from Plantel where motivo = "" and nivel in ["inicial"] and subnivel in ["general"]',1)[0].count
preescolar_escuelas_total = client.query('select count(clave) from Plantel where motivo = "" and nivel in ["preescolar", "ipreescolar"]',1)[0].count
primaria_escuelas_total = client.query('select count(clave) from Plantel where motivo = "" and nivel = "primaria"',1)[0].count
secundaria_escuelas_total = client.query('select count(clave) from Plantel where motivo = "" and nivel = "secundaria"',1)[0].count
superior_escuelas_total = client.query('select count(clave) from Plantel where nivel = "superior" and estatus = "Activa"',1)[0].count

#aulas existentes
inicial_aulas_existentes = client.query('select sum(V386, V397) from (select sum(V386) as V386, sum(V397) as V397 from (select expand(out("Resultado")) from Plantel where motivo = "" and nivel in ["inicial"] and subnivel in ["general"]))',1)[0].sum
preescolar_aulas_existentes_general = client.query('select sum(V534) from (select expand(out("Resultado")) from Plantel where motivo = "" and nivel in ["preescolar"] and subnivel = "general")',1)[0].sum
preescolar_aulas_existentes_inicial = client.query('select sum(V408) from (select expand(out("Resultado")) from Plantel where motivo = "" and nivel in ["ipreescolar"])',1)[0].sum
preescolar_aulas_existentes = preescolar_aulas_existentes_general + preescolar_aulas_existentes_inicial
primaria_aulas_existentes = client.query('select sum(V895) from (select expand(out(Resultado)) from Plantel where motivo = "" and nivel = "primaria")',1)[0].sum
secundaria_aulas_existentes = client.query('select sum(V717) from (select expand(out(Resultado)) from Plantel where motivo = "" and nivel = "secundaria")',1)[0].sum
superior_aulas_existentes = client.query('select sum(S264) from (select expand(out("Resultado")) from Plantel where estatus="Activa" and nivel in ["superior"])',1)[0].sum

#aulas uso
inicial_aulas_uso = client.query('select sum(V391, V402) from (select sum(V391) as V391, sum(V402) as V402 from (select expand(out("Resultado")) from Plantel where motivo = "" and nivel in ["inicial"] and subnivel in ["general"]))',1)[0].sum
preescolar_aulas_uso_general = client.query('select sum(V539) from (select expand(out("Resultado")) from Plantel where motivo = "" and nivel in ["preescolar"] and subnivel = "general")',1)[0].sum
preescolar_aulas_uso_inicial = client.query('select sum(V413) from (select expand(out("Resultado")) from Plantel where motivo = "" and nivel in ["ipreescolar"])',1)[0].sum
preescolar_aulas_uso = preescolar_aulas_uso_general + preescolar_aulas_uso_inicial
primaria_aulas_uso = client.query('select sum(V903) from (select expand(out(Resultado)) from Plantel where motivo = "" and nivel = "primaria")',1)[0].sum
secundaria_aulas_uso = client.query('select sum(V722) from (select expand(out(Resultado)) from Plantel where motivo = "" and nivel = "secundaria")',1)[0].sum
superior_aulas_uso = client.query('select sum(S267) from (select expand(out("Resultado")) from Plantel where estatus="Activa" and nivel in ["superior"])',1)[0].sum

#total grupos
inicial_grupos_total = client.query('select sum(V53, V69) from (select sum(V53) as V53, sum(V69) as V69 from (select expand(out("Resultado")) from Plantel where motivo = "" and nivel in ["inicial"] and subnivel in ["general"]))',1)[0].sum
preescolar_grupos_general = client.query('select sum(V64) from (select expand(out("Resultado")) from Plantel where motivo = "" and nivel in ["preescolar"] and subnivel = "general")',1)[0].sum
preescolar_grupos_inicial = client.query('select sum(V133) from (select expand(out("Resultado")) from Plantel where motivo = "" and nivel in ["ipreescolar"])',1)[0].sum
preescolar_personal_comunitaria = client.query('select sum(V52) from (select expand(out("Resultado")) from Plantel where motivo = "" and nivel in ["preescolar"] and subnivel = "comunitaria")',1)[0].sum
preescolar_grupos_total = preescolar_grupos_general + preescolar_grupos_inicial + preescolar_personal_comunitaria
primaria_grupos_general = client.query('select sum(V348) from (select expand(out(Resultado)) from Plantel where motivo = "" and nivel = "primaria" and subnivel = "general")',1)[0].sum
primaria_grupos_comunitaria = client.query('select sum(V408) from (select expand(out(Resultado)) from Plantel where motivo = "" and nivel = "primaria" and subnivel = "comunitaria")',1)[0].sum
primaria_grupos_total = primaria_grupos_general + primaria_grupos_comunitaria
secundaria_grupos_total = client.query('select sum(sum, sum2) from (select sum(V165), sum(V757) from (select expand(out(Resultado)) from Plantel where motivo = "" and nivel = "secundaria"))',1)[0].sum
superior_grupos_total = "ND"

#alumnos
#hombres
inicial_alumnos_hombres = client.query('select sum(V41, V57) from (select sum(V41) as V41, sum(V57) as V57 from (select expand(out("Resultado")) from Plantel where motivo = "" and nivel in ["inicial"] and subnivel in ["general"]))',1)[0].sum
preescolar_alumnos_hombres_general = client.query('select sum(V53) from (select expand(out("Resultado")) from Plantel where motivo = "" and nivel in ["preescolar"] and subnivel = "general")',1)[0].sum
preescolar_alumnos_hombres_inicial = client.query('select sum(V122) from (select expand(out("Resultado")) from Plantel where motivo = "" and nivel in ["ipreescolar"])',1)[0].sum
preescolar_alumnos_hombres_comunitaria = client.query('select sum(V9) from (select expand(out("Resultado")) from Plantel where motivo = "" and nivel in ["preescolar"] and subnivel = "comunitaria")',1)[0].sum
preescolar_alumnos_hombres = preescolar_alumnos_hombres_general + preescolar_alumnos_hombres_inicial + preescolar_alumnos_hombres_comunitaria
primaria_alumnos_hombres_comunitaria = client.query('select sum(V339) from (select expand(out(Resultado)) from Plantel where motivo = "" and nivel = "primaria" and subnivel = "comunitaria")',1)[0].sum
primaria_alumnos_hombres_general = client.query('select sum(V301, V312) from (select sum(V301) as V301, sum(V312) as V312 from (select expand(out(Resultado)) from Plantel where motivo = "" and nivel = "primaria" and subnivel = "general"))',1)[0].sum
primaria_alumnos_hombres = primaria_alumnos_hombres_comunitaria + primaria_alumnos_hombres_general

secundaria_alumnos_hombres = client.query('select sum(sum, sum2) from (select sum(V130), sum(V138) from (select expand(out(Resultado)) from Plantel where motivo = "" and nivel = "secundaria"))',1)[0].sum
superior_alumnos_hombres = client.query('select sum(S234H, S132H) from (SELECT SUM(S234H) as S234H, sum(S132H) as S132H FROM (SELECT expand(out("Resultado")) FROM Carrera))',1)[0].sum

#mujeres
inicial_alumnos_mujeres = client.query('select sum(V45, V61) from (select sum(V45) as V45, sum(V61) as V61 from (select expand(out("Resultado")) from Plantel where motivo = "" and nivel in ["inicial"] and subnivel in ["general"]))',1)[0].sum
preescolar_alumnos_mujeres_inicial = client.query('select sum(V127) from (select expand(out("Resultado")) from Plantel where motivo = "" and nivel in ["ipreescolar"])',1)[0].sum
preescolar_alumnos_mujeres_comunitaria = client.query('select sum(V14) from (select expand(out("Resultado")) from Plantel where motivo = "" and nivel in ["preescolar"] and subnivel = "comunitaria")',1)[0].sum
preescolar_alumnos_mujeres_general = client.query('select sum(V58) from (select expand(out("Resultado")) from Plantel where motivo = "" and nivel in ["preescolar"] and subnivel = "general")',1)[0].sum
preescolar_alumnos_mujeres = preescolar_alumnos_mujeres_inicial + preescolar_alumnos_mujeres_comunitaria + preescolar_alumnos_mujeres_general
primaria_alumnos_mujeres_general = client.query('select sum(V324, V335) from (select sum(V324) as V324, sum(V335) as V335 from (select expand(out(Resultado)) from Plantel where motivo = "" and nivel = "primaria" and subnivel = "general"))',1)[0].sum
primaria_alumnos_mujeres_comunitaria = client.query('select sum(V351) from (select expand(out(Resultado)) from Plantel where motivo = "" and nivel = "primaria" and subnivel = "comunitaria")',1)[0].sum
primaria_alumnos_mujeres = primaria_alumnos_mujeres_general + primaria_alumnos_mujeres_comunitaria
secundaria_alumnos_mujeres = client.query('select sum(sum, sum2) from (select sum(V147), sum(V155) from (select expand(out(Resultado)) from Plantel where motivo = "" and nivel = "secundaria"))',1)[0].sum
superior_alumnos_mujeres = client.query('select sum(S234M, S132M) from (SELECT SUM(S234M) as S234M, sum(S132M) as S132M FROM (SELECT expand(out("Resultado")) FROM Carrera))',1)[0].sum
#total
primaria_alumnos_general = client.query('select sum(V347) from (select expand(out(Resultado)) from Plantel where motivo = "" and nivel = "primaria" and subnivel = "general")',1)[0].sum
primaria_alumnos_comunitaria = client.query('select sum(V363) from (select expand(out(Resultado)) from Plantel where motivo = "" and nivel = "primaria" and subnivel = "comunitaria")',1)[0].sum

inicial_alumnos_total = client.query('select sum(V49, V65) from (select sum(V49) as V49, sum(V65) as V65 from (select expand(out("Resultado")) from Plantel where motivo = "" and nivel in ["inicial"] and subnivel in ["general"]))',1)[0].sum
preescolar_alumnos_total_general = client.query('select sum(V63) from (select expand(out("Resultado")) from Plantel where motivo = "" and nivel in ["preescolar"] and subnivel = "general")',1)[0].sum
preescolar_alumnos_total_comunitaria = client.query('select sum(V19) from (select expand(out("Resultado")) from Plantel where motivo = "" and nivel in ["preescolar"] and subnivel = "comunitaria")',1)[0].sum
preescolar_alumnos_total_inicial = client.query('select sum(V132) from (select expand(out("Resultado")) from Plantel where motivo = "" and nivel in ["ipreescolar"])',1)[0].sum
preescolar_alumnos_total = preescolar_alumnos_total_general + preescolar_alumnos_total_comunitaria + preescolar_alumnos_total_inicial
primaria_alumnos_total = primaria_alumnos_general + primaria_alumnos_comunitaria
secundaria_alumnos_total = client.query('select sum(V164) from (select expand(out(Resultado)) from Plantel where motivo = "" and nivel = "secundaria")',1)[0].sum
superior_alumnos_total = client.query('SELECT sum(SUM, SUM2) FROM (SELECT SUM(S284), SUM(S12) FROM (SELECT expand(out("Resultado")) FROM Plantel WHERE estatus = "Activa" and nivel in ["superior"]))',1)[0].sum

#personal
inicial_personal = client.query('select sum(V292) from (select expand(out("Resultado")) from Plantel where motivo = "" and nivel in ["inicial"] and subnivel in ["general"])',1)[0].sum
preescolar_personal_general = client.query('select sum(V485) from (select expand(out(Resultado)) from Plantel where motivo = "" and nivel = "preescolar" and subnivel = "general")',1)[0].sum
primaria_personal_general = client.query('select sum(V836) from (select expand(out(Resultado)) from Plantel where motivo = "" and nivel = "primaria" and subnivel = "general")',1)[0].sum
primaria_personal_comunitaria = client.query('select sum(V408) from (select expand(out(Resultado)) from Plantel where motivo = "" and nivel = "primaria" and subnivel = "comunitaria")',1)[0].sum
primaria_personal_total = primaria_personal_general + primaria_personal_comunitaria
secundaria_personal_total = client.query('select sum(V619,V609,V611,V612,V613,V614,V615,V616,V617,V618,V610,V620,V621,V622,V974,V975,V976,V977,V1026,V1027,V757) from (select sum(V609) as V609, sum(V610) as V610, sum(V611) as V611, sum(V612) as V612, sum(V613) as V613, sum(V614) as V614, sum(V615) as V615, sum(V616) as V616, sum(V617) as V617, sum(V618) as V618, sum(V619) as V619, sum(V620) as V620, sum(V621) as V621, sum(V622) as V622, sum(V974) as V974, sum(V975) as V975, sum(V976) as V976, sum(V977) as V977, sum(V1026) as V1026, sum(V1027) as V1027, sum(V757) as V757  from (select expand(out(Resultado)) from Plantel where motivo = "" and nivel = "secundaria"))',1)[0].sum
superior_personal_total = client.query('select sum(S38) from (select expand(out("Resultado")) from Plantel where estatus="Activa" and nivel in ["superior"])',1)[0].sum
#docentes
inicial_personal_docentes = client.query('select sum(V160, V161, V162, V163, V167, V168, V169, V170, V174, V175, V176, V177) from (select sum(V160) as V160, sum(V161) as V161, sum(V162) as V162, sum(V163) as V163, sum(V167) as V167, sum(V168) as V168, sum(V169) as V169, sum(V170) as V170, sum(V174) as V174, sum(V175) as V175, sum(V176) as V176, sum(V177) as V177, sum(V159) as V159  from (select expand(out("Resultado")) from Plantel where motivo = "" and nivel in ["inicial"] and subnivel in ["general"]))',1)[0].sum
preescolar_personal_docentes_general = client.query('select sum(V471, V472, V475, V476) from (select sum(V471) as V471, sum(V472) as V472, sum(V475) as V475, sum(V476) as V476 from (select expand(out(Resultado)) from Plantel where motivo = "" and nivel = "preescolar" and subnivel = "general"))',1)[0].sum
preescolar_personal_docentes_inicial = client.query('select sum(V164, V165, V171, V172, V178, V179) from (select sum(V164) as V164, sum(V165) as V165, sum(V171) as V171, sum(V172) as V172, sum(V178) as V178, sum(V179) as V179 from (select expand(out(Resultado)) from Plantel where nivel in ["ipreescolar"]))',1)[0].sum
preescolar_personal_docentes = preescolar_personal_docentes_general + preescolar_personal_docentes_inicial + preescolar_personal_comunitaria
primaria_personal_docentes_general = client.query('select sum(V820, V821, V824, V825) from (select sum(V824) as V824, sum(V825) as V825, sum(V820) as V820, sum(V821) as V821 from (select expand(out(Resultado)) from Plantel where motivo = "" and nivel = "primaria" and subnivel = "general"))',1)[0].sum
primaria_personal_docentes_comunitaria = client.query('select sum(V408) from (select expand(out(Resultado)) from Plantel where motivo = "" and nivel = "primaria" and subnivel = "comunitaria")',1)[0].sum
primaria_personal_docentes = primaria_personal_docentes_general + primaria_personal_docentes_comunitaria
secundaria_personal_docentes = client.query('select sum(V619,V609,V613,V614,V615,V616,V617,V618,V610,V620,V1026,V1027,V757) from (select sum(V609) as V609, sum(V610) as V610, sum(V611) as V611, sum(V612) as V612, sum(V613) as V613, sum(V614) as V614, sum(V615) as V615, sum(V616) as V616, sum(V617) as V617, sum(V618) as V618, sum(V619) as V619, sum(V620) as V620, sum(V621) as V621, sum(V622) as V622, sum(V974) as V974, sum(V975) as V975, sum(V976) as V976, sum(V977) as V977, sum(V1026) as V1026, sum(V1027) as V1027, sum(V757) as V757  from (select expand(out(Resultado)) from Plantel where motivo = "" and nivel = "secundaria"))',1)[0].sum
superior_personal_docentes = client.query('select sum(S24, S25) from (select sum(S24) as S24, sum(S25) as S25 from (select expand(out("Resultado")) from Plantel where estatus="Activa" and nivel in ["superior"]))',1)[0].sum

#directivos sin grupo
inicial_personal_dir_s_gpo = client.query('select sum(V207) from (select expand(out("Resultado")) from Plantel where motivo = "" and nivel in ["inicial"] and subnivel in ["general"])',1)[0].sum
preescolar_personal_dir_s_gpo = client.query('select sum(V473, V474) from (select sum(V473) as V473, sum(V474) as V474 from (select expand(out(Resultado)) from Plantel where motivo = "" and nivel = "preescolar" and subnivel = "general"))',1)[0].sum
primaria_personal_dir_s_gpo = client.query('select sum(V822, V823) from (select sum(V822) as V822, sum(V823) as V823 from (select expand(out(Resultado)) from Plantel where motivo = "" and nivel = "primaria" and subnivel = "general"))',1)[0].sum
secundaria_personal_dir_s_gpo = client.query('select sum(V612,V611) from (select sum(V611) as V611, sum(V612) as V612 from (select expand(out(Resultado)) from Plantel where motivo = "" and nivel = "secundaria"))',1)[0].sum
superior_personal_dir_s_gpo = client.query('select sum(S23) from (select expand(out("Resultado")) from Plantel where estatus="Activa" and nivel in ["superior"])',1)[0].sum

#advo
inicial_personal_advo = client.query('select sum(V216, V213, V210) from (select sum(V216) as V216, sum(V213) as V213, sum(V210) as V210 from (select expand(out("Resultado")) from Plantel where motivo = "" and nivel in ["inicial"] and subnivel in ["general"]))',1)[0].sum
preescolar_personal_advo = client.query('select sum(V803, V804, V805, V806, V483, V484) from (select sum(V803) as V803, sum(V804) as V804, sum(V805) as V805, sum(V806) as V806, sum(V483) as V483, sum(V484) as V484 from (select expand(out(Resultado)) from Plantel where motivo = "" and nivel = "preescolar" and subnivel = "general"))',1)[0].sum
primaria_personal_advo = client.query('select sum(V834, V835, V1278, V1279, V1280, V1281) from (select sum(V834) as V834, sum(V835) as V835, sum(V1278) as V1278, sum(V1279) as V1279, sum(V1280) as V1280, sum(V1281) as V1281 from (select expand(out(Resultado)) from Plantel where motivo = "" and nivel = "primaria" and subnivel = "general"))',1)[0].sum
secundaria_personal_advo = client.query('select sum(V974,V975,V976,V977,V621,V622) from (select sum(V609) as V609, sum(V610) as V610, sum(V974) as V974, sum(V975) as V975, sum(V976) as V976, sum(V977) as V977, sum(V622) as V622, sum(V621) as V621 from (select expand(out(Resultado)) from Plantel where motivo = "" and nivel = "secundaria"))',1)[0].sum
superior_personal_advo = client.query('select sum(S26, S26, S28, S31) from (select sum(S26) as S26, sum(S27) as S27, sum(S28) as S28, sum(S31) as S31 from (select expand(out("Resultado")) from Plantel where estatus="Activa" and nivel in ["superior"]))',1)[0].sum

#especial
inicial_personal_especial = client.query('select sum (V143, V159, V233, V258, V274, V203, V291) from (select sum(V143) as V143, sum(V159) as V159, sum(V233) as V233, sum(V258) as V258, sum(V274) as V274, sum(V203) as V203, sum(V291) as V291 from (select expand(out("Resultado")) from Plantel where motivo = "" and nivel in ["inicial"] and subnivel in ["general"]))',1)[0].sum
preescolar_personal_especial = client.query('select sum(V477, V478, V479, V480, V481, V482) from (select sum(V477) as V477, sum(V478) as V478, sum(V479) as V479, sum(V480) as V480, sum(V481) as V481, sum(V482) as V482 from (select expand(out(Resultado)) from Plantel where motivo = "" and nivel = "preescolar" and subnivel = "general"))',1)[0].sum
primaria_personal_especial = client.query('select sum(V826, V827, V828, V829, V830, V831, V832, V833) from (select sum(V833) as V833, sum(V832) as V832, sum(V831) as V831, sum(V830) as V830, sum(V829) as V829, sum(V828) as V828, sum(V827) as V827, sum(V826) as V826 from (select expand(out(Resultado)) from Plantel where motivo = "" and nivel = "primaria" and subnivel = "general"))',1)[0].sum
secundaria_personal_especial = client.query('select sum(V615,V616,V617,V618,V619,V620,V1026,V1027) from (select sum(V615) as V615, sum(V616) as V616, sum(V617) as V617, sum(V618) as V618, sum(V619) as V619, sum(V620) as V620, sum(V1026) as V1026, sum(V1027) as V1027 from (select expand(out(Resultado)) from Plantel where motivo = "" and nivel = "secundaria"))',1)[0].sum
superior_personal_especial = 0

preescolar_personal_total = preescolar_personal_docentes_inicial + preescolar_personal_general + preescolar_personal_comunitaria
inicial_personal_total = inicial_personal - preescolar_personal_docentes_inicial
table_data = [
    ['Nivel', 'Escuelas', 'Aulas Ex', 'Aulas Uso', 'Grupos', 'Alumnos_H', 'Alumnos_M', 'Alumnos', 'Docentes', 'Dir s/gpo', 'Advos', 'Especial', 'Personal'],
    ['Inicial', inicial_escuelas_total, inicial_aulas_existentes, inicial_aulas_uso, inicial_grupos_total, inicial_alumnos_hombres, inicial_alumnos_mujeres, inicial_alumnos_total, inicial_personal_docentes, inicial_personal_dir_s_gpo, inicial_personal_advo, inicial_personal_especial, inicial_personal_total],
    ['Preescolar', preescolar_escuelas_total, preescolar_aulas_existentes, preescolar_aulas_uso, preescolar_grupos_total, preescolar_alumnos_hombres, preescolar_alumnos_mujeres, preescolar_alumnos_total, preescolar_personal_docentes, preescolar_personal_dir_s_gpo, preescolar_personal_advo, preescolar_personal_especial, preescolar_personal_total],
    ['Primaria', primaria_escuelas_total, primaria_aulas_existentes, primaria_aulas_uso, primaria_grupos_total, primaria_alumnos_hombres, primaria_alumnos_mujeres, primaria_alumnos_total, primaria_personal_docentes, primaria_personal_dir_s_gpo, primaria_personal_advo, primaria_personal_especial, primaria_personal_total],
    ['Secundaria', secundaria_escuelas_total, secundaria_aulas_existentes, secundaria_aulas_uso, secundaria_grupos_total, secundaria_alumnos_hombres, secundaria_alumnos_mujeres, secundaria_alumnos_total, secundaria_personal_docentes, secundaria_personal_dir_s_gpo, secundaria_personal_advo, secundaria_personal_especial, secundaria_personal_total],
    #['Media', media_escuelas_total, media_aulas_existentes],
    ['Superior', superior_escuelas_total, superior_aulas_existentes, superior_aulas_uso, superior_grupos_total, superior_alumnos_hombres, superior_alumnos_mujeres, superior_alumnos_total, superior_personal_docentes, superior_personal_dir_s_gpo, superior_personal_advo, superior_personal_especial, superior_personal_total],
]
table = AsciiTable(table_data)
print table.table
