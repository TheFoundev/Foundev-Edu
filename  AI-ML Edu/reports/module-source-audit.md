# Module-to-source alignment audit

## Batch 1 — 20-project library

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

---

## Batch 2 — 36-project library

Modules audited: 247

Each entry records the module’s declared source path(s) and source symbol/search cue. Lessons start with an accessible explanation, then cite and excerpt the implementation or documented boundary. The paths are checked for existence; this report does not claim that automated checks can prove semantic correctness. Review the listed excerpts against their module title before publication.

## abstractive-document-summarization

- **Task, Input Contract, and Source Scope** — `main.py` → `main`; mapped files: `README.md`, `main.py`.
- **Dataset Generation, Labels, and Splits** — `src/data.py` → `load_data`; mapped files: `src/data.py`.
- **Features and Intermediate Representation** — `src/data.py` → `split_sentences`; mapped files: `src/data.py`, `src/model.py`.
- **Core Algorithm and Model Mechanics** — `src/model.py` → `score_length`; mapped files: `src/model.py`.
- **Training, Metrics, and Validation** — `src/model.py` → `rouge_l`; mapped files: `src/model.py`, `tests/test_pipeline.py`.
- **Inference, Demo, Tests, and Responsible Limits** — `app.py` → `api_summarize`; mapped files: `app.py`, `main.py`, `tests/test_pipeline.py`, `README.md`.

## algorithmic-trading-signals

- **Task, Input Contract, and Source Scope** — `main.py` → `main`; mapped files: `README.md`, `main.py`.
- **Dataset Generation, Labels, and Splits** — `src/data.py` → `load_data`; mapped files: `src/data.py`.
- **Features and Intermediate Representation** — `src/data.py` → `make_prices`; mapped files: `src/data.py`, `src/model.py`.
- **Temporal Targets, Backtesting, and Risk** — `src/model.py` → `forward_returns`; mapped files: `src/model.py`.
- **Training, Metrics, and Validation** — `tests/test_pipeline.py` → `test_the_rsi_of_a_rising_series_is_high`; mapped files: `src/model.py`, `tests/test_pipeline.py`.
- **Inference, Demo, and User Interface** — `web/api_impl.py` → `summary`; mapped files: `web/api_impl.py`, `main.py`.
- **Tests, Limitations, and Responsible Extensions** — `tests/test_pipeline.py` → `test_the_rsi_of_a_falling_series_is_low`; mapped files: `tests/test_pipeline.py`, `README.md`, `src/model.py`.

## autonomous-driving-perception

- **Task, Input Contract, and Source Scope** — `main.py` → `main`; mapped files: `README.md`, `main.py`.
- **Dataset Generation, Labels, and Splits** — `src/data.py` → `load_data`; mapped files: `src/data.py`.
- **Features and Intermediate Representation** — `src/data.py` → `make_scene`; mapped files: `src/data.py`, `src/model.py`.
- **Lane and Vehicle Perception Boundaries** — `src/model.py` → `detect_vehicles`; mapped files: `src/model.py`.
- **Training, Metrics, and Validation** — `src/model.py` → `evaluate`; mapped files: `src/model.py`, `tests/test_pipeline.py`.
- **Inference, Demo, and User Interface** — `web/api_impl.py` → `summary`; mapped files: `web/api_impl.py`, `main.py`.
- **Tests, Limitations, and Responsible Extensions** — `tests/test_pipeline.py` → `test_the_lane_iou_of_two_masks_that_do_not_touch_is_zero`; mapped files: `tests/test_pipeline.py`, `README.md`, `src/model.py`.

## detectron2-instance-segmentation

- **Task, Input Contract, and Source Scope** — `main.py` → `main`; mapped files: `README.md`, `main.py`.
- **Dataset Generation, Labels, and Splits** — `src/data.py` → `load_data`; mapped files: `src/data.py`.
- **Features and Intermediate Representation** — `src/data.py` → `make_sample`; mapped files: `src/data.py`, `src/model.py`.
- **Core Algorithm and Model Mechanics** — `src/model.py` → `segment`; mapped files: `src/model.py`.
- **Training, Metrics, and Validation** — `src/model.py` → `evaluate`; mapped files: `src/model.py`, `tests/test_pipeline.py`.
- **Inference, Demo, Tests, and Responsible Limits** — `web/api_impl.py` → `summary`; mapped files: `web/api_impl.py`, `main.py`, `tests/test_pipeline.py`, `README.md`.

## end-to-end-speech-recognition-with-speechbrain

