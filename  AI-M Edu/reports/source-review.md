# AI/ML source review and completion report

Source folder: `/home/aziz/foundev/AIML-foundev-main/Artificial Intelligence & Machine Learning`
Output folder: `/home/aziz/foundev/Mini projects edu/AI - ML`

The package curricula and curated file maps were prepared from the supplied project overview/workflow documents and inspected source entry points. Every cited source path was checked for existence. Automated checks cannot establish factual accuracy; unresolved implementation boundaries are listed below.

## Project-by-project review items

### FactCheck Studio: Factual Consistency and Summarization (`abstractive-text-summarizer`)

- The shipped Flask endpoint is deterministic lexical consistency scoring; it does not load a neural checkpoint. The research model code is a separate, older stack and no trained checkpoint is bundled. WORKFLOW statements that contradict the API/UI implementation need review.

### CampusWise: College FAQ Retrieval-Augmented Generation (`college-faq-chatbot-rag`)

- A local vector database and external LLM configuration are required; retrieved snippets can still be incomplete or wrong. The static console is not the Streamlit chat backend.

### FraudGuard: Credit Card Fraud Detection (`credit-card-fraud-detection`)

- A real score depends on a separately supplied model/data artifact; class imbalance means accuracy alone is misleading. Validate privacy and threshold choices before real decisions.

### YieldSight: County-Level Crop Yield Prediction (`crop-yield-prediction`)

- The workflow needs Earth Engine exports and large raster data not included in the package. Optional error-map dependencies are missing from the declared environment; results require spatially honest evaluation.

### Note Sense: Currency Note Recognition (`currency-note-recognition-for-visually-impaired`)

- There is no trained CNN or connected web API: the detector uses ORB matching against reference images; the page is static. README claims about server/detector paths conflict with the actual tree. Hard-coded paths and optional speech dependencies require repair/review.

### Similarity Radar: Document Similarity Checking (`document-plagiarism-checker`)

- The repository uses live web search and source-pair scoring, not the advertised TF-IDF/local corpus model. Similarity is not proof of plagiarism; provider availability and document privacy require review.

### Cockpit: Driver Drowsiness Detection (`driver-drowsiness-detection`)

- No project-specific drowsiness model is trained; desktop geometry/state logic and the MediaPipe variant differ. A missing landmark asset or camera failure prevents operation. It is a learning prototype, not a safety-certified driver aid.

### MoodTunes: Emotion Detection and Music Recommendation (`emotion-detection-from-text-and-face`)

- The expected face weights are absent and training provenance is unavailable. Facial/text emotion labels are uncertain and sensitive; no mood inference should be treated as fact.

### FAMS: Face Recognition Attendance System (`face-recognition-attendance-system`)

- The app uses Haar + LBPH rather than deep learning. Biometric data and attendance records need consent, access controls, retention rules, and correction paths.

### Signal Control Room: Helmet and Seatbelt Detection (`helmet-seatbelt-violation-detection`)

- Generic COCO weights do not reliably supply dedicated helmet/seatbelt classes; custom model path and deployed behavior differ. No automated output should be treated as enforcement evidence.

### Underwriting Desk: Loan Default Risk Modeling (`loan-default-prediction`)

- The web UI is a heuristic demo, not the trained pipeline. The legacy training path requires missing CSV inputs and porting; no model artifact is supplied. Credit decisions need rigorous fairness, calibration, and legal review.

### Groove Observatory: Audio Feature Music Recommendation (`music-recommender-from-audio-features`)

- This is deterministic cosine-neighbor ranking over a local 2,261-row, ten-feature catalogue, not a learned recommender. Catalog coverage and popularity bias limit results.

### LeafLens: Plant Leaf Disease Image Classification (`plant-leaf-disease-detection-cnn`)

- Training notebook/code and Django interface exist, but required trained model artifacts are missing; current tests are stubs and do not prove inference. Field photos differ from curated data; diagnosis requires expert confirmation.

### ExamForge: Syllabus-Based Question Generation (`question-paper-generator-from-syllabus`)

- The app depends on remote curriculum catalogue and a local Ollama llama2 service; question correctness is not guaranteed. Requirements omit dependencies noted in workflow; teacher review is mandatory.

### TalentMatch Lens: Resume and Job Description Matching (`resume-screening-and-jd-matching`)

- The embedding model is used zero-shot and no evaluation/training data is supplied. Similarity can encode proxy bias and must not rank or reject applicants without meaningful human review.

### DemandSight: Retail Sales Analytics (`retail-sales-forecasting`)

- No forecasting model exists: the implementation aggregates transaction data. The ETL requires MySQL and pymysql is omitted from requirements. Seasonal prediction is an extension, not shipped behavior.

### SignBridge: Rule-Based Sign Language Text Translation (`sign-language-to-text-translation`)

- The core is rule-based gloss restructuring and token-to-clip mapping, not video recognition or general language translation. Clip coverage and dialect/culture constraints need signer review.

### TrendCast: Stock Price Trend Research (`stock-price-trend-predictor`)

- The source is research-oriented and the UI is static; historical signals do not establish future returns. Avoid look-ahead leakage and never present outputs as investment advice.

### DEWS: Student Dropout Risk Prediction (`student-dropout-risk-prediction`)

- The UI is a demo; the historical pipeline scripts are documented as mostly broken/legacy. Labels are an administrative rule. Risk scores must support voluntary services, not punitive decisions.

### PlateSight: Vehicle Number Plate Recognition (`vehicle-number-plate-recognition`)

- The repository includes YOLOv5 code and Streamlit app but model/checkpoint availability and OCR behavior need verification. Plate data is personal information; protect, minimize, and expire it.

