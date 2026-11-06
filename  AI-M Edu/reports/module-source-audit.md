# Module-to-source alignment audit

Modules audited: 130

Each entry records the module’s declared source path(s) and source symbol/search cue. Lessons start with an accessible explanation, then cite and excerpt the implementation or documented boundary. The paths are checked for existence; this report does not claim that automated checks can prove semantic correctness. Review the listed excerpts against their module title before publication.

## abstractive-text-summarizer

- **Evidence and Factuality** — `data_pairing/pair_data.py` → `parse_story_file`; mapped files: `README.md`, `data_pairing/pair_data.py`.
- **Synthetic Pair Construction** — `data_generation/create_data.py` → `apply_transformation`; mapped files: `data_generation/create_data.py`, `data_generation/augmentation_ops.py`.
- **FactCC Multi-task Model** — `modeling/model.py` → `forward`; mapped files: `modeling/model.py`, `modeling/utils.py`.
- **Research Pipeline and Data** — `modeling/run.py` → `train`; mapped files: `modeling/run.py`, `data_pairing/pair_data.py`.
- **Shipped Flask Service and Static UI** — `src/api.py` → `verify`; mapped files: `src/api.py`, `js/app.js`, `index.html`.
- **Evaluation, Limits, and Extensions** — `modeling/run.py` → `evaluate`; mapped files: `modeling/run.py`, `PROJECT_OVERVIEW.md`, `WORKFLOW.md`.

## college-faq-chatbot-rag

- **RAG and Source Documents** — `src/ingestion.py` → `run_ingestion`; mapped files: `src/document_loader.py`, `src/ingestion.py`.
- **Chunking and Embeddings** — `src/chunker.py` → `chunk_documents`; mapped files: `src/chunker.py`, `src/embeddings.py`.
- **Chroma Retrieval and MMR** — `src/retriever.py` → `_semantic_retrieve`; mapped files: `src/vector_store.py`, `src/retriever.py`.
- **Hybrid Ranking and Adaptive Retrieval** — `src/retriever.py` → `_hybrid_retrieve`; mapped files: `src/retriever.py`, `src/query_normalizer.py`.
- **Grounded Generation and Streamlit** — `src/rag_chain.py` → `ask`; mapped files: `src/rag_chain.py`, `src/prompt.py`, `app/app.py`.
- **Evaluation, Safety, and Operations** — `src/evaluation/ragas_eval.py` → `run_ragas_evaluation`; mapped files: `scripts/evaluate.py`, `src/evaluation/ragas_eval.py`.
- **Retrieval Debugging Lab** — `src/query_rewriter.py` → `rewrite`; mapped files: `src/query_rewriter.py`, `scripts/evaluate_retrieval.py`.
- **Capstone and Deployment Boundaries** — `config/settings.py` → `Settings`; mapped files: `config/settings.py`, `WORKFLOW.md`.

## credit-card-fraud-detection

- **Fraud as Imbalanced Classification** — `src/train.py` → `new_grid_search`; mapped files: `src/train.py`, `PROJECT_OVERVIEW.md`.
- **Dataset and Leakage Controls** — `src/train.py` → `split_dataset`; mapped files: `src/train.py`, `src/settings.py`.
- **Balanced Logistic Regression** — `src/train.py` → `new_grid_search`; mapped files: `src/train.py`.
- **Training and Model Artifacts** — `src/train.py` → `save_search_results`; mapped files: `src/train.py`, `src/flask_app.py`.
- **Flask Prediction API and Console** — `src/flask_app.py` → `predict_fraud`; mapped files: `src/flask_app.py`, `index.html`, `js/app.js`.
- **Metrics, Fairness, and Monitoring** — `tests/test_flask.py` → `test_multiple_data_points`; mapped files: `tests/test_flask.py`, `src/train.py`.

## crop-yield-prediction

