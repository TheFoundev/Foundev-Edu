#!/usr/bin/env python3
"""Refine Data Science & Analytics learning packages against their source trees."""
from __future__ import annotations
import ast,json,re,os,shutil,zipfile
from pathlib import Path
from urllib.parse import quote
ROOT=Path(__file__).resolve().parents[1]
SOURCE_ROOTS=[ROOT.parent/'projects',ROOT.parent/'Projects-main',ROOT/'Data Science & Analytics',ROOT.parent/'Mini projects edu/Data Science & Analytics']
EDU=ROOT/'Data Science & Analytics edu'
GROUPS={
'automated-eda-tool':[[1],[2,3],[4,5],[6,7],[8,9],[10,11,12,13],[14,15,16,17],[18],[19],[20],[21]],
'rainfall-analysis-and-prediction':[[1,2],[3,4],[5,6],[7,8],[9,10],[11,12],[13],[14],[15,17],[16],[18]],
'social-media-sentiment-dashboard':[[1,2],[3,4],[5,6],[7,8],[9,10],[11],[12],[13],[14]],
}
GROUP_TITLES={
'automated-eda-tool':['API and Feature Selection','PCA Pipeline and Categorical Encoding','Scaling, Null Handling, and Outliers','Summary Statistics and Cleaning Runner','Application Shell and Authentication','Dashboard and Data Upload Flow','Reusable UI Components and Frontend Entry','Cleaning CLI and Batch Execution','Tests and Evidence Boundaries','Dependencies and Runtime Configuration','Documented Goals Compared with Implemented Code'],
'rainfall-analysis-and-prediction':['Model Base Classes and Package Structure','CemaNeige Snow and Temperature Components','CemaNeige-GR4J Coupling and Ice Variants','Hysteresis Variants and State','GR4J and HBV Runoff Models','Ice Melt and Model Initialization','Monte Carlo and Array Utilities','Metrics and Plotting','Environment and Test Configuration','Model Test Suite','Package Documentation and Source Limits'],
'social-media-sentiment-dashboard':['Application Entry and Account Model','Analytics Metrics and Sentiment/Trend','Dashboard Configuration and Data Manager','Discord and Facebook Fetchers','Instagram and Medium Fetchers','Reddit and TikTok Fetchers','Twitter and YouTube Fetchers','Scheduler, Utilities, and Tests','Dependencies and Project Documentation'],
}
EXTRA_SOURCE={'rainfall-analysis-and-prediction':{10:['rrmpg/__init__.py','rrmpg/models/basemodel.py','README.rst']},'social-media-sentiment-dashboard':{9:['src/main.py','src/analytics/sentiment_analysis.py','README.md']}}
CODE_EXT={'.py','.pyi','.js','.jsx','.ts','.tsx','.java','.sql','.sh','.go','.yaml','.yml','.toml','.json','.rst','.md'}
IMPLEMENTATION_EXT={'.py','.pyi','.js','.jsx','.ts','.tsx','.java','.sql','.sh','.go','.yaml','.yml','.tf','.scala','.r','.json','.xml','.toml'}
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def dump(p,x):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def write(p,s):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(s.rstrip()+'\n',encoding='utf-8')
def unique(seq):return list(dict.fromkeys(seq))
def source_root_for(slug):
 for base in SOURCE_ROOTS:
  p=base/slug
  if p.is_dir() and any(x.is_file() and x.suffix.lower() in IMPLEMENTATION_EXT and '__pycache__' not in x.parts and 'node_modules' not in x.parts for x in p.rglob('*')):return base
 return None

