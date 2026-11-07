#!/usr/bin/env python3
"""Build source-grounded AI/ML education packages from the supplied repositories."""
from __future__ import annotations
import json, re, shutil, zipfile, ast, warnings
from datetime import datetime, timezone
from pathlib import Path

SOURCE = Path('/home/aziz/foundev/AIML-foundev-main/Artificial Intelligence & Machine Learning')
TARGET = Path('/home/aziz/foundev/Mini projects edu/AI - ML')
MODULE_FACTS = {}
PROJECT_REFERENCES = {}

# Curated progression reflects actual repository patterns; project guide sections and code paths
# provide implementation facts, while these titles prevent generic curriculum drift.
CURRICULA = {
'abstractive-text-summarizer': [('Evidence and Factuality','claims, evidence spans, and supported statements'),('Synthetic Pair Construction','corruption transforms and factuality labels'),('FactCC Multi-task Model','consistency, entailment, and semantic role objectives'),('Research Pipeline and Data','pairing, generation, augmentation, and training entrypoints'),('Shipped Flask Service and Static UI','lexical overlap scoring, request flow, and model_checkpoint=false'),('Evaluation, Limits, and Extensions','error analysis, neural checkpoint gap, and responsible interpretation')],
'college-faq-chatbot-rag': [('RAG and Source Documents','document ingestion and retrieval augmented generation'),('Chunking and Embeddings','document loading, chunk boundaries, and vector representations'),('Chroma Retrieval and MMR','candidate retrieval, diversity, and relevance'),('Hybrid Ranking and Adaptive Retrieval','BM25, weighted fusion, adaptive-k, and relevance gate'),('Grounded Generation and Streamlit','prompt context, optional rewriting, and chat flow'),('Evaluation, Safety, and Operations','RAGAS, source attribution, privacy, and failure analysis'),('Retrieval Debugging Lab','query normalization, empty retrieval, and chunk inspection'),('Capstone and Deployment Boundaries','static console versus backend, config, and production gaps')],
'credit-card-fraud-detection': [('Fraud as Imbalanced Classification','rare positives, labels, and operational costs'),('Dataset and Leakage Controls','feature split, scaling, and held-out evaluation'),('Balanced Logistic Regression','class_weight, decision scores, and thresholding'),('Training and Model Artifacts','train.py, serialization, and service loading'),('Flask Prediction API and Console','request validation, response, and UI flow'),('Metrics, Fairness, and Monitoring','precision/recall tradeoffs, drift, and human review')],
'crop-yield-prediction': [('County-Year Prediction Problem','geography, year, targets, and supervised learning'),('Earth Engine and MODIS Data','export, nine bands, and raster organization'),('Feature Engineering and Sequences','spatiotemporal inputs and preprocessing'),('Neural Architectures','CNN, RNN, and Gaussian-process model components'),('Training, Checkpoints, and Prediction','run.py workflow and county-year inference'),('Evaluation, Uncertainty, and Reproducibility','spatial leakage, calibration, missing dependencies, and limits'),('Visualization and Interpretation','county plots, error maps, and uncertainty-aware reading')],
'currency-note-recognition-for-visually-impaired': [('Recognition Task and Reference Images','denomination labels, camera input, and local reference set'),('ORB Keypoints and Descriptors','oriented FAST, rotated BRIEF, and scale/rotation tolerance'),('KNN Matching and Ratio Test','two-nearest-neighbour filtering and 0.789 cutoff'),('Winner Voting and Filename Labels','per-reference evidence and denomination extraction'),('Detector, Assets, and Static UI','actual detect.py flow, image/audio assets, and disconnected page'),('Accessibility, Evaluation, and Safety','lighting, note variation, fallback cues, and no trained model')],
'document-plagiarism-checker': [('Similarity Is Not a Verdict','scope, text input, and limitations of similarity'),('Sentence Segmentation and Querying','exact-phrase search query construction'),('Live Search and Source Pairing','web search results, pairing rule, and blocked domains'),('Scoring and PDF/Pasted Input','scoring calculation, upload flow, and result rendering'),('Flask Routes and State','request/response, stored scans, and front-end integration'),('Evaluation, Privacy, and Academic Integrity','false positives, source availability, and human review')],
'driver-drowsiness-detection': [('Signals and Eye Aspect Ratio','facial landmarks and geometric signal'),('Drowsiness State Machine','thresholds, consecutive frames, and alert state'),('Desktop dlib Implementation','68-point predictor, OpenCV capture, and dependencies'),('MediaPipe/Streamlit Variants','different landmark indexing and browser-facing workflow'),('HUD, PWA, and Data Flow','static Cockpit UI versus actual detector and offline assets'),('Calibration, Evaluation, and Safety','lighting, driver variation, false alarms, and non-medical/non-safety certification'),('Debugging and Robustness','missing model asset, camera failures, and frame lifecycle')],
'emotion-detection-from-text-and-face': [('Emotion Labels and Modalities','text versus face input and label interpretation'),('Text Inference Pipeline','preprocessing, backend route, and model output'),('Face CNN Input Pipeline','RGB 224x224 tensor, missing model artifact, and loader'),('Music Recommendation Rules','deterministic mapping from labels to tracks'),('Frontend, API, and Optional Infrastructure','webui/Next.js, backend, Docker, and Redis boundaries'),('Evaluation, Bias, and Consent','subjective labels, sensitive biometric data, and model limitations'),('End-to-End Debugging','missing weights, dependency setup, and mode-specific errors')],
'face-recognition-attendance-system': [('Capture and Identity Records','student registration, image capture, and CSV registry'),('Haar Cascade Face Detection','grayscale conversion, detectMultiScale, and bounding boxes'),('LBPH Face Representation','local binary patterns and trained recognizer'),('Attendance Matching and Persistence','thresholding, CSV attendance, and optional MySQL mirror'),('Desktop Workflow and Assets','training.py, retrain.py, testing.py, and GUI boundaries'),('Evaluation, Consent, and Security','biometric privacy, false matches, auditability, and human correction')],
'helmet-seatbelt-violation-detection': [('Detection Versus Violation Decision','object detection labels and downstream rules'),('YOLOv8x and COCO Classes','generic detector, boxes, confidence, and class names'),('Heuristic Violation Inference','COCO-path rules actually used versus custom-model path'),('Application, Accounts, and Database','main_app, database manager, and UI workflow'),('Weights, Evaluation, and Error Analysis','missing/custom weights, class coverage, and video conditions'),('Safety, Privacy, and Human Review','surveillance limits, false positives, and enforcement safeguards'),('Debugging the Pipeline','frame processing, model errors, and unavailable assets')],
'loan-default-prediction': [('Target Definition and Two-Stage Loss','default probability and loss severity decomposition'),('Features and Data Pipeline','train/test CSV contract and engineered features'),('Class Imbalance and Logistic Baseline','class weighting and threshold selection'),('Gradient Boosting and Log Severity','boosted model, log targets, and clipping'),('Legacy Training Versus Browser Heuristic','train_predict.py/models.py and disconnected demo UI'),('Evaluation, Fairness, and Decision Support','calibration, subgroup checks, missing data, and human oversight')],
'music-recommender-from-audio-features': [('Content-Based Recommendation','catalogue, seed track, and feature vectors'),('Feature Cleaning and Scaling','deduplication, case folding, and min-max normalization'),('Cosine Similarity and Ranking','vector geometry and neighborhood results'),('API and Dataset Flow','2261 rows, ten features, Flask endpoints, and static UI'),('Testing and Explanation','artist selection, cleaning, visualization, and Audio DNA'),('Evaluation, Bias, and Product Limits','catalogue bias, cold start, diversity, and user control')],
'plant-leaf-disease-detection-cnn': [('Image Classification Problem','classes, image labels, and prediction scope'),('Dataset Preparation','folder structure, labels, train/validation/test separation'),('CNN Architecture','256x256x3 input, convolution, pooling, and classifier'),('Training and Model Artifacts','notebook, train_cnn.py, checkpoints, and preprocessing'),('Django Inference Path and Missing Assets','views, predictor, routes, stub tests, and absent production model'),('Evaluation, Generalization, and Farm Safety','class metrics, field shift, expert confirmation, and limits')],
'question-paper-generator-from-syllabus': [('Syllabus and Chapter Selection','board/class/subject and catalogue API'),('Prerequisite Graph and Topic Selection','chapter dependencies and recursive selection'),('Prompt Contracts and Local LLM','Ollama llama2, constrained generation, and output validation'),('Question and Study Material Routes','Flask endpoints, generated content, and templates'),('PDF/OMR Companion Tools','separate utilities and app boundaries'),('Evaluation, Reliability, and Teacher Review','hallucination, curriculum validity, missing dependencies, and approval'),('Setup, Testing, and Debugging','configuration, API failures, model availability, and tests')],
'resume-screening-and-jd-matching': [('Text Extraction and Input Boundaries','resume documents, job descriptions, and parsing'),('Preprocessing and Sentence Embeddings','all-MiniLM-L6-v2 and 384-dimensional vectors'),('Cosine Matching and Ranking','similarity scores and candidate ordering'),('Skill-Level Explanation','extractor, matcher, explainer, and evidence spans'),('Flask UI and Model Runtime','app route, batch processing, and spaCy/model dependencies'),('Evaluation, Fairness, and Human Oversight','proxy bias, missing context, privacy, and non-decision use')],
'retail-sales-forecasting': [('Transaction Data and Business Questions','orders, products, region, sales, profit'),('ETL and SQL Aggregation','database loading, group/sum/mean, and query scripts'),('Calendar Buckets and Weighted Metrics','monthly buckets, margin, and sales-weighted discount'),('Dashboard Data Flow','Flask/static UI, query outputs, and charts'),('Testing and Reconciliation','totals, signed profit, nulls, and missing pymysql dependency'),('Forecasting Claims and Extensions','no ML forecast exists, seasonality proposal, and responsible metrics')],
'sign-language-to-text-translation': [('Language, Gloss, and Scope','text-to-sign gloss versus full language translation'),('Tokenization and Tagging','language-aware tokenization and tag enums'),('Rule-Based Gloss Restructuring','mapping_rules and regular expression transformations'),('Token-to-Clip Resolution','PakistanSignLanguage mapping, digits, and spelling fallback'),('CLI, Library, and Static Demo','slt command, package structure, UI limitations'),('Testing, Metrics, and Accessibility','CLI tests, coverage, signer review, and cultural/linguistic limits'),('Model Boundaries and Extensions','deterministic pipeline versus recognition/generation ML'),('Packaging and Reproducible Use','pyproject, requirements, and downloaded assets')],
'stock-price-trend-predictor': [('Market Series and Prediction Scope','time series, stock data, and target definitions'),('Data Acquisition and Feature Building','update_data, make_dataset, and Google Trends'),('Research Signal and Look-Ahead Bias','rolling mean shifted prior window and historical signal'),('Notebook Models and Visualization','research notebooks and exploration boundary'),('Static UI and Project Scripts','UI, environment checks, and pipeline connectivity'),('Time-Series Evaluation and Financial Risk','chronological split, baselines, leakage, and no investment advice')],
'student-dropout-risk-prediction': [('Outcome Labels and Policy Context','administrative withdrawal definition and grades 6–12'),('Database and Data Preparation','SQL creation, missingness, and engineered features'),('Classification Pipeline','legacy pipeline scripts and intended classifier stages'),('Metrics and Population Analysis','precision/recall, subgroup plots, and evaluation limits'),('DEWS Static Interface and Pipeline Gaps','functional demo UI versus broken/legacy scripts'),('Privacy, Fairness, and Supportive Use','student privacy, bias, intervention support, and human review')],
'vehicle-number-plate-recognition': [('Plate Localisation Versus Character Recognition','where the plate is versus what characters it contains'),('YOLOv5 Model Loading','hub custom checkpoint, model variants, and confidence'),('Detection Output and Unwired OCR Helpers','bounding boxes, annotated images, and why the OCR helpers are not called'),('Streamlit Application and Configuration','app.py, static landing page, and model dependencies'),('Evaluation and Failure Analysis','lighting, angle, detector classes, and missing character-level evaluation'),('Privacy, Security, and Deployment','plate data retention, access controls, and human verification'),('Debugging Model Assets','checkpoint downloads, environment pins, and startup diagnostics')],
}