- **Task, Input Contract, and Source Scope** — `main.py` → `main`; mapped files: `README.md`, `main.py`.
- **Dataset Generation, Labels, and Splits** — `src/data.py` → `load_data`; mapped files: `src/data.py`.
- **Features and Intermediate Representation** — `src/data.py` → `features`; mapped files: `src/data.py`, `src/model.py`.
- **Core Algorithm and Model Mechanics** — `src/model.py` → `train`; mapped files: `src/model.py`.
- **Training, Metrics, and Validation** — `tests/test_pipeline.py` → `test_the_data_is_split_in_two`; mapped files: `src/model.py`, `tests/test_pipeline.py`.
- **Inference, Demo, and User Interface** — `web/api_impl.py` → `summary`; mapped files: `web/api_impl.py`, `main.py`.
- **Tests, Limitations, and Responsible Extensions** — `tests/test_pipeline.py` → `test_the_features_have_the_size_that_was_asked_for`; mapped files: `tests/test_pipeline.py`, `README.md`, `src/model.py`.

## facial-attribute-analysis-kiosk

- **Task, Input Contract, and Source Scope** — `main.py` → `main`; mapped files: `README.md`, `main.py`.
- **Dataset Generation, Labels, and Splits** — `src/data.py` → `load_data`; mapped files: `src/data.py`.
- **Features and Intermediate Representation** — `src/data.py` → `draw_face`; mapped files: `src/data.py`, `src/model.py`.
- **Core Algorithm and Model Mechanics** — `src/model.py` → `train`; mapped files: `src/model.py`.
- **Training, Metrics, and Validation** — `tests/test_pipeline.py` → `test_the_face_is_drawn_with_the_two_attributes`; mapped files: `src/model.py`, `tests/test_pipeline.py`.
- **Inference, Demo, Tests, and Responsible Limits** — `app.py` → `summary`; mapped files: `app.py`, `main.py`, `tests/test_pipeline.py`, `README.md`.

## gan-image-generation

- **Task, Input Contract, and Source Scope** — `main.py` → `main`; mapped files: `README.md`, `main.py`.
- **Dataset Generation, Labels, and Splits** — `src/data.py` → `load_data`; mapped files: `src/data.py`.
- **Features and Intermediate Representation** — `src/data.py` → `make_images`; mapped files: `src/data.py`, `src/model.py`.
- **Generator and Discriminator Roles** — `src/model.py` → `build_generator`; mapped files: `src/model.py`.
- **Adversarial Training and Sample Review** — `src/model.py` → `train`; mapped files: `src/model.py`.
- **Training, Metrics, and Validation** — `tests/test_pipeline.py` → `test_the_generator_makes_an_image_of_the_right_size`; mapped files: `src/model.py`, `tests/test_pipeline.py`.
- **Inference, Demo, and User Interface** — `web/api_impl.py` → `summary`; mapped files: `web/api_impl.py`, `main.py`.
- **Tests, Limitations, and Responsible Extensions** — `tests/test_pipeline.py` → `test_the_discriminator_says_how_real_an_image_is`; mapped files: `tests/test_pipeline.py`, `README.md`, `src/model.py`.

## hybrid-recommender-with-content-features

- **Task, Input Contract, and Source Scope** — `main.py` → `main`; mapped files: `README.md`, `main.py`.
- **Dataset Generation, Labels, and Splits** — `src/data.py` → `load_data`; mapped files: `src/data.py`.
- **Features and Intermediate Representation** — `src/data.py` → `make_catalog`; mapped files: `src/data.py`, `src/model.py`.
- **Collaborative and Content Scores** — `src/model.py` → `recommend`; mapped files: `src/model.py`.
- **Training, Metrics, and Validation** — `src/model.py` → `precision_at_k`; mapped files: `src/model.py`, `tests/test_pipeline.py`.
- **Inference, Demo, and User Interface** — `web/api_impl.py` → `summary`; mapped files: `web/api_impl.py`, `main.py`.
- **Tests, Limitations, and Responsible Extensions** — `tests/test_pipeline.py` → `test_the_precision_is_a_share`; mapped files: `tests/test_pipeline.py`, `README.md`, `src/model.py`.

## hyperparameter-optimization-service

- **Task, Input Contract, and Source Scope** — `main.py` → `main`; mapped files: `README.md`, `main.py`.
- **Dataset Generation, Labels, and Splits** — `src/data.py` → `load_data`; mapped files: `src/data.py`.
- **Trial Storage and Search Parameters** — `src/model.py` → `ensure_db`; mapped files: `src/data.py`, `src/model.py`.
- **Trial Persistence and Search API** — `app.py` → `search`; mapped files: `app.py`.
- **Training, Metrics, and Validation** — `tests/test_pipeline.py` → `test_the_trials_are_written_in_the_database`; mapped files: `src/model.py`, `tests/test_pipeline.py`.
- **Inference, Demo, and User Interface** — `app.py` → `trials`; mapped files: `app.py`, `main.py`.
- **Tests, Limitations, and Responsible Extensions** — `tests/test_pipeline.py` → `test_the_trials_of_the_runs_add_up`; mapped files: `tests/test_pipeline.py`, `README.md`, `src/model.py`.

