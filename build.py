# Builds job-boards.html (artifact) and index.html (GitHub Pages) from template + data.
import json,os,sys
here=os.path.dirname(os.path.abspath(__file__))
tpl,data_path=sys.argv[1],sys.argv[2]
d=json.load(open(data_path))
soon=[{k:v for k,v in o.items() if k!='launchDate'} for o in d['soon']]
jt={"jobBoard":"Jobtoday","countries":"ES, GB","description":"Leading job board for frontline and hourly hiring in hospitality, retail and logistics.","industry":"Yes – Frontline / Hourly"}
new=[o['jobBoard'] for o in soon]+['Jobtoday']
data={'organic':soon+[jt]+d['organic'],'market':d['market']}
t=open(tpl).read().replace('__DATA__',json.dumps(data,ensure_ascii=False)).replace('__NEW__',json.dumps(new))
open(here+'/job-boards.html','w').write(t)
head='<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n<meta name="robots" content="noindex, nofollow">\n<meta name="color-scheme" content="light dark">\n<style>body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>\n'
i=t.find('<div class="hero">')
open(here+'/index.html','w').write(head+t[:i]+'</head>\n<body>\n'+t[i:]+'\n</body>\n</html>\n')
