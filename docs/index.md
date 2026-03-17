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

## Additional Resources

- [Suggested Datasets](https://denisecase.github.io/pro-analytics-02/reference/datasets/cintel/)

---

### Dataset 1: Adult Clinic Data

#### Dataset
This dataset contains patient records from an adult clinic.
Each row represents a patient visit and includes:

- `age_years` – patient age
- `height_inches` – patient height

#### Signals
Two signals were analyzed:

- **age_years**
- **height_inches**

These values were evaluated against reasonable ranges for adult patients.

#### Experiments
The anomaly detection pipeline was modified to include minimum and maximum thresholds for both age and height.
An additional column called `anomaly_reason` was created to indicate whether an anomaly was caused by age or height values outside expected limits.

#### Results
The pipeline detected two anomalies where the age values were extremely high (102 and 118 years).

#### Interpretation
This suggests either data entry errors or extremely rare cases. In a real clinical system, these records would be flagged for verification to make sure they were correct.

---

### Dataset 2: Transit Ridership Data

#### Dataset
This dataset represents daily transit ridership observations.
Each row contains:

- `day` – sequential day of observation
- `rides` – total number of transit rides recorded that day

#### Signals
The primary signal analyzed was:

- **rides** (daily ridership)

#### Experiments
A modified anomaly detection pipeline was created to identify unusually high ridership values.
A threshold was set to detect ridership spikes that may represent unusual transit demand.

#### Results
The system detected ridership spikes on days where the number of rides exceeded the expected range.

Example anomaly:

| day | rides | anomaly_reason |
|----|----|----|
| 15 | 8000 | ridership spike |

#### Interpretation
The spike likely represents a special event or abnormal demand on the transit system for some reason. In the real world, this could trigger some sort of alert for teams monitoring transit volumes.

---

### Summary

These experiments demonstrate that the same anomaly detection pipeline structure can be adapted for different domains by:

- changing the dataset
- modifying thresholds
- adjusting the anomaly logic

This flexibility is important for continuous intelligence systems.
