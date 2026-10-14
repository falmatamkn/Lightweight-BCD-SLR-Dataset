# A Systematic Literature Review of Lightweight Machine Learning for Breast Cancer Detection

This repository contains the extracted study data and supporting reproducibility materials for the systematic literature review:

**A Systematic Literature Review of Lightweight Machine Learning for Breast Cancer Detection**

## Revised Study Version

The latest release accompanies the revised manuscript. It provides the expanded study dataset, updated database search strategies, VOSviewer thesaurus, and supporting figures prepared following peer review.

The two earlier releases correspond to the previous study version and remain available for historical reference. Use the latest release to access the materials associated with the revised manuscript.

## Dataset Description

The dataset contains information extracted from the included studies on lightweight machine learning techniques for breast cancer detection.

The extracted information includes, where available:

- Publication information
- Datasets and data modalities
- Lightweight machine learning techniques
- Taxonomy classifications
- Predictive performance metrics
- Parameter counts
- GFLOPs
- Model size and memory information
- Inference time and latency
- Deployment information

Resource and performance measurements are recorded as reported in the original studies. Missing measurements should not be interpreted as zero values.

The extracted data support the taxonomy, comparative analyses, and visualizations presented in the revised manuscript.

## Repository Contents

| File or folder | Description |
|---|---|
| `StudyData_revised` | Expanded study dataset and extracted information used in the revised manuscript. |
| `Search_String` | Updated database-specific search strings, search dates, and applied filters. |
| `VOSviewer_Reviewer/bcd_thesaurus_v5_R1` | Thesaurus used to standardize and merge terms for the keyword analysis. |
| `VOSviewer_Reviewer/vos_settings` | Settings used for the VOSviewer analysis. |

## Reproducing the VOSviewer Analysis

The keyword co-occurrence analysis was conducted using **VOSviewer version [version number]**, with the following settings:

- **Analysis type:** Co-occurrence
- **Unit of analysis:** Author keywords
- **Counting method:** Full counting
- **Minimum occurrence threshold:** 3 occurrences
- **Number of keywords included in the final analysis:** 25

The thesaurus at `VOSviewer_Reviewer/bcd_thesaurus_v5_R1` was used to standardize keyword labels and merge equivalent terms. Further analysis settings are documented in `VOSviewer_Reviewer/vos_settings`.

To reproduce the analysis, use the same bibliographic input data, apply the supplied thesaurus, and configure VOSviewer using the settings above and those recorded in the settings file.

Use the supplied input data and thesaurus with these settings to reproduce the analysis. The thesaurus documents the term replacements and exclusions applied during keyword standardization.

## Authors

- Falmata Modu
- Rajesh Prasad
- Farouq Aliyu
- Peter Onwualu

## Data Availability and Versioning

These materials are publicly available to support transparency, reproducibility, and further research on lightweight machine learning for breast cancer detection.

Each release identifies a specific version of the study materials. When using or citing the revised dataset, include its release tag and release URL to identify the exact version used.
