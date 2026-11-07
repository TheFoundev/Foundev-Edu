#!/usr/bin/env python3
"""Generate a separate source-grounded education library for /foundev/AI-ML."""
from __future__ import annotations
import ast, json, re, runpy, shutil, sys
from pathlib import Path

SOURCE = Path('/home/aziz/foundev/AI-ML')
TARGET = Path('/home/aziz/foundev/Mini projects edu/AI-ML 36 Edu')
TARGET.mkdir(parents=True, exist_ok=True)
(TARGET/'tools').mkdir(parents=True, exist_ok=True)
CORE_TOOL = TARGET / 'tools/build_36_core.py'
if not CORE_TOOL.exists():
    shutil.copy2(Path('/home/aziz/foundev/Mini projects edu/ AI-ML Edu/tools/build_ai_ml_packages.py'), CORE_TOOL)
ctx = runpy.run_path(str(CORE_TOOL))
G = ctx['build'].__globals__
G['SOURCE'] = SOURCE
G['TARGET'] = TARGET

# These are extra deep dives for systems whose algorithms need a distinct module beyond
# the common data → representation → model → evaluation → inference progression.
EXTRAS = {
'algorithmic-trading-signals': [
 ('Temporal Targets, Backtesting, and Risk','src/model.py','forward_returns','A backtest is a replay of decisions through time; it must not use tomorrow’s data to decide what to do today.','forward_returns defines the next-period target; the README says prices are simulated and the backtest omits fees, slippage, sizing, and shorting.'),
],
'autonomous-driving-perception': [
 ('Lane and Vehicle Perception Boundaries','src/model.py','detect_vehicles','Lane pixels and vehicle boxes are different outputs and need separate checks.','The source estimates lanes and vehicle boxes with threshold and connected-component logic on procedural scenes, not a learned driving model.'),
],
'gan-image-generation': [
 ('Generator and Discriminator Roles','src/model.py','build_generator','The generator proposes an image; the discriminator judges whether an image resembles the training examples.','build_generator and build_discriminator create separate small convolutional networks for the synthetic 16×16 shape task.'),
 ('Adversarial Training and Sample Review','src/model.py','train','Training is a contest between two learners; a stable loss does not guarantee useful samples.','train alternates generator/discriminator updates and demo saves a sample grid; training is deliberately short and produces rough shapes.'),
],
'hybrid-recommender-with-content-features': [
 ('Collaborative and Content Scores','src/model.py','recommend','Collaborative filtering learns patterns from ratings; content similarity compares item descriptions/tags.','The code combines truncated-SVD scores with a profile averaged from tags of highly rated items; the users and ratings are synthetic.'),
],
'hyperparameter-optimization-service': [
 ('Trial Persistence and Search API','app.py','search','A search service records each candidate setting and score so a result can be inspected later.','run_search writes a small random-search trial record to SQLite; FastAPI exposes search and trial routes, with no distributed workers or pruning.'),
],
'ml-experiment-tracking-and-registry': [
 ('Experiment Records and Model Registry','src/model.py','best_run','A registry remembers which run and artifact path produced a selected model.','Three model configurations are logged to SQLite; the best-run lookup is a simple local registry, not a governed remote model store.'),
],
'model-explainability-with-shap': [
 ('Global and Local Explanations','src/model.py','local_explanation','A global explanation summarizes patterns across examples; a local explanation describes one prediction.','The source computes global importance and per-row TreeExplainer values; explanations are model-specific and do not prove causation.'),
],
'monai-medical-imaging-pipeline': [
 ('3D Segmentation and Patient-Level Labels','src/model.py','segment','A voxel mask marks locations in a volume; a patient-level label summarizes an entire scan.','The code thresholds synthetic 3D lesion volumes and classifies with two hand-built volume features; it is not a trained medical imaging model.'),
],
'movie-recommender-with-als': [
 ('Latent Factors and Ranking Metrics','src/model.py','fit','Latent factors represent users and movies in a smaller shared space; ranking metrics measure whether useful items appear near the top.', 'fit learns a biased matrix factorization with SGD; RMSE and precision@5 are evaluated on a small synthetic ratings matrix.'),
],
'multi-model-time-series-forecasting': [
 ('Baselines and Forecast Comparison','src/model.py','seasonal_naive','A baseline is a simple forecast that a more complex method must beat on the same future window.','The repository compares naive, mean, linear-trend and seasonal-naive baselines and an optional SARIMAX model on one synthetic series.'),
 ('Rolling-Origin Evaluation and Leakage','src/model.py','rolling_origin_evaluation','In a rolling-origin evaluation, each forecast is made using only observations available before that forecast time.','rolling_origin_evaluation reports time-ordered holdout performance; the README notes the small synthetic series and lack of extensive rolling validation.'),
],
'multi-person-pose-estimation-with-mmpose': [
 ('Person Grouping and Joint Geometry','src/model.py','estimate','A detector first finds people; a keypoint estimate then assigns joint locations to each person.', 'The source groups bright line segments into figures and estimates joints from bounding-box proportions rather than learned pose features.'),
],
'named-entity-recognition-pipeline': [
 ('BIO Tags, Token Features, and Entity Spans','src/model.py','spans','A BIO tag marks a token as beginning, inside, or outside an entity; adjacent tags are combined into a span.', 'The pipeline uses token shape, prefixes, and neighboring tokens with logistic regression, then evaluates exact entity spans on template-generated sentences.'),
],
'neural-text-to-speech-synthesis': [
 ('Pronunciation Rules and Phoneme Sequence','src/model.py','synthesize','Text-to-speech first needs a pronunciation representation; this project uses hand-written rules and a small lexicon.', 'The project is explicitly not neural TTS: rule-based grapheme-to-phoneme conversion feeds a classical formant renderer.'),
 ('Formants, Duration, and Prosody','src/model.py','_render_phrase','Vowels contribute resonant frequencies, consonants contribute noise or bursts, and duration/pitch shape the phrase.', 'The source renders vowel formants and consonants with a rule-based signal model; duration is fitted on a 44-phrase corpus.'),
],
'offline-speech-recognition-engine': [
 ('Dynamic Time Warping and Template Matching','src/model.py','dtw_distance','Dynamic time warping compares two sequences while allowing their timing to stretch or compress.', 'The recognizer uses per-word synthetic templates and DTW; it has only eight command words and no language model.'),
],
'outlier-detection-benchmark': [
 ('Detector Comparison and Evaluation','src/model.py','zscore_scores','An outlier detector gives each row a score; a benchmark compares scores against known synthetic labels.', 'The source compares z-score, Isolation Forest, LOF and one-class SVM on generated Gaussian, ring, and clustered data using ROC AUC.'),
],
'real-time-pose-estimation-app': [
 ('Detect People and Group Image Parts','src/model.py','find_people','Detection locates candidate people; grouping joins bright components into one person region before estimating joints.','find_people and merge_parts use bright-pixel geometry; they do not run a learned detector.'),
 ('Regress Keypoints from Cropped Features','src/model.py','fit_ridge','A regressor maps a fixed-size crop description to joint coordinates; it needs examples with known target joints.','fit_ridge and predict_joints use ridge regression on synthetic frames; this is not MediaPipe or a trained pose backbone.'),
 ('API Input, Model Persistence, and Safety','app.py','uploaded_frame','An inference endpoint checks an uploaded image, runs the model, and returns a structured result.', 'The Flask API applies key checking/rate limits and loads a saved model; uploaded_frame handles the upload path, and the camera path depends on optional OpenCV.'),
],
'recommender-algorithm-benchmark': [
 ('Ranking Metrics and Catalogue Coverage','src/model.py','evaluate','Precision asks how many recommended items are relevant; recall asks how many relevant items were recovered; coverage measures catalogue breadth.', 'The benchmark compares popularity, item-item cosine, SVD and NMF using precision@5, recall@5, and catalogue coverage on synthetic ratings.'),
],
'retrieval-augmented-document-q-a': [
 ('Passage Retrieval, Answer Extraction, and Attribution','src/model.py','answer','Retrieval selects a passage; extractive answering copies a sentence from that passage and should identify its source.', 'The implementation uses TF-IDF passage retrieval and returns a source sentence; it does not call an LLM or generate new text.'),
],
'sales-forecasting-with-prophet': [
 ('Additive Components and Forecast Horizon','src/model.py','predict','An additive forecast combines trend, weekly/yearly seasonal effects, and optional holiday bumps.', 'The source builds a Prophet-style additive forecast on generated sales; the dataset is synthetic and no confidence interval/changepoint model is implemented.'),
],
'segment-anything-sam-fine-tuning': [
 ('Image Encoding and Prompt Types','src/model.py','encode_image','An image encoder creates a compact representation; a point, box, or mask prompt tells a decoder which object to segment.', 'The source uses a small encoder and supports point, box, and mask prompts on synthetic single-shape images.'),
 ('Prompt Decoding, Fine-Tuning, and Mask Metrics','src/model.py','fine_tune','Fine-tuning changes selected parameters using labeled examples; IoU checks the overlap between predicted and target masks.', 'The training loop fine-tunes the decoder and reports IoU/success; the encoder is not trained and the project does not implement Meta SAM.'),
],
'speech-to-text-transcription-service': [
 ('Energy Segmentation and Word Decoding','src/model.py','segment','A transcription pipeline first separates word-sized audio regions, then labels each region and joins the labels.', 'The service segments tone-based synthetic words by energy and decodes ten digit labels; no real speech is recorded or recognized.'),
],
'streaming-anomaly-detection': [
 ('Online Updates, Thresholds, and Detection Delay','src/model.py','simulate','An online detector updates its baseline as each value arrives and flags values far from that baseline.', 'The stream uses drift and injected spikes; the detector updates mean/variance with EWMA, sweeps thresholds, and measures detection delay.'),
],
'tensorflow-object-detection-api': [
 ('Object Proposals and Box Matching','src/model.py','proposal_boxes','A proposal marks a possible object region; IoU measures how much that box overlaps a labelled box.', 'The source finds connected components, computes crop features, and uses a random forest; it does not use the TensorFlow Object Detection API.'),
],
'time-series-classification-pipelines': [
 ('Time-Domain and Frequency Features','src/model.py','featurize','A classifier can summarize a sequence with statistics and frequency components before making a prediction.', 'The pipeline extracts time-domain and FFT features for a random forest; data is synthetic and there is no temporal cross-validation.'),
],
'train-a-gpt-language-model-from-scratch': [
 ('Self-Attention Model Architecture','src/model.py','build_model','Self-attention lets each character representation use information from other positions in its context window.','The implementation builds a small embedding/self-attention model; it is not large-scale GPT pretraining.'),
 ('Temperature Sampling and Generated Text','src/model.py','sample','Sampling turns model probabilities into a next-character choice; temperature changes how concentrated or varied those choices are.','sample generates continuations from the tiny character model; the corpus is only a few paragraphs, so it tends to memorize.'),
],
'wav2vec2-low-resource-asr-fine-tuning': [
 ('Frame Labels, Greedy Decoding, and Error Rate','src/model.py','decode','Frame-level predictions must be collapsed into token sequences before comparing the transcript with a reference.', 'The source classifies synthetic tone frames and greedily collapses labels; it is not Wav2Vec 2.0 and has no language model.'),
],
}