# Paths point to real files from the scanned source trees, in the same order as each curriculum.
SOURCE_MAP = {
'abstractive-text-summarizer':[['README.md','data_pairing/pair_data.py'],['data_generation/create_data.py','data_generation/augmentation_ops.py'],['modeling/model.py','modeling/utils.py'],['modeling/run.py','data_pairing/pair_data.py'],['src/api.py','js/app.js','index.html'],['modeling/run.py','PROJECT_OVERVIEW.md','WORKFLOW.md']],
'college-faq-chatbot-rag':[['src/document_loader.py','src/ingestion.py'],['src/chunker.py','src/embeddings.py'],['src/vector_store.py','src/retriever.py'],['src/retriever.py','src/query_normalizer.py'],['src/rag_chain.py','src/prompt.py','app/app.py'],['scripts/evaluate.py','src/evaluation/ragas_eval.py'],['src/query_rewriter.py','scripts/evaluate_retrieval.py'],['config/settings.py','WORKFLOW.md']],
'credit-card-fraud-detection':[['src/train.py','PROJECT_OVERVIEW.md'],['src/train.py','src/settings.py'],['src/train.py'],['src/train.py','src/flask_app.py'],['src/flask_app.py','index.html','js/app.js'],['tests/test_flask.py','src/train.py']],
'crop-yield-prediction':[['run.py','cyp/data/feature_engineering.py'],['cyp/data/exporting.py','data/README.md'],['cyp/data/preprocessing.py','cyp/data/feature_engineering.py'],['cyp/models/convnet.py','cyp/models/rnn.py','cyp/models/gp.py'],['run.py','cyp/models/base.py'],['cyp/models/base.py','cyp/analysis/counties_plot.py'],['cyp/analysis/counties_plot.py','index.html']],
'currency-note-recognition-for-visually-impaired':[['Currency Detection using OpenCV in ML/detect.py','Currency Detection using OpenCV in ML/utils.py'],['Currency Detection using OpenCV in ML/detect.py'],['Currency Detection using OpenCV in ML/detect.py','Currency Detection using OpenCV in ML/utils.py'],['Currency Detection using OpenCV in ML/detect.py'],['index.html','js/app.js','server.py','detector.py'],['Currency Detection using OpenCV in ML/detect.py','PROJECT_OVERVIEW.md']],
'document-plagiarism-checker':[['app.py','PROJECT_OVERVIEW.md'],['app.py'],['app.py','static/js/app.js'],['app.py','templates/index.html'],['app.py','static/js/app.js'],['test_app.py','app.py']],
'driver-drowsiness-detection':[['blinkDetect.py','PROJECT_OVERVIEW.md'],['blinkDetect.py'],['blinkDetect.py','main.py'],['streamlit_app/streamlit_app.py','streamlit_app/streamlit_app_pwa.py'],['index.html','js/app.js','streamlit_app/sw.js'],['blinkDetect.py','WORKFLOW.md'],['blinkDetect.py','streamlit_app/streamlit_app.py']],
'emotion-detection-from-text-and-face':[['backend/app.py','frontend/app/text-music/page.tsx'],['backend/app.py','backend/model_loader.py'],['backend/app.py','backend/model_loader.py','training/emotion-detection-and-music-recommendation-system.ipynb'],['backend/app.py','webui/js/app.js'],['backend/app.py','frontend/app/page.tsx','docker-compose.yml'],['backend/app.py','PROJECT_OVERVIEW.md'],['backend/model_loader.py','WORKFLOW.md']],
'face-recognition-attendance-system':[['AMS_Run.py','training.py'],['AMS_Run.py'],['AMS_Run.py','training.py','TrainingImageLabel/Trainner.yml'],['AMS_Run.py','testing.py'],['AMS_Run.py','index.html','WORKFLOW.md'],['AMS_Run.py','PROJECT_OVERVIEW.md']],
'helmet-seatbelt-violation-detection':[['source/main_app.py','source/helmet_detection_yolo8_max_accuracy.py'],['source/helmet_detection_yolo8_max_accuracy.py'],['source/helmet_detection_yolo8_max_accuracy.py'],['source/main_app.py','source/database_manager.py','source/user_authentication_v1.py'],['source/helmet_detection_yolo8_max_accuracy.py','WORKFLOW.md'],['source/main_app.py','PROJECT_OVERVIEW.md'],['source/helmet_detection_yolo8_max_accuracy.py','WORKFLOW.md']],
'loan-default-prediction':[['models.py','train_predict.py'],['train_predict.py','models.py'],['models.py','tools/lr_clf.py'],['train_predict.py','models.py'],['index.html','js/app.js','WORKFLOW.md'],['models.py','tools/lr_clf.py']],
'music-recommender-from-audio-features':[['src/main_cosine_similarity.py','src/api.py'],['src/main_cosine_similarity.py'],['src/main_cosine_similarity.py'],['src/api.py','index.html','js/app.js'],['tests/test_clean_dataset.py','tests/test_cosine_similarity.py','tests/test_artist_selection.py'],['src/api.py','PROJECT_OVERVIEW.md']],
'plant-leaf-disease-detection-cnn':[['home/models.py','home/predictor.py'],['prepare_dataset.py','Code.ipynb'],['Code.ipynb'],['Code.ipynb','train_cnn.py'],['home/views.py','home/urls.py','home/predictor.py'],['home/tests.py','home/predictor.py']],
'question-paper-generator-from-syllabus':[['content_generate.py','app.py'],['app.py','utils.py'],['content_generate.py','app.py'],['app.py','templates/index.html','templates/result.html'],['omr_generator_app.py','generator.py','omr_pdf.py'],['content_generate.py','app.py','PROJECT_OVERVIEW.md'],['WORKFLOW.md','app.py']],
'resume-screening-and-jd-matching':[['src/extractor.py','app.py'],['src/preprocessor.py','src/embedder.py'],['src/matcher.py','src/embedder.py'],['src/explainer.py','src/matcher.py'],['app.py','index.html','WORKFLOW.md'],['PROJECT_OVERVIEW.md','src/explainer.py']],
'retail-sales-forecasting':[['index.html','js/app.js','dataset/Superstore.csv'],['sql/retail_analysis.sql','run_all_queries.py','app.py'],['index.html','js/app.js','sql/retail_analysis.sql'],['index.html','js/app.js','app.py'],['WORKFLOW.md','requirements.txt','run_all_queries.py'],['js/app.js','PROJECT_OVERVIEW.md']],
'sign-language-to-text-translation':[['README.md','sign_language_translator/cli.py'],['sign_language_translator/text/tokenizer.py','sign_language_translator/text/tagger.py'],['sign_language_translator/languages/sign/mapping_rules.py','sign_language_translator/languages/sign/pakistan_sign_language.py'],['sign_language_translator/languages/sign/pakistan_sign_language.py'],['sign_language_translator/cli.py','index.html','js/app.js'],['tests/test_cli.py','sign_language_translator/text/metrics.py'],['sign_language_translator/languages/sign/pakistan_sign_language.py','PROJECT_OVERVIEW.md'],['sign_language_translator/cli.py','pyproject.toml','WORKFLOW.md']],
'stock-price-trend-predictor':[['src/features/build_features.py','README.md'],['src/data/update_data.py','src/data/make_dataset.py'],['src/features/build_features.py','notebooks/01-cpj-machine-learning.ipynb'],['notebooks/02-cpj-research-model.ipynb','notebooks/03-cpj-visualisation.ipynb'],['index.html','js/app.js','test_environment.py'],['src/features/build_features.py','notebooks/02-cpj-research-model.ipynb']],
'student-dropout-risk-prediction':[['db_creation/add_dropout_column.sql','pipeline/__1_and_2_Read_and_Describe_Data.py'],['pipeline/__1_and_2_Read_and_Describe_Data.py','pipeline/__3_Missing_Data_Processing.py'],['pipeline/__4_Generate_Features.py','pipeline/__5_Classifier.py'],['pipeline/__6_Evaluate.py','pipeline/precision_recall_population graph.py'],['index.html','js/app.js','WORKFLOW.md'],['db_creation/add_dropout_column.sql','pipeline/__6_Evaluate.py']],
'vehicle-number-plate-recognition':[['app.py','PROJECT_OVERVIEW.md'],['models/yolo.py','models/yolov5s.yaml','models/yolov5x.yaml'],['utils/helper.py','app.py'],['app.py','.streamlit/config.toml'],['app.py','WORKFLOW.md'],['app.py','PROJECT_OVERVIEW.md'],['app.py','WORKFLOW.md']],
}

