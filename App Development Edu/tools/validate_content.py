#!/usr/bin/env python3
"""Structural validator for the Mobile Mini Projects educational packages.

This validates content shape, paths, IDs, assessment relationships, manifests,
and ZIP integrity. It does not prove educational accuracy or run the apps.
"""
from __future__ import annotations
import json, re, sys, zipfile
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
PROJECTS=ROOT/'projects'
REPORTS=ROOT/'reports'
DIST=ROOT/'dist'
REQUIRED_ROOT={'manifest.json','project.json','README.md','prerequisites.md','setup-guide.md','architecture.md','glossary.md','references.json','modules','final-project'}

def read_json(path, errors):
    try: return json.loads(path.read_text(encoding='utf-8'))
    except Exception as exc:
        errors.append(f'Invalid JSON `{path.relative_to(ROOT)}`: {exc}')
        return None

def check_package(folder: Path):
    errors=[]; warnings=[]; passed=[]
    slug=folder.name
    for name in REQUIRED_ROOT:
        if not (folder/name).exists(): errors.append(f'Missing required path: {name}')
    pjson=read_json(folder/'project.json',errors) if (folder/'project.json').exists() else {}
    manifest=read_json(folder/'manifest.json',errors) if (folder/'manifest.json').exists() else {}
    if pjson and pjson.get('slug')!=slug: errors.append('project.json slug does not match folder name.')
    if pjson and not all(pjson.get(k) for k in ['title','description','problem','audience','stack','difficulty','prerequisites','learning_outcomes','estimated_duration_hours','content_schema_version']): errors.append('project.json has empty required educational fields.')
    if not pjson: pjson={}
    passed.append('Required package root files and project metadata checked.')
    modules_dir=folder/'modules'
    module_dirs=sorted((p for p in modules_dir.glob('module-*') if p.is_dir()),key=lambda x:x.name) if modules_dir.exists() else []
    if len(module_dirs)<6: errors.append(f'Only {len(module_dirs)} modules found; minimum is six.')
    module_ids=set(); lesson_ids=set(); question_ids=set(); exercise_ids=set(); module_prerequisites=[]
    lessons=questions=0
    expected={'manifest.json','project.json','README.md','prerequisites.md','setup-guide.md','architecture.md','glossary.md','references.json','modules','final-project'}
    for md in module_dirs:
        expected.add(f'modules/{md.name}')
        mpath=md/'module.json'; apath=md/'assessment.json'; kpath=md/'answer-key.json'
        for f in [mpath,apath,kpath]:
            if not f.is_file(): errors.append(f'Missing required module file: {f.relative_to(folder)}')
            else: expected.add(str(f.relative_to(folder)).replace('\\','/'))
        mod=read_json(mpath,errors) if mpath.exists() else {}
        assessment=read_json(apath,errors) if apath.exists() else {}
        key=read_json(kpath,errors) if kpath.exists() else {}
        if not mod: mod={}
        mid=mod.get('module_id')
        if not mid or mid in module_ids: errors.append(f'Missing or duplicate module ID in {md.name}: {mid}')
        module_ids.add(mid)
        module_prerequisites.extend((md.name,x) for x in mod.get('prerequisites',[]))
        for field in ['title','description','learning_objectives','learning_objective_ids','source_files','prerequisites','ordered_lesson_ids','estimated_duration_minutes','concepts','practical_outcomes','completion_criteria']:
            if field not in mod or (field!='prerequisites' and mod[field] in ('',[],None)): errors.append(f'{md.name}/module.json missing `{field}`')
        for source_file in mod.get('source_files',[]):
            if not (ROOT.parent/'projects'/slug/source_file).is_file(): errors.append(f'{md.name}/module.json has a missing source file `{source_file}`')
        lesson_dir=md/'lessons'; exercise_dir=md/'exercises'
        lesson_files=sorted(lesson_dir.glob('*.md')) if lesson_dir.exists() else []
        if not lesson_files: errors.append(f'{md.name} has no standalone lesson Markdown.')
        actual_ids=[]
        for lp in lesson_files:
            expected.add(str(lp.relative_to(folder)).replace('\\','/')); lessons+=1
            body=lp.read_text(encoding='utf-8')
            match=re.search(r'\*\*Lesson ID:\*\* `([^`]+)`',body)
            lid=match.group(1) if match else None
            if not lid or lid in lesson_ids: errors.append(f'Missing or duplicate lesson ID in {lp.relative_to(folder)}: {lid}')
            lesson_ids.add(lid); actual_ids.append(lid)
            if body.count('```')<2: errors.append(f'{lp.relative_to(folder)} lacks a source code example.')
            for heading in ['Purpose and learning objectives','Prerequisites','Progressive explanation','Practical exercise','Common mistakes and debugging','Best practices and security','Summary','Knowledge checks','References']:
                if f'## {heading}' not in body: errors.append(f'{lp.relative_to(folder)} lacks section `{heading}`')
            for rel in re.findall(r'\]\(([^)]+)\)',body):
                if rel.startswith(('http://','https://','#','mailto:')): continue
                target=(lp.parent/rel.split('#',1)[0]).resolve()
                if not target.exists(): errors.append(f'Broken lesson link in {lp.relative_to(folder)}: {rel}')
        expected_ids=mod.get('ordered_lesson_ids',[])
        if len(expected_ids)!=len(set(expected_ids)) or set(expected_ids)!=set(actual_ids): errors.append(f'{md.name} lesson IDs do not match module.json ordered_lesson_ids.')
        exfiles=sorted(exercise_dir.glob('*.json')) if exercise_dir.exists() else []
        if not exfiles: errors.append(f'{md.name} has no substantive exercise JSON.')
        for ep in exfiles:
            expected.add(str(ep.relative_to(folder)).replace('\\','/'))
            ex=read_json(ep,errors) or {}; eid=ex.get('exercise_id')
            if not eid or eid in exercise_ids: errors.append(f'Missing or duplicate exercise ID: {eid}')
            exercise_ids.add(eid)
            for field in ['objective','problem','requirements','constraints','expected_behavior','acceptance_criteria','hints','difficulty','estimated_time_minutes']:
                if not ex.get(field): errors.append(f'{ep.relative_to(folder)} missing exercise field `{field}`')
        if assessment:
            if assessment.get('module_id')!=mid: errors.append(f'{md.name} assessment module_id mismatch.')
            qs=assessment.get('questions',[]); questions+=len(qs)
            if len(qs)!=10: errors.append(f'{md.name} has {len(qs)} questions; expected exactly 10.')
            if len({q.get('text','').strip() for q in qs})!=len(qs): errors.append(f'{md.name} has duplicate question text.')
            if [q.get('difficulty') for q in qs].count('basic')!=3 or [q.get('difficulty') for q in qs].count('intermediate')!=5 or [q.get('difficulty') for q in qs].count('advanced')!=2: errors.append(f'{md.name} must use 3 basic, 5 intermediate, 2 advanced questions.')
            for q in qs:
                qid=q.get('question_id')
                if not qid or qid in question_ids: errors.append(f'Missing or duplicate question ID: {qid}')
                question_ids.add(qid)
                if q.get('lesson_id') not in lesson_ids and q.get('lesson_id') not in actual_ids: errors.append(f'{qid} references a missing lesson.')
                if q.get('learning_objective_id') not in mod.get('learning_objective_ids',[]):
                    errors.append(f'{qid} references a missing learning objective.')
                opts=q.get('options',[])
                if len(opts)!=4 or len({o.get('text') for o in opts})!=4 or len({o.get('option_id') for o in opts})!=4: errors.append(f'{qid} must have four distinct options with unique IDs.')
                for opt in opts:
                    if any(k in opt for k in ['is_correct','correct','answer','explanation']): errors.append(f'{qid} reveals answer data in student-facing assessment.')
        if key:
            if key.get('module_id')!=mid: errors.append(f'{md.name} answer key module_id mismatch.')
            ans=key.get('answers',[])
            if len(ans)!=10: errors.append(f'{md.name} answer key has {len(ans)} entries; expected 10.')
            qmap={q.get('question_id'):q for q in assessment.get('questions',[])} if assessment else {}
            amap={a.get('question_id'):a for a in ans}
            if set(qmap)!=set(amap): errors.append(f'{md.name} question and answer-key IDs do not match.')
            for qid,a in amap.items():
                q=qmap.get(qid,{})
                option_ids={o.get('option_id') for o in q.get('options',[])}
                if a.get('correct_option_id') not in option_ids: errors.append(f'{qid} answer key points to an invalid correct option.')
                wrong=a.get('incorrect_explanations',{})
                if set(wrong)!=option_ids-{a.get('correct_option_id')} or not a.get('correct_explanation') or any(not x.strip() for x in wrong.values()): errors.append(f'{qid} lacks a complete correct/incorrect explanation set.')
                if a.get('related_lesson_id') not in actual_ids or not a.get('tested_concept') or not a.get('supporting_reference'): errors.append(f'{qid} lacks lesson/concept/supporting reference.')
                elif not (kpath.parent/a['supporting_reference']).resolve().exists(): errors.append(f'{qid} has a broken supporting source reference: {a["supporting_reference"]}')
    for module_dir,prerequisite in module_prerequisites:
        if prerequisite not in module_ids: errors.append(f'{module_dir} references missing prerequisite module `{prerequisite}`')
    for required in ['final-project/requirements.md','final-project/evaluation-rubric.json','final-project/solution-guide.md']:
        if not (folder/required).is_file(): errors.append(f'Missing final-project deliverable `{required}`')
        else: expected.add(required)
    refs=read_json(folder/'references.json',errors) if (folder/'references.json').exists() else {}
    if refs:
        for source in refs.get('source_references',[]):
            if not (ROOT.parent/'projects'/slug/source.get('path','')).exists(): errors.append(f'Broken source reference: {source.get("path")}')
    # Check internal package links from every Markdown file.
    for mdfile in folder.rglob('*.md'):
        expected.add(str(mdfile.relative_to(folder)).replace('\\','/'))
        body=mdfile.read_text(encoding='utf-8')
        for rel in re.findall(r'\]\(([^)]+)\)',body):
            if rel.startswith(('http://','https://','#','mailto:')): continue
            target=(mdfile.parent/rel.split('#',1)[0]).resolve()
            if not target.exists(): errors.append(f'Broken package link in {mdfile.relative_to(folder)}: {rel}')
    if not (folder/'final-project/evaluation-rubric.json').exists(): pass
    else: read_json(folder/'final-project/evaluation-rubric.json',errors)
    for schema in (ROOT/'schemas').glob('*.json'): read_json(schema,errors)
    actual_files=sorted(str(p.relative_to(folder)).replace('\\','/') for p in folder.rglob('*') if p.is_file() and p.name!='manifest.json')
    expected_files=sorted(x for x in expected if (folder/x).is_file() and x!='manifest.json')
    unexpected=sorted(set(actual_files)-set(expected_files))
    missing_inventory=sorted(set(expected_files)-set(actual_files))
    if unexpected: errors.append('Unexpected files: '+', '.join(unexpected))
    if missing_inventory: errors.append('Required files missing from expected inventory: '+', '.join(missing_inventory))
    if manifest:
        if manifest.get('project_slug')!=slug: errors.append('Manifest slug mismatch.')
        for field in ['content_schema_version','package_version','generation_timestamp','included_files','validation_status']:
            if field not in manifest: errors.append(f'Manifest is missing `{field}`.')
        if manifest.get('module_count')!=len(module_dirs): errors.append('Manifest module count mismatch.')
        if manifest.get('lesson_count')!=lessons: errors.append('Manifest lesson count mismatch.')
        if manifest.get('question_count')!=questions: errors.append('Manifest question count mismatch.')
        if sorted(manifest.get('included_files',[]))!=expected_files: errors.append('Manifest included_files do not match package files (manifest excluded).')
        manifest['validation_status']='passed structural validation' if not errors else 'failed structural validation'
        (folder/'manifest.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    passed += ['JSON parsed; package-internal and source links checked.','Unique module, lesson, exercise, and question IDs checked.','Per-module lesson references, 10-question assessments, option sets, answer keys, and explanations checked.','Manifest counts and included_files checked.']
    if not errors: passed.append('Required file inventory is complete; no unlisted package files detected.')
    warnings += ['Structural validation does not establish instructional accuracy, compile apps, prove provider/API behavior, verify device behavior, or establish deployment.','Confirm framework/provider documentation versions and run platform-specific builds in the intended environment.']
    source_package=ROOT.parent/'projects'/slug/'package.json'
    if source_package.exists():
        try:
            source_deps=json.loads(source_package.read_text(encoding='utf-8')).get('dependencies',{})
            if source_deps.get('expo'): warnings.append(f'Source dependency review: Expo is pinned to `{source_deps.get("expo")}` and React Native to `{source_deps.get("react-native")}`; current official Expo references may describe a newer SDK, so learners must consult version-matched SDK documentation before changing dependencies.')
        except Exception: warnings.append('Source dependency review: package.json needs human inspection.')
    if slug=='bluewallet': warnings.append('BlueWallet has no key management or signing; Electrum broadcast intentionally refuses unsigned transactions. Never use real funds.')
    if slug=='covid-alert': warnings.append('Exposure checks and symptom scores are simulated/informational only; not medical or public-health advice.')
    if slug=='peyara-remote-mouse': warnings.append('Relay has no TLS/client authentication; keep on loopback or a trusted isolated lab. Real input is explicitly opt-in.')
    if slug=='rocket-chat-mobile': warnings.append('No server was connected during package generation; offline is the default and a compatible endpoint remains runtime review.')
    report=['# Validation report — '+slug,'',f'- Generated: {datetime.now(timezone.utc).isoformat()}',f'- Modules: {len(module_dirs)}; lessons: {lessons}; questions: {questions}',f'- Structural result: **{"PASS" if not errors else "FAIL"}**','','## Passed checks','']+[f'- {x}' for x in passed]+['','## Errors','']+([f'- {x}' for x in errors] or ['- None.'])+['','## Warnings and human/runtime review','']+[f'- {x}' for x in warnings]+['','## Source-specific findings','']
    # Derive findings from each lesson's cited source summary and module metadata.
    for md in module_dirs:
        obj=read_json(md/'module.json',[])
        if obj and obj.get('concepts'): report.append(f'- **{obj["title"]}:** '+('; '.join(obj['concepts'][-2:])))
    report += ['','## Runtime and deployment status','', 'No source application was executed or deployed by this validator. See the package README and the source project README for available local test commands; execute platform builds and authorized external-service checks separately.','']
    REPORTS.mkdir(parents=True,exist_ok=True); (REPORTS/f'{slug}.md').write_text('\n'.join(report),encoding='utf-8')
    return {'slug':slug,'modules':len(module_dirs),'lessons':lessons,'questions':questions,'errors':errors,'warnings':warnings}

def main():
    REPORTS.mkdir(parents=True,exist_ok=True); DIST.mkdir(parents=True,exist_ok=True)
    folders=sorted(p for p in PROJECTS.iterdir() if p.is_dir()) if PROJECTS.exists() else []
    results=[check_package(p) for p in folders]
    zips=[]
    for r in results:
        folder=PROJECTS/r['slug']; archive=DIST/f'{r["slug"]}.zip'
        with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED) as z:
            for p in folder.rglob('*'):
                if p.is_file(): z.write(p,Path(r['slug'])/p.relative_to(folder))
        with zipfile.ZipFile(archive) as z:
            bad=z.testzip()
            if bad: r['errors'].append(f'ZIP integrity failure at {bad}')
            if any(Path(name).parts[0]!=r['slug'] for name in z.namelist() if name): r['errors'].append('ZIP entries do not all have the project slug as their root.')
        zips.append(archive)
    total={'projects':len(results),'modules':sum(r['modules'] for r in results),'lessons':sum(r['lessons'] for r in results),'questions':sum(r['questions'] for r in results),'errors':sum(len(r['errors']) for r in results)}
    summary=['# Mobile educational package validation summary','',f'- Timestamp: {datetime.now(timezone.utc).isoformat()}',f'- Projects: {total["projects"]}; modules: {total["modules"]}; lessons: {total["lessons"]}; questions: {total["questions"]}',f'- Structural errors: {total["errors"]}',f'- ZIP archives verified: {len(zips)}','', '## Project results','']
    for r in results: summary.append(f'- **{r["slug"]}:** {r["modules"]} modules, {r["lessons"]} lessons, {r["questions"]} questions — {"PASS" if not r["errors"] else "FAIL"}')
    summary += ['', 'Structural checks do not establish educational accuracy or prove that apps, APIs, devices, providers, or infrastructure work. App execution and deployment were not performed by this validator.','']
    (REPORTS/'summary.md').write_text('\n'.join(summary),encoding='utf-8')
    print(json.dumps(total,indent=2))
    for r in results:
        if r['errors']: print(r['slug']+': '+ '; '.join(r['errors']))
    return 1 if total['errors'] else 0

if __name__=='__main__': sys.exit(main())