- **County-Year Prediction Problem** — `run.py` → `train_cnn`; mapped files: `run.py`, `cyp/data/feature_engineering.py`.
- **Earth Engine and MODIS Data** — `cyp/data/exporting.py` → `export`; mapped files: `cyp/data/exporting.py`, `data/README.md`.
- **Feature Engineering and Sequences** — `cyp/data/feature_engineering.py` → `Engineer`; mapped files: `cyp/data/preprocessing.py`, `cyp/data/feature_engineering.py`.
- **Neural Architectures** — `cyp/models/convnet.py` → `forward`; mapped files: `cyp/models/convnet.py`, `cyp/models/rnn.py`, `cyp/models/gp.py`.
- **Training, Checkpoints, and Prediction** — `cyp/models/base.py` → `_train`; mapped files: `run.py`, `cyp/models/base.py`.
- **Evaluation, Uncertainty, and Reproducibility** — `cyp/models/base.py` → `analyze_results`; mapped files: `cyp/models/base.py`, `cyp/analysis/counties_plot.py`.
- **Visualization and Interpretation** — `cyp/analysis/counties_plot.py` → `plot_county_errors`; mapped files: `cyp/analysis/counties_plot.py`, `index.html`.

## currency-note-recognition-for-visually-impaired

- **Recognition Task and Reference Images** — `Currency Detection using OpenCV in ML/detect.py` → `detectAndCompute`; mapped files: `Currency Detection using OpenCV in ML/detect.py`, `Currency Detection using OpenCV in ML/utils.py`.
- **ORB Keypoints and Descriptors** — `Currency Detection using OpenCV in ML/detect.py` → `BFMatcher`; mapped files: `Currency Detection using OpenCV in ML/detect.py`.
- **KNN Matching and Ratio Test** — `Currency Detection using OpenCV in ML/detect.py` → `knnMatch`; mapped files: `Currency Detection using OpenCV in ML/detect.py`, `Currency Detection using OpenCV in ML/utils.py`.
- **Winner Voting and Filename Labels** — `Currency Detection using OpenCV in ML/detect.py` → `max_val`; mapped files: `Currency Detection using OpenCV in ML/detect.py`.
- **Detector, Assets, and Static UI** — `js/app.js` → `detectWithBackend`; mapped files: `index.html`, `js/app.js`, `server.py`, `detector.py`.
- **Accessibility, Evaluation, and Safety** — `Currency Detection using OpenCV in ML/detect.py` → `display`; mapped files: `Currency Detection using OpenCV in ML/detect.py`, `PROJECT_OVERVIEW.md`.

## document-plagiarism-checker

- **Similarity Is Not a Verdict** — `app.py` → `sentence_matches`; mapped files: `app.py`, `PROJECT_OVERVIEW.md`.
- **Sentence Segmentation and Querying** — `app.py` → `split_sentences`; mapped files: `app.py`.
- **Live Search and Source Pairing** — `app.py` → `scan_text`; mapped files: `app.py`, `static/js/app.js`.
- **Scoring and PDF/Pasted Input** — `app.py` → `plagiarism`; mapped files: `app.py`, `templates/index.html`.
- **Flask Routes and State** — `app.py` → `plagiarism`; mapped files: `app.py`, `static/js/app.js`.
- **Evaluation, Privacy, and Academic Integrity** — `test_app.py` → `test_app`; mapped files: `test_app.py`, `app.py`.

## driver-drowsiness-detection

- **Signals and Eye Aspect Ratio** — `blinkDetect.py` → `eye_aspect_ratio`; mapped files: `blinkDetect.py`, `PROJECT_OVERVIEW.md`.
- **Drowsiness State Machine** — `blinkDetect.py` → `checkEyeStatus`; mapped files: `blinkDetect.py`.
- **Desktop dlib Implementation** — `blinkDetect.py` → `getLandmarks`; mapped files: `blinkDetect.py`, `main.py`.
- **MediaPipe/Streamlit Variants** — `streamlit_app/streamlit_app.py` → `calculate_ear`; mapped files: `streamlit_app/streamlit_app.py`, `streamlit_app/streamlit_app_pwa.py`.
- **HUD, PWA, and Data Flow** — `streamlit_app/sw.js` → `urlsToCache`; mapped files: `index.html`, `js/app.js`, `streamlit_app/sw.js`.
- **Calibration, Evaluation, and Safety** — `blinkDetect.py` → `checkBlinkStatus`; mapped files: `blinkDetect.py`, `WORKFLOW.md`.
- **Debugging and Robustness** — `blinkDetect.py` → `getLandmarks`; mapped files: `blinkDetect.py`, `streamlit_app/streamlit_app.py`.