MODEL_CUES = {
'abstractive-document-summarization':['score_length','search_length','summarize','rouge_l'],
'algorithmic-trading-signals':['rsi','add_features','forward_returns','train'],
'autonomous-driving-perception':['lane_iou','detect_vehicles','match_detections','evaluate'],
'detectron2-instance-segmentation':['segment','mask_iou','evaluate','train'],
'end-to-end-speech-recognition-with-speechbrain':['features','train','demo'],
'facial-attribute-analysis-kiosk':['train','demo'],
'gan-image-generation':['build_generator','build_discriminator','train','demo'],
'hybrid-recommender-with-content-features':['build_matrix','fit','recommend','precision_at_k'],
'hyperparameter-optimization-service':['run_search','ensure_db','train','demo'],
'image-super-resolution-enhancer':['downsample','upscale','psnr','evaluate'],
'industrial-defect-detection':['make_patch','reconstruction_scores','train','demo'],
'ml-experiment-tracking-and-registry':['candidates','train','best_run','demo'],
'model-explainability-with-shap':['explain','global_importance','local_explanation','check_against_the_truth'],
'monai-medical-imaging-pipeline':['make_volume','segment','volume_features','dice'],
'movie-recommender-with-als':['fit','predict','recommend','precision_at_5'],
'multi-model-time-series-forecasting':['seasonal_naive','moving_average','rolling_origin_evaluation','sarimax_forecast'],
'multi-person-pose-estimation-with-mmpose':['draw_person','estimate','pck','train'],
'named-entity-recognition-pipeline':['token_features','featurize','spans','train'],
'neural-text-to-speech-synthesis':['phrase_syllables','target_duration','synthesize','_render_phrase'],
'offline-speech-recognition-engine':['synthesize','frame_features','dtw_distance','train'],
'outlier-detection-benchmark':['gaussian','zscore_scores','train','demo'],
'real-time-pose-estimation-app':['find_people','fit_ridge','estimate','pck'],
'recommender-algorithm-benchmark':['build_matrix','fit_all','recommend_matrix','evaluate'],
'retrieval-augmented-document-q-a':['load_data','sentences','answer','train'],
'sales-forecasting-with-prophet':['make_sales','fit','predict','weekend_effect_lookup'],
'segment-anything-sam-fine-tuning':['encode_image','decode_point','fine_tune','segment'],
'semantic-segmentation-with-u-net-and-deeplab':['make_sample','build_unet','dice_score','train'],
'speech-to-text-transcription-service':['tone','features','segment','transcribe'],
'streaming-anomaly-detection':['make_stream','simulate','evaluate','train'],
'tensorflow-object-detection-api':['make_scene','proposal_boxes','box_iou','train'],
'time-series-classification-pipelines':['make_series','extract','featurize','train'],
'topic-modeling-with-bertopic':['load_data','train','demo'],
'train-a-gpt-language-model-from-scratch':['load_data','build_model','sample','train'],
'wake-word-keyword-spotting':['wake_clip','features','train','demo'],
'wav2vec2-low-resource-asr-fine-tuning':['word_signal','frame_features','decode','word_distance'],
'weed-species-detection':['make_leaf','features','train','demo'],
}