# Primary symbols/cell cues keep the teaching excerpt tied to the module rather than the
# first function in a file. Empty values intentionally mean a source-document review stage.
CODE_HINTS={
'abstractive-text-summarizer':['parse_story_file','apply_transformation','forward','train','verify','evaluate'],
'college-faq-chatbot-rag':['run_ingestion','chunk_documents','_semantic_retrieve','_hybrid_retrieve','ask','run_ragas_evaluation','rewrite','Settings'],
'credit-card-fraud-detection':['new_grid_search','split_dataset','new_grid_search','save_search_results','predict_fraud','test_multiple_data_points'],
'crop-yield-prediction':['train_cnn','export','Engineer','forward','_train','analyze_results','plot_county_errors'],
'currency-note-recognition-for-visually-impaired':['detectAndCompute','BFMatcher','knnMatch','max_val','detectWithBackend','display'],
'document-plagiarism-checker':['sentence_matches','split_sentences','scan_text','plagiarism','plagiarism','test_app'],
'driver-drowsiness-detection':['eye_aspect_ratio','checkEyeStatus','getLandmarks','calculate_ear','urlsToCache','checkBlinkStatus','getLandmarks'],
'emotion-detection-from-text-and-face':['predict','predict_text','classify_emotion','get_music_by_emotion','predict','predict','load_emotion_model'],
'face-recognition-attendance-system':['take_img','take_img','trainimg','Fillattendances','trainimg','Fillattendances'],
'helmet-seatbelt-violation-detection':['process_detections','detect','process_coco_detections','login','is_model_ready','record_violation','process_detections'],
'loan-default-prediction':['DefaultClassifier','FeatureSelector','DefaultClassifier','PartialRegressor','demoSeverity','predict_proba'],
'music-recommender-from-audio-features':['recommend','for feature in acoustic_features','cosine_similarity','recommend','recommended_songs','recommend'],
'plant-leaf-disease-detection-cnn':['predict','spliting data','conv2d','model.add(Conv2D','predict','predict'],
'question-paper-generator-from-syllabus':['fetch_textbooks_list','build_prerequisite_tree','generate_content_with_ollama','generate_fib_content','OMRGenerator','sanitize_ollama_json','fetch_textbooks_list'],
'resume-screening-and-jd-matching':['extract_text_from_pdf','clean_text','rank_candidates','generate_explanation','load_models','generate_explanation'],
'retail-sales-forecasting':['loadData','SELECT','wDisc','monthlySeries','read_sql','renderKpis'],
'sign-language-to-text-translation':['translate','tokenize','restructure_sentence','tokens_to_sign_dicts','runPipeline','test_slt_translate','tokens_to_sign_dicts','slt'],
'stock-price-trend-predictor':['research','update_daily','research','sns.lineplot','main','research'],
'student-dropout-risk-prediction':['dropout','impute_mean','Classifier','plot_precision_recall_n','scoreOf','dropout'],
'vehicle-number-plate-recognition':['instantiate_model','forward','filter_text','instantiate_model','results.render','instantiate_model','download_success'],
}

SOURCES = {
'python':('Python documentation','https://docs.python.org/3/'),
'sklearn':('scikit-learn user guide','https://scikit-learn.org/stable/user_guide.html'),
'torch':('PyTorch Learn the Basics','https://docs.pytorch.org/tutorials/beginner/basics/intro.html'),
'opencv':('OpenCV documentation','https://docs.opencv.org/4.x/'),
'flask':('Flask documentation','https://flask.palletsprojects.com/'),
'privacy':('NIST Privacy Framework','https://www.nist.gov/privacy-framework'),
'fairness':('NIST AI Risk Management Framework','https://www.nist.gov/itl/ai-risk-management-framework'),
}

TITLES = {
'abstractive-text-summarizer':'FactCheck Studio: Factual Consistency and Summarization',
'college-faq-chatbot-rag':'CampusWise: College FAQ Retrieval-Augmented Generation',
'credit-card-fraud-detection':'FraudGuard: Credit Card Fraud Detection',
'crop-yield-prediction':'YieldSight: County-Level Crop Yield Prediction',
'currency-note-recognition-for-visually-impaired':'Note Sense: Currency Note Recognition',
'document-plagiarism-checker':'Similarity Radar: Document Similarity Checking',
'driver-drowsiness-detection':'Cockpit: Driver Drowsiness Detection',
'emotion-detection-from-text-and-face':'MoodTunes: Emotion Detection and Music Recommendation',
'face-recognition-attendance-system':'FAMS: Face Recognition Attendance System',
'helmet-seatbelt-violation-detection':'Signal Control Room: Helmet and Seatbelt Detection',
'loan-default-prediction':'Underwriting Desk: Loan Default Risk Modeling',
'music-recommender-from-audio-features':'Groove Observatory: Audio Feature Music Recommendation',
'plant-leaf-disease-detection-cnn':'LeafLens: Plant Leaf Disease Image Classification',
'question-paper-generator-from-syllabus':'ExamForge: Syllabus-Based Question Generation',
'resume-screening-and-jd-matching':'TalentMatch Lens: Resume and Job Description Matching',
'retail-sales-forecasting':'DemandSight: Retail Sales Analytics',
'sign-language-to-text-translation':'SignBridge: Rule-Based Sign Language Text Translation',
'stock-price-trend-predictor':'TrendCast: Stock Price Trend Research',
'student-dropout-risk-prediction':'DEWS: Student Dropout Risk Prediction',
'vehicle-number-plate-recognition':'PlateSight: Vehicle Number Plate Recognition',
}

PROJECT_INFO = {}
MODULE_FACTS = {}
PROJECT_REFERENCES = {}

