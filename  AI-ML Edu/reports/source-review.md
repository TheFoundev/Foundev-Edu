# AI/ML source review and completion report

## Batch 1 — 20-project library

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

---

## Batch 2 — 36-project library

Source: `/home/aziz/foundev/AI-ML`

Packages: 36

For each project, the package lessons follow the actual README-described implementation and its source functions. The README blockquote is treated as the requested/aspirational brief; the Features and Notes sections plus cited source methods define what is taught as implemented. No source application or model training was run.

## Abstractive Document Summarization (`abstractive-document-summarization`)

**Source implementation:** A compact document summarizer using sentence ranking.

**Brief distinction:** Build a document summarization system for news, legal, or meeting transcripts using BART, T5, or PEGASUS with ROUGE evaluation and chunking for long documents.

**Implemented behaviors taught:**
- TF-IDF sentence scoring with a position bonus
- The length of the summary is searched over the corpus, and the length that scores best is the one that is kept
- ROUGE-L evaluation against reference summaries, with the score of every length
- A small Flask page that summarizes a pasted document
- Demo mode that prints an original document and its summary

**Source limitations/review:**
- The brief says abstractive, but this implementation is extractive: it selects whole sentences.
- There is no neural encoder-decoder, tokenizer download or generation step.
- Evaluation uses a small hand-written set of documents and reference summaries.

## Algorithmic Trading Signals (`algorithmic-trading-signals`)

**Source implementation:** Technical indicators and a small next-day direction model.

**Brief distinction:** Turn market and technical data into trading strategies: feature engineering, supervised return prediction, backtesting, and portfolio-level evaluation.

**Implemented behaviors taught:**
- RSI, moving averages, a gap feature and a momentum feature (the rate of change over ten days)
- A random forest that says whether the price goes up the next day
- A backtest that trades the predictions, with the return, the Sharpe ratio and the drawdown
- The buy and hold of the same window as the baseline

**Source limitations/review:**
- Prices are simulated; results say nothing about real markets.
- The backtest ignores fees, slippage, position sizing and short selling.
- A real study needs walk-forward validation, multiple assets and proper risk controls.

## Autonomous Driving Perception (`autonomous-driving-perception`)

**Source implementation:** A tiny road-scene perception pipeline using thresholding and connected components.

**Brief distinction:** Study and extend an open-source driver-assistance perception stack: lane detection, vehicle detection, and driver-attention monitoring on real driving video.

**Implemented behaviors taught:**
- A lane detector and a vehicle detector over a road scene
- The lane threshold is fitted on one part of the scenes and the metrics are measured on the rest, so the numbers are not the ones the threshold was chosen for
- The lane edges are not reported as vehicles: the mask is thinned before the blobs are found, and a blob has to fill its own box
- The IoU of two boxes is the matching rule, and every detection is used at most once
- A demo that writes the scene and the lane mask to a picture

**Source limitations/review:**
- Scenes are drawn procedurally; there is no real camera or driving dataset.
- Lane and vehicle detection are classical image operations, not a trained network.
- The evaluation is a sanity check, not a benchmark against KITTI or nuScenes.

## Detectron2 Instance Segmentation (`detectron2-instance-segmentation`)

**Source implementation:** Instance masks for simple synthetic shapes.

**Brief distinction:** Implement instance segmentation for robotics or medical imagery with Mask R-CNN and RetinaNet, including custom dataset registration, mAP evaluation, and visualization.

**Implemented behaviors taught:**
- Procedural images containing circles and squares
- Threshold plus connected-component mask extraction
- Per-instance IoU matching against ground truth
- Threshold sweep during training

**Source limitations/review:**
- Only two shape types on a clean background are supported.
- There is no learned backbone, region proposal network or COCO training.
- Overlapping shapes are merged by connected components and count as one instance.

## End-to-End Speech Recognition with SpeechBrain (`end-to-end-speech-recognition-with-speechbrain`)

**Source implementation:** A digit recognizer built on synthetic speech-like audio.

**Brief distinction:** Train end-to-end speech systems (ASR, speaker verification, or TTS) with SpeechBrain recipes on public corpora and package the model behind a servable interface.