FEATURE_CUE_OVERRIDES={'hyperparameter-optimization-service':'ensure_db','movie-recommender-with-als':'predict','topic-modeling-with-bertopic':'demo'}
FEATURE_TITLE_OVERRIDES={'hyperparameter-optimization-service':'Trial Storage and Search Parameters','movie-recommender-with-als':'Rating Prediction from Latent Factors','topic-modeling-with-bertopic':'Topic Assignments and Output Representation'}
API_CUE_OVERRIDES={'hyperparameter-optimization-service':'trials'}
METRIC_CUE_OVERRIDES={'recommender-algorithm-benchmark':'test_every_recommender_is_measured'}

SIX_MODULES={'abstractive-document-summarization','detectron2-instance-segmentation','facial-attribute-analysis-kiosk','image-super-resolution-enhancer','industrial-defect-detection','outlier-detection-benchmark','semantic-segmentation-with-u-net-and-deeplab','tensorflow-object-detection-api','time-series-classification-pipelines','topic-modeling-with-bertopic','wake-word-keyword-spotting','weed-species-detection'}

EXTRA_TITLES = {
'gan-image-generation':['Generator and Discriminator Roles','Adversarial Training and Sample Review'],
'train-a-gpt-language-model-from-scratch':['Character Tokens and Next-Character Sequences','Self-Attention, Training, and Sampling'],
'neural-text-to-speech-synthesis':['Pronunciation Rules and Phoneme Sequence','Formant Synthesis and Prosody'],
'segment-anything-sam-fine-tuning':['Image Encoding and Prompt Types','Prompt Decoding, Fine-Tuning, and Mask Metrics'],
'multi-model-time-series-forecasting':['Baselines and Forecast Comparison','Rolling-Origin Evaluation and Leakage'],
}


