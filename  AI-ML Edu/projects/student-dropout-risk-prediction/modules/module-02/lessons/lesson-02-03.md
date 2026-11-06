# Database and Data Preparation: Validate outputs and identify limitations for database and data preparation

**Lesson ID:** `lesson-02-03`  
**Module:** Database and Data Preparation  
**Source focus:** `pipeline/__1_and_2_Read_and_Describe_Data.py` → `impute_mean`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by DEWS: Student Dropout Risk Prediction. By the end, you can describe SQL creation, missingness, and engineered features, trace the database and data preparation implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about SQL creation, missingness, and engineered features. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

The source-specific focus for this module is `impute_mean` in `pipeline/__3_Missing_Data_Processing.py`. Use the excerpt below to trace the actual inputs, transformation, and output for SQL creation, missingness, and engineered features. Where a behavior is absent, follow the documented boundary rather than assuming it exists.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: The UI is a demo; the historical pipeline scripts are documented as mostly broken/legacy. Labels are an administrative rule. Risk scores must support voluntary services, not punitive decisions.

## Step-by-step source investigation

1. Open `pipeline/__3_Missing_Data_Processing.py` and inspect `impute_mean`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with `PROJECT_OVERVIEW.md` and `WORKFLOW.md`; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `pipeline/__3_Missing_Data_Processing.py` (not executed during package generation):

```python
def impute_mean(variable, data_in, data_out):

    #Define Data
    data = pd.read_csv(data_in, index_col=0)
    data.columns = [camel_to_snake(col) for col in data.columns]

    #Get Row Index for Variable
    number = (data.columns.get_loc(str(variable)))+1

    #Generate Mean
    m_var = data[str(variable)].mean()
    meanVar = int(round(m_var))

    in_file = open(data_in, 'rU')
    reader = csv.reader(in_file)
    out_file = open(data_out, "w")
    writer = csv.writer(out_file)
    for row in reader:
        #Monthly_income = row[6]
        variable_observation = row[number]
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For database and data preparation, use the repository's own output format and the available test fixture where possible.

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

You can now validate outputs and identify limitations for database and data preparation, identify its source location, and state a limitation. The key project-specific fact is: Validate outputs and identify limitations for database and data preparation. In this repository, the claim must be grounded in the documented behavior and source paths: pipeline/__1_and_2_Read_and_Describe_Data.py; pipeline/__3_Missing_Data_Processing.py.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository files `PROJECT_OVERVIEW.md` and `WORKFLOW.md` (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