def source_focus(source_root,slug,files,title,descriptions,prefer_test=False):
 project=source_root/slug
 symbols=[]
 for desc in descriptions:
  m=re.search(r'prominent declared symbols visible in the inspected excerpt include\s+(.+?);',desc,re.I)
  if m:symbols.extend(re.findall(r'[A-Za-z_$][A-Za-z0-9_$]*',m.group(1)))
 symbols=unique(symbols)
 candidates=[]
 for rel in files:
  f=project/rel
  if not f.is_file() or f.suffix.lower() not in IMPLEMENTATION_EXT:continue
  try:lines=f.read_text(encoding='utf-8-sig',errors='replace').splitlines()
  except:continue
  test=bool(re.search(r'(^|/)(tests?|test)(/|$)|test[_-]|[_-]test\.',rel,re.I))
  if prefer_test and not test:continue
  if not prefer_test and test and any(not re.search(r'(^|/)(tests?|test)(/|$)|test[_-]|[_-]test\.',x,re.I) for x in files if (project/x).is_file()):continue
  funcs=[]
  if f.suffix=='.py':
   try:
    tree=ast.parse('\n'.join(lines));funcs=[n for n in ast.walk(tree) if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef,ast.ClassDef))]
   except:pass
  else:
   for i,line in enumerate(lines):
    m=re.search(r'\b(?:function|class|def)\s+([A-Za-z_$][\w$]*)',line)
    if m:funcs.append((m.group(1),i))
  found=next((s for s in symbols if re.search(r'(?<![\w])'+re.escape(s)+r'(?![\w])','\n'.join(lines))),None)
  if not found:
   if funcs:
    if f.suffix=='.py':
     toks=set(re.findall(r'[a-z0-9]{3,}',title.lower()))
     funcs.sort(key=lambda n:sum(t in n.name.lower() for t in toks),reverse=True)
     found=funcs[0].name
    else:found=funcs[0][0]
   else:
    found=next((tok for tok in re.findall(r'[A-Za-z_$][A-Za-z0-9_$]{2,}',title+' '+' '.join(descriptions)) if tok.lower() in '\n'.join(lines).lower()),None)
  if not found:continue
  i=next((i for i,l in enumerate(lines) if re.search(r'(?<![\w])'+re.escape(found)+r'(?![\w])',l)),0)
  if f.suffix=='.py':
   node=next((n for n in funcs if n.name==found),None)
   if node:i=node.lineno-1
  start=max(0,i-3);end=min(len(lines),i+18);code='\n'.join(lines[start:end]).strip()
  if code:candidates.append((0 if test==prefer_test else 1, bool(found in symbols), len(found), rel, found, start+1,end,code,f.suffix.lstrip('.') or 'text'))
 if not candidates:
  # Fall back to a mapped code file and derive a cue from its first declaration.
  for rel in files:
   f=project/rel
   if f.is_file() and f.suffix.lower() in CODE_EXT:
    lines=f.read_text(encoding='utf-8-sig',errors='replace').splitlines();code='\n'.join(lines[:18])
    return {'file':rel,'cue':Path(rel).stem,'start':1,'end':min(18,len(lines)),'code':code,'lang':f.suffix.lstrip('.') or 'text'}
  raise FileNotFoundError(f'No readable source file for {slug}: {files}')
 candidates.sort(reverse=True)
 _,_,_,rel,cue,start,end,code,lang=candidates[0]
 return {'file':rel,'cue':cue,'start':start,'end':end,'code':code[:2200],'lang':lang}