def section_text(text, title):
    match=re.search(r'^## '+re.escape(title)+r'\s*$(.*?)(?=^## |\Z)',text,re.M|re.S|re.I)
    return match.group(1).strip() if match else ''

def bullets(body):
    result=[]; current=None
    for line in body.splitlines():
        if re.match(r'^\s*[-*]\s+',line):
            if current: result.append(re.sub(r'\s+',' ',current).strip())
            current=re.sub(r'^\s*[-*]\s+','',line).strip()
        elif current and line.startswith(('  ','\t')):
            current+=' '+line.strip()
        elif current and not line.strip():
            result.append(re.sub(r'\s+',' ',current).strip());current=None
    if current:result.append(re.sub(r'\s+',' ',current).strip())
    return result

def functions(path):
    try:
        tree=ast.parse(path.read_text(encoding='utf-8-sig',errors='replace'))
        return [n.name for n in tree.body if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef,ast.ClassDef))]
    except Exception:return []

def readme_parts(p):
    text=(p/'README.md').read_text(encoding='utf-8-sig',errors='replace')
    lines=text.splitlines()
    title=next((x.lstrip('# ').strip() for x in lines if x.startswith('# ')),p.name.replace('-',' ').title())
    before_features=section_text(text,'Overview')
    intro=[]
    started=False
    for line in lines[1:]:
        if line.startswith(('>','##')): break
        if not line.strip():
            if started: break
            continue
        started=True
        if not line.lstrip().startswith(('|','```')):intro.append(line.strip())
    description=' '.join(intro)[:650] or next((x.strip() for x in before_features.splitlines() if x.strip() and not x.lstrip().startswith(('>','|','```','#'))),f"A source-grounded walkthrough of {title}.")
    brief=next((x.lstrip('> ').strip() for x in lines if x.startswith('> ')),description)
    feature_list=bullets(section_text(text,'Features'))
    notes=bullets(section_text(text,'Notes and limitations'))
    stack_raw=section_text(text,'Stack')
    stack_match=re.search(r'`([^`]+)`',stack_raw)
    stack=[x.strip() for x in stack_match.group(1).split(';')] if stack_match else ['Python']
    run_commands=section_text(text,'Run')
    return text,title,description,brief,feature_list,notes,stack,run_commands