## emotion-detection-from-text-and-face

- **Emotion Labels and Modalities** — `backend/app.py` → `predict`; mapped files: `backend/app.py`, `frontend/app/text-music/page.tsx`.
- **Text Inference Pipeline** — `backend/app.py` → `predict_text`; mapped files: `backend/app.py`, `backend/model_loader.py`.
- **Face CNN Input Pipeline** — `backend/app.py` → `classify_emotion`; mapped files: `backend/app.py`, `backend/model_loader.py`, `training/emotion-detection-and-music-recommendation-system.ipynb`.
- **Music Recommendation Rules** — `backend/app.py` → `get_music_by_emotion`; mapped files: `backend/app.py`, `webui/js/app.js`.
- **Frontend, API, and Optional Infrastructure** — `backend/app.py` → `predict`; mapped files: `backend/app.py`, `frontend/app/page.tsx`, `docker-compose.yml`.
- **Evaluation, Bias, and Consent** — `backend/app.py` → `predict`; mapped files: `backend/app.py`, `PROJECT_OVERVIEW.md`.
- **End-to-End Debugging** — `backend/model_loader.py` → `load_emotion_model`; mapped files: `backend/model_loader.py`, `WORKFLOW.md`.

## face-recognition-attendance-system

- **Capture and Identity Records** — `AMS_Run.py` → `take_img`; mapped files: `AMS_Run.py`, `training.py`.
- **Haar Cascade Face Detection** — `AMS_Run.py` → `take_img`; mapped files: `AMS_Run.py`.
- **LBPH Face Representation** — `AMS_Run.py` → `trainimg`; mapped files: `AMS_Run.py`, `training.py`, `TrainingImageLabel/Trainner.yml`.
- **Attendance Matching and Persistence** — `AMS_Run.py` → `Fillattendances`; mapped files: `AMS_Run.py`, `testing.py`.
- **Desktop Workflow and Assets** — `AMS_Run.py` → `trainimg`; mapped files: `AMS_Run.py`, `index.html`, `WORKFLOW.md`.
- **Evaluation, Consent, and Security** — `AMS_Run.py` → `Fillattendances`; mapped files: `AMS_Run.py`, `PROJECT_OVERVIEW.md`.

## helmet-seatbelt-violation-detection

- **Detection Versus Violation Decision** — `source/helmet_detection_yolo8_max_accuracy.py` → `process_detections`; mapped files: `source/main_app.py`, `source/helmet_detection_yolo8_max_accuracy.py`.
- **YOLOv8x and COCO Classes** — `source/helmet_detection_yolo8_max_accuracy.py` → `detect`; mapped files: `source/helmet_detection_yolo8_max_accuracy.py`.
- **Heuristic Violation Inference** — `source/helmet_detection_yolo8_max_accuracy.py` → `process_coco_detections`; mapped files: `source/helmet_detection_yolo8_max_accuracy.py`.
- **Application, Accounts, and Database** — `source/main_app.py` → `login`; mapped files: `source/main_app.py`, `source/database_manager.py`, `source/user_authentication_v1.py`.
- **Weights, Evaluation, and Error Analysis** — `source/helmet_detection_yolo8_max_accuracy.py` → `is_model_ready`; mapped files: `source/helmet_detection_yolo8_max_accuracy.py`, `WORKFLOW.md`.
- **Safety, Privacy, and Human Review** — `source/main_app.py` → `record_violation`; mapped files: `source/main_app.py`, `PROJECT_OVERVIEW.md`.
- **Debugging the Pipeline** — `source/helmet_detection_yolo8_max_accuracy.py` → `process_detections`; mapped files: `source/helmet_detection_yolo8_max_accuracy.py`, `WORKFLOW.md`.