GAPS = {
'abstractive-text-summarizer':['The shipped Flask endpoint is deterministic lexical consistency scoring; it does not load a neural checkpoint. The research model code is a separate, older stack and no trained checkpoint is bundled. WORKFLOW statements that contradict the API/UI implementation need review.'],
'college-faq-chatbot-rag':['A local vector database and external LLM configuration are required; retrieved snippets can still be incomplete or wrong. The static console is not the Streamlit chat backend.'],
'credit-card-fraud-detection':['A real score depends on a separately supplied model/data artifact; class imbalance means accuracy alone is misleading. Validate privacy and threshold choices before real decisions.'],
'crop-yield-prediction':['The workflow needs Earth Engine exports and large raster data not included in the package. Optional error-map dependencies are missing from the declared environment; results require spatially honest evaluation.'],
'currency-note-recognition-for-visually-impaired':['There is no trained CNN or connected web API: the detector uses ORB matching against reference images; the page is static. README claims about server/detector paths conflict with the actual tree. Hard-coded paths and optional speech dependencies require repair/review.'],
'document-plagiarism-checker':['The repository uses live web search and source-pair scoring, not the advertised TF-IDF/local corpus model. Similarity is not proof of plagiarism; provider availability and document privacy require review.'],
'driver-drowsiness-detection':['No project-specific drowsiness model is trained; desktop geometry/state logic and the MediaPipe variant differ. A missing landmark asset or camera failure prevents operation. It is a learning prototype, not a safety-certified driver aid.'],
'emotion-detection-from-text-and-face':['The expected face weights are absent and training provenance is unavailable. Facial/text emotion labels are uncertain and sensitive; no mood inference should be treated as fact.'],
'face-recognition-attendance-system':['The app uses Haar + LBPH rather than deep learning. Biometric data and attendance records need consent, access controls, retention rules, and correction paths.'],
'helmet-seatbelt-violation-detection':['Generic COCO weights do not reliably supply dedicated helmet/seatbelt classes; custom model path and deployed behavior differ. No automated output should be treated as enforcement evidence.'],
'loan-default-prediction':['The web UI is a heuristic demo, not the trained pipeline. The legacy training path requires missing CSV inputs and porting; no model artifact is supplied. Credit decisions need rigorous fairness, calibration, and legal review.'],
'music-recommender-from-audio-features':['This is deterministic cosine-neighbor ranking over a local 2,261-row, ten-feature catalogue, not a learned recommender. Catalog coverage and popularity bias limit results.'],
'plant-leaf-disease-detection-cnn':['Training notebook/code and Django interface exist, but required trained model artifacts are missing; current tests are stubs and do not prove inference. Field photos differ from curated data; diagnosis requires expert confirmation.'],
'question-paper-generator-from-syllabus':['The app depends on remote curriculum catalogue and a local Ollama llama2 service; question correctness is not guaranteed. Requirements omit dependencies noted in workflow; teacher review is mandatory.'],
'resume-screening-and-jd-matching':['The embedding model is used zero-shot and no evaluation/training data is supplied. Similarity can encode proxy bias and must not rank or reject applicants without meaningful human review.'],
'retail-sales-forecasting':['No forecasting model exists: the implementation aggregates transaction data. The ETL requires MySQL and pymysql is omitted from requirements. Seasonal prediction is an extension, not shipped behavior.'],
'sign-language-to-text-translation':['The core is rule-based gloss restructuring and token-to-clip mapping, not video recognition or general language translation. Clip coverage and dialect/culture constraints need signer review.'],
'stock-price-trend-predictor':['The source is research-oriented and the UI is static; historical signals do not establish future returns. Avoid look-ahead leakage and never present outputs as investment advice.'],
'student-dropout-risk-prediction':['The UI is a demo; the historical pipeline scripts are documented as mostly broken/legacy. Labels are an administrative rule. Risk scores must support voluntary services, not punitive decisions.'],
'vehicle-number-plate-recognition':['The repository includes YOLOv5 code and Streamlit app but model/checkpoint availability and OCR behavior need verification. Plate data is personal information; protect, minimize, and expire it.'],
}


def read(p: Path, name: str) -> str:
    try: return (p/name).read_text(encoding='utf-8-sig', errors='replace')
    except OSError: return ''
def section(text, heading):
    lines=text.splitlines(); start=next((i for i,x in enumerate(lines) if x.strip().lower()==heading.lower()),None)
    if start is None:return ''
    end=next((i for i in range(start+1,len(lines)) if re.match(r'^#{1,2} ',lines[i])),len(lines))
    return '\n'.join(lines[start+1:end]).strip()
def clean(s, limit=3600):
    s=re.sub(r'\n{3,}','\n\n',s.strip())
    return s[:limit] + ('\n\n[Excerpt shortened; consult the cited source guide for full detail.]' if len(s)>limit else '')
def explain_distractor(text, correct):
    if 'black box' in text: return 'Source tracing is required by the lesson: behavior must be linked to an input, transformation, output, and cited implementation.'
    if 'guarantees the behavior' in text: return 'The project has documented missing or conditional artifacts, so the lesson requires checking runtime prerequisites before claiming behavior.'
    if 'polished interface proves' in text: return 'A front end can be disconnected or static; the lesson distinguishes presentation code from the model and backend path.'
    if 'overall accuracy' in text: return 'The lesson calls for task-appropriate metrics and error analysis; one aggregate score cannot establish reliability across classes or conditions.'
    if 'calibrated probability' in text: return 'A numeric score is not automatically calibrated; the lesson explicitly warns against turning an unvalidated score into a decision.'
    if 'real identifiable user records' in text: return 'This violates the lesson’s data-minimization guidance; use synthetic or consented data and avoid sensitive logs.'
    if 'expected successful input' in text: return 'The taught test plan includes edge and missing-resource cases, not only the happy path.'
    if 'project title is sufficient evidence' in text: return 'Titles and catalog descriptions are not implementation evidence; the lesson requires checking source files and workflow documentation.'
    if 'Future work' in text: return 'The lesson requires marking proposed work separately; roadmap language does not establish shipped functionality.'
    return 'This incorrectly treats a mixed pipeline as wholly learned; inspect each stage because rules, retrieval, interfaces, and models may differ.'