def get_api(project_path):
    choices=[project_path/'app.py',project_path/'web/api_impl.py']
    for f in choices:
        if f.exists():
            names=functions(f)
            if names:
                preferred=[n for n in names if re.search(r'api|predict|summary|summarize|transcribe|search|recommend|run_prompt|run_training|run_sample|home|index',n,re.I)]
                cue=(preferred or names)[-1 if preferred else 0]
                return f.relative_to(project_path).as_posix(),cue,names
    return 'main.py','main',functions(project_path/'main.py')

DOCS={
'Python documentation':'https://docs.python.org/3/','NumPy documentation':'https://numpy.org/doc/stable/','Pandas documentation':'https://pandas.pydata.org/docs/','scikit-learn user guide':'https://scikit-learn.org/stable/user_guide.html','TensorFlow tutorials':'https://www.tensorflow.org/tutorials','Keras guides':'https://keras.io/guides/','PyTorch tutorials':'https://docs.pytorch.org/tutorials/','Flask documentation':'https://flask.palletsprojects.com/en/stable/','FastAPI documentation':'https://fastapi.tiangolo.com/','Matplotlib documentation':'https://matplotlib.org/stable/','SciPy documentation':'https://docs.scipy.org/doc/scipy/','Pillow documentation':'https://pillow.readthedocs.io/en/stable/','Hugging Face Transformers':'https://huggingface.co/docs/transformers/main/index','SHAP TreeExplainer':'https://shap.readthedocs.io/en/stable/generated/shap.TreeExplainer.html','MONAI documentation':'https://docs.monai.io/en/stable/','SpeechBrain documentation':'https://speechbrain.readthedocs.io/en/latest/','Prophet quick start':'https://facebook.github.io/prophet/docs/quick_start.html','MediaPipe documentation':'https://ai.google.dev/edge/mediapipe/solutions/vision/pose_landmarker','MMPose documentation':'https://mmpose.readthedocs.io/en/latest/','SentencePiece repository':'https://github.com/google/sentencepiece','Transformers model documentation':'https://huggingface.co/docs/transformers/main/index','TensorFlow Lite guide':'https://www.tensorflow.org/lite/guide'}

def relevant_refs(stack,slug):
    keys=['Python documentation']
    words=' '.join(stack).lower()
    for match,key in [('numpy','NumPy documentation'),('pandas','Pandas documentation'),('scikit','scikit-learn user guide'),('tensorflow','TensorFlow tutorials'),('keras','Keras guides'),('pytorch','PyTorch tutorials'),('flask','Flask documentation'),('fastapi','FastAPI documentation'),('matplotlib','Matplotlib documentation'),('scipy','SciPy documentation'),('pillow','Pillow documentation'),('shap','SHAP TreeExplainer'),('monai','MONAI documentation'),('speechbrain','SpeechBrain documentation'),('prophet','Prophet quick start'),('mediapipe','MediaPipe documentation'),('mmpose','MMPose documentation')]:
        if match in words and key not in keys:keys.append(key)
    if 'wav2vec' in slug or 'gpt' in slug or 'abstractive' in slug or 'bert' in slug:keys.append('Hugging Face Transformers')
    if 'wake-word' in slug:keys.append('TensorFlow Lite guide')
    return [(k,DOCS[k]) for k in dict.fromkeys(keys[:6])]

def mk_module(title,files,plain,fact,cue):
    example=f'{cue}()' if re.fullmatch(r'[A-Za-z_][A-Za-z0-9_]*',cue) else cue
    return {'title':title,'files':'; '.join(dict.fromkeys(files)),'plain':plain,'fact':fact,'example':example}