## image-super-resolution-enhancer

- **Task, Input Contract, and Source Scope** — `main.py` → `main`; mapped files: `README.md`, `main.py`.
- **Dataset Generation, Labels, and Splits** — `src/data.py` → `load_data`; mapped files: `src/data.py`.
- **Features and Intermediate Representation** — `src/data.py` → `make_image`; mapped files: `src/data.py`, `src/model.py`.
- **Core Algorithm and Model Mechanics** — `src/model.py` → `upscale`; mapped files: `src/model.py`.
- **Training, Metrics, and Validation** — `src/model.py` → `psnr`; mapped files: `src/model.py`, `tests/test_pipeline.py`.
- **Inference, Demo, Tests, and Responsible Limits** — `web/api_impl.py` → `summary`; mapped files: `web/api_impl.py`, `main.py`, `tests/test_pipeline.py`, `README.md`.

## industrial-defect-detection

- **Task, Input Contract, and Source Scope** — `main.py` → `main`; mapped files: `README.md`, `main.py`.
- **Dataset Generation, Labels, and Splits** — `src/data.py` → `load_data`; mapped files: `src/data.py`.
- **Features and Intermediate Representation** — `src/data.py` → `make_patch`; mapped files: `src/data.py`, `src/model.py`.
- **Core Algorithm and Model Mechanics** — `src/model.py` → `reconstruction_scores`; mapped files: `src/model.py`.
- **Training, Metrics, and Validation** — `tests/test_pipeline.py` → `test_a_clean_patch_and_a_defective_one_are_not_the_same`; mapped files: `src/model.py`, `tests/test_pipeline.py`.
- **Inference, Demo, Tests, and Responsible Limits** — `web/api_impl.py` → `summary`; mapped files: `web/api_impl.py`, `main.py`, `tests/test_pipeline.py`, `README.md`.

## ml-experiment-tracking-and-registry

- **Task, Input Contract, and Source Scope** — `main.py` → `main`; mapped files: `README.md`, `main.py`.
- **Dataset Generation, Labels, and Splits** — `src/data.py` → `load_data`; mapped files: `src/data.py`.
- **Features and Intermediate Representation** — `src/model.py` → `candidates`; mapped files: `src/data.py`, `src/model.py`.
- **Experiment Records and Model Registry** — `src/model.py` → `best_run`; mapped files: `src/model.py`.
- **Training, Metrics, and Validation** — `tests/test_pipeline.py` → `test_there_are_several_candidates`; mapped files: `src/model.py`, `tests/test_pipeline.py`.
- **Inference, Demo, and User Interface** — `app.py` → `run_training`; mapped files: `app.py`, `main.py`.
- **Tests, Limitations, and Responsible Extensions** — `tests/test_pipeline.py` → `test_the_runs_are_stored`; mapped files: `tests/test_pipeline.py`, `README.md`, `src/model.py`.

## model-explainability-with-shap

- **Task, Input Contract, and Source Scope** — `main.py` → `main`; mapped files: `README.md`, `main.py`.
- **Dataset Generation, Labels, and Splits** — `src/data.py` → `load_data`; mapped files: `src/data.py`.
- **Features and Intermediate Representation** — `src/model.py` → `explain`; mapped files: `src/data.py`, `src/model.py`.
- **Global and Local Explanations** — `src/model.py` → `local_explanation`; mapped files: `src/model.py`.
- **Training, Metrics, and Validation** — `src/model.py` → `global_importance`; mapped files: `src/model.py`, `tests/test_pipeline.py`.
- **Inference, Demo, and User Interface** — `web/api_impl.py` → `summary`; mapped files: `web/api_impl.py`, `main.py`.
- **Tests, Limitations, and Responsible Extensions** — `tests/test_pipeline.py` → `test_the_importance_ranks_the_features`; mapped files: `tests/test_pipeline.py`, `README.md`, `src/model.py`.

## monai-medical-imaging-pipeline

- **Task, Input Contract, and Source Scope** — `main.py` → `main`; mapped files: `README.md`, `main.py`.
- **Dataset Generation, Labels, and Splits** — `src/data.py` → `load_data`; mapped files: `src/data.py`.
- **Features and Intermediate Representation** — `src/data.py` → `make_volume`; mapped files: `src/data.py`, `src/model.py`.
- **3D Segmentation and Patient-Level Labels** — `src/model.py` → `segment`; mapped files: `src/model.py`.
- **Training, Metrics, and Validation** — `src/model.py` → `dice`; mapped files: `src/model.py`, `tests/test_pipeline.py`.
- **Inference, Demo, and User Interface** — `web/api_impl.py` → `summary`; mapped files: `web/api_impl.py`, `main.py`.
- **Tests, Limitations, and Responsible Extensions** — `tests/test_pipeline.py` → `test_the_dice_of_two_masks_that_do_not_touch_is_zero`; mapped files: `tests/test_pipeline.py`, `README.md`, `src/model.py`.