def lesson(slug,title,module,lesson_id,stage,focus,plain,fact,exercise,source_root=None):
 source_url=quote(os.path.relpath(source_root/slug/focus['file'],EDU/'projects'/slug/'modules'/module['module_id']/'lessons').replace('\\','/'),safe='/._-') if source_root else None
 source_list=', '.join('`'+x+'`' for x in module['source_files'])
 steps=[
  [f'Explain {module["title"]} without code first.',f'Find the input or record shape in {source_list}.',f'Predict what output the next step needs.'],
  [f'Open `{focus["file"]}` and find `{focus["cue"]}`.', 'Trace arguments/input, branches, transformations, and returned or stored values.', 'Follow one caller or consumer into the next mapped file.'],
  [f'Choose an empty, malformed, boundary, or missing-resource case for `{focus["cue"]}`.', 'Compare the expected behavior with the test or error path in the mapped sources.', 'Record what evidence a test would provide and what it would not prove.']
 ][stage-1]
 everyday=[f"In plain language, {plain} Think of this as a small set of stages that turns a known input into a useful result.",f"In plain language, {plain} Follow one example through input, transformation, and output before considering edge cases.",f"In plain language, {plain} A method is trustworthy only within the inputs and checks its source actually covers."][stage-1]
 return f'''# {module['title']}: {['Start with the idea','Read the implementation','Test a boundary'][stage-1]}

**Lesson ID:** `{lesson_id}`  
**Module ID:** `{module['module_id']}`  
**Source focus:** `{focus['file']}` → `{focus['cue']}`

## Purpose and learning objectives

This lesson develops the module outcome: {module['learning_objectives'][stage-1]['text']}

## Prerequisites

{('Complete the previous lesson in this module. ' if stage>1 else 'Basic Python and command-line navigation. ')}Read the source file map: {source_list}.

## Beginner explanation

{everyday}

## Step-by-step source reading

{chr(10).join(f'{i}. {x}' for i,x in enumerate(steps,1))}

## Source evidence

The source finding for this lesson is: {fact}

**Source:** {f'[`{focus["file"]}`]({source_url})' if source_url else f'`{focus["file"]}` (captured from an earlier generated source excerpt; the source tree is absent from this workspace)'} at lines {f'{focus["start"]}–{focus["end"]}' if focus.get('start') else 'captured excerpt'}; not executed during refinement.

{chr(10).join(f'### {sf}\n\n'+('This is the source excerpt for the module focus.' if sf==focus['file'] else 'This related source path supports the combined module; follow its caller or consumer.') for sf in module['source_files'])}

```{focus['lang']}
{focus['code']}
```

Read surrounding code before making claims about callers, runtime, or external services.

## Expected behavior and limits

{fact} Use only the datasets and paths named by the source. Synthetic examples do not establish performance on real or sensitive data.

## Practical exercise

Complete [`{exercise}`](../exercises/{exercise}). Trace the focus cue, add one edge case, and record an expected output and safe check.

## Common mistakes and debugging

- Assuming an imported package or declared function is used on the execution path without following its caller.
- Confusing synthetic data, mocks, or small tests with field performance.
- Reporting a metric without checking labels, data split, and metric definition.
- Compare the source excerpt with the complete function and tests before editing.

## Best practices and security

Use representative but non-sensitive data; keep credentials out of code; make split strategy and metric assumptions explicit; do not present synthetic benchmark outputs as operational guarantees.

## Summary

You began with a plain-language model, followed `{focus['cue']}` in `{focus['file']}`, and identified an edge or verification boundary.

## Knowledge checks

1. What does this stage do in everyday terms?
2. What input and output does `{focus['cue']}` connect?
3. What edge case or evaluation limit should be checked?

## References

- [Package README](../../../README.md)
{f'- [Source file]({source_url})' if source_url else '- Check source-review.md: original source files are not present in this workspace.'}
'''

def archived_excerpt_focus(slug,source_files,old_texts):
    pattern=re.compile(r'^###\s+([^\n]+)\s*\n\s*```([A-Za-z0-9_+.-]*)\s*\n(.*?)\n```',re.M|re.S)
    for body in old_texts:
        for match in pattern.finditer(body):
            rel=match.group(1).strip()
            if rel in source_files:
                code=match.group(3).strip()
                cue_match=re.search(r'(?:def|function|class|export function|export const)\s+([A-Za-z_$][\w$]*)',code)
                cue=cue_match.group(1) if cue_match else Path(rel).stem
                return {'file':rel,'cue':cue,'start':None,'end':None,'code':code[:2200],'lang':match.group(2) or 'text','source_status':'source tree absent; excerpt retained from earlier package'}
    return None

def choose_source_for_group(slug,group,oldmods,group_title,source_files,source_root,old_texts):
 descs=[m.get('description','') for m in oldmods]
 is_test='test' in group_title.lower() or any('test' in Path(x).name.lower() for x in source_files)
 if source_root:
  return source_focus(source_root,slug,source_files,group_title,descs,prefer_test=is_test)
 archived=archived_excerpt_focus(slug,source_files,old_texts)
 if archived:return archived
 raise FileNotFoundError(f'No source tree or retained excerpt for {slug} {group_title}')

