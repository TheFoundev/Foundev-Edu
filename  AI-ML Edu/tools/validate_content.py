#!/usr/bin/env python3
"""Structural validator for standalone AI/ML learning packages; cannot verify pedagogical truth."""
from __future__ import annotations
import json, re
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SOURCE=Path('/home/aziz/foundev/AIML-foundev-main/Artificial Intelligence & Machine Learning')
REQUIRED_PROJECT={'manifest.json','project.json','README.md','prerequisites.md','setup-guide.md','architecture.md','glossary.md','references.json','modules','final-project'}
REQUIRED_MODULE={'module.json','lessons','exercises','assessment.json','answer-key.json'}
ALLOWED_TOP=REQUIRED_PROJECT

def validate(p:Path):
    passed=[]; errors=[]; warnings=[]; review=[]
    def check(ok,msg): (passed if ok else errors).append(msg)
    check(p.is_dir(),f'Project directory exists: {p.name}')
    for n in sorted(REQUIRED_PROJECT): check((p/n).exists(),f'Required project content exists: {n}')
    for n in sorted(x.name for x in p.iterdir()): check(n in ALLOWED_TOP,f'No unexpected top-level item: {n}')
    def load(path):
        try: return json.loads(path.read_text(encoding='utf-8'))
        except Exception as e: errors.append(f'Invalid/unreadable JSON {path.relative_to(p)}: {e}'); return None
    pd=load(p/'project.json'); manifest=load(p/'manifest.json'); load(p/'references.json')
    if isinstance(pd,dict):
        for key in ('title','slug','description','problem_solved','target_audience','technology_stack','difficulty_level','prerequisites','learning_outcomes','estimated_completion_time','content_schema_version'):
            check(key in pd,f'project.json includes {key}')
        check(pd.get('slug')==p.name,'project slug matches directory')
    dirs=sorted((p/'modules').glob('module-*')) if (p/'modules').exists() else []
    check(6<=len(dirs)<=12,'module count is between 6 and 12')
    mids=set(); all_lids=set(); lesson_count=question_count=0; source_rows=[]
    expected_files=set()
    for md in dirs:
        for n in sorted(REQUIRED_MODULE): check((md/n).exists(),f'{md.name}: required item exists: {n}')
        m=load(md/'module.json'); a=load(md/'assessment.json'); k=load(md/'answer-key.json')
        if not isinstance(m,dict): continue
        mid=m.get('module_id'); check(bool(mid) and mid not in mids,f'{md.name}: unique module ID'); mids.add(mid)
        focus=m.get('source_code_focus',{})
        check(isinstance(focus,dict) and bool(focus.get('symbol_or_search_term')),f'{md.name}: source code focus is documented')
        if isinstance(focus,dict) and focus.get('excerpt_file'):
            check(focus['excerpt_file'] in m.get('source_files',[]),f'{md.name}: excerpt file is in the source file map')
        for sf in m.get('source_files',[]): check((SOURCE/p.name/sf).is_file(),f'{md.name}: source path exists: {sf}')
        source_rows.append({'module':m.get('title',''),'paths':m.get('source_files',[]),'symbol':focus.get('symbol_or_search_term') if isinstance(focus,dict) else '', 'excerpt_file':focus.get('excerpt_file') if isinstance(focus,dict) else None})
        declared=m.get('lesson_ids',[]); lf=sorted((md/'lessons').glob('*.md')); lessons={x.stem for x in lf}; lesson_count+=len(lf)
        check(set(declared)==lessons,f'{md.name}: declared lesson IDs match lesson files')
        check(len(declared)>=3,f'{md.name}: at least three lessons')
        for f in lf:
            lid=f.stem; check(lid not in all_lids,f'{md.name}: unique lesson ID {lid}'); all_lids.add(lid)
            body=f.read_text(errors='replace'); check(len(body)>1300,f'{md.name}/{lid}: substantive standalone lesson')
            for term in ('Purpose and learning objectives','Prerequisites','plain language','Step-by-step','Expected behavior','Practical exercise','Common mistakes','Best practices','Summary','Knowledge check','References'):
                check(term.lower() in body.lower(),f'{md.name}/{lid}: includes {term}')
            check(body.find('## The idea in plain language') < body.find('## Code-reading example'),f'{md.name}/{lid}: plain-language explanation precedes source-code teaching')
            if focus.get('excerpt_file'):
                check(f"Source excerpt from `{focus['excerpt_file']}`" in body,f'{md.name}/{lid}: excerpt matches declared source file')
                match=re.search(r'Source excerpt from `[^`]+`.*?```[a-zA-Z0-9_+-]*\n(.*?)\n```',body,re.S)
                normalize=lambda value:re.sub(r'[^a-z0-9]','',str(value).lower())
                excerpt=match.group(1) if match else ''
                check(normalize(focus.get('symbol_or_search_term','')) in normalize(excerpt),f'{md.name}/{lid}: declared source symbol is visible in excerpt')
        for sf in m.get('source_files',[]): check((SOURCE/p.name/sf).is_file(),f'{md.name}: source citation exists: {sf}')
        if isinstance(a,dict):
            qs=a.get('questions',[]); question_count+=len(qs)
            check(a.get('module_id')==mid,f'{md.name}: assessment module matches')
            check(len(qs)==10,f'{md.name}: exactly 10 MCQs')
            check([sum(q.get('difficulty_level')==lv for q in qs) for lv in ('basic','intermediate','advanced')]==[3,5,2],f'{md.name}: 3/5/2 difficulty distribution')
            qids=set(); optionids={}
            for q in qs:
                qid=q.get('question_id',''); check(bool(qid) and qid not in qids,f'{md.name}: unique question ID {qid}'); qids.add(qid)
                check(bool(q.get('question_text','').strip()),f'{md.name}/{qid}: question text present')
                check(q.get('related_lesson_id') in declared,f'{md.name}/{qid}: related lesson exists')
                check(q.get('related_learning_objective') in m.get('learning_objectives',[]),f'{md.name}/{qid}: learning objective exists')
                opts=q.get('options',[]); ids=[o.get('option_id') for o in opts]; texts=[o.get('text','').strip() for o in opts]
                check(len(opts)==4 and len(set(ids))==4 and len(set(texts))==4 and all(texts),f'{md.name}/{qid}: four distinct options and IDs'); optionids[qid]=set(ids)
                check(not any(set(o).intersection({'correct_option_id','is_correct','answer_key','correct_answer'}) for o in opts),f'{md.name}/{qid}: no answer indicator field in student assessment')
            if isinstance(k,dict):
                entries=k.get('answers',[]); keyed={}
                for row in entries: keyed.setdefault(row.get('question_id'),[]).append(row)
                check(set(keyed)==qids and all(len(v)==1 for v in keyed.values()),f'{md.name}: exactly one answer key per question')
                for qid,rows in keyed.items():
                    if len(rows)!=1: continue
                    row=rows[0]; correct=row.get('correct_option_id'); wrong=row.get('incorrect_option_explanations',{})
                    check(correct in optionids.get(qid,set()),f'{md.name}/{qid}: correct option exists')
                    check(len(row.get('explanation','').strip())>=35,f'{md.name}/{qid}: complete correct explanation')
                    check(set(wrong)==optionids.get(qid,set())-{correct} and all(len(str(x).strip())>=25 for x in wrong.values()),f'{md.name}/{qid}: all three distractors explained')
                    check(bool(row.get('concept_tested')) and row.get('related_lesson_id') in declared,f'{md.name}/{qid}: concept and lesson documented')
        ex=list((md/'exercises').glob('*.md')) if (md/'exercises').exists() else []
        check(bool(ex),f'{md.name}: practical exercises exist')
        for f in ex: check(len(f.read_text(errors='replace'))>500,f'{md.name}/{f.name}: exercise has requirements and acceptance details')
    check((p/'final-project/requirements.md').is_file() and (p/'final-project/solution-guide.md').is_file() and (p/'final-project/evaluation-rubric.json').is_file(),'final-project package complete')
    if isinstance(manifest,dict):
        check(manifest.get('project_slug')==p.name,'manifest slug matches project')
        check(manifest.get('module_count')==len(dirs),'manifest module count matches')
        check(manifest.get('lesson_count')==lesson_count,'manifest lesson count matches')
        check(manifest.get('assessment_question_count')==question_count,'manifest question count matches')
        included=set(manifest.get('included_files',[])); actual={x.relative_to(p).as_posix() for x in p.rglob('*') if x.is_file() and x.name!='manifest.json'}
        check(included==actual,'manifest file inventory matches package files')
        check('manifest.json' not in included,'manifest does not list itself')
        manifest['validation_status']='passed structural validation' if not errors else 'failed structural validation'
        (p/'manifest.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n')
    warnings.append('Structural checks cannot establish whether a technical statement, code explanation, quiz answer, reference target, privacy recommendation, or model claim is factually/educationally correct.')
    review.append('Human review required: compare every lesson and answer key with source code, especially documented source gaps and ethical/safety limits.')
    report={'project_slug':p.name,'generated_at':datetime.now(timezone.utc).isoformat(),'status':'passed' if not errors else 'failed','passed_count':len(passed),'error_count':len(errors),'warning_count':len(warnings),'review_count':len(review),'passed':passed,'errors':errors,'warnings':warnings,'human_review':review,'source_alignment':source_rows}
    return report

