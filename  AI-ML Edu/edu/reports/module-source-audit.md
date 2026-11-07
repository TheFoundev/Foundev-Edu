# Module-to-source alignment audit

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