## loan-default-prediction

- **Target Definition and Two-Stage Loss** — `models.py` → `DefaultClassifier`; mapped files: `models.py`, `train_predict.py`.
- **Features and Data Pipeline** — `models.py` → `FeatureSelector`; mapped files: `train_predict.py`, `models.py`.
- **Class Imbalance and Logistic Baseline** — `models.py` → `DefaultClassifier`; mapped files: `models.py`, `tools/lr_clf.py`.
- **Gradient Boosting and Log Severity** — `models.py` → `PartialRegressor`; mapped files: `train_predict.py`, `models.py`.
- **Legacy Training Versus Browser Heuristic** — `js/app.js` → `demoSeverity`; mapped files: `index.html`, `js/app.js`, `WORKFLOW.md`.
- **Evaluation, Fairness, and Decision Support** — `models.py` → `predict_proba`; mapped files: `models.py`, `tools/lr_clf.py`.

## music-recommender-from-audio-features

- **Content-Based Recommendation** — `src/api.py` → `recommend`; mapped files: `src/main_cosine_similarity.py`, `src/api.py`.
- **Feature Cleaning and Scaling** — `src/main_cosine_similarity.py` → `for feature in acoustic_features`; mapped files: `src/main_cosine_similarity.py`.
- **Cosine Similarity and Ranking** — `src/main_cosine_similarity.py` → `cosine_similarity`; mapped files: `src/main_cosine_similarity.py`.
- **API and Dataset Flow** — `src/api.py` → `recommend`; mapped files: `src/api.py`, `index.html`, `js/app.js`.
- **Testing and Explanation** — `tests/test_cosine_similarity.py` → `recommended_songs`; mapped files: `tests/test_clean_dataset.py`, `tests/test_cosine_similarity.py`, `tests/test_artist_selection.py`.
- **Evaluation, Bias, and Product Limits** — `src/api.py` → `recommend`; mapped files: `src/api.py`, `PROJECT_OVERVIEW.md`.

## plant-leaf-disease-detection-cnn

- **Image Classification Problem** — `home/predictor.py` → `predict`; mapped files: `home/models.py`, `home/predictor.py`.
- **Dataset Preparation** — `Code.ipynb` → `spliting data`; mapped files: `prepare_dataset.py`, `Code.ipynb`.
- **CNN Architecture** — `Code.ipynb` → `conv2d`; mapped files: `Code.ipynb`.
- **Training and Model Artifacts** — `train_cnn.py` → `model.add(Conv2D`; mapped files: `Code.ipynb`, `train_cnn.py`.
- **Django Inference Path and Missing Assets** — `home/views.py` → `predict`; mapped files: `home/views.py`, `home/urls.py`, `home/predictor.py`.
- **Evaluation, Generalization, and Farm Safety** — `home/predictor.py` → `predict`; mapped files: `home/tests.py`, `home/predictor.py`.

## question-paper-generator-from-syllabus

- **Syllabus and Chapter Selection** — `content_generate.py` → `fetch_textbooks_list`; mapped files: `content_generate.py`, `app.py`.
- **Prerequisite Graph and Topic Selection** — `app.py` → `build_prerequisite_tree`; mapped files: `app.py`, `utils.py`.
- **Prompt Contracts and Local LLM** — `content_generate.py` → `generate_content_with_ollama`; mapped files: `content_generate.py`, `app.py`.
- **Question and Study Material Routes** — `app.py` → `generate_fib_content`; mapped files: `app.py`, `templates/index.html`, `templates/result.html`.
- **PDF/OMR Companion Tools** — `omr_pdf.py` → `OMRGenerator`; mapped files: `omr_generator_app.py`, `generator.py`, `omr_pdf.py`.
- **Evaluation, Reliability, and Teacher Review** — `app.py` → `sanitize_ollama_json`; mapped files: `content_generate.py`, `app.py`, `PROJECT_OVERVIEW.md`.
- **Setup, Testing, and Debugging** — `app.py` → `fetch_textbooks_list`; mapped files: `WORKFLOW.md`, `app.py`.