def source_snippet(project, paths, topic, meaning, hint=''):
    stop={'the','and','for','from','with','into','this','that','when','what','which','actual','project','module','source','stage','pipeline','system','using','versus','based','problem','task','input','output'}
    terms={x for x in re.findall(r'[a-z][a-z0-9_]{2,}',(topic+' '+meaning).lower()) if x not in stop}
    aliases={
        'aspect':['ear','eye_aspect_ratio','landmark'], 'drowsiness':['drowsy','closed','counter','alarm','ear'], 'state':['checkEyeStatus','checkBlinkStatus','threshold','counter'],
        'cascade':['detectmultiscale','cascadeclassifier','face'], 'haar':['detectmultiscale','cascadeclassifier'],
        'lbph':['lbph','recognizer','train'], 'attendance':['attendance','markattendance','csv'], 'capture':['take_img','detectMultiScale','TrainingImage'],
        'orb':['orb_create','detectandcompute','keypoints','descriptors'], 'keypoints':['orb_create','detectandcompute','keypoints','descriptors'],
        'knn':['knnmatch','bfmatcher','ratio','distance'], 'ratio':['knnmatch','0.789','distance'], 'voting':['max_val','max_pt','good_matches','training_set'],
        'imbalanced':['class_weight','logisticregression','fraud','threshold'], 'fraud':['class_weight','logisticregression','fraud'],
        'segmentation':['sentence','segment','query','split'], 'querying':['sentence','segment','query'],
        'similarity':['similarity','cosine','rank','score'], 'ranking':['similarity','cosine','rank','sort_values'],
        'cosine':['cosine_similarity','similarity','rank'], 'cleaning':['clean','normalize','minmax','deduplicate'],
        'etl':['mysql','sql','query','database','read_sql'], 'aggregation':['groupby','sum','mean','group by'],
        'syllabus':['chapter','textbook','subject','fetch'], 'chapter':['chapter','textbook','subject'],
        'generation':['ollama','prompt','generate','question'], 'prompt':['ollama','prompt','messages'],
        'yolov8x':['yolo','predict','model','weights'], 'helmet':['helmet','yolo','detect','violation'], 'violation':['process_detections','process_coco_detections','process_custom_helmet_detections'],
        'cnn':['conv2d','convolution','sequential','model'], 'architecture':['conv2d','convolution','sequential'],
        'crop':['crop','plate','ocr','pytesseract'], 'ocr':['filter_text','save_results','ocr_result','region_threshold'], 'plate':['filter_text','save_results','ocr_result','region_threshold'],
        'feature':['feature','scaler','normalize','minmax'], 'embedding':['embedding','sentence_transformer','encode'], 'artifact':['save_search_results','joblib','pickle','model'],
        'recommendation':['recommend','similarity','cosine','rank'], 'retrieval':['retriever','search','similarity','mmr'],
        'training':['fit(','train','optimizer','loss'], 'metrics':['precision','recall','f1','roc_auc','evaluate'],
        'severity':['severity','loss','gradientboosting','log'], 'api':['route','endpoint','request','response'],
        'preprocessing':['preprocess','transform','clean','normalize'], 'tokenization':['tokenizer','tokenize','tag'],
        'gloss':['mappingrule','mapping_rules','restructure','gloss'], 'clip':['tokens_to_sign','clip','lookup'],
    }
    for term in list(terms): terms.update(aliases.get(term,[]))
    candidates=[]
    for rel in paths:
        path=project/rel
        candidates_before=len(candidates)
        if path.suffix.lower()=='.sql':
            try: sql_lines=path.read_text(encoding='utf-8-sig',errors='replace').splitlines()
            except OSError: sql_lines=[]
            for i,line in enumerate(sql_lines):
                if hint and hint.lower() in line.lower():
                    code='\n'.join(sql_lines[max(0,i-5):min(len(sql_lines),i+10)])
                    return rel,'sql',code
            if len(candidates)>candidates_before: continue
        if path.suffix.lower()=='.ipynb':
            try: notebook=json.loads(path.read_text(encoding='utf-8-sig'))
            except Exception: notebook={}
            for cell in notebook.get('cells',[]):
                if cell.get('cell_type')!='code': continue
                code=''.join(cell.get('source',[])); score=sum(1 for term in terms if term in code.lower())
                if hint and hint.lower() in code.lower():
                    score+=100
                    code_lines=code.splitlines()
                    hit=next(i for i,line in enumerate(code_lines) if hint.lower() in line.lower())
                    code='\n'.join(code_lines[max(0,hit-5):min(len(code_lines),hit+12)])
                if score>0 and len(code.strip())>35: candidates.append((score,rel,'python',code[:1800]))
            continue
        if path.suffix.lower() not in {'.py','.js','.ts','.tsx'}: continue
        try: lines=path.read_text(encoding='utf-8-sig',errors='replace').splitlines()
        except OSError: continue
        if path.suffix=='.py':
            try:
                with warnings.catch_warnings():
                    warnings.simplefilter('ignore',SyntaxWarning)
                    tree=ast.parse('\n'.join(lines))
                nodes=[n for n in ast.walk(tree) if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef,ast.ClassDef)) and n.name!='main']
                for n in nodes:
                    lo=n.lineno-1; hi=min(len(lines),getattr(n,'end_lineno',n.lineno+10),lo+20)
                    code='\n'.join(lines[lo:hi]); searchable=(n.name+' '+code).lower()
                    if hint and hint.lower()==n.name.lower() and len(code.strip())>35:
                        return rel,'python',code
                    score=sum(1 for term in terms if term in searchable)
                    if hint and hint.lower() in (n.name+' '+code).lower(): score+=20
                    if hint and hint.lower()==n.name.lower(): score+=100
                    if score>0 and len(code.strip())>35: candidates.append((score,rel,'python',code))
            except SyntaxError: pass
        for i,line in enumerate(lines):
            if re.search(r'\b(function|const|let|class|async)\b',line) and not line.lstrip().startswith(('//','*')):
                code='\n'.join(lines[i:min(len(lines),i+18)]); score=sum(1 for term in terms if term in code.lower())
                if hint and hint.lower() in code.lower(): score+=20
                if hint and (re.search(r'\bfunction\s+'+re.escape(hint)+r'\b',line,re.I) or re.search(r'\b(?:const|let|var)\s+'+re.escape(hint)+r'\b',line,re.I) or re.search(r'\b'+re.escape(hint)+r'\s*=',line,re.I)):
                    return rel,'javascript',code
                if score>0: candidates.append((score,rel,'javascript',code))
        if path.suffix.lower()=='.py' and len(candidates)==candidates_before:
            for i,line in enumerate(lines):
                if hint and hint.lower() in line.lower():
                    lo=max(0,i-4); code='\n'.join(lines[lo:min(len(lines),i+10)])
                    candidates.append((100+sum(1 for term in terms if term in code.lower()),rel,'python',code))
                    continue
                if i%5==0:
                    code='\n'.join(lines[i:min(len(lines),i+14)]); score=sum(1 for term in terms if term in code.lower())
                    if score>0:candidates.append((score,rel,'python',code))
    if candidates:
        candidates.sort(key=lambda item:(item[0],-len(item[3])),reverse=True)
        score,rel,lang,code=candidates[0]
        if score>0:return rel,lang,code
    return None

def relevant_overview_fact(algorithm, topic, meaning, fallback=''):
    chunks=[x.strip() for x in re.split(r'\n(?=###? )',algorithm) if x.strip()]
    generic={'the','and','for','from','with','into','this','that','what','which','project','module','source','stage','system','using','based','prediction','predictor','model','learning','classification','classifier','algorithm','analysis','evaluation','training','result','results','feature','features','data','workflow','pipeline','implementation','content','safety','operations','extension','extensions','application','actual','versus','label','labels','metric','metrics','performance','accuracy','threshold','decision','decisions','fairness','privacy','risk','risks','testing','debugging','reproducibility','uncertainty','score','scores','validation','boundaries','limit','limits','basic','advanced','output','outputs','input','inputs','topic','concept','concepts','business','question','questions','objective','problem','extension','extensions'}
    terms={x for x in re.findall(r'[a-z][a-z0-9_]{2,}',(topic+' '+meaning).lower()) if x not in generic}
    if not chunks:return ''
    scored=[]
    for chunk in chunks:
        head=chunk.splitlines()[0].lower(); content=chunk.lower()
        head_hits=sum(term in head for term in terms); body_hits=sum(term in content for term in terms)
        score=3*head_hits+body_hits
        scored.append((score,head_hits,body_hits,chunk))
    scored.sort(key=lambda x:x[0],reverse=True)
    best=scored[0]
    # A heading match is the strongest topic-alignment signal. If the source guide
    # only matches on broad body words, use the mapped code excerpt instead.
    return clean(best[3],1100) if best[1]>0 else ''
def write(path, content):
    path.parent.mkdir(parents=True,exist_ok=True); path.write_text(content.rstrip()+'\n',encoding='utf-8')
def relfiles(p):
    skip={'.git','.venv','venv','__pycache__','node_modules','chroma_db','uploads','data','models'}
    out=[]
    for f in sorted(p.rglob('*')):
        if f.is_file() and not any(x in skip for x in f.relative_to(p).parts[:-1]) and len(f.relative_to(p).parts)<=5:
            if f.suffix.lower() in {'.py','.ipynb','.html','.js','.ts','.tsx','.sql','.yaml','.yml','.toml','.json'} or f.name in {'README.md','WORKFLOW.md','PROJECT_OVERVIEW.md','requirements.txt','environment.yml'}:
                out.append(f.relative_to(p).as_posix())
    return out

