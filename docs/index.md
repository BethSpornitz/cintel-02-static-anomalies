# Continuous Intelligence

This site provides documentation for this project.
Use the navigation to explore module-specific materials.

## How-To Guide

Many instructions are common to all our projects.

See
[⭐ **Workflow: Apply Example**](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/)
to get these projects running on your machine.

## Project Documentation Pages (docs/)

- **Home** - this documentation landing page
- **Project Instructions** - instructions specific to this module
- **Your Files** - how to copy the example and create your version
- **Glossary** - project terms and concepts

## Custom Project

### Dataset
The dataset used for this project contains patient records from a clinic and includes two variables: age_years and height_inches. Each row represents a patient visit with the patient’s age in years and height in inches.

### Signals
The primary signals used were age_years and height_inches from the dataset. I also created a derived signal called anomaly_reason to explain why a record was identified as an anomaly.

### Experiments
I modified the anomaly detection pipeline to better fit adult clinic data. I introduced both upper and lower thresholds for age and height and added a column called anomaly_reason that labels whether the anomaly was caused by unrealistic age or height values.

### Results
After running the modified pipeline, two records were detected as anomalies. Both anomalies were due to unrealistic age values (ages 102 and 118). No height anomalies were detected using the defined thresholds.

### Interpretation
The results show that the anomaly detection pipeline can successfully identify unrealistic patient data values. Adding the anomaly_reason column improves the interpretability by clearly identifying the cause of each anomaly. This approach would help analysts or data quality teams quickly identify potential data entry issues in larger datasets.

## Additional Resources

- [Suggested Datasets](https://denisecase.github.io/pro-analytics-02/reference/datasets/cintel/)