**Implemented behaviors taught:**
- Synthetic spoken digits made from tone formants
- Log-band audio features without external audio libraries
- Random forest classifier with a confusion summary
- Demo that recognizes a freshly generated word

**Source limitations/review:**
- Audio is synthesized from tones, not recorded human speech.
- The feature extractor is a simplified log-band energy representation, not real MFCCs.
- Accuracy on synthetic tones does not transfer to a real speech dataset.

## Facial Attribute Analysis Kiosk (`facial-attribute-analysis-kiosk`)

**Source implementation:** A small synthetic face-attribute classifier with a Flask kiosk page.

**Brief distinction:** Wrap state-of-the-art face verification and attribute analysis (age, gender, emotion, anti-spoofing) into a REST API or real-time interactive kiosk.

**Implemented behaviors taught:**
- Procedural 32x32 face images with glasses and smile variants
- Pixel features and a multi-output random forest
- Per-attribute accuracy metrics
- Flask page that shows a sample and its predictions

**Source limitations/review:**
- The faces are drawn with rectangles and ellipses; there are no photos or real people.
- The model reads pixel patterns from the synthetic generator, not facial structure.
- Glasses and smile are the only two attributes; there is no face detection step.

## GAN Image Generation (`gan-image-generation`)

**Source implementation:** A tiny GAN that learns to draw simple shapes.

**Brief distinction:** Implement and stabilize generative adversarial networks (DCGAN, WGAN-GP, CycleGAN) to synthesize faces, digits, or style-transferred images with FID evaluation.

**Implemented behaviors taught:**
- Synthetic 16x16 shape dataset
- Small convolutional generator and discriminator
- Short adversarial training loop
- Saved sample grid after training

**Source limitations/review:**
- The dataset only contains simple bright shapes on a dark background.
- Training is deliberately short; the samples are rough blobs, not photorealistic images.
- This is a teaching implementation, not a stable GAN recipe.

## Hybrid Recommender with Content Features (`hybrid-recommender-with-content-features`)

**Source implementation:** Blend collaborative filtering with item tags for recommendations.

**Brief distinction:** Combine collaborative filtering with content features such as genres and tags using LightFM to solve the cold-start problem and expose recommendations through a REST API.

**Implemented behaviors taught:**
- Synthetic user ratings and item tag vectors
- Truncated SVD collaborative scores
- Content similarity from a user's liked-item profile
- Precision@5 evaluation and a demo recommendation list

**Source limitations/review:**
- Users, items and ratings are simulated.
- The content profile is a simple average of tags from highly rated items.
- There is no cold-start handling, implicit feedback or online serving layer.

## Hyperparameter Optimization Service (`hyperparameter-optimization-service`)

**Source implementation:** A small random-search service that records every trial.

**Brief distinction:** Systematically optimize model hyperparameters and pruning schedules with Optuna's TPE sampler and visualizations, embedded into a reproducible training workflow.

**Implemented behaviors taught:**
- Synthetic classification dataset
- Random search over random-forest hyperparameters
- SQLite trial log with parameters and scores
- FastAPI endpoints for search and results

**Source limitations/review:**
- The search space is deliberately tiny and runs on one CPU.
- There is no pruning, distributed workers or persistent study server.
- SQLite is used as a simple local trial store.

## Image Super-Resolution Enhancer (`image-super-resolution-enhancer`)

**Source implementation:** Upscale small images with bicubic resampling and sharpening.

**Brief distinction:** Enhance blurry or low-resolution images such as document scans, satellite, or medical imagery with Real-ESRGAN and benchmark quality metrics and runtime on CPU versus GPU.

**Implemented behaviors taught:**
- Synthetic low/high resolution image pairs
- Bicubic upscaling with an unsharp mask
- PSNR and mean absolute error evaluation
- Before/after image saved for inspection

**Source limitations/review:**
- There is no learned super-resolution network; this is an interpolation baseline.
- The synthetic images are simple shapes, so PSNR is much friendlier than real photos.
- Sharpening parameters are tuned on the generated validation images.

## Industrial Defect Detection (`industrial-defect-detection`)

**Source implementation:** Find scratches and blotches on synthetic material textures.