## resume-screening-and-jd-matching

- **Text Extraction and Input Boundaries** — `src/extractor.py` → `extract_text_from_pdf`; mapped files: `src/extractor.py`, `app.py`.
- **Preprocessing and Sentence Embeddings** — `src/preprocessor.py` → `clean_text`; mapped files: `src/preprocessor.py`, `src/embedder.py`.
- **Cosine Matching and Ranking** — `src/matcher.py` → `rank_candidates`; mapped files: `src/matcher.py`, `src/embedder.py`.
- **Skill-Level Explanation** — `src/explainer.py` → `generate_explanation`; mapped files: `src/explainer.py`, `src/matcher.py`.
- **Flask UI and Model Runtime** — `app.py` → `load_models`; mapped files: `app.py`, `index.html`, `WORKFLOW.md`.
- **Evaluation, Fairness, and Human Oversight** — `src/explainer.py` → `generate_explanation`; mapped files: `PROJECT_OVERVIEW.md`, `src/explainer.py`.

## retail-sales-forecasting

- **Transaction Data and Business Questions** — `js/app.js` → `loadData`; mapped files: `index.html`, `js/app.js`, `dataset/Superstore.csv`.
- **ETL and SQL Aggregation** — `sql/retail_analysis.sql` → `SELECT`; mapped files: `sql/retail_analysis.sql`, `run_all_queries.py`, `app.py`.
- **Calendar Buckets and Weighted Metrics** — `js/app.js` → `wDisc`; mapped files: `index.html`, `js/app.js`, `sql/retail_analysis.sql`.
- **Dashboard Data Flow** — `js/app.js` → `monthlySeries`; mapped files: `index.html`, `js/app.js`, `app.py`.
- **Testing and Reconciliation** — `run_all_queries.py` → `read_sql`; mapped files: `WORKFLOW.md`, `requirements.txt`, `run_all_queries.py`.
- **Forecasting Claims and Extensions** — `js/app.js` → `renderKpis`; mapped files: `js/app.js`, `PROJECT_OVERVIEW.md`.

## sign-language-to-text-translation

- **Language, Gloss, and Scope** — `sign_language_translator/cli.py` → `translate`; mapped files: `README.md`, `sign_language_translator/cli.py`.
- **Tokenization and Tagging** — `sign_language_translator/text/tokenizer.py` → `tokenize`; mapped files: `sign_language_translator/text/tokenizer.py`, `sign_language_translator/text/tagger.py`.
- **Rule-Based Gloss Restructuring** — `sign_language_translator/languages/sign/pakistan_sign_language.py` → `restructure_sentence`; mapped files: `sign_language_translator/languages/sign/mapping_rules.py`, `sign_language_translator/languages/sign/pakistan_sign_language.py`.
- **Token-to-Clip Resolution** — `sign_language_translator/languages/sign/pakistan_sign_language.py` → `tokens_to_sign_dicts`; mapped files: `sign_language_translator/languages/sign/pakistan_sign_language.py`.
- **CLI, Library, and Static Demo** — `js/app.js` → `runPipeline`; mapped files: `sign_language_translator/cli.py`, `index.html`, `js/app.js`.
- **Testing, Metrics, and Accessibility** — `tests/test_cli.py` → `test_slt_translate`; mapped files: `tests/test_cli.py`, `sign_language_translator/text/metrics.py`.
- **Model Boundaries and Extensions** — `sign_language_translator/languages/sign/pakistan_sign_language.py` → `tokens_to_sign_dicts`; mapped files: `sign_language_translator/languages/sign/pakistan_sign_language.py`, `PROJECT_OVERVIEW.md`.
- **Packaging and Reproducible Use** — `sign_language_translator/cli.py` → `slt`; mapped files: `sign_language_translator/cli.py`, `pyproject.toml`, `WORKFLOW.md`.