def select_questions(group, old_dirs, new_module_id):
 candidates={d:[] for d in ('basic','intermediate','advanced')}
 answer_lookup={}
 for md in old_dirs:
  ap=md/'assessment.json';kp=md/'answer-key.json'
  if not ap.exists() or not kp.exists():continue
  assessment=load(ap);key=load(kp); amap={a['question_id']:a for a in key.get('answers',[])}
  for q in assessment.get('questions',[]):
   diff=q.get('difficulty','intermediate')
   if diff not in candidates:diff='intermediate'
   if q['question_id'] in amap:candidates[diff].append((q,amap[q['question_id']]))
 quota={'basic':3,'intermediate':5,'advanced':2}; selected=[]
 for diff,count in quota.items():
  pool=candidates[diff]
  unique_text=[]
  for pair in pool:
   if pair[0].get('text') not in {x[0].get('text') for x in unique_text}:unique_text.append(pair)
  selected.extend(unique_text[:count])
 # Fill rare shortages using remaining distinct questions; set the target mix with lesson progression.
 while len(selected)<10:
  remaining=[pair for bucket in candidates.values() for pair in bucket if pair not in selected]
  if not remaining:break
  selected.append(remaining[0])
 questions=[];answers=[]
 for i,(oldq,olda) in enumerate(selected[:10],1):
  qid=f'{new_module_id}-q{i:02d}';stage=1 if i<=3 else 2 if i<=8 else 3
  options=oldq.get('options',[]);idmap={o.get('option_id'):f'{qid}-o{j}' for j,o in enumerate(options,1)}
  newq=dict(oldq);newq['question_id']=qid;newq['options']=[{**o,'option_id':idmap[o.get('option_id')]} for o in options]
  newq['lesson_id']=f'{new_module_id}-lesson-{stage:02d}'
  newq['learning_objective_id']=f'{new_module_id}-objective-{stage}'
  newq['difficulty']='basic' if i<=3 else 'intermediate' if i<=8 else 'advanced'
  if 'related_lesson_id' in newq:newq['related_lesson_id']=newq['lesson_id']
  questions.append(newq)
  ans=dict(olda);ans['question_id']=qid;ans['correct_option_id']=idmap.get(olda.get('correct_option_id'),f'{qid}-o1')
  ans['related_lesson_id']=newq['lesson_id'];ans['tested_concept']=olda.get('tested_concept',new_module_id)
  old_wrong=olda.get('incorrect_explanations',[])
  ans['incorrect_explanations']=[{**w,'option_id':idmap.get(w.get('option_id'),w.get('option_id'))} for w in old_wrong]
  answers.append(ans)
 return {'module_id':new_module_id,'title':'','instructions':'Choose one best answer; use this module’s source evidence and lessons.','questions':questions}, {'module_id':new_module_id,'answers':answers}

def make_groups(slug,module_count):
 if slug in GROUPS:return GROUPS[slug]
 return [[i] for i in range(1,module_count+1)]
def merged_title(slug,group,oldmods,newidx):
 if slug in GROUP_TITLES:return GROUP_TITLES[slug][newidx-1]
 if len(oldmods)==1:return oldmods[0].get('title',f'Module {newidx}')
 return ' and '.join(m.get('title','Source Module') for m in oldmods)