**Brief distinction:** Detect manufacturing defects without defect labels by training unsupervised anomaly models (PatchCore, PaDiM) on MVTec AD and visualizing anomaly heatmaps.

**Implemented behaviors taught:**
- Procedural fabric-like texture with optional defects
- PCA reconstruction error as an anomaly score
- ROC AUC and threshold-based precision/recall
- Sample defect images saved for inspection

**Source limitations/review:**
- Textures and defects are generated; there is no MVTec or camera data.
- Only image-level labels are evaluated; defect localisation is not scored.
- A production line would need per-material calibration and much more data.

## ML Experiment Tracking and Registry (`ml-experiment-tracking-and-registry`)

**Source implementation:** A tiny experiment tracker and model registry backed by SQLite.

**Brief distinction:** Operationalize an ML project lifecycle: track experiments, version datasets and models in a registry, and deploy a reproducible REST prediction endpoint.

**Implemented behaviors taught:**
- Train three model configurations on the same split
- Log parameters, metrics and artefact paths to SQLite
- Best-run lookup and a simple model registry
- FastAPI endpoints for runs and the current best model

**Source limitations/review:**
- Artefacts are pickled locally; there is no remote store or model server.
- Runs are not nested and there is no UI beyond the JSON API.
- The registry is a table lookup, not a governed production registry.

## Model Explainability with SHAP (`model-explainability-with-shap`)

**Source implementation:** Permutation importance and partial dependence for a tabular model.

**Brief distinction:** Explain black-box classifiers and regressors (churn, fraud, diagnosis) with Shapley-value attributions and build an explainability report for stakeholders.

**Implemented behaviors taught:**
- Synthetic dataset with a known non-linear signal
- Random forest baseline accuracy
- SHAP values for every prediction, with `TreeExplainer`
- Global importance from the mean absolute SHAP value
- A local explanation: why one prediction was made
- A check that the explanation finds the signal the data was built from
- Permutation importance and a partial-dependence curve next to it
- Saved chart with the three explanations

**Source limitations/review:**
- Permutation importance describes this model on this dataset, not causality.
- The dataset is synthetic, so the 'true' generating features are known by construction.
- There are no per-row SHAP values or interaction effects.

## MONAI Medical Imaging Pipeline (`monai-medical-imaging-pipeline`)

**Source implementation:** A small 3D lesion segmentation and classification pipeline.

**Brief distinction:** Develop a medical imaging pipeline (organ or tumor segmentation, disease classification) using MONAI with pretrained architectures and Dice-based 3D evaluation.

**Implemented behaviors taught:**
- Synthetic 3D volumes with spherical lesions
- Intensity normalisation and percentile thresholding
- Dice score for segmentation and accuracy for patient labels
- Slice visualisation saved for inspection

**Source limitations/review:**
- Volumes are generated in memory; no DICOM or NIfTI files are read.
- Segmentation is a threshold, not a trained U-Net.
- The patient classifier uses two hand-built features and logistic regression.

## Movie Recommender with ALS (`movie-recommender-with-als`)

**Source implementation:** Matrix factorisation for movie recommendations, written from scratch.

**Brief distinction:** Create an implicit-feedback recommender on MovieLens with alternating least squares, evaluating ranking quality with MAP@K and building a lightweight Flask demo.

**Implemented behaviors taught:**
- Synthetic users, movies, genres and ratings
- Biased matrix factorisation trained with SGD
- RMSE and precision@5 evaluation
- Demo recommendation list with titles

**Source limitations/review:**
- Ratings are simulated from genre preferences plus noise.
- There is no implicit feedback, temporal drift or production serving path.
- Only a small dense matrix is supported; scaling to real catalogues is out of scope.

## Multi-Model Time-Series Forecasting (`multi-model-time-series-forecasting`)

**Source implementation:** Compare simple forecasting baselines on a seasonal series.

**Brief distinction:** Benchmark classical and deep forecasters (ARIMA, TCN, N-BEATS, Transformer) on multivariate energy or traffic series with proper rolling-window backtesting.

