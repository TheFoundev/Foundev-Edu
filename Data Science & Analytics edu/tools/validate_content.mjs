import fs from 'node:fs';
import path from 'node:path';

const root = path.resolve(process.argv[2] || 'Data Science & Analytics edu');
const errors = [];
const totals = { projects: 0, modules: 0, lessons: 0, questions: 0 };
const load = file => {
  try { return JSON.parse(fs.readFileSync(file, 'utf8')); }
  catch (error) { errors.push(`${file}: invalid JSON: ${error.message}`); return null; }
};
const walk = dir => fs.readdirSync(dir, { withFileTypes: true }).flatMap(entry => {
  const file = path.join(dir, entry.name);
  return entry.isDirectory() ? walk(file) : [file];
});

for (const slug of fs.readdirSync(path.join(root, 'projects')).sort()) {
  const projectDir = path.join(root, 'projects', slug);
  if (!fs.statSync(projectDir).isDirectory()) continue;
  totals.projects++;
  const manifest = load(path.join(projectDir, 'manifest.json'));
  const project = load(path.join(projectDir, 'project.json'));
  if (!manifest || !project) continue;
  if (project.slug !== slug || manifest.project_slug !== slug) errors.push(`${slug}: slug mismatch`);
  const files = walk(projectDir).map(file => path.relative(projectDir, file).replaceAll('\\', '/'))
    .filter(file => file !== 'manifest.json').sort();
  if (JSON.stringify(files) !== JSON.stringify([...(manifest.included_files || [])].sort())) errors.push(`${slug}: manifest file inventory mismatch`);

  const moduleDirs = fs.readdirSync(path.join(projectDir, 'modules')).filter(name => name.startsWith('module-')).sort();
  let lessonCount = 0, questionCount = 0;
  const moduleIds = new Set(), lessonIds = new Set(), questionIds = new Set();
  for (const dirName of moduleDirs) {
    const base = path.join(projectDir, 'modules', dirName);
    const module = load(path.join(base, 'module.json'));
    const assessment = load(path.join(base, 'assessment.json'));
    const key = load(path.join(base, 'answer-key.json'));
    if (!module || !assessment || !key) continue;
    totals.modules++;
    if (moduleIds.has(module.module_id)) errors.push(`${slug}: duplicate module ID ${module.module_id}`);
    moduleIds.add(module.module_id);
    const lessonFiles = fs.readdirSync(path.join(base, 'lessons')).filter(file => file.endsWith('.md')).sort();
    const lessons = lessonFiles.map(file => ({ file, text: fs.readFileSync(path.join(base, 'lessons', file), 'utf8') }));
    const ids = lessons.map(({ text }) => text.match(/Lesson ID:\*\*\s*`([^`]+)`/)?.[1]).filter(Boolean);
    if (JSON.stringify(ids) !== JSON.stringify(module.ordered_lesson_ids || [])) errors.push(`${slug}/${dirName}: ordered lesson ID mismatch`);
    for (const id of ids) {
      if (lessonIds.has(id)) errors.push(`${slug}: duplicate lesson ID ${id}`);
      lessonIds.add(id);
    }
    lessonCount += ids.length;
    for (const source of module.source_files || []) {
      if (!lessons.some(({ text }) => text.includes(`### ${source}`))) errors.push(`${slug}/${dirName}: source anchor absent from lesson text: ${source}`);
    }
    if (!(module.source_files || []).some(source => /\.(py|pyi|java|go|js|jsx|ts|tsx|sql|sh|rs|c|h|cc|cpp|cxx)$/i.test(source))) errors.push(`${slug}/${dirName}: no implementation source anchor`);

    const questions = assessment.questions || [], answers = key.answers || [];
    questionCount += questions.length;
    if (questions.length !== 10) errors.push(`${slug}/${dirName}: expected 10 questions, got ${questions.length}`);
    const answerById = new Map(answers.map(answer => [answer.question_id, answer]));
    if (answerById.size !== questions.length || answers.length !== questions.length) errors.push(`${slug}/${dirName}: one unique answer key is required per question`);
    for (const question of questions) {
      const qid = question.question_id;
      if (questionIds.has(qid)) errors.push(`${slug}: duplicate question ID ${qid}`);
      questionIds.add(qid);
      const options = question.options || [];
      const optionIds = options.map(option => option.option_id);
      if (options.length !== 4 || new Set(optionIds).size !== 4) errors.push(`${slug}/${dirName}/${qid}: expected four distinct options`);
      if (!ids.includes(question.related_lesson_id) || !ids.includes(question.lesson_id)) errors.push(`${slug}/${qid}: invalid lesson reference`);
      if (!(module.learning_objectives || []).some(objective => objective.objective_id === question.learning_objective_id)) errors.push(`${slug}/${qid}: invalid learning objective`);
      const answer = answerById.get(qid);
      if (!answer) continue;
      const incorrect = answer.incorrect_option_explanations || [];
      if (!optionIds.includes(answer.correct_option_id)) errors.push(`${slug}/${qid}: correct option does not exist`);
      if (incorrect.length !== 3 || new Set(incorrect.map(item => item.option_id)).size !== 3 || incorrect.some(item => !optionIds.includes(item.option_id) || item.option_id === answer.correct_option_id || !item.explanation?.trim())) errors.push(`${slug}/${qid}: incomplete/invalid distractor explanations`);
      if (!answer.correct_explanation?.trim() || !answer.tested_concept?.trim() || !answer.related_lesson_id) errors.push(`${slug}/${qid}: incomplete answer explanation metadata`);
    }
  }
  totals.lessons += lessonCount;
  totals.questions += questionCount;
  const expected = { modules: moduleDirs.length, lessons: lessonCount, questions: questionCount };
  if (JSON.stringify(manifest.counts) !== JSON.stringify(expected)) errors.push(`${slug}: manifest counts do not match ${JSON.stringify(expected)}`);
  console.log(`${slug}: ${expected.modules} modules, ${lessonCount} lessons, ${questionCount} questions`);
}

const result = { ...totals, errors: errors.length, status: errors.length ? 'FAIL' : 'PASS' };
fs.mkdirSync(path.join(root, 'reports'), { recursive: true });
fs.writeFileSync(path.join(root, 'reports', 'structural-validation.json'), JSON.stringify(result, null, 2) + '\n');
console.log(JSON.stringify(result));
if (errors.length) { console.error(errors.join('\n')); process.exit(1); }
