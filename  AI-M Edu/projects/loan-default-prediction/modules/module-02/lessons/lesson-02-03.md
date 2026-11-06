# Features and Data Pipeline: Validate outputs and identify limitations for features and data pipeline

**Lesson ID:** `lesson-02-03`  
**Module:** Features and Data Pipeline  
**Source focus:** `train_predict.py` → `FeatureSelector`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by Underwriting Desk: Loan Default Risk Modeling. By the end, you can describe train/test CSV contract and engineered features, trace the features and data pipeline implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about train/test CSV contract and engineered features. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

The source-specific focus for this module is `FeatureSelector` in `models.py`. Use the excerpt below to trace the actual inputs, transformation, and output for train/test CSV contract and engineered features. Where a behavior is absent, follow the documented boundary rather than assuming it exists.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: The web UI is a heuristic demo, not the trained pipeline. The legacy training path requires missing CSV inputs and porting; no model artifact is supplied. Credit decisions need rigorous fairness, calibration, and legal review.

## Step-by-step source investigation

1. Open `models.py` and inspect `FeatureSelector`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with `PROJECT_OVERVIEW.md` and `WORKFLOW.md`; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `models.py` (not executed during package generation):

```python
class FeatureSelector(object):

    def __init__(self):
        self.strong = ['f528-f527', 'f528-f274', 'f527-f274', 'hasnull', 'f271', 'f2',
                       'f332', 'f776','f336', 'f777', 'f4', 'f5', 'f647', 'trial2']
        self.tail_feature_300 = ['f607', 'f723', 'f453', 'f452', 'f604', 'f454', 'f457', 'f456', 'f459', 'f163', 'f162', 'f164', 'f752', 'f769', 'f502', 'f510', 'f455', 'f512', 'f762', 'f761', 'f283', 'f688', 'f206', 'f42', 'f750', 'f606', 'f681', 'f683', 'f684', 'f685', 'f686', 'f687', 'f608', 'f505', 'f504', 'f469', 'f610', 'f549', 'f616', 'f615', 'f507', 'f758', 'f759', 'f420', 'f119', 'f299', 'f503', 'f115', 'f501', 'f500', 'f293', 'f757', 'f291', 'f113', 'f215', 'f214', 'f511', 'f192', 'f692', 'f691', 'f690', 'f697', 'f506', 'f592', 'f595', 'f550', 'f537', 'f534', 'f94', 'f530', 'f531', 'f198', 'f625', 'f749', 'f748', 'f538', 'f539', 'f644', 'f435', 'f345', 'f109', 'f346', 'f472', 'f105', 'f104', 'f103', 'f439', 'hasnull', 'f95', 'f184', 'f182', 'f224', 'f497', 'f188', 'f583', 'f581', 'f580', 'f585', 'f584', 'f521', 'f28', 'f633', 'f730', 'f736', 'f482', 'f483', 'f480', 'f481', 'f486', 'f487', 'f484', 'f485', 'f400', 'f207', 'f285', 'f323', 'f130', 'f131', 'f515', 'f137', 'f527', 'f335', 'f232', 'f33', 'f36', 'f48', 'f678', 'f568', 'f125', 'f722', 'f720', 'f120', 'f123', 'f724', 'f728', 'f129', 'f747', 'f554', 'f555', 'f557', 'f419', 'f551', 'f552', 'f415', 'f414', 'f558', 'f559', 'f124', 'f753', 'f325', 'f89', 'f321', 'f85', 'f84', 'f242', 'f83', 'f190', 'f675', 'f627', 'f528', 'f770', 'f152', 'f718', 'f719', 'f158', 'f389', 'f714', 'f712', 'f713', 'f710', 'f711', 'f547', 'f546', 'f90', 'f544', 'f543', 'f542', 'f541', 'f540', 'f460', 'f461', 'f99', 'f464', 'f466', 'f548', 'f317', 'f315', 'f252', 'f495', 'f494', 'f18', 'f496', 'f491', 'f490', 'f493', 'f492', 'f576', 'f709', 'f708', 'f387', 'f329', 'f347', 'f8', 'f703', 'f705', 'f704', 'f707', 'f706', 'f572', 'f570', 'f571', 'f262', 'f577', 'f574', 'f575', 'f114', 'f578', 'f579', 'f477', 'f476', 'f268', 'f470', 'f309', 'f666', 'f307', 'f301', 'f475', 'f78', 'f62', 'f396', 'f446', 'f447', 'f445', 'f174', 'f172', 'f173', 'f449', 'f569', 'f274', 'f565', 'f564', 'f567', 'f777', 'f561', 'f560', 'f772', 'f562', 'f52', 'f467', 'f93', 'f372', 'f355', 'f284', 'f754', 'f77']
        self.exclude = self.tail_feature_300
        
    def _reduce(self, df, columns):
        table = defaultdict(list)
        for col in columns:
            vec = df[col]
            key = (vec.dropna().count(), vec.min(), vec.max(), vec.mean(), vec.median())
            table[key].append(col)
        return [a[0] for a in table.values()]
        
    def fit(self, X, y=None):
        dtypes = X.dtypes.apply(lambda x: x.name).to_dict()
        int_cols, float_cols, str_cols = [], [], []
        for col, dtype in dtypes.iteritems():
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For features and data pipeline, use the repository's own output format and the available test fixture where possible.

## Practical exercise

Complete [`exercise-02-03.md`](../exercises/exercise-02-03.md).

## Common mistakes and debugging

- Confusing a visual mockup or demo heuristic with the model/pipeline implementation.
- Assuming an absent data file, weight, service, or credential is bundled.
- Reporting accuracy without checking class balance, split strategy, or an appropriate baseline.
- Editing a pipeline before establishing input shape and output contract.
- Treating confidence/similarity as calibrated probability or proof.

## Best practices and responsible use

Keep data provenance and split boundaries explicit, make errors visible, log no sensitive raw inputs unnecessarily, and retain a human correction path for consequential outputs. Test failure and missing-artifact cases as well as the happy path.

## Summary

You can now validate outputs and identify limitations for features and data pipeline, identify its source location, and state a limitation. The key project-specific fact is: Validate outputs and identify limitations for features and data pipeline. In this repository, the claim must be grounded in the documented behavior and source paths: train_predict.py; models.py.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository files `PROJECT_OVERVIEW.md` and `WORKFLOW.md` (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