def build_project(p):
    text,title,description,brief,features,notes,stack,run=readme_parts(p)
    slug=p.name
    data_path=p/'src/data.py'; model_path=p/'src/model.py'; main_path=p/'main.py'; test_path=p/'tests/test_pipeline.py'
    data_names=functions(data_path); model_names=functions(model_path); test_names=functions(test_path)
    def choose(names, candidates, default=None):return next((c for c in candidates if c in names), default or (names[0] if names else 'main'))
    data_focus=choose(data_names,['load_data','synthesize','make_scene','make_sample','make_image','make_images','make_patch','make_leaf','make_volume','make_series','make_sales','make_prices','make_stream','draw_face','draw_line','make_frame','make_example','wake_clip','word_signal','tone','features','frame_features'])
    feature_focus=choose(data_names,['features','frame_features','feature','make_sequences','token_features','featurize','crop_features','make_catalog','make_scene','make_sample','make_patch','make_volume','make_series','make_leaf','draw_person','crops'],None)
    feature_focus=FEATURE_CUE_OVERRIDES.get(slug,feature_focus)
    model_focus=MODEL_CUES.get(slug,[])
    model_names_focus=[n for n in model_focus if n in model_names]
    if not model_names_focus:model_names_focus=[n for n in model_names if n not in {'train','demo'}][:3]
    if not model_names_focus:model_names_focus=['train']
    if not feature_focus or feature_focus=='load_data':
        feature_focus=choose(model_names,['add_features','normalized','build_matrix','extract','token_features','featurize','encode_image','crop_features','score_length','make_sequences'],model_names_focus[0])
    feature_focus=FEATURE_CUE_OVERRIDES.get(slug,feature_focus)
    test_focus=choose(test_names,[n for n in test_names if n not in {'test_pipeline_runs','test_seed_is_usable'}], 'test_pipeline_runs')
    test_limit_focus=choose(test_names,[n for n in test_names if n not in {'test_pipeline_runs','test_seed_is_usable',test_focus}], 'test_pipeline_runs')
    metric_focus=choose(model_names,['rouge_l','psnr','evaluate','precision_at_k','precision_at_5','mase','rmse','dice_score','dice','pck','mean_joint_error','formant_error','word_distance','precision_at_k','recall','score','accuracy','global_importance','check_against_the_truth'],test_focus)
    metric_focus=METRIC_CUE_OVERRIDES.get(slug,metric_focus)
    api_file,api_focus,api_names=get_api(p)
    api_focus=API_CUE_OVERRIDES.get(slug,api_focus)
    app_present=api_file!='main.py'
    model_feature=next((x for x in features if any(k in x.lower() for k in ['model','classif','recommend','segment','detect','forecast','score','train','feature','metric','generate','extract','rank','attention','network','encoder','decoder'])),features[0] if features else 'The source provides a small data-to-output pipeline.')
    metric_feature=next((x for x in features if any(k in x.lower() for k in ['metric','accuracy','precision','recall','auc','dice','iou','rouge','rmse','mae','score','evaluation','error','rate'])),features[-1] if features else 'The source has a small smoke-test suite.')
    gaps=notes or ['The README describes a compact educational implementation; test input ranges and edge cases before generalizing results.']
    flow=f"main.py → src/data.py ({', '.join(data_names[:3])}) → src/model.py ({', '.join(model_names_focus[:4])}) → {api_file} ({api_focus})" if app_present else f"main.py ({choose(functions(main_path),['main'])}) → src/data.py ({', '.join(data_names[:3])}) → src/model.py ({', '.join(model_names_focus[:4])}) → demo/output"
    modules=[]
    modules.append(mk_module('Task, Input Contract, and Source Scope',['README.md','main.py'],f"Think of {title} as a small workshop: the input is prepared, a method transforms it, and a result is checked. The brief and the implementation may describe different levels of ambition.",f"README overview: {description} The project brief asks: {brief} The supplied entry point is main.py and dispatches the actual train/demo workflow.",'main'))
    modules.append(mk_module('Dataset Generation, Labels, and Splits',['src/data.py'],f"A dataset is a set of examples and target labels; this repository creates or loads the specific examples named in its README.",f"Implemented data functions: {', '.join(data_names)}. README feature: {features[0] if features else description}.",data_focus))
    modules.append(mk_module(FEATURE_TITLE_OVERRIDES.get(slug,'Features and Intermediate Representation'),['src/data.py','src/model.py'],f"Features are the measurements or encoded representations the algorithm can use; their shape determines what the model can learn.",f"Feature/data path functions: {', '.join([n for n in data_names+model_names if any(k in n.lower() for k in ['feature','frame','token','sequence','vector','matrix','normal','crop','encode','extract','split'])][:7] or data_names[:4])}. README feature: {features[1] if len(features)>1 else model_feature}.",feature_focus))
    modules.append(mk_module('Core Algorithm and Model Mechanics',['src/model.py'],f"The model or algorithm is the rule that maps prepared examples to scores, labels, masks, recommendations, or generated output; the real implementation may be simpler than the project brief.",f"Actual model functions: {', '.join(model_names_focus)}. Implemented feature: {model_feature} README notes: {gaps[0]}.",model_names_focus[0]))
    modules.append(mk_module('Training, Metrics, and Validation',['src/model.py','tests/test_pipeline.py'],f"Training adjusts or configures the method; evaluation checks it on held-out examples with task-appropriate metrics.",f"Model training/evaluation functions: {', '.join([n for n in model_names if any(k in n.lower() for k in ['train','eval','score','metric','accuracy','precision','recall','auc','iou','dice','rouge','rmse','mae','error','loss','test'])][:8] or model_names_focus)}. Test focus: {test_focus}. README metric/feature: {metric_feature}.",metric_focus))
    api_files=([x for x in ('app.py',api_file,'main.py') if (p/x).is_file()] if app_present else ['main.py','src/model.py'])
    modules.append(mk_module('Inference, Demo, and User Interface',api_files,f"Inference means applying the trained or configured method to a new input; a user interface is only the path that sends that input and displays the result.",f"{'Application' if app_present else 'CLI/demo'} functions: {', '.join(api_names[:8] if app_present else functions(main_path)[:5])}. The selected source entry is {api_file}:{api_focus}; actual project output includes: {features[-1] if features else description}.",api_focus if app_present else 'demo'))
    modules.append(mk_module('Tests, Limitations, and Responsible Extensions',['tests/test_pipeline.py','README.md','src/model.py'],f"Tests are spot checks, not proof that the method works on every population or in production. Treat the README limits as part of the model’s operating conditions.",f"Test functions: {', '.join(test_names[:8])}. Documented limitations: {' '.join(gaps)}",test_limit_focus))
    # Add source-specific deep dives only where the pipeline has distinct stages that deserve separate teaching.
    extra_modules=[]
    for extra in EXTRAS.get(slug,[]):
        title_extra,rel,focus,plain_extra,fact_extra=extra
        files=[x.strip() for x in rel.split(';')]
        extra_modules.append(mk_module(title_extra,files,plain_extra,fact_extra,focus))
    if extra_modules:
        modules=modules[:3]+extra_modules+modules[4:]
    if slug in SIX_MODULES:
        combined=modules[5]
        combined['title']='Inference, Demo, Tests, and Responsible Limits'
        combined['files']='; '.join(dict.fromkeys((combined['files']+'; tests/test_pipeline.py; README.md').split('; ')))
        combined['plain']=f"A demo presents one output; tests and limitations tell you how far that output should be trusted. {combined['plain']}"
        combined['fact']+=f" Tests provide bounded checks: {', '.join(test_names[:6])}. Documented limits: {' '.join(gaps)}"
        modules=modules[:6]
    title=title
    G['TITLES'][slug]=title
    G['CURRICULA'][slug]=[(m['title'],m['plain']) for m in modules]
    G['GAPS'][slug]=gaps
    G['CODE_HINTS'][slug]=[m['example'][:-2] if m['example'].endswith('()') and m['example'].count('(')==1 else re.sub(r'\(.*','',m['example']) for m in modules]
    G['SOURCE_MAP'][slug]=[[x.strip() for x in m['files'].split(';') if x.strip()] for m in modules]
    G['MODULE_FACTS'][slug]=[m['fact'] for m in modules]
    G['PROJECT_REFERENCES'][slug]=relevant_refs(stack,slug)
    G['PROJECT_INFO'][slug]={'description':description,'problem':f"{brief} Actual implementation note: {features[0] if features else description}",'stack':stack,'features':'\n'.join('- '+x for x in features),'data_flow':flow,'gaps':gaps}
    return p

