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
The dataset used for this project contains adult clinic patient records with two measurements: age_years and height_inches. Each row represents a patient visit.

### Signals
The primary signals used were age_years and height_inches. I also created a derived signal called anomaly_reason to explain why a record was identified as an anomaly.

### Experiments
I adapted the anomaly detection pipeline from the pediatric example to an adult clinic context by introducing realistic lower and upper bounds for age and height and adding an anomaly_reason column.

### Results
The pipeline detected two anomalies caused by unrealistic age values (102 and 118). No height anomalies were detected using the defined thresholds.

### Interpretation
This modification demonstrates how anomaly detection rules must be adapted to the domain of the data. Adding the anomaly_reason column improves interpretability and would help analysts quickly identify data quality issues in larger datasets.

## Additional Resources

- [Suggested Datasets](https://denisecase.github.io/pro-analytics-02/reference/datasets/cintel/)