def build(project):
    slug=project.name
    readme=read(project,'README.md'); overview=read(project,'PROJECT_OVERVIEW.md') or readme; workflow=read(project,'WORKFLOW.md') or readme
    target=TARGET/'projects'/slug
    if target.exists(): shutil.rmtree(target)
    target.mkdir(parents=True)
    title=TITLES[slug]; curriculum=CURRICULA[slug]
    meta={}
    try: meta=json.loads(read(project,'project-metadata.json'))
    except Exception: pass
    info=PROJECT_INFO.get(slug,{})
    description=(meta.get('description') or meta.get('summary') or info.get('description') or '').strip()
    if len(description)<40:
        summary=section(overview,'## Project Summary') or section(overview,'## 1. Project Summary') or section(overview,'## Overview')
        cells=[]
        for line in summary.splitlines():
            if '|' in line:
                parts=[x.strip() for x in line.strip().strip('|').split('|')]
                if not parts or all(re.fullmatch(r':?-{2,}:?',x or '-') for x in parts): continue
                if parts[0].lower() in {'field','item'}: continue
                cells.extend(parts[1:] if len(parts)>1 else parts)
            elif line.strip(): cells.append(line.strip())
        summary=' '.join(cells)
        summary=re.sub(r'\[([^\]]+)\]\([^)]+\)',r'\1',summary)
        summary=re.sub(r'[`*_]','',summary)
        summary=re.sub(r'\s+',' ',summary).strip(' |:-')
        description=summary[:700].strip()
    if len(description)<40:
        description=f'A source-grounded learning package for {title}, based on the supplied repository.'
    stack=list(info.get('stack',[]))
    req=read(project,'requirements.txt') or read(project,'environment.yml')
    if not stack:
        for line in req.splitlines():
            x=line.strip()
            if x and not x.startswith(('#','-','name:','channels:','dependencies:')) and len(stack)<14: stack.append(x[:90])
    if not stack: stack=['See source project dependency manifest and setup guide']
    brief=' '.join(line.lstrip('> ').strip() for line in readme.splitlines() if line.startswith('> '))
    problem=section(overview,'## Problem Statement') or section(overview,'## 2. Problem Statement') or info.get('problem') or brief or description
    existing=section(overview,'### Existing (verified in the code)') or section(overview,'### Existing (verified in source)') or section(overview,'### Existing (verified in code)') or info.get('features','')
    future=section(overview,'### Future / not built') or section(overview,'### Future / not implemented') or section(overview,'### Future (not present)') or section(overview,'### Future (not in repository)') or '\n'.join('- '+x for x in info.get('gaps',[])) or section(readme,'## Notes and limitations')
    architecture=section(overview,'## System Architecture') or section(overview,'## 5. System Architecture') or info.get('data_flow','') or section(readme,'## Structure')
    algorithm='\n\n'.join(x for x in [section(overview,'## Machine Learning or Algorithm Explanation'),section(overview,'## 7. Machine Learning or Algorithm Explanation')] if x)
    fileguide=section(overview,'## File-by-File Code Guide') or section(overview,'## 8. File-by-File Code Guide')
    flow=section(overview,'## Data Flow') or section(overview,'## 9. Data Flow')
    refs=[{'title':n,'url':u,'type':'official-documentation'} for n,u in PROJECT_REFERENCES.get(slug,[SOURCES['python'],SOURCES['sklearn'],SOURCES['torch'],SOURCES['privacy'],SOURCES['fairness']])]
    sourcepaths=relfiles(project)
    outcomes=[f'Explain the implementation stages of {title} using named source files.', 'Separate model or algorithm behavior from its interface, data pipeline, and configured dependencies.', 'Inspect likely failure modes, metrics, limitations, privacy, and human-review needs appropriate to the application.', 'Propose a reproducible, source-aligned extension and test plan.']
    write(target/'project.json',json.dumps({'title':title,'slug':slug,'description':description,'problem_solved':clean(problem,1600),'target_audience':'Intermediate learners with basic Python familiarity; some projects require additional math, data, or system prerequisites.','technology_stack':stack,'difficulty_level':'intermediate to advanced','prerequisites':['Python fundamentals and command-line use','Basic data handling and charts','Introductory probability and supervised learning; read the project prerequisite guide for project-specific needs'],'learning_outcomes':outcomes,'estimated_completion_time':'18–30 hours, depending on optional data/model downloads','content_schema_version':'1.0.0'},indent=2))
    write(target/'README.md',f"""# {title}\n\n## Overview and purpose\n\n{clean(description,1000)}\n\n## Real-world context and scope\n\n{clean(problem,1500)}\n\nThe material describes the repository as supplied. **Implemented behavior** is based on the source README and entry points; **proposed or missing functionality** is listed separately below. Do not infer production readiness from a polished interface or project title.\n\n### Verified implementation notes\n\n{clean(existing or 'Read the matching source README and cited implementation files for the implementation inventory.',2400)}\n\n### Proposed, absent, or uncertain behavior\n\n{clean(future or '\n'.join('- '+x for x in GAPS[slug]),1800)}\n\n## Technology stack\n\n{chr(10).join('- `'+x+'`' for x in stack)}\n\n## System requirements and setup\n\nUse a supported Python environment appropriate to the source dependency pins. Some projects also require data files, trained weights, external APIs, cameras, GPU resources, a database, or an LLM runtime. These are identified in `setup-guide.md`; they are not assumed to be included. Follow the setup instructions in the source `README.md` and do not paste credentials into tracked files.\n\n## Architecture and important components\n\n{clean(architecture,2600) or 'See source architecture guide and module lessons.'}\n\n## Directory structure\n\nSource paths central to the learning material:\n\n{chr(10).join('- `'+x+'`' for x in sourcepaths[:60])}\n\n## Installation, environment, and database\n\nSee [`setup-guide.md`](setup-guide.md) for repository-specific commands, environment variables, optional services, and data/model requirements. Database setup is only applicable when the source workflow documents a database.\n\n## Testing\n\nUse only tests and checks present in the source repository. This learning package has not run the source application or trained a model. Expected test behavior and missing coverage are described in the source README and lessons.\n\n## Security, privacy, and responsible use\n\nTreat credentials, uploaded data, biometric data, student/financial records, and generated outputs as sensitive where relevant. Apply data minimization, consent and access controls, retention limits, secure secret handling, documented error handling, and human review. For consequential decisions, model outputs are educational signals only. Project-specific hazards appear in the final project guide and source review report.\n\n## Troubleshooting\n\nStart with missing assets and dependency versions, then validate input shape/schema, check configured API/database/model services, inspect logs, and compare observed behavior with the exact source path described in `architecture.md`. Many repositories contain a static UI or stub that is not wired to the model.\n\n## Expected outcome\n\nComplete the final project to explain and reproduce the repository's actual data-to-output path, demonstrate a tested source-aligned extension, and document its limitations.\n\n## Further learning\n\nSee `references.json` for official framework references and the source repository README plus cited files for implementation details.\n""")
    write(target/'prerequisites.md',f"""# Prerequisites — {title}\n\n## Skills\n- Python functions, modules, exceptions, and virtual environments.\n- Reading JSON, CSV, images, API requests, or model artifacts as applicable to the source.\n- Basic train/validation/test separation, metrics, and error analysis.\n- Command-line navigation and careful handling of sensitive input.\n\n## Project-specific preparation\n\n{clean((read(project,'WORKFLOW.md') or readme)[:2600],2600) or 'Inspect the source README and dependency manifest before setup. Identify required datasets, weights, external services, and hardware.'}\n\n## Readiness check\n\nBefore starting, locate the documented entry point, identify any unavailable artifact, and explain what output the repository can produce without that artifact.\n""")
    write(target/'setup-guide.md',f"""# Setup guide — {title}\n\n1. Obtain the matching source project and inspect `README.md`, `requirements.txt`, and the cited implementation files.\n2. Create a fresh virtual environment using the source's documented Python version. Do not reuse an unknown environment.\n3. Install only declared dependencies using the repository's own instructions; compare requirements with actual imports.\n4. Prepare datasets, checkpoints, API keys, database, camera, or local model runtime only if the source README or code requires them. Keep secrets out of source control.\n5. Start the documented backend/CLI/desktop app in the documented order. A static UI may not connect to a backend.\n6. Run source tests only after dependencies and data are present; separately verify the expected interface response and a known example.\n\n## Source setup notes\n\n{clean(workflow[:7600],7600) or 'The source has no complete setup guide. Review manifests and imports, then record a reproducible environment before attempting execution.'}\n\n## Known setup risks\n\n{chr(10).join('- '+x for x in GAPS[slug])}\n""")
    write(target/'architecture.md',f"""# Architecture — {title}\n\n## Component map\n\n{clean(architecture,4500) or clean(section(overview,'## System Architecture') or overview[:3000],3000)}\n\n## Data and control flow\n\n{clean(flow,3200) or 'Use the project-specific lessons to trace input → preprocessing → algorithm/model → postprocessing → presentation. Verify each transition against the listed source files.'}\n\n## Algorithm/model details\n\n{clean(algorithm,6000) or 'The source README and implementation files define the behavior taught here; the lesson cites the selected code path and marks unavailable features explicitly.'}\n\n## Source inventory\n\n{clean(fileguide,4200) or chr(10).join('- `'+x+'`' for x in sourcepaths[:70])}\n\n## Implemented versus proposed\n\nImplemented behavior is limited to the source entry points and code paths described above.\n\n{chr(10).join('- '+x for x in GAPS[slug])}\n""")
    gloss_terms={'feature':'A measurable input value supplied to an algorithm.','label':'The target category/value a supervised model learns to predict.','inference':'Using an already configured model or algorithm to produce an output.','threshold':'A cutoff that turns a score into a category or action.','leakage':'Information from outside the permitted training period/split that makes evaluation unrealistically easy.','baseline':'A simple comparison method that helps reveal whether a complex method adds value.','artifact':'A file such as a checkpoint, dataset, or index that the program needs at runtime.','human review':'A qualified person checks context and corrects or rejects an automated suggestion.'}
    write(target/'glossary.md','# Glossary\n\n'+ '\n'.join(f'## {k.title()}\n\n{v}\n' for k,v in gloss_terms.items())+'\n## Project terms\n\nRead module lessons for domain-specific terms, algorithm names, tensor shapes, and file contracts.\n')
    write(target/'references.json',json.dumps({'project_slug':slug,'references':[{'title':'Source project README','url':'../README.md','type':'package-documentation'},{'title':'Source project workflow','url':'../setup-guide.md','type':'package-documentation'},*refs]},indent=2))
    allfacts=[]
    for mi,(mtopic,meaning) in enumerate(curriculum,1):
        mid=f'{slug}-module-{mi:02d}'; mdir=target/'modules'/f'module-{mi:02d}'; (mdir/'lessons').mkdir(parents=True); (mdir/'exercises').mkdir()
        proposed=SOURCE_MAP.get(slug,[])
        srcfiles=proposed[mi-1] if mi<=len(proposed) else ['PROJECT_OVERVIEW.md']
        srcfiles=[x for x in srcfiles if (project/x).is_file()]
        if not srcfiles: srcfiles=['PROJECT_OVERVIEW.md']
        srcfile='; '.join(srcfiles)
        lesson_ids=[f'lesson-{mi:02d}-{j:02d}' for j in range(1,4)]
        objectives=[f'Explain {meaning} in plain language and connect it to {srcfile}.',f'Trace one input through the {mtopic.lower()} stage and identify its output and assumptions.',f'Diagnose one failure mode or limitation before extending this stage.']
        hint=CODE_HINTS.get(slug,[])[mi-1] if mi<=len(CODE_HINTS.get(slug,[])) else ''
        localfacts=[]
        focus=[f'Understand {meaning}',f'Inspect the project implementation of {mtopic.lower()}',f'Validate outputs and identify limitations for {mtopic.lower()}']
        snippet=source_snippet(project,srcfiles,mtopic,meaning,hint)
        focus_file=snippet[0] if snippet else srcfiles[0]
        codefact=relevant_overview_fact(algorithm,mtopic,meaning)
        if codefact:
            codefact += f'\n\nConnect this explanation to `{snippet[0] if snippet else srcfiles[0]}` and the source focus `{hint}`.'
        else:
            codefact=f'The source-specific focus for this module is `{hint}` in `{snippet[0] if snippet else srcfiles[0]}`. Use the excerpt below to trace the actual inputs, transformation, and output for {meaning}. Where a behavior is absent, follow the documented boundary rather than assuming it exists.'
        code_example=(f"Source excerpt from `{snippet[0]}` (not executed during package generation):\n\n```{snippet[1]}\n{snippet[2].strip()}\n```\n\nRead the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation." if snippet else "```python\ndef inspect_input(value):\n    # Pseudocode only: find and use the real project function in the cited files.\n    if value is None:\n        raise ValueError('input is required')\n    return project_specific_stage(value)\n```\n\nThis is teaching pseudocode, not a source function. `project_specific_stage` is a placeholder; locate the real implementation before adapting it.")
        write(mdir/'module.json',json.dumps({'module_id':mid,'title':mtopic,'description':f'Begins with a plain-language explanation of {meaning}, then traces the corresponding implementation and its limits in {slug}.','learning_objectives':objectives,'prerequisites':['Read project prerequisites and the previous module when present.'],'lesson_ids':lesson_ids,'estimated_duration_minutes':150,'concepts_covered':[meaning,'source tracing','failure analysis','responsible use'],'practical_outcomes':[f'Trace the {mtopic.lower()} stage through the cited source paths.',f'Produce a small test or diagnostic for {meaning}.'],'completion_criteria':['Complete the three lessons and exercise.','Answer all ten module questions using material from these lessons.','Submit a short source citation and limitation note.'],'source_files':srcfiles,'source_code_focus':{'symbol_or_search_term':hint or 'source implementation and documented boundary','excerpt_file':snippet[0] if snippet else None}},indent=2))
        for j,lid in enumerate(lesson_ids,1):
            fact=codefact if j==2 else f'{focus[j-1]}. In this repository, the claim must be grounded in the documented behavior and source paths: {srcfile}.'
            localfacts.append(fact)
            lesson=f"""# {mtopic}: {focus[j-1]}\n\n**Lesson ID:** `{lid}`  \n**Module:** {mtopic}  \n**Source focus:** `{srcfiles[0]}` → `{hint or 'source behavior and limitations'}`\n\n## Purpose and learning objectives\n\nThis lesson begins with an everyday explanation and then follows the implementation used by {title}. By the end, you can describe {meaning}, trace the {mtopic.lower()} implementation to source code, and identify one way it can fail.\n\n## Prerequisites\n\nBasic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.\n\n## The idea in plain language\n\nIn everyday language, this module is about {meaning}. First understand what information enters this stage, what it changes, and what it sends onward.\n\n## What this project actually implements\n\n{codefact}\n\nThis is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: {GAPS[slug][0]}\n\n## Step-by-step source investigation\n\n1. Open `{focus_file}` and inspect `{hint or 'the implementation described in the source guide'}`.\n2. Read its inputs and output, then follow its caller and the next step in the data flow.\n3. Record the data representation at each boundary (text, image, table, vector, score, or response).\n4. Inspect validation, fallback, and exception behavior.\n5. Compare the behavior with the source `README.md` and nearby implementation; report any contradiction instead of silently choosing a claim.\n\n## Code-reading example\n\n{code_example}\n\n## Expected behavior\n\nA correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For {mtopic.lower()}, use the repository's own output format and the available test fixture where possible.\n\n## Practical exercise\n\nComplete [`exercise-{mi:02d}-{j:02d}.md`](../exercises/exercise-{mi:02d}-{j:02d}.md).\n\n## Common mistakes and debugging\n\n- Confusing a visual mockup or demo heuristic with the model/pipeline implementation.\n- Assuming an absent data file, weight, service, or credential is bundled.\n- Reporting accuracy without checking class balance, split strategy, or an appropriate baseline.\n- Editing a pipeline before establishing input shape and output contract.\n- Treating confidence/similarity as calibrated probability or proof.\n\n## Best practices and responsible use\n\nKeep data provenance and split boundaries explicit, make errors visible, log no sensitive raw inputs unnecessarily, and retain a human correction path for consequential outputs. Test failure and missing-artifact cases as well as the happy path.\n\n## Summary\n\nYou can now {focus[j-1].lower()}, identify its source location, and state a limitation. The key project-specific fact is: {fact}\n\n## Knowledge check\n\n1. What input enters this stage, and what output leaves it?\n2. Which source path proves the behavior?\n3. What assumption would make the output unreliable?\n\n## References\n\n- The matching source repository `README.md` and cited code files (paths relative to that repository).\n- [{SOURCES['python'][0]}]({SOURCES['python'][1]})\n- [{SOURCES['fairness'][0]}]({SOURCES['fairness'][1]})\n"""
            write(mdir/'lessons'/f'{lid}.md',lesson)
            write(mdir/'exercises'/f'exercise-{mi:02d}-{j:02d}.md',f"""# Exercise {mi:02d}.{j:02d}: {focus[j-1]}\n\n**Exercise ID:** `exercise-{mi:02d}-{j:02d}`  \n**Objective:** Demonstrate understanding of {meaning} with source evidence.  \n**Difficulty:** {'Intermediate' if j<3 else 'Advanced'}  \n**Estimated time:** {25+10*j} minutes\n\n## Problem\n\nTrace one real input through the {mtopic.lower()} portion of `{focus_file}`. Explain what the source does, distinguish verified behavior from any proposed feature, and identify an edge case.\n\n## Requirements\n- Cite at least two relevant source lines or symbols.\n- Record input, transformation, output, and failure behavior.\n- Build one small test, hand-worked example, or diagnostic appropriate to the project.\n- State whether the result is implemented, configured, or only described.\n\n## Constraints\nDo not use real personal/biometric/financial data or expose secrets. Do not claim execution unless you performed it.\n\n## Expected behavior and acceptance criteria\n- The explanation matches the cited source.\n- The example has a stated expected result and meaningful edge case.\n- A limitation and human review requirement are documented.\n\n## Hints\nStart at the documented entry point; follow one function call at a time; inspect tests and setup docs before assuming an artifact exists.\n""")
        # ten distinct questions per module, with answers drawn verbatim from lesson teaching and distractors drawn from common confusions.
        facts=[localfacts[0],codefact,localfacts[2],f'{srcfile} is the repository location to inspect for this module stage.',f'{GAPS[slug][0]}',f'The module requires tracing input, transformation, output, and failure behavior.',f'A test or diagnostic should check both expected output and an edge case.',f'An interface can be present without proving a model or backend is connected.',f'An output score is not automatically calibrated probability or proof.',f'Sensitive inputs require minimization, access controls, and a human correction path.']
        concepts=['plain-language model of the stage','source-specific algorithm behavior','edge-case reasoning','source navigation','implementation limitation','data-flow tracing','testing practice','system-boundary reasoning','score interpretation','responsible data handling']
        questions=[]; answers=[]
        for qn,correct in enumerate(facts,1):
            qid=f'{slug}-m{mi:02d}-q{qn:02d}'; lid=lesson_ids[(qn-1)%3]
            prompt_templates=[f'Which statement best explains {mtopic.lower()} in this project?',f'When inspecting {mtopic.lower()}, which implementation claim is supported by the module lessons?',f'A learner is tracing {mtopic.lower()}. Which conclusion follows from the taught source behavior?',f'Which statement is the best source-grounded interpretation of {mtopic.lower()}?',f'An engineer is reviewing {mtopic.lower()}. Which risk or limitation should be documented?',f'Which investigation step best validates {mtopic.lower()}?',f'Which test design matches the module guidance for {mtopic.lower()}?',f'A UI displays a result during {mtopic.lower()}. What can safely be concluded?',f'How should a learner interpret an output from {mtopic.lower()}?',f'Which data-handling practice is appropriate while studying {mtopic.lower()}?']
            wrongpool=[
                'The stage should be treated as a black box; source tracing does not add useful evidence.',
                'The repository guarantees the behavior even when required data, model weights, or services are missing.',
                'A polished interface proves that every advertised model and backend feature is implemented.',
                'A single overall accuracy value is sufficient to establish reliability on every population and input condition.',
                'If a score is numeric, it is a calibrated probability and can directly determine a consequential action.',
                'The safest test is to use real identifiable user records and keep them in application logs.',
                'A test only needs to cover the expected successful input; missing assets and malformed input are irrelevant.',
                'The project title is sufficient evidence of the algorithm and data flow; code and workflow documentation can be ignored.',
                'Future work described in a proposal should be reported as completed functionality.',
                'If an implementation uses a learned model anywhere, every output component is itself learned.'
            ]
            # Keep three unique distractors and rotate their choice to avoid a stable answer position.
            ds=[wrongpool[(qn+k)%len(wrongpool)] for k in range(3)]
            opts=[{'option_id':f'{qid}-o{i+1}','text':t} for i,t in enumerate([correct,*ds])]
            shift=(qn*3+mi)%4; opts=opts[shift:]+opts[:shift]
            copt=next(x['option_id'] for x in opts if x['text']==correct)
            diff='basic' if qn<=3 else ('intermediate' if qn<=8 else 'advanced')
            questions.append({'question_id':qid,'question_text':prompt_templates[(qn-1)%len(prompt_templates)],'options':opts,'difficulty_level':diff,'related_learning_objective':objectives[(qn-1)%len(objectives)],'related_lesson_id':lid})
            wrongmap={x['option_id']:explain_distractor(x['text'],correct) for x in opts if x['option_id']!=copt}
            answers.append({'question_id':qid,'correct_option_id':copt,'explanation':f'The lesson establishes that {correct[:1].lower()+correct[1:]} This is the answer that follows from the module material; check the cited source path before applying it.', 'incorrect_option_explanations':wrongmap,'concept_tested':concepts[qn-1], 'related_lesson_id':lid,'supporting_reference':srcfile})
        write(mdir/'assessment.json',json.dumps({'module_id':mid,'title':mtopic,'instructions':'Choose one best answer. Every question is based on this module; consult the lessons before answering.','questions':questions},indent=2))
        write(mdir/'answer-key.json',json.dumps({'module_id':mid,'answers':answers},indent=2))
    # final package; include requirements, milestones, rubric, and mentor checks
    write(target/'final-project'/'requirements.md',f"""# Final project requirements — {title}\n\n## Objective\n\nBuild a reproducible, source-grounded demonstration and explanation of {title}. The submission must clearly distinguish the behavior that exists in the repository from an extension proposed by the learner.\n\n## Functional requirements\n1. Trace a representative input through the implemented system and cite source files.\n2. Implement or reproduce one bounded, source-aligned feature in an isolated branch/workspace.\n3. Validate inputs and handle at least one failure mode.\n4. Present results with the required context, caveats, and human correction path.\n\n## Non-functional requirements\n- Reproducible setup with documented dependency/data/model requirements.\n- No secrets or real sensitive personal data in code, logs, or screenshots.\n- Clear separation between inference, presentation, and proposed functionality.\n- Appropriate metrics and subgroup/error checks for the domain.\n\n## Milestones\n1. Repository and artifact audit.\n2. Data-flow and architecture diagram.\n3. Minimal source-aligned implementation.\n4. Tests for normal, edge, and missing-resource cases.\n5. Evaluation, limitation, and responsible-use review.\n6. Reproducible report and demo.\n\n## Deliverables\nSource changes or a notebook; setup note; architecture/data-flow diagram; tests; small synthetic or consented data fixture; evaluation note; limitation/ethics note; demo output.\n\n## Acceptance criteria\n- Every key claim maps to source or an explicitly labeled proposal.\n- A new learner can follow setup without undisclosed credentials.\n- Tests include at least one edge case and one failure case.\n- Evaluation matches the task and data split; no unsupported performance claims.\n- The demo does not claim production or consequential-decision readiness.\n\n## Testing checklist\n- [ ] Valid input and expected output\n- [ ] Empty/malformed input\n- [ ] Missing data, model, network, or service dependency as applicable\n- [ ] Repeated run or deterministic behavior where expected\n- [ ] Privacy/security and human-review check\n\n## Extensions\nCompare a baseline; add calibrated uncertainty; improve accessibility; add monitoring/drift checks; expand a dataset only with documented provenance and permission.\n""")
    write(target/'final-project'/'evaluation-rubric.json',json.dumps({'criteria':[{'criterion':'Source fidelity','weight':25,'levels':{'excellent':'Claims and diagram match code; proposals are clearly labeled.','competent':'Most claims map to source with minor omissions.','developing':'Several claims rely on titles or stale docs.','insufficient':'Implementation is materially misrepresented.'}},{'criterion':'Implementation and reproducibility','weight':20,'levels':{'excellent':'Isolated, documented, repeatable implementation with clear dependencies.','competent':'Works with minor setup gaps.','developing':'Core steps or artifacts are unclear.','insufficient':'Cannot reproduce or relies on undisclosed resources.'}},{'criterion':'Testing and evaluation','weight':20,'levels':{'excellent':'Normal, edge, and failure cases; task-appropriate metrics and limitations.','competent':'Useful tests but limited edge coverage.','developing':'Happy-path only or weak metrics.','insufficient':'No credible validation.'}},{'criterion':'Responsible use and privacy','weight':20,'levels':{'excellent':'Specific privacy, bias, safety, and human-review controls.','competent':'Relevant risks noted.','developing':'Generic risk language.','insufficient':'Unsafe or unsupported consequential claims.'}},{'criterion':'Communication','weight':15,'levels':{'excellent':'Clear architecture, demo, and caveats.','competent':'Mostly understandable.','developing':'Important assumptions omitted.','insufficient':'Cannot explain result or scope.'}}]},indent=2))
    write(target/'final-project'/'solution-guide.md',f"""# Mentor solution guide — {title}\n\n## Review approach\n\nA strong submission follows the actual repository path rather than recreating features based on the catalogue title. Check `architecture.md`, all module source-file citations, and the source README.\n\n## Expected solution characteristics\n- Correctly identifies the algorithm/model and whether it is trained, pretrained, rule-based, retrieval-based, or only a heuristic.\n- Names required artifacts and reports absent assets honestly.\n- Keeps preprocessing consistent between training and inference.\n- Selects metrics and split strategy appropriate to class balance, chronology, geography, or group structure.\n- Includes understandable failure behavior and domain-specific ethical safeguards.\n\n## Project-specific review notes\n\n{chr(10).join('- '+x for x in GAPS[slug])}\n\nDo not award correctness for fabricated benchmark scores or claims that this package's examples ran. Review source evidence, tests, and limitations before accepting the demo.\n""")
    # manifest is created after all files; include all package-relative files except the manifest itself.
    files=sorted(x.relative_to(target).as_posix() for x in target.rglob('*') if x.is_file() and x.name!='manifest.json')
    lessons=sum(1 for x in files if '/lessons/' in x and x.endswith('.md'))
    qs=sum(len(json.loads((target/f'modules/module-{i:02d}/assessment.json').read_text())['questions']) for i in range(1,len(curriculum)+1))
    write(target/'manifest.json',json.dumps({'project_slug':slug,'content_schema_version':'1.0.0','package_version':'1.0.0','generation_timestamp':datetime.now(timezone.utc).isoformat(),'module_count':len(curriculum),'lesson_count':lessons,'assessment_question_count':qs,'included_files':files,'validation_status':'pending structural validation; educational accuracy requires human review'},indent=2))
    return target

if __name__=='__main__':
    missing=sorted(set(CURRICULA)-{p.name for p in SOURCE.iterdir() if p.is_dir()})
    if missing: raise SystemExit(f'Missing source projects: {missing}')
    built=[build(SOURCE/s) for s in CURRICULA]
    print(f'Built {len(built)} packages at {TARGET}/projects')
    total_modules=sum(len(CURRICULA[p.name]) for p in built)
    print(f'Modules: {total_modules}; lessons: {total_modules*3}; questions: {total_modules*10}')