def initialize_workspace():
    TARGET.mkdir(parents=True,exist_ok=True)
    for name in ('projects','schemas','tools','reports','dist'):(TARGET/name).mkdir(parents=True,exist_ok=True)
    prior=Path('/home/aziz/foundev/Mini projects edu/ AI-ML Edu')
    for name in ('project.schema.json','module.schema.json','assessment.schema.json'):
        src=prior/'schemas'/name; dst=TARGET/'schemas'/name
        if src.exists():shutil.copy2(src,dst)
    schema_path=TARGET/'schemas/module.schema.json'
    schema=json.loads(schema_path.read_text())
    for key in ('source_files','source_code_focus'):
        if key not in schema['required']:schema['required'].append(key)
    schema['properties']['source_files']={'type':'array','minItems':1,'items':{'type':'string'}}
    schema['properties']['source_code_focus']={'type':'object','required':['excerpt_file','symbol_or_search_term'],'properties':{'excerpt_file':{'type':['string','null']},'symbol_or_search_term':{'type':'string'}},'additionalProperties':False}
    schema_path.write_text(json.dumps(schema,indent=2)+'\n')
    validator_source=prior/'tools/validate_content.py'
    validator_target=TARGET/'tools/validate_content.py'
    validator=validator_source.read_text()
    validator=validator.replace("/home/aziz/foundev/AIML-foundev-main/Artificial Intelligence & Machine Learning",str(SOURCE))
    validator_target.write_text(validator)
    (TARGET/'README.md').write_text('''# AI/ML 36-Project Learning Library\n\nThis is a new, separate library for the 36 source projects in `/home/aziz/foundev/AI-ML`. It is kept separate from the earlier 20-project AI/ML library. Each package maps its lessons and code excerpts to the actual source files; project READMEs document deliberate simplifications and missing production features.\n\n- `projects/` — 36 standalone learning packages\n- `dist/` — one ZIP per project\n- `schemas/` — shared package schemas\n- `tools/` — reproducible builder and structural/source-focus validator\n- `reports/module-source-audit.md` — every module's source files and code focus\n- `reports/source-review.md` — source limitations requiring human review\n\nEach module starts with a plain-language explanation before moving to a cited source-code excerpt. The code examples are excerpts from the supplied repositories and were not executed by the generator.\n''',encoding='utf-8')
    (TARGET/'CONTENT_STANDARDS.md').write_text('''# Content standards\n\n1. Teach source behavior, not the aspirational brief; label the difference clearly.\n2. Begin every module with a beginner-friendly explanation, then trace the actual source symbol, its inputs, transformation, and output.\n3. Cite source paths and include a short real code/config excerpt where available.\n4. Include three progressive standalone lessons per module with exercises and source-based knowledge checks.\n5. Create exactly ten MCQs per module, four options each, with a separate answer key and distractor explanations.\n6. Cover data provenance, split/leakage risks, metrics, model/artifact availability, and deployment boundaries.\n7. Include limitations and responsible-use safeguards for sensitive or consequential domains.\n8. Run the structural validator; treat its output as evidence of structure/source-cue alignment, not proof of educational accuracy.\n9. Keep these 36 packages separate from the previous 20-project AI/ML library.\n''',encoding='utf-8')