**Implemented behaviors taught:**
- Synthetic series with trend and weekly seasonality
- Naive, mean, linear-trend and seasonal-naive baselines
- Optional SARIMAX comparison
- MAE/RMSE table and a forecast plot

**Source limitations/review:**
- The series is simulated and much cleaner than real sales or traffic data.
- No neural forecasting model is trained.
- Only one holdout split is used, not rolling-origin evaluation.

## Multi-Person Pose Estimation with MMPose (`multi-person-pose-estimation-with-mmpose`)

**Source implementation:** Estimate two people's joints with a geometric baseline.

**Brief distinction:** Build a multi-person keypoint system for sports analytics or ergonomics monitoring with MMPose top-down and bottom-up models and OKS-based accuracy evaluation.

**Implemented behaviors taught:**
- Synthetic scenes with two stick figures
- Thresholding plus left/right grouping
- Joint positions estimated from each figure's bounding box
- PCK evaluation and an annotated output image

**Source limitations/review:**
- Figures are bright lines on a dark background with no occlusion or camera noise.
- Joint positions are estimated from bounding-box proportions, not learned features.
- This will not work on real photographs.

## Named Entity Recognition Pipeline (`named-entity-recognition-pipeline`)

**Source implementation:** A token classifier for people, organisations and places.

**Brief distinction:** Extract structured entities such as names, dates, organizations, and biomedical terms from unstructured text with spaCy rule-based and transformer NER models.

**Implemented behaviors taught:**
- Gazetteer-based sentence generator with BIO tags
- Token shape, prefix and neighbour features
- Logistic regression token classifier
- Entity-level precision, recall and F1

**Source limitations/review:**
- Sentences are generated from templates and fixed name lists.
- The model uses hand-built features rather than contextual embeddings.
- Entity-level evaluation is a simple span match, not a full CoNLL scorer.

## Neural Text-to-Speech Synthesis (`neural-text-to-speech-synthesis`)

**Source implementation:** A formant-based text-to-speech engine that writes WAV files.

**Brief distinction:** Generate natural speech from text with attention-based Tacotron2 plus WaveGlow vocoders, fine-tuning on a small custom voice corpus and evaluating output quality.

**Implemented behaviors taught:**
- A rule-based grapheme-to-phoneme engine: digraphs (`ch`, `sh`, `th`, `ph`, `ng`, `ck`, ...), r-coloured vowels, the magic `e` (`phone` → /fow-n/), the silent `e` and a lexicon of the most frequent English words
- Formant synthesis: every vowel is rendered with its three formants (F1, F2, F3), every consonant with noise, a burst or a nasal murmur
- A duration model: a linear regression over the length of a word and its number of syllables, fitted on a corpus of 44 phrases, with the time shared between the syllables and the phonemes
- A prosody model: the pitch declines over a phrase, a question rises at the end, a stressed syllable gets an accent and is a little longer, and the voice carries a small jitter and shimmer
- WAV output and a waveform plot
- An **objective** evaluation: the formant peaks of the synthesized vowels are measured with an FFT and compared with the targets of the phonemes (the *formant error* in Hz)

**Source limitations/review:**
- **This is not a neural TTS.** There is no acoustic model, no attention, no vocoder and no learned pronunciation; the project implements the classical pipeline that such a system would replace. A real Tacotron2 + WaveGlow build needs a GPU, a training corpus of hours and a dependency on TensorFlow, none of which fit in this environment.
- The pronunciation is rule based: the rules cover the common patterns of English and the lexicon covers the most frequent words, but an arbitrary proper noun will be pronounced wrongly. CMUdict would be the right source; it is not bundled.
- The duration model is fitted on 44 phrases whose target durations come from the usual rule of thumb (a word costs about 140 ms, a syllable about 85 ms). It is not fitted on a recorded corpus, so the MAE (about 0.1 s) measures how well the regression fits that formula, not how well it matches a speaker.
- The formant error measures that the waveform **contains** the formants that were asked for. It is a fidelity measure, not an intelligibility score: a MOS panel or an ASR round trip (synthesise → recognise → word error rate) would be the objective test this project still lacks.
- The speech is robotic: the formants do not move inside a vowel (no coarticulation), the pitch is a simple contour and there is no stress model beyond the first vowel of a word.