def main():
    reports=ROOT/'reports'; reports.mkdir(exist_ok=True); summary=[]
    for p in sorted((ROOT/'projects').iterdir()):
        if not p.is_dir(): continue
        r=validate(p); summary.append(r)
        (reports/f'{p.name}-validation.json').write_text(json.dumps(r,indent=2)+'\n')
        print(f"{p.name}: {r['status']} ({r['passed_count']} checks, {r['error_count']} errors)")
    total={'project_count':len(summary),'passed_projects':sum(x['status']=='passed' for x in summary),'failed_projects':sum(x['status']!='passed' for x in summary),'passed_checks':sum(x['passed_count'] for x in summary),'errors':sum(x['error_count'] for x in summary),'warnings':sum(x['warning_count'] for x in summary),'human_review_items':sum(x['review_count'] for x in summary),'projects':summary}
    (reports/'validation-summary.json').write_text(json.dumps(total,indent=2)+'\n')
    audit_lines=['# Module-to-source alignment audit','',f"Modules audited: {sum(len(x['source_alignment']) for x in summary)}",'','Each entry records the module’s declared source path(s) and source symbol/search cue. Lessons start with an accessible explanation, then cite and excerpt the implementation or documented boundary. The paths are checked for existence; this report does not claim that automated checks can prove semantic correctness. Review the listed excerpts against their module title before publication.','']
    for project_report in summary:
        audit_lines += [f"## {project_report['project_slug']}",'']
        for row in project_report['source_alignment']:
            cue=f"`{row['excerpt_file']}` → `{row['symbol']}`" if row['excerpt_file'] else f"Document/code boundary → `{row['symbol']}`"
            audit_lines.append(f"- **{row['module']}** — {cue}; mapped files: {', '.join('`'+x+'`' for x in row['paths'])}.")
        audit_lines.append('')
    (reports/'module-source-audit.md').write_text('\n'.join(audit_lines)+'\n')
    lines=['# AI/ML content validation report','',f"Projects: {total['project_count']} | Passed: {total['passed_projects']} | Failed: {total['failed_projects']} | Structural errors: {total['errors']}",'','## Results','']
    for r in summary:
        lines.append(f"- **{r['project_slug']}** — {r['status']}; {r['passed_count']} checks, {r['error_count']} errors. Human review: source alignment, technical correctness, and sensitive-use caveats.")
        lines.extend(f"  - ERROR: {e}" for e in r['errors'])
    lines+=['','## Human review limits','','The validator checks package structure, JSON, IDs, references, counts, answer-key shape, and source-path existence. It does not verify factual correctness, pedagogical adequacy, or external link availability. Read each package source-review notes and compare module claims and MCQs with the supplied implementation.']
    (reports/'validation-report.md').write_text('\n'.join(lines)+'\n')
    print(f"TOTAL: {total['passed_projects']}/{total['project_count']} passed; {total['errors']} errors; {total['passed_checks']} checks")
    if total['errors']: raise SystemExit(1)
if __name__=='__main__': main()