## movie-recommender-with-als

- **Task, Input Contract, and Source Scope** — `main.py` → `main`; mapped files: `README.md`, `main.py`.
- **Dataset Generation, Labels, and Splits** — `src/data.py` → `load_data`; mapped files: `src/data.py`.
- **Rating Prediction from Latent Factors** — `src/model.py` → `predict`; mapped files: `src/data.py`, `src/model.py`.
- **Latent Factors and Ranking Metrics** — `src/model.py` → `fit`; mapped files: `src/model.py`.
- **Training, Metrics, and Validation** — `src/model.py` → `precision_at_5`; mapped files: `src/model.py`, `tests/test_pipeline.py`.
- **Inference, Demo, and User Interface** — `web/api_impl.py` → `summary`; mapped files: `web/api_impl.py`, `main.py`.
- **Tests, Limitations, and Responsible Extensions** — `tests/test_pipeline.py` → `test_the_recommendations_never_include_a_seen_item`; mapped files: `tests/test_pipeline.py`, `README.md`, `src/model.py`.

## multi-model-time-series-forecasting

- **Task, Input Contract, and Source Scope** — `main.py` → `main`; mapped files: `README.md`, `main.py`.
- **Dataset Generation, Labels, and Splits** — `src/data.py` → `load_data`; mapped files: `src/data.py`.
- **Features and Intermediate Representation** — `src/data.py` → `make_series`; mapped files: `src/data.py`, `src/model.py`.
- **Baselines and Forecast Comparison** — `src/model.py` → `seasonal_naive`; mapped files: `src/model.py`.
- **Rolling-Origin Evaluation and Leakage** — `src/model.py` → `rolling_origin_evaluation`; mapped files: `src/model.py`.
- **Training, Metrics, and Validation** — `src/model.py` → `mase`; mapped files: `src/model.py`, `tests/test_pipeline.py`.
- **Inference, Demo, and User Interface** — `web/api_impl.py` → `summary`; mapped files: `web/api_impl.py`, `main.py`.
- **Tests, Limitations, and Responsible Extensions** — `tests/test_pipeline.py` → `test_the_seasonal_forecast_keeps_the_days_in_the_week`; mapped files: `tests/test_pipeline.py`, `README.md`, `src/model.py`.

## multi-person-pose-estimation-with-mmpose

- **Task, Input Contract, and Source Scope** — `main.py` → `main`; mapped files: `README.md`, `main.py`.
- **Dataset Generation, Labels, and Splits** — `src/data.py` → `load_data`; mapped files: `src/data.py`.
- **Features and Intermediate Representation** — `src/data.py` → `make_scene`; mapped files: `src/data.py`, `src/model.py`.
- **Person Grouping and Joint Geometry** — `src/model.py` → `estimate`; mapped files: `src/model.py`.
- **Training, Metrics, and Validation** — `src/model.py` → `pck`; mapped files: `src/model.py`, `tests/test_pipeline.py`.
- **Inference, Demo, and User Interface** — `web/api_impl.py` → `summary`; mapped files: `web/api_impl.py`, `main.py`.
- **Tests, Limitations, and Responsible Extensions** — `tests/test_pipeline.py` → `test_the_pck_of_a_wrong_answer_is_low`; mapped files: `tests/test_pipeline.py`, `README.md`, `src/model.py`.

## named-entity-recognition-pipeline

- **Task, Input Contract, and Source Scope** — `main.py` → `main`; mapped files: `README.md`, `main.py`.
- **Dataset Generation, Labels, and Splits** — `src/data.py` → `load_data`; mapped files: `src/data.py`.
- **Features and Intermediate Representation** — `src/data.py` → `make_example`; mapped files: `src/data.py`, `src/model.py`.
- **BIO Tags, Token Features, and Entity Spans** — `src/model.py` → `spans`; mapped files: `src/model.py`.
- **Training, Metrics, and Validation** — `tests/test_pipeline.py` → `test_the_spans_of_a_labeled_sentence`; mapped files: `src/model.py`, `tests/test_pipeline.py`.
- **Inference, Demo, and User Interface** — `web/api_impl.py` → `summary`; mapped files: `web/api_impl.py`, `main.py`.
- **Tests, Limitations, and Responsible Extensions** — `tests/test_pipeline.py` → `test_the_spans_of_a_bio_labeled_sentence`; mapped files: `tests/test_pipeline.py`, `README.md`, `src/model.py`.