## Offline Speech Recognition Engine (`offline-speech-recognition-engine`)

**Source implementation:** A command-word recognizer using DTW template matching.

**Brief distinction:** Engineer a fully offline ASR system with CTC sequence modeling and n-gram language-model rescoring, benchmarking word error rate on LibriSpeech test data.

**Implemented behaviors taught:**
- Synthetic command words built from tone sequences
- Frame-level log-band features
- Dynamic time warping against per-word templates
- Accuracy on held-out samples and a demo recording

**Source limitations/review:**
- Audio is synthetic and limited to eight command words.
- DTW template matching does not scale to a real vocabulary.
- There is no language model; every frame sequence is independent.

## Outlier Detection Benchmark (`outlier-detection-benchmark`)

**Source implementation:** Compare four outlier detectors on several synthetic datasets.

**Brief distinction:** Benchmark dozens of outlier detectors (LOF, Isolation Forest, autoencoders) on tabular and credit-fraud data to flag rare anomalous records.

**Implemented behaviors taught:**
- Gaussian, ring and clustered 2D datasets with labelled outliers
- Z-score, isolation forest, LOF and one-class SVM
- ROC AUC comparison table
- Scatter plot of scores and predictions

**Source limitations/review:**
- Outliers are injected synthetically; real anomaly data is much messier.
- Hyperparameters are fixed per detector rather than tuned.
- ROC AUC is the only metric; precision at a fixed budget is not evaluated.

## Real-Time Pose Estimation App (`real-time-pose-estimation-app`)

**Source implementation:** A single-person pose estimator with a small Flask API.

**Brief distinction:** Create real-time human pose, hand, and face-mesh applications such as a fitness rep counter, gesture controller, or rehabilitation angle-measuring app.

**Implemented behaviors taught:**
- Moving synthetic figure across frames
- A detector that finds the people in a frame and joins the parts of one person together
- A trained keypoint regressor: the joints are learned from the frames with a ridge regression, not read off the bounding box
- PCK and the mean joint error as the metrics
- Flask endpoint returning joint coordinates as JSON
- A picture you upload, and a camera when OpenCV is installed
- An API key, a rate limit and a model that can be saved and trained again

**Source limitations/review:**
- MediaPipe is not used, so the regressor is a ridge regression over the brightness of a small grid of the person, not a neural network. The detector also assumes bright figures on a dark background.
- The camera needs OpenCV and a camera; without them the simulator and the upload are the inputs.
- The person is found by the bright pixels, so a person on a bright background is not found.

## Recommender Algorithm Benchmark (`recommender-algorithm-benchmark`)

**Source implementation:** Compare four recommendation strategies on the same ratings.

**Brief distinction:** Systematically compare dozens of recommender algorithms (matrix factorization, GNN, sequential models) on public datasets with unified, reproducible pipelines.

**Implemented behaviors taught:**
- Synthetic ratings with popularity and genre effects
- Popularity, item-item cosine, SVD and NMF recommenders
- Precision@5, recall@5 and catalogue coverage
- Recommendation samples for one user

**Source limitations/review:**
- The dataset is small and synthetic.
- Only top-5 recommendations are evaluated.
- There is no hyperparameter search or neural recommender.

## Retrieval-Augmented Document Q&A (`retrieval-augmented-document-q-a`)

**Source implementation:** Retrieve passages with TF-IDF and answer with the best sentence.

**Brief distinction:** Build a retrieval-augmented question-answering assistant over PDFs or wiki pages with embeddings, vector stores, and evaluation of answer faithfulness.

**Implemented behaviors taught:**
- Small built-in document collection
- TF-IDF passage retrieval
- Extractive answer selection with source attribution
- Retrieval hit rate and answer overlap metrics

**Source limitations/review:**
- Answers are sentences copied from the documents, not generated text.
- The corpus has twelve short passages and a handful of questions.
- There are no embeddings, chunking strategies or LLM calls.

## Sales Forecasting with Prophet (`sales-forecasting-with-prophet`)

**Source implementation:** A Prophet-style additive sales forecast with weekly and yearly effects.

