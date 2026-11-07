#!/usr/bin/env python3
"""Bring App Development Edu modules to three progressive, source-linked lessons."""
from __future__ import annotations
import json,re,os
from pathlib import Path
from urllib.parse import quote
ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT.parent/'App Development'
PACKAGES=ROOT/'projects'

def focus_from(body,files):
 m=re.search(r'\*\*Source focus:\*\*\s*`([^`]+)`\s*[—-]\s*`([^`]+)`',body)
 return (m.group(1),m.group(2)) if m else (files[0],Path(files[0]).stem)
def excerpt_from(slug,file,cue,body):
 pat=re.compile(r'^###\s+([^\n]+)\s*\n\s*```([A-Za-z0-9_+.-]*)\s*\n(.*?)\n```',re.M|re.S)
 blocks=[(m.group(1).strip(),m.group(2).strip() or 'text',m.group(3)) for m in pat.finditer(body)]
 block=next((x for x in blocks if x[0]==file),None)
 path=SOURCE/slug/file
 if path.is_file():
  lines=path.read_text(encoding='utf-8-sig',errors='replace').splitlines()
  hit=next((i for i,l in enumerate(lines) if cue.lower() in l.lower()),None)
  if hit is not None:
   start=max(0,hit-4);return file,path.suffix.lstrip('.') or 'text','\n'.join(lines[start: min(len(lines),hit+20)])[:2600]
 if block:
  lines=block[2].splitlines();hit=next((i for i,l in enumerate(lines) if cue.lower() in l.lower()),0);return file,block[1],'\n'.join(lines[max(0,hit-4):hit+20])[:2600]
 return file,'text','Source excerpt unavailable; inspect this source path and locate the focus symbol before teaching this module.'
def src_url(slug,file,from_dir):
 return quote(os.path.relpath(SOURCE/slug/file,from_dir).replace('\\','/'),safe='/._-')
def lesson_md(slug,title,module,stage,lid,focus,code,exercise):
 file,cue=focus;codefile,lang,body=code;link=src_url(slug,codefile,ROOT/'projects'/slug/'modules'/module['module_id']/'lessons')
 desc=module.get('description','')
 intro=[
  f"Imagine **{title}** as a small part of a phone app: it receives a value or action and helps produce a result. This module’s plain-language model is: {desc}",
  f"In everyday terms, the code path behind **{title}** is like following one item through a workshop: locate the input, see what changes, then find the output. {desc}",
  f"A feature is only reliable within the cases it handles. In plain terms, **{title}** means: {desc} Today we trace one normal path and one boundary."
 ][stage-1]
 walkthrough=[
  'Before reading the excerpt, name the input, the result the user expects, and one assumption the app makes.',
  f"Open `{file}` and locate `{cue}`. Read the signature, guards, transformation, and return/state update in that order.",
  f"Use `{file}` at `{cue}` to inspect a failure or edge case. Follow its caller and test rather than inferring behavior from the screen."
 ][stage-1]
 return f'''# {title}: {['Begin with the idea','Trace the source','Check behavior and limits'][stage-1]}

**Lesson ID:** `{lid}`  
**Module ID:** `{module['module_id']}`  
**Source focus:** `{file}` → `{cue}`

## Purpose and learning objectives

{walkthrough} By the end, explain the behavior and identify what the source does not establish.

## Prerequisites

{('Complete the previous lesson in this module. ' if stage>1 else 'Basic programming and a way to read the source project.') }Read the project [README](../../../README.md) and [setup guide](../../../setup-guide.md).

## Progressive explanation

### Beginner explanation

{intro}

### Step toward the implementation

{walkthrough} The source files for this module are {', '.join('`'+f+'`' for f in module.get('source_files',[]))}.

## Source evidence

Excerpt from [`{codefile}`]({link}); copied from the source, not executed during package refinement. Read surrounding lines for full context.

```{lang}
{body.strip()}
```

### Read it step by step

1. Find the focus cue `{cue}` and identify its arguments or input values.
2. Follow the condition or transformation and identify the returned value or state update.
3. Trace one caller and compare the result with the README claim.
4. Note any local-only, mock, placeholder, or external-service boundary.

## Expected behavior and boundaries

The lesson should produce a source-backed explanation of **{title}**. A test or code excerpt establishes only the behavior it covers; it does not prove an external API, device, deployment, or provider works.

## Practical exercise

Complete [`{exercise}`](../exercises/{exercise}). Add an input or edge case, cite the source, and write the expected result before changing code.

## Common mistakes and debugging

- Inferring feature behavior from the product name or screen alone.
- Skipping the caller, model/state layer, or error path.
- Treating local sample data or a mock response as a real service result.
- Debug by tracing input → validation → transformation → output and then checking the relevant test.

## Best practices and security

Protect credentials and personal data, validate untrusted inputs, request only necessary device permissions, and keep provider/device behavior explicitly unverified until tested in an authorized environment.

## Summary

You began with the module’s plain meaning, traced `{cue}` in `{file}`, and identified one limit or testable boundary.

## Knowledge checks

1. What input or action reaches the source focus?
2. What does the code change or return?
3. Which edge case or integration boundary needs verification?

## References

- [Project README](../../../README.md)
- [Setup guide](../../../setup-guide.md)
- [Source file]({link})
'''

