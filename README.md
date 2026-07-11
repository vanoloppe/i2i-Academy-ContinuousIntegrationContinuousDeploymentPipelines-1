# i2i Academy - Continuous Integration & Continuous Deployment Pipelines

This project implements a fully automated **Continuous Integration & Continuous Deployment (CI/CD)** pipeline for a Python-based application using **GitHub Actions**, **pytest**, and **Selenium** (Headless Chrome). 

---

## 🎯 Project Objectives & Overview

The primary goal of this project is to build and configure a continuous testing and deployment pipeline that automatically triggers on every code push to:
1. Validate low-level logic with **Unit Tests** using `pytest`.
2. Validate end-to-end user-facing UI loading with **Automated UI Tests** using `Selenium WebDriver` in a headless environment.
3. Automatically simulate a production deployment if and only if all tests pass.

---

## 📚 Theoretical Knowledge

### 1. What is the main difference between a Unit Test and a UI Test (Selenium) in terms of what they actually validate?
* **Answer**: Unit tests validate the smallest isolated parts of the application (such as individual functions or classes) in memory for logical correctness, whereas UI tests validate the end-to-end integration and user interface behavior by simulating actual user interactions in a real browser.

### 2. Why is it important to automate both of these testing types in a CI/CD pipeline before code goes to production?
* **Answer**: Automating both testing types in a CI/CD pipeline guarantees that both the low-level code logic and the final user-facing features remain bug-free, preventing regression issues from reaching production.

### 3. Why do we need to run Selenium in "Headless" mode when executing UI tests inside a cloud container like a GitHub Actions runner?
* **Answer**: Headless mode is necessary because cloud containers and CI/CD runners (like GitHub Actions) are headless Linux/Ubuntu systems that do not run a graphical user interface (GUI) or display server, requiring the browser to execute in-memory.

---

## 📁 Repository Structure

```text
├── .github/
│   └── workflows/
│       └── ci-cd.yml      # GitHub Actions CI/CD configuration
├── app.py                 # Application source code (Email validator)
├── test_app.py            # Pytest Unit test suite
├── test_ui.py             # Pytest & Selenium UI test suite
├── requirements.txt       # Python dependencies configuration
└── README.md              # Detailed project documentation
```

---

## 💻 Tech Stack & Dependencies

- **Core Language**: Python 3.x
- **Testing Framework**: pytest (v9.1.1+)
- **UI Automation**: Selenium WebDriver (v4.45.0+)
- **CI/CD Platform**: GitHub Actions
- **Browser**: Google Chrome / ChromeDriver (Managed automatically via Selenium Manager)

---

## 🛠️ Local Environment Setup

Follow these steps to run and test the project on your local machine:

### 1. Clone the Repository
```bash
git clone https://github.com/vanoloppe/i2i-Academy-ContinuousIntegrationContinuousDeploymentPipelines-1.git
cd i2i-Academy-ContinuousIntegrationContinuousDeploymentPipelines-1
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
```

### 3. Activate the Virtual Environment
* **Windows (PowerShell)**:
  ```powershell
  .\venv\Scripts\Activate.ps1
  ```
* **Windows (Command Prompt)**:
  ```cmd
  .\venv\Scripts\activate.bat
  ```
* **Linux/macOS**:
  ```bash
  source venv/bin/activate
  ```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🧪 Running Tests

Once the virtual environment is activated, you can run the test suite locally.

### Run All Tests
```bash
pytest
```

### Run Only Unit Tests
```bash
pytest test_app.py
```

### Run Only Selenium UI Tests (Headless)
```bash
pytest test_ui.py
```

---

## 🚀 GitHub Actions CI/CD Pipeline

The pipeline is configured in `.github/workflows/ci-cd.yml`. It runs automatically on every code push to any branch. 

### Pipeline Steps (Sequential Execution)

- **Step A (Environment Setup)**: 
  Installs Python 3.10 and configures the dependencies listed in `requirements.txt` (`pytest`, `selenium`) in a clean Ubuntu runner environment.
- **Step B (Unit Test Execution)**: 
  Runs `pytest test_app.py` to ensure core code functions properly.
- **Step C (UI Test Execution)**: 
  Runs `pytest test_ui.py`. The browser runs in **headless mode** (`--headless=new`, `--no-sandbox`, `--disable-dev-shm-usage`) to operate seamlessly inside the graphical-interface-free GitHub Actions container.
- **Step D (Simulated Deployment)**: 
  If and only if both test steps pass successfully, the pipeline executes the deployment simulation step, logging:
  `"All tests passed! Application successfully deployed to production."`