**Brief distinction:** Forecast retail sales, demand, or web traffic with Prophet seasonality and holiday components, producing prediction intervals for business planning dashboards.

**Implemented behaviors taught:**
- Synthetic daily sales with trend, weekly and yearly patterns
- Additive decomposition and a horizon forecast
- Holiday bumps included in the generator
- MAE, MAPE and forecast plot

**Source limitations/review:**
- The sales series is synthetic; no store data is used.
- The forecast does not model promotions or inventory constraints.
- Confidence intervals and changepoint detection are not implemented.

## Segment Anything (SAM) Fine-tuning (`segment-anything-sam-fine-tuning`)

**Source implementation:** Point-prompted segmentation with thresholding and connected components.

**Brief distinction:** Build an interactive annotation and segmentation tool by fine-tuning Meta's SAM on a small labeled dataset such as surgical tools or surface defects.

**Implemented behaviors taught:**
- Synthetic images with one or two foreground shapes
- An encoder that turns an image into an embedding and a decoder that turns a prompt and an embedding into a mask
- Three prompt types: a point, a box and a mask
- A fine tuning loop that fits the parameters of the decoder and reports the loss after every round
- IoU and success-rate evaluation
- A FastAPI endpoint that answers with the mask (run length encoded), the bounding box and the IoU with the truth

**Source limitations/review:**
- Only one bright shape per image is supported.
- The point prompt must land inside the shape.
- There is no encoder training or mask decoder network.

## Semantic Segmentation with U-Net and DeepLab (`semantic-segmentation-with-u-net-and-deeplab`)

**Source implementation:** A tiny U-Net for synthetic shape segmentation.

**Brief distinction:** Segment road scenes, cells, or organs by training U-Net/DeepLabV3+/PSPNet backbones with pretrained encoders and comparing Dice and IoU metrics across architectures.

**Implemented behaviors taught:**
- Synthetic 32x32 images and binary masks
- Small encoder-decoder U-Net in Keras
- Dice and pixel accuracy metrics
- Prediction panel saved after training

**Source limitations/review:**
- Images are simple shapes on a noisy background, not photographs.
- Training is very short; this is a pipeline demonstration, not a strong segmenter.
- There is no augmentation library or pretrained encoder.

## Speech-to-Text Transcription Service (`speech-to-text-transcription-service`)

**Source implementation:** Transcribe synthetic spoken digit strings.

**Brief distinction:** Build a transcription and subtitle-generation service around OpenAI Whisper, optionally fine-tuned on domain vocabulary such as medical or legal speech.

**Implemented behaviors taught:**
- Tone-based synthetic words with silence between them
- Energy-based word segmentation
- Random forest word classifier and sentence decode
- Word error rate plus a Flask transcription page

**Source limitations/review:**
- No real speech is recorded or recognized.
- The vocabulary is ten digits and the audio is generated from tones.
- A real service needs a trained acoustic model, language model and audio decoding.

## Streaming Anomaly Detection (`streaming-anomaly-detection`)

**Source implementation:** An online EWMA detector for a simulated metric stream.

**Brief distinction:** Detect anomalies in real-time time series such as server metrics and Twitter volume by implementing and scoring custom detectors on the Numenta Anomaly Benchmark.

**Implemented behaviors taught:**
- Streaming values with drift and injected spikes
- Online mean/variance updates with an EWMA
- Point-level precision, recall and detection delay
- Threshold sweep and a saved timeline plot

**Source limitations/review:**
- The stream is generated, not read from NAB.
- The detector is univariate and assumes one value per timestamp.
- Thresholds are tuned on the same simulated distribution.

## TensorFlow Object Detection API (`tensorflow-object-detection-api`)

**Source implementation:** Detect and classify simple shapes in synthetic images.

**Brief distinction:** Train and deploy custom object detectors (people, helmets, vehicles) on domain images using the TensorFlow Model Garden detection API with COCO-pretrained checkpoints.

**Implemented behaviors taught:**
- Synthetic scenes with circles and squares
- Connected-component proposals
- Crop features and a random forest shape classifier
- Box precision, recall and class accuracy