## stock-price-trend-predictor

- **Market Series and Prediction Scope** — `src/features/build_features.py` → `research`; mapped files: `src/features/build_features.py`, `README.md`.
- **Data Acquisition and Feature Building** — `src/data/update_data.py` → `update_daily`; mapped files: `src/data/update_data.py`, `src/data/make_dataset.py`.
- **Research Signal and Look-Ahead Bias** — `src/features/build_features.py` → `research`; mapped files: `src/features/build_features.py`, `notebooks/01-cpj-machine-learning.ipynb`.
- **Notebook Models and Visualization** — `notebooks/03-cpj-visualisation.ipynb` → `sns.lineplot`; mapped files: `notebooks/02-cpj-research-model.ipynb`, `notebooks/03-cpj-visualisation.ipynb`.
- **Static UI and Project Scripts** — `test_environment.py` → `main`; mapped files: `index.html`, `js/app.js`, `test_environment.py`.
- **Time-Series Evaluation and Financial Risk** — `src/features/build_features.py` → `research`; mapped files: `src/features/build_features.py`, `notebooks/02-cpj-research-model.ipynb`.

## student-dropout-risk-prediction

- **Outcome Labels and Policy Context** — `db_creation/add_dropout_column.sql` → `dropout`; mapped files: `db_creation/add_dropout_column.sql`, `pipeline/__1_and_2_Read_and_Describe_Data.py`.
- **Database and Data Preparation** — `pipeline/__3_Missing_Data_Processing.py` → `impute_mean`; mapped files: `pipeline/__1_and_2_Read_and_Describe_Data.py`, `pipeline/__3_Missing_Data_Processing.py`.
- **Classification Pipeline** — `pipeline/__5_Classifier.py` → `Classifier`; mapped files: `pipeline/__4_Generate_Features.py`, `pipeline/__5_Classifier.py`.
- **Metrics and Population Analysis** — `pipeline/precision_recall_population graph.py` → `plot_precision_recall_n`; mapped files: `pipeline/__6_Evaluate.py`, `pipeline/precision_recall_population graph.py`.
- **DEWS Static Interface and Pipeline Gaps** — `js/app.js` → `scoreOf`; mapped files: `index.html`, `js/app.js`, `WORKFLOW.md`.
- **Privacy, Fairness, and Supportive Use** — `db_creation/add_dropout_column.sql` → `dropout`; mapped files: `db_creation/add_dropout_column.sql`, `pipeline/__6_Evaluate.py`.

## vehicle-number-plate-recognition

- **Plate Localisation Versus Character Recognition** — `app.py` → `instantiate_model`; mapped files: `app.py`, `PROJECT_OVERVIEW.md`.
- **YOLOv5 Model Loading** — `models/yolo.py` → `forward`; mapped files: `models/yolo.py`, `models/yolov5s.yaml`, `models/yolov5x.yaml`.
- **Detection Output and Unwired OCR Helpers** — `utils/helper.py` → `filter_text`; mapped files: `utils/helper.py`, `app.py`.
- **Streamlit Application and Configuration** — `app.py` → `instantiate_model`; mapped files: `app.py`, `.streamlit/config.toml`.
- **Evaluation and Failure Analysis** — `app.py` → `results.render`; mapped files: `app.py`, `WORKFLOW.md`.
- **Privacy, Security, and Deployment** — `app.py` → `instantiate_model`; mapped files: `app.py`, `PROJECT_OVERVIEW.md`.
- **Debugging Model Assets** — `app.py` → `download_success`; mapped files: `app.py`, `WORKFLOW.md`.