## neural-text-to-speech-synthesis

- **Task, Input Contract, and Source Scope** — `main.py` → `main`; mapped files: `README.md`, `main.py`.
- **Dataset Generation, Labels, and Splits** — `src/data.py` → `load_data`; mapped files: `src/data.py`.
- **Features and Intermediate Representation** — `src/data.py` → `syllable_count`; mapped files: `src/data.py`, `src/model.py`.
- **Pronunciation Rules and Phoneme Sequence** — `src/model.py` → `synthesize`; mapped files: `src/model.py`.
- **Formants, Duration, and Prosody** — `src/model.py` → `_render_phrase`; mapped files: `src/model.py`.
- **Training, Metrics, and Validation** — `src/model.py` → `formant_error`; mapped files: `src/model.py`, `tests/test_pipeline.py`.
- **Inference, Demo, and User Interface** — `web/api_impl.py` → `summary`; mapped files: `web/api_impl.py`, `main.py`.
- **Tests, Limitations, and Responsible Extensions** — `tests/test_pipeline.py` → `test_pipeline_runs`; mapped files: `tests/test_pipeline.py`, `README.md`, `src/model.py`.

## offline-speech-recognition-engine

- **Task, Input Contract, and Source Scope** — `main.py` → `main`; mapped files: `README.md`, `main.py`.
- **Dataset Generation, Labels, and Splits** — `src/data.py` → `load_data`; mapped files: `src/data.py`.
- **Features and Intermediate Representation** — `src/data.py` → `frame_features`; mapped files: `src/data.py`, `src/model.py`.
- **Dynamic Time Warping and Template Matching** — `src/model.py` → `dtw_distance`; mapped files: `src/model.py`.
- **Training, Metrics, and Validation** — `tests/test_pipeline.py` → `test_the_distance_of_a_sequence_with_itself_is_zero`; mapped files: `src/model.py`, `tests/test_pipeline.py`.
- **Inference, Demo, and User Interface** — `web/api_impl.py` → `summary`; mapped files: `web/api_impl.py`, `main.py`.
- **Tests, Limitations, and Responsible Extensions** — `tests/test_pipeline.py` → `test_the_distance_of_two_empty_sequences_is_not_a_number`; mapped files: `tests/test_pipeline.py`, `README.md`, `src/model.py`.

## outlier-detection-benchmark

- **Task, Input Contract, and Source Scope** — `main.py` → `main`; mapped files: `README.md`, `main.py`.
- **Dataset Generation, Labels, and Splits** — `src/data.py` → `load_data`; mapped files: `src/data.py`.
- **Features and Intermediate Representation** — `src/data.py` → `gaussian`; mapped files: `src/data.py`, `src/model.py`.
- **Detector Comparison and Evaluation** — `src/model.py` → `zscore_scores`; mapped files: `src/model.py`.
- **Training, Metrics, and Validation** — `tests/test_pipeline.py` → `test_every_detector_is_measured_on_every_dataset`; mapped files: `src/model.py`, `tests/test_pipeline.py`.
- **Inference, Demo, Tests, and Responsible Limits** — `web/api_impl.py` → `summary`; mapped files: `web/api_impl.py`, `main.py`, `tests/test_pipeline.py`, `README.md`.

## real-time-pose-estimation-app

- **Task, Input Contract, and Source Scope** — `main.py` → `main`; mapped files: `README.md`, `main.py`.
- **Dataset Generation, Labels, and Splits** — `src/data.py` → `load_data`; mapped files: `src/data.py`.
- **Features and Intermediate Representation** — `src/data.py` → `make_frame`; mapped files: `src/data.py`, `src/model.py`.
- **Detect People and Group Image Parts** — `src/model.py` → `find_people`; mapped files: `src/model.py`.
- **Regress Keypoints from Cropped Features** — `src/model.py` → `fit_ridge`; mapped files: `src/model.py`.
- **API Input, Model Persistence, and Safety** — `app.py` → `uploaded_frame`; mapped files: `app.py`.
- **Training, Metrics, and Validation** — `src/model.py` → `pck`; mapped files: `src/model.py`, `tests/test_pipeline.py`.
- **Inference, Demo, and User Interface** — `app.py` → `api_summary`; mapped files: `app.py`, `main.py`.
- **Tests, Limitations, and Responsible Extensions** — `tests/test_pipeline.py` → `test_the_detector_finds_nothing_in_an_empty_image`; mapped files: `tests/test_pipeline.py`, `README.md`, `src/model.py`.

## recommender-algorithm-benchmark