**Source limitations/review:**
- Only circles and squares on a clean background are supported.
- There are no overlapping objects or real photographs.
- The proposal stage is connected components, not a region proposal network.

## Time-Series Classification Pipelines (`time-series-classification-pipelines`)

**Source implementation:** Classify short time series with summary and frequency features.

**Brief distinction:** Apply unified time-series pipelines to classification and forecasting tasks such as human activity recognition using sktime's scikit-compatible API.

**Implemented behaviors taught:**
- Synthetic sine, square and trending series
- Time-domain and FFT-based features
- Random forest classifier with a confusion matrix
- Single-series prediction in demo mode

**Source limitations/review:**
- Classes are generated from simple formulas with noise.
- The classifier only sees summary features, not the raw sequence.
- There is no temporal cross-validation.

## Topic Modeling with BERTopic (`topic-modeling-with-bertopic`)

**Source implementation:** Group short news snippets into topics with TF-IDF and NMF.

**Brief distinction:** Uncover latent themes in large text corpora such as research abstracts, reviews, or support tickets with transformer embeddings, HDBSCAN clustering, and interactive charts.

**Implemented behaviors taught:**
- Small built-in news corpus
- TF-IDF vectorisation and NMF topic factors
- Document assignment with confidence scores
- Top terms and representative documents per topic

**Source limitations/review:**
- Documents are short synthetic news snippets.
- Topics come from word frequencies, not sentence embeddings.
- The number of topics is fixed rather than discovered.

## Train a GPT Language Model from Scratch (`train-a-gpt-language-model-from-scratch`)

**Source implementation:** A character-level transformer trained on a tiny public-domain-style corpus.

**Brief distinction:** Train a GPT language model from scratch on a domain corpus (code, chats, literature) and study scaling behavior, sampling strategies, and fine-tuning.

**Implemented behaviors taught:**
- Character tokeniser built from the training text
- Small embedding plus self-attention block
- Next-character training with sparse categorical loss
- Sampled continuation saved after training

**Source limitations/review:**
- The corpus is a few paragraphs, so the model memorises rather than generalises.
- There is no tokeniser training, positional encoding study or large-scale pretraining.
- Sampling is temperature-based and often produces odd words.

## Wake-Word Keyword Spotting (`wake-word-keyword-spotting`)

**Source implementation:** Spot a wake phrase in synthetic audio.

**Brief distinction:** Build an always-listening wake-word recognizer for smart devices using the Google Speech Commands dataset with quantization for on-device deployment.

**Implemented behaviors taught:**
- Synthetic positive phrase and negative background clips
- Log-band audio features
- Random forest keyword detector
- Accuracy and false-positive rate

**Source limitations/review:**
- All clips are synthesized from tones and noise.
- This is a binary detector, not a streaming microphone application.
- The negative clips do not cover real background sounds.

## Wav2Vec2 Low-Resource ASR Fine-tuning (`wav2vec2-low-resource-asr-fine-tuning`)

**Source implementation:** Frame-level phonetic classification with greedy decoding.

**Brief distinction:** Adapt self-supervised speech representations by fine-tuning Wav2Vec 2.0 with very limited labels for low-resource language or accented ASR.

**Implemented behaviors taught:**
- Synthetic words made from phoneme-like tone segments
- Frame features and frame-level labels
- Random forest frame classifier
- Greedy collapse decoding and word error rate

**Source limitations/review:**
- The audio is synthesized and the 'phonemes' are tone bands.
- The model classifies independent frames; it is not a self-supervised speech model.
- Greedy decoding is simple and has no language model.

## Weed Species Detection (`weed-species-detection`)

**Source implementation:** Classify synthetic weed species from leaf features.

**Brief distinction:** Classify eight Australian weed species in pasture imagery with transfer-learned ResNet50 and InceptionV3 models and discuss precision-agriculture deployment on drones.

**Implemented behaviors taught:**
- Procedurally drawn leaves for four species
- Shape and colour summary features
- Random forest classifier with per-species accuracy
- Sample leaf images saved for inspection

**Source limitations/review:**
- Leaves are simple geometric shapes, not field photographs.
- Features are hand-built instead of learned by a CNN.
- There is no augmentation, transfer learning or background variation.