def main():
 total=0
 for package in sorted(PACKAGES.iterdir()):
  if not package.is_dir():continue
  slug=package.name; modules_dir=package/'modules'
  for md in sorted(p for p in modules_dir.glob('module-*') if p.is_dir()):
   mp=md/'module.json'; module=json.loads(mp.read_text(encoding='utf-8'));old=sorted((md/'lessons').glob('*.md'))
   if not old:continue
   original=old[0].read_text(encoding='utf-8',errors='replace'); files=module.get('source_files',[])
   focus_file,cue=focus_from(original,files)
   if focus_file not in files and files:focus_file=files[0]
   code=excerpt_from(slug,focus_file,cue,original)
   module['source_files']=list(dict.fromkeys(files))
   module['source_code_focus']={'excerpt_file':code[0],'symbol_or_search_term':cue}
   objectives=module.get('learning_objectives',[])
   objective_ids=module.get('learning_objective_ids',[])
   while len(objectives)<3:objectives.append({'objective_id':f'{module["module_id"]}-objective-{len(objectives)+1}','text':'Trace the source behavior and test one boundary.'})
   if not objective_ids:objective_ids=[x.get('objective_id',f'{module["module_id"]}-objective-{i+1}') for i,x in enumerate(objectives)]
   objectives=objectives[:3];objective_ids=objective_ids[:3]
   module['learning_objectives']=objectives;module['learning_objective_ids']=objective_ids
   lidbase=f'{module["module_id"]}-lesson-'
   lids=[lidbase+f'{i:02d}' for i in range(1,4)]
   module['ordered_lesson_ids']=lids
   module['estimated_duration_minutes']=max(150,module.get('estimated_duration_minutes',0))
   module['completion_criteria']=['Complete all three progressive lessons and the exercise.','Trace the named source function and explain its boundary.','Complete the module assessment.']
   for f in old:f.unlink()
   exercise=next((f.name for f in (md/'exercises').glob('*.json')),None)
   if not exercise:exercise='exercise-'+md.name.split('-')[-1]+'.json'
   for stage,lid in enumerate(lids,1):
    (md/'lessons'/f'lesson-{stage:02d}.md').write_text(lesson_md(slug,module.get('title',md.name),module,stage,lid, (focus_file,cue),code,exercise),encoding='utf-8')
   assessment=json.loads((md/'assessment.json').read_text(encoding='utf-8'))
   questions=assessment.get('questions',[])
   for i,q in enumerate(questions):
    stage=0 if i<3 else 1 if i<8 else 2
    q['lesson_id']=lids[stage]
    q['learning_objective_id']=objective_ids[stage]
   (md/'assessment.json').write_text(json.dumps(assessment,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
   keypath=md/'answer-key.json';key=json.loads(keypath.read_text(encoding='utf-8'))
   qmap={q.get('question_id'):q for q in questions}
   for a in key.get('answers',[]):
    if a.get('question_id') in qmap:
     a['related_lesson_id']=qmap[a['question_id']]['lesson_id']
     a['supporting_reference']=os.path.relpath(SOURCE/slug/focus_file,md)
   keypath.write_text(json.dumps(key,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
   mp.write_text(json.dumps(module,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
   total+=1
  manifest=json.loads((package/'manifest.json').read_text(encoding='utf-8'))
  mdirs=[p for p in modules_dir.glob('module-*') if p.is_dir()]
  manifest['lesson_count']=sum(len(list((m/'lessons').glob('*.md'))) for m in mdirs)
  manifest['question_count']=sum(len(json.loads((m/'assessment.json').read_text()).get('questions',[])) for m in mdirs)
  manifest['included_files']=sorted(p.relative_to(package).as_posix() for p in package.rglob('*') if p.is_file() and p.name!='manifest.json')
  manifest['validation_status']='pending validation'
  (package/'manifest.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
 print('Refined App Development modules:',total)
if __name__=='__main__':main()