- **Task, Input Contract, and Source Scope** — `main.py` → `main`; mapped files: `README.md`, `main.py`.
- **Dataset Generation, Labels, and Splits** — `src/data.py` → `load_data`; mapped files: `src/data.py`.
- **Features and Intermediate Representation** — `src/model.py` → `build_matrix`; mapped files: `src/data.py`, `src/model.py`.
- **Ranking Metrics and Catalogue Coverage** — `src/model.py` → `evaluate`; mapped files: `src/model.py`.
- **Training, Metrics, and Validation** — `tests/test_pipeline.py` → `test_every_recommender_is_measured`; mapped files: `src/model.py`, `tests/test_pipeline.py`.
- **Inference, Demo, and User Interface** — `web/api_impl.py` → `summary`; mapped files: `web/api_impl.py`, `main.py`.
- **Tests, Limitations, and Responsible Extensions** — `tests/test_pipeline.py` → `test_the_normalisation_keeps_the_direction`; mapped files: `tests/test_pipeline.py`, `README.md`, `src/model.py`.

## retrieval-augmented-document-q-a

- **Task, Input Contract, and Source Scope** — `main.py` → `main`; mapped files: `README.md`, `main.py`.
- **Dataset Generation, Labels, and Splits** — `src/data.py` → `load_data`; mapped files: `src/data.py`.
- **Features and Intermediate Representation** — `src/model.py` → `sentences`; mapped files: `src/data.py`, `src/model.py`.
- **Passage Retrieval, Answer Extraction, and Attribution** — `src/model.py` → `answer`; mapped files: `src/model.py`.
- **Training, Metrics, and Validation** — `tests/test_pipeline.py` → `test_the_text_is_split_into_sentences`; mapped files: `src/model.py`, `tests/test_pipeline.py`.
- **Inference, Demo, and User Interface** — `web/api_impl.py` → `summary`; mapped files: `web/api_impl.py`, `main.py`.
- **Tests, Limitations, and Responsible Extensions** — `tests/test_pipeline.py` → `test_the_answer_cites_a_source`; mapped files: `tests/test_pipeline.py`, `README.md`, `src/model.py`.

## sales-forecasting-with-prophet

- **Task, Input Contract, and Source Scope** — `main.py` → `main`; mapped files: `README.md`, `main.py`.
- **Dataset Generation, Labels, and Splits** — `src/data.py` → `load_data`; mapped files: `src/data.py`.
- **Features and Intermediate Representation** — `src/data.py` → `make_sales`; mapped files: `src/data.py`, `src/model.py`.
- **Additive Components and Forecast Horizon** — `src/model.py` → `predict`; mapped files: `src/model.py`.
- **Training, Metrics, and Validation** — `tests/test_pipeline.py` → `test_the_model_is_fitted_on_the_training_data`; mapped files: `src/model.py`, `tests/test_pipeline.py`.
- **Inference, Demo, and User Interface** — `web/api_impl.py` → `summary`; mapped files: `web/api_impl.py`, `main.py`.
- **Tests, Limitations, and Responsible Extensions** — `tests/test_pipeline.py` → `test_the_weekday_effect_is_looked_up`; mapped files: `tests/test_pipeline.py`, `README.md`, `src/model.py`.

## segment-anything-sam-fine-tuning

- **Task, Input Contract, and Source Scope** — `main.py` → `main`; mapped files: `README.md`, `main.py`.
- **Dataset Generation, Labels, and Splits** — `src/data.py` → `load_data`; mapped files: `src/data.py`.
- **Features and Intermediate Representation** — `src/data.py` → `make_sample`; mapped files: `src/data.py`, `src/model.py`.
- **Image Encoding and Prompt Types** — `src/model.py` → `encode_image`; mapped files: `src/model.py`.
- **Prompt Decoding, Fine-Tuning, and Mask Metrics** — `src/model.py` → `fine_tune`; mapped files: `src/model.py`.
- **Training, Metrics, and Validation** — `src/model.py` → `evaluate`; mapped files: `src/model.py`, `tests/test_pipeline.py`.
- **Inference, Demo, and User Interface** — `app.py` → `_predictions`; mapped files: `app.py`, `main.py`.
- **Tests, Limitations, and Responsible Extensions** — `tests/test_pipeline.py` → `test_a_point_outside_an_object_gives_an_empty_mask`; mapped files: `tests/test_pipeline.py`, `README.md`, `src/model.py`.

## semantic-segmentation-with-u-net-and-deeplab

