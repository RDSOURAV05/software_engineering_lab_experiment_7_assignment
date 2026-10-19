[![CI](https://github.com/RDSOURAV05/software_engineering_lab_experiment_7_assignment/actions/workflows/ci.yml/badge.svg)](https://github.com/RDSOURAV05/software_engineering_lab_experiment_7_assignment/actions/workflows/ci.yml)

# SAFE-VISION: AI-Powered Media Moderation & Quality Assurance System

## Abstract
SAFE-VISION is an automated multimodal computer vision and quality assurance platform designed for content safety, advertisement moderation, and dataset acquisition. The system processes multimodal ad media and face detection inputs, categorizing content into universal safe categories (SAFE_FOR_ALL) and age-gated categories (SAFE_14_PLUS). This repository manages the core engineering practices, including automated PyTest unit test suites, Git feature-branch workflows, and GitHub Actions CI/CD pipelines.

## Team Members & Project Roles
| Name | Roll No | GitHub Username | Assigned Module |
| :--- | :--- | :--- | :--- |
| **Sourav** | **51** | **RDSOURAV05** | **Dataset Acquisition & Management** |
| Joseph Benedict | 31 | `josephunited` | SafeAd AI Module |
| Juwel Jo | 33 | `JuwelJo` | Face Detection / Dataset Assistance |
| Sooraj Jose George | 50 | `SoorajGeorge123` | Face Detection Module |

## Technology Used
- **Programming Language**: Python 3.11 / 3.13
- **Testing Framework**: PyTest
- **Data Processing**: Pandas
- **CI/CD Automation**: GitHub Actions
- **Version Control & Agile**: Git, GitHub Issues & GitHub Projects (Kanban)
- **Deployment & Cloud**: Docker, FastAPI, AWS EC2 / Heroku

## How to Run Locally

### 1. Clone Repository & Setup Environment
```bash
git clone https://github.com/RDSOURAV05/software_engineering_lab_experiment_7_assignment.git
cd software_engineering_lab_experiment_7_assignment
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Execute Unit Test Suite
```bash
pytest -v
```