def refine_ds_package(package):
 slug=package.name; old_dirs=sorted((package/'modules').glob('module-*'),key=lambda x:int(re.search(r'(\d+)$',x.name).group(1)))
 source_root=source_root_for(slug)
 old_mods=[load(d/'module.json') for d in old_dirs]; old_assess=[load(d/'assessment.json') for d in old_dirs]; old_keys=[load(d/'answer-key.json') for d in old_dirs]
 groups=make_groups(slug,len(old_dirs)); snapshots={i+1:(old_dirs[i],old_mods[i],old_assess[i],old_keys[i]) for i in range(len(old_dirs))}
 # Snapshot original lesson text and source excerpts before removing generated module folders.
 old_lesson_text={i+1:[f.read_text(encoding='utf-8',errors='replace') for f in sorted(old_dirs[i].joinpath('lessons').glob('*.md'))] for i in range(len(old_dirs))}
 new_modules=[]
 shutil.rmtree(package/'modules',ignore_errors=True)
 for mi,group in enumerate(groups,1):
  selected=[snapshots[i] for i in group]
  group_mods=[x[1] for x in selected]; title=merged_title(slug,group,group_mods,mi)
  source_files=unique([s for m in group_mods for s in m.get('source_files',[])])
  if slug in EXTRA_SOURCE and mi in EXTRA_SOURCE[slug]:source_files=unique(source_files+EXTRA_SOURCE[slug][mi])
  concepts=unique([c for m in group_mods for c in m.get('concepts',[])])
  description=' '.join(m.get('description','') for m in group_mods)
  group_old_texts=[t for i in group for t in old_lesson_text[i]]
  focus=choose_source_for_group(slug,group,group_mods,title,source_files,source_root,group_old_texts)
  if not focus:raise RuntimeError(f'No source focus for {slug} {title}')
  new_id=f'{slug}-module-{mi:02d}'; lesson_ids=[f'{new_id}-lesson-{j:02d}' for j in range(1,4)]
  objective_text=[f'Explain {title.lower()} in plain language using the project source.',f'Trace `{focus["cue"]}` in `{focus["file"]}` and explain its inputs, behavior, and output.',f'Use a test or boundary case to assess what the implementation proves and what remains unverified.']
  objective_ids=[f'{new_id}-objective-{j}' for j in range(1,4)]
  module={'module_id':new_id,'title':title,'description':f'Begins with an everyday explanation, then traces {focus["cue"]} in {focus["file"]}. Source units combined: '+', '.join(m.get('title','') for m in group_mods)+'.','learning_objectives':[{'objective_id':oid,'text':txt} for oid,txt in zip(objective_ids,objective_text)],'learning_objective_ids':objective_ids,'source_files':source_files,'source_code_focus':{'excerpt_file':focus['file'],'symbol_or_search_term':focus['cue'],'line_start':focus.get('start'),'line_end':focus.get('end'),'source_status':focus.get('source_status','verified source file exists')},'prerequisites':[f'{slug}-module-{mi-1:02d}'] if mi>1 else [],'ordered_lesson_ids':lesson_ids,'estimated_duration_minutes':160,'concepts':concepts+[f'source focus: {focus["cue"]}'], 'practical_outcomes':[f'Trace `{focus["cue"]}` through `{focus["file"]}`.','Explain one data or control boundary.'],'completion_criteria':['Complete all three lessons and the source exercise.','Answer ten module questions using lesson evidence.','Distinguish actual code behavior from assumptions and proposed extensions.']}
  # Select one concrete source finding from the old modules, then add the real focus cue.
  findings=[]
  for old in group_mods:
   findings.extend([x for x in old.get('concepts',[]) if isinstance(x,str) and x.strip()])
  finding='; '.join(findings[:4]) or description
  # Three progressive, independently readable lessons.
  for stage,lid in enumerate(lesson_ids,1):
   plain={'automated-eda-tool':'An EDA tool is a workbench that helps inspect and prepare a table before analysis.','rainfall-analysis-and-prediction':'A rainfall-runoff model is a bucket system: rain enters, stores fill or drain, and the model estimates flow.','social-media-sentiment-dashboard':'A social analytics pipeline collects posts, organizes them, scores text, then summarizes trends.'}.get(slug,f'In plain language, {title.lower()} is one stage in turning source data into a result.')
   finding_context=finding
   lesson_body=f'''# {title}: {['Begin with the concept','Trace the code','Test the boundary'][stage-1]}

**Lesson ID:** `{lid}`  
**Module ID:** `{new_id}`  
**Source focus:** `{focus['file']}` → `{focus['cue']}`

## Purpose and learning objectives

{objective_text[stage-1]}

## Prerequisites

{('Complete the earlier lesson in this module first. ' if stage>1 else 'Basic Python and source-file navigation. ')}This module covers: {', '.join(m.get('title','') for m in group_mods)}.

## Beginner explanation

{plain} This is a mental model, not a claim that every named source component uses a production-grade implementation.

## Step-by-step source reading

1. Open `{focus['file']}` and locate `{focus['cue']}`.
2. Identify its input and returned, stored, displayed, or emitted output.
3. Follow one caller/test into a related source path: {', '.join('`'+s+'`' for s in source_files[:5])}.
4. Compare that path with the source README, test fixtures, and documented limitations.

## Source evidence

The selected source finding is: {finding_context}

**Excerpt:** `{focus['file']}`{f' at lines {focus["start"]}–{focus["end"]}' if focus.get('start') else ''}. {focus.get('source_status','Source code was not executed during refinement.')}

{chr(10).join(f'### {sf}\n\n'+('The excerpt below is the selected implementation focus.' if sf==focus['file'] else 'This mapped path is part of the module scope; inspect it alongside its callers and tests.') for sf in source_files)}

```{focus['lang']}
{focus['code']}
```

{('First read the signature/declared data shape; then follow the code and caller.' if stage==1 else 'Trace branches and transformations. Do not infer runtime success from a declaration alone.' if stage==2 else 'Use the test or boundary to separate checked behavior from real-world performance, deployment, or provider claims.')}

## Expected behavior and limits

{finding_context} The repository’s README notes and tests are part of the scope; no application execution is claimed by this package.

## Practical exercise

Complete [`exercise-{mi:02d}.md`](../exercises/exercise-{mi:02d}.md). Cite the focus symbol and source path, record an expected result, and describe one edge case.

## Common mistakes and debugging

- Confusing the repository’s title or project brief with the implementation that is present.
- Treating a test definition as evidence that the test passed.
- Ignoring sample-data, small-dataset, synthetic-input, or runtime limitations.
- Follow the focus symbol through its caller before drawing conclusions.

## Best practices and security

Use non-sensitive test data, protect credentials, document split and metric assumptions, and do not present synthetic results as production performance. For hiring, public policy, finance, health, or personal data, require qualified human review.

## Summary

You moved from a plain-language model to `{focus['cue']}` in the source and identified one verification boundary.

## Knowledge checks

1. What input does this stage receive?
2. What does `{focus['cue']}` change, return, or measure?
3. What limitation would you report before using the result outside this sample?

## References

- [Package README](../../../README.md)
- Source project files listed in module.json (relative to the Data Science & Analytics source tree).
'''
   write(package/'modules'/f'module-{mi:02d}'/'lessons'/f'lesson-{stage:02d}.md',lesson_body)
  exercise=f'''# Exercise: {title}\n\n**Exercise ID:** `exercise-{mi:02d}`\n**Objective:** Trace `{focus['cue']}` in `{focus['file']}`.\n**Difficulty:** Intermediate\n**Estimated time:** 45 minutes\n\n## Problem\nExplain the source behavior in this module and show how one representative input reaches the output.\n\n## Requirements\n- Cite the selected source focus and a related caller/test.\n- Record inputs, transformations, output, and one boundary case.\n- Separate source evidence from README claims and proposed features.\n\n## Constraints\nUse synthetic or public permitted data only. Do not claim code ran unless you actually ran it.\n\n## Expected behavior and acceptance criteria\n- Explanation matches cited source.\n- One normal path and one failure/edge case are described.\n- Limitations and human-review needs are stated where relevant.\n\n## Hints\nRead the function signature first, then search callers and tests.\n'''
  write(package/'modules'/f'module-{mi:02d}'/'exercises'/f'exercise-{mi:02d}.md',exercise)
  # Rebuild the module bank from original source-grounded questions, balancing the level mix.
  assessment_pairs=[]
  for olddir,oldmod,oldass,oldkey in selected:
   answers={a.get('question_id'):a for a in oldkey.get('answers',[])}
   for q in oldass.get('questions',[]):
    if q.get('question_id') in answers:assessment_pairs.append((q,answers[q['question_id']]))
  target_mix={'basic':3,'intermediate':5,'advanced':2}; chosen=[]; used_text=set()
  for level,need in target_mix.items():
   pool=[pair for pair in assessment_pairs if pair[0].get('difficulty')==level]
   while need:
    pair=next((x for x in pool if x[0].get('text') not in used_text),None)
    if pair is None:break
    chosen.append(pair);used_text.add(pair[0].get('text'));pool.remove(pair);need-=1
  if len(chosen)<10:
   for pair in assessment_pairs:
    if pair[0].get('text') not in used_text:
     chosen.append(pair);used_text.add(pair[0].get('text'))
     if len(chosen)==10:break
  if len(chosen)<10:raise RuntimeError(f'Not enough unique assessment questions for {slug}/{new_id}')
  qlist=[];alist=[]
  for qi,(oldq,olda) in enumerate(chosen[:10],1):
   qid=f'{new_id}-q{qi:02d}';stage=1 if qi<=3 else 2 if qi<=8 else 3
   oldopts=oldq.get('options',[]);idmap={o.get('option_id'):f'{qid}-o{oi}' for oi,o in enumerate(oldopts,1)}
   q=dict(oldq);q['question_id']=qid;q['options']=[{**o,'option_id':idmap.get(o.get('option_id'),f'{qid}-o{oi}')} for oi,o in enumerate(oldopts,1)];q['lesson_id']=lesson_ids[stage-1];q['related_lesson_id']=lesson_ids[stage-1];q['learning_objective_id']=objective_ids[stage-1];q['difficulty']='basic' if qi<=3 else 'intermediate' if qi<=8 else 'advanced'
   qlist.append(q)
   a=dict(olda);a['question_id']=qid;a['correct_option_id']=idmap.get(olda.get('correct_option_id'),f'{qid}-o1');a['related_lesson_id']=lesson_ids[stage-1];a['tested_concept']=a.get('tested_concept',title);a['supporting_reference']=focus['file']
   a['incorrect_option_explanations']=[{**e,'option_id':idmap.get(e.get('option_id'),e.get('option_id'))} for e in olda.get('incorrect_option_explanations',olda.get('incorrect_explanations',[]))]
   a['correct_explanation']=a.get('correct_explanation','')+f" Source focus for this module: {focus['cue']} in {focus['file']}."
   alist.append(a)
  write(package/'modules'/f'module-{mi:02d}'/'assessment.json',json.dumps({'module_id':new_id,'title':title,'instructions':'Choose one best answer. The questions address this module; read its three lessons.','questions':qlist},indent=2,ensure_ascii=False))
  write(package/'modules'/f'module-{mi:02d}'/'answer-key.json',json.dumps({'module_id':new_id,'answers':alist},indent=2,ensure_ascii=False))
  dump(package/'modules'/f'module-{mi:02d}'/'module.json',module)
  new_modules.append(module)
 # Replace modules as one complete set.
 for d in list((package/'modules').glob('module-*')):
  if d.is_dir() and not d.name.startswith('module-'):continue
  if d.is_dir() and not (d/'module.json').exists():shutil.rmtree(d)
 # remove old module dirs not in new contiguous set
 for d in (package/'modules').glob('module-*'):
  try:n=int(d.name.split('-')[-1])
  except:continue
  if n>len(groups):shutil.rmtree(d)
 manifest=load(package/'manifest.json')
 manifest['module_count']=len(groups);manifest['lesson_count']=len(groups)*3;manifest['question_count']=len(groups)*10;manifest['counts']={'modules':len(groups),'lessons':len(groups)*3,'questions':len(groups)*10}
 manifest['included_files']=sorted(f.relative_to(package).as_posix() for f in package.rglob('*') if f.is_file() and f.name!='manifest.json')
 manifest['validation_status']='pending refined structural validation'
 dump(package/'manifest.json',manifest)

if __name__=='__main__':
    from copy import deepcopy
    for package in sorted((EDU/'projects').iterdir()):
        if package.is_dir():refine_ds_package(package)
    print('Refined Data Science packages')