- **Task, Input Contract, and Source Scope** — `main.py` → `main`; mapped files: `README.md`, `main.py`.
- **Dataset Generation, Labels, and Splits** — `src/data.py` → `load_data`; mapped files: `src/data.py`.
- **Features and Intermediate Representation** — `src/data.py` → `make_sample`; mapped files: `src/data.py`, `src/model.py`.
- **Core Algorithm and Model Mechanics** — `src/model.py` → `build_unet`; mapped files: `src/model.py`.
- **Training, Metrics, and Validation** — `src/model.py` → `dice_score`; mapped files: `src/model.py`, `tests/test_pipeline.py`.
- **Inference, Demo, Tests, and Responsible Limits** — `web/api_impl.py` → `summary`; mapped files: `web/api_impl.py`, `main.py`, `tests/test_pipeline.py`, `README.md`.

## speech-to-text-transcription-service

- **Task, Input Contract, and Source Scope** — `main.py` → `main`; mapped files: `README.md`, `main.py`.
- **Dataset Generation, Labels, and Splits** — `src/data.py` → `load_data`; mapped files: `src/data.py`.
- **Features and Intermediate Representation** — `src/data.py` → `features`; mapped files: `src/data.py`, `src/model.py`.
- **Energy Segmentation and Word Decoding** — `src/model.py` → `segment`; mapped files: `src/model.py`.
- **Training, Metrics, and Validation** — `tests/test_pipeline.py` → `test_the_signal_is_split_into_words`; mapped files: `src/model.py`, `tests/test_pipeline.py`.
- **Inference, Demo, and User Interface** — `app.py` → `api_transcribe`; mapped files: `app.py`, `main.py`.
- **Tests, Limitations, and Responsible Extensions** — `tests/test_pipeline.py` → `test_the_words_are_transcribed`; mapped files: `tests/test_pipeline.py`, `README.md`, `src/model.py`.

## streaming-anomaly-detection

- **Task, Input Contract, and Source Scope** — `main.py` → `main`; mapped files: `README.md`, `main.py`.
- **Dataset Generation, Labels, and Splits** — `src/data.py` → `load_data`; mapped files: `src/data.py`.
- **Features and Intermediate Representation** — `src/data.py` → `make_stream`; mapped files: `src/data.py`, `src/model.py`.
- **Online Updates, Thresholds, and Detection Delay** — `src/model.py` → `simulate`; mapped files: `src/model.py`.
- **Training, Metrics, and Validation** — `src/model.py` → `evaluate`; mapped files: `src/model.py`, `tests/test_pipeline.py`.
- **Inference, Demo, and User Interface** — `web/api_impl.py` → `summary`; mapped files: `web/api_impl.py`, `main.py`.
- **Tests, Limitations, and Responsible Extensions** — `tests/test_pipeline.py` → `test_the_spike_is_found`; mapped files: `tests/test_pipeline.py`, `README.md`, `src/model.py`.

## tensorflow-object-detection-api

- **Task, Input Contract, and Source Scope** — `main.py` → `main`; mapped files: `README.md`, `main.py`.
- **Dataset Generation, Labels, and Splits** — `src/data.py` → `load_data`; mapped files: `src/data.py`.
- **Features and Intermediate Representation** — `src/data.py` → `make_scene`; mapped files: `src/data.py`, `src/model.py`.
- **Object Proposals and Box Matching** — `src/model.py` → `proposal_boxes`; mapped files: `src/model.py`.
- **Training, Metrics, and Validation** — `tests/test_pipeline.py` → `test_the_precision_and_the_recall_are_shares`; mapped files: `src/model.py`, `tests/test_pipeline.py`.
- **Inference, Demo, Tests, and Responsible Limits** — `web/api_impl.py` → `summary`; mapped files: `web/api_impl.py`, `main.py`, `tests/test_pipeline.py`, `README.md`.

## time-series-classification-pipelines

- **Task, Input Contract, and Source Scope** — `main.py` → `main`; mapped files: `README.md`, `main.py`.
- **Dataset Generation, Labels, and Splits** — `src/data.py` → `load_data`; mapped files: `src/data.py`.
- **Features and Intermediate Representation** — `src/data.py` → `make_series`; mapped files: `src/data.py`, `src/model.py`.
- **Time-Domain and Frequency Features** — `src/model.py` → `featurize`; mapped files: `src/model.py`.
- **Training, Metrics, and Validation** — `tests/test_pipeline.py` → `test_the_split_is_in_time`; mapped files: `src/model.py`, `tests/test_pipeline.py`.
- **Inference, Demo, Tests, and Responsible Limits** — `web/api_impl.py` → `summary`; mapped files: `web/api_impl.py`, `main.py`, `tests/test_pipeline.py`, `README.md`.

## topic-modeling-with-bertopic