def main():
    initialize_workspace()
    project_folders=sorted(x for x in SOURCE.iterdir() if x.is_dir() and (x/'README.md').is_file())
    if len(project_folders)!=36:raise SystemExit(f'Expected 36 source projects, found {len(project_folders)}')
    # This is a separate collection; do not add or overwrite packages in the earlier library.
    for p in project_folders:
        source_project=build_project(p)
        ctx['build'](source_project)
        print('Built',p.name,'modules',len(G['CURRICULA'][p.name]))
    # Preserve a separate project set and ZIP only projects built from this source root.
    built={p.name for p in SOURCE.iterdir() if p.is_dir() and (p/'README.md').exists()}
    for z in (TARGET/'dist').glob('*.zip'): z.unlink()
    import zipfile
    for slug in sorted(built):
        folder=TARGET/'projects'/slug
        if not folder.exists():continue
        with zipfile.ZipFile(TARGET/'dist'/f'{slug}.zip','w',zipfile.ZIP_DEFLATED) as archive:
            for f in sorted(folder.rglob('*')):
                if f.is_file(): archive.write(f,Path(slug)/f.relative_to(folder))
    total=sum(len(ctx['CURRICULA'][slug]) for slug in built)
    print('TOTAL',len(built),'projects',total,'modules',total*3,'lessons',total*10,'questions')

if __name__=='__main__':main()
