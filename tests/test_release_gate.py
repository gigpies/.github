from pathlib import Path
import tempfile,subprocess,os,textwrap
workflow=(Path(__file__).resolve().parents[1]/'.github/workflows/source-release.yml').read_text()
script=textwrap.dedent(workflow.split('        run: |\n',1)[1])
with tempfile.TemporaryDirectory(prefix='gigpies-release-check-') as d:
 p=Path(d);gh=p/'gh';gh.write_text('''#!/usr/bin/python3
import os,sys,json
case=os.environ['CASE'];args=sys.argv[1:]
if case=='api-failure': sys.exit(1)
if args[:2]==['release','create']:
 open(os.environ['RECEIPT'],'w').write('draft')
 assert '--draft' in args and '--verify-tag' in args
elif '/git/ref/tags/' in args[1]:
 print(json.dumps({'object':{'type':'tag' if case=='annotated' else 'commit','sha':'a'*40}}))
elif '/git/tags/' in args[1]:
 print(json.dumps({'object':{'type':'commit','sha':'b'*40}}))
elif '/compare/' in args[1]:
 print('diverged' if case=='off-main' else 'ahead')
elif '/actions/workflows/ci.yml/runs?' in args[1]:
 print(0 if case=='no-ci' else 1)
else: raise Exception(args)
''');gh.chmod(0o755)
 for case in ['lightweight','annotated','invalid-tag','wrong-ref','off-main','no-ci','api-failure']:
  receipt=p/case
  env=dict(os.environ,PATH=str(p)+':'+os.environ['PATH'],GH_REPO='gigpies/example',GITHUB_REF='refs/heads/feature' if case=='wrong-ref' else 'refs/heads/main',RELEASE_TAG='bad;tag' if case=='invalid-tag' else 'v1.2.3',CASE=case,RECEIPT=str(receipt))
  r=subprocess.run(['bash','-c',script],env=env,text=True,capture_output=True)
  expected=case in ['lightweight','annotated']
  assert (r.returncode==0)==expected,(case,r.stdout,r.stderr)
  assert receipt.exists()==expected,case
  print(case,'PASS')
print('No GitHub releases or tags were created; all calls used a local fixture.')