- **Task, Input Contract, and Source Scope** — `main.py` → `main`; mapped files: `README.md`, `main.py`.
- **Dataset Generation, Labels, and Splits** — `src/data.py` → `load_data`; mapped files: `src/data.py`.
- **Topic Assignments and Output Representation** — `src/model.py` → `demo`; mapped files: `src/data.py`, `src/model.py`.
- **Core Algorithm and Model Mechanics** — `src/model.py` → `train`; mapped files: `src/model.py`.
- **Training, Metrics, and Validation** — `tests/test_pipeline.py` → `test_every_document_gets_a_topic`; mapped files: `src/model.py`, `tests/test_pipeline.py`.
- **Inference, Demo, Tests, and Responsible Limits** — `src/model.py` → `demo`; mapped files: `main.py`, `src/model.py`, `tests/test_pipeline.py`, `README.md`.

## train-a-gpt-language-model-from-scratch

- **Task, Input Contract, and Source Scope** — `main.py` → `main`; mapped files: `README.md`, `main.py`.
- **Dataset Generation, Labels, and Splits** — `src/data.py` → `load_data`; mapped files: `src/data.py`.
- **Features and Intermediate Representation** — `src/model.py` → `make_sequences`; mapped files: `src/data.py`, `src/model.py`.
- **Self-Attention Model Architecture** — `src/model.py` → `build_model`; mapped files: `src/model.py`.
- **Temperature Sampling and Generated Text** — `src/model.py` → `sample`; mapped files: `src/model.py`.
- **Training, Metrics, and Validation** — `tests/test_pipeline.py` → `test_the_vocabulary_covers_the_text`; mapped files: `src/model.py`, `tests/test_pipeline.py`.
- **Inference, Demo, and User Interface** — `src/model.py` → `demo`; mapped files: `main.py`, `src/model.py`.
- **Tests, Limitations, and Responsible Extensions** — `tests/test_pipeline.py` → `test_pipeline_runs`; mapped files: `tests/test_pipeline.py`, `README.md`, `src/model.py`.

## wake-word-keyword-spotting

- **Task, Input Contract, and Source Scope** — `main.py` → `main`; mapped files: `README.md`, `main.py`.
- **Dataset Generation, Labels, and Splits** — `src/data.py` → `load_data`; mapped files: `src/data.py`.
- **Features and Intermediate Representation** — `src/data.py` → `features`; mapped files: `src/data.py`, `src/model.py`.
- **Core Algorithm and Model Mechanics** — `src/model.py` → `train`; mapped files: `src/model.py`.
- **Training, Metrics, and Validation** — `tests/test_pipeline.py` → `test_the_accuracy_and_the_false_positive_rate_are_shares`; mapped files: `src/model.py`, `tests/test_pipeline.py`.
- **Inference, Demo, Tests, and Responsible Limits** — `src/model.py` → `demo`; mapped files: `main.py`, `src/model.py`, `tests/test_pipeline.py`, `README.md`.

## wav2vec2-low-resource-asr-fine-tuning

- **Task, Input Contract, and Source Scope** — `main.py` → `main`; mapped files: `README.md`, `main.py`.
- **Dataset Generation, Labels, and Splits** — `src/data.py` → `load_data`; mapped files: `src/data.py`.
- **Features and Intermediate Representation** — `src/data.py` → `frame_features`; mapped files: `src/data.py`, `src/model.py`.
- **Frame Labels, Greedy Decoding, and Error Rate** — `src/model.py` → `decode`; mapped files: `src/model.py`.
- **Training, Metrics, and Validation** — `src/model.py` → `word_distance`; mapped files: `src/model.py`, `tests/test_pipeline.py`.
- **Inference, Demo, and User Interface** — `src/model.py` → `demo`; mapped files: `main.py`, `src/model.py`.
- **Tests, Limitations, and Responsible Extensions** — `tests/test_pipeline.py` → `test_pipeline_runs`; mapped files: `tests/test_pipeline.py`, `README.md`, `src/model.py`.

## weed-species-detection

- **Task, Input Contract, and Source Scope** — `main.py` → `main`; mapped files: `README.md`, `main.py`.
- **Dataset Generation, Labels, and Splits** — `src/data.py` → `load_data`; mapped files: `src/data.py`.
- **Features and Intermediate Representation** — `src/data.py` → `features`; mapped files: `src/data.py`, `src/model.py`.
- **Core Algorithm and Model Mechanics** — `src/model.py` → `train`; mapped files: `src/model.py`.
- **Training, Metrics, and Validation** — `tests/test_pipeline.py` → `test_every_species_is_measured`; mapped files: `src/model.py`, `tests/test_pipeline.py`.
- **Inference, Demo, Tests, and Responsible Limits** — `src/model.py` → `demo`; mapped files: `main.py`, `src/model.py`, `tests/test_pipeline.py`, `README.md`.
