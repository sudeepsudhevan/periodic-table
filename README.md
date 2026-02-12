# Agile Docker Periodic Table

A modern, responsive, and Docker-ready Periodic Table of Elements application. This project demonstrates an Agile workflow, CI/CD integration, and automated testing.

**[🔴 Live Demo](https://sudeepsudhevan.github.io/periodic-table/)**

## 🚀 Features

-   **Interactive Table**: Click on any element (H to Og) to view detailed properties.
-   **Responsive Design**: Optimized for Desktop (Grid), Tablet (Stacked), and Mobile (Scrollable).
-   **Detailed Views**: `details.html` dynamically fetches data from `elements.json`.
-   **Agile Workflow**: Includes Issue Templates and GitHub Project integration.
-   **Automated Testing**: Unit tests for HTML structure and content.
-   **CI/CD**: GitHub Actions pipeline for auto-testing and Docker building.
-   **Dockerized**: Run anywhere with a lightweight Nginx container.

---

## 🛠️ How to Use

### 1. Run Locally (Python)
If you don't want to use Docker, you can serve the static files using Python:
```bash
python -m http.server 8000
```
Open [http://localhost:8000](http://localhost:8000) in your browser.

### 2. Run with Docker
Build and run the container:
```bash
# Build the image
docker build -t periodic-table .

# Run the container (Map port 8080 to container port 80)
docker run -d -p 8080:80 periodic-table
```
Open [http://localhost:8080](http://localhost:8080) in your browser.

---

## 🔄 Implementing Agile Features

This project is set up to simulate a real-world Agile environment.

### 1. Issue Templates
When you create a new issue, choose a template:
-   **Bug Report**: For reporting errors (includes steps to reproduce).
-   **Feature Request**: For proposing new ideas (includes problem & solution).

### 2. GitHub Project Board
Use a GitHub Project (Kanban board) to track your work:
1.  Create a Project (Template: "Team Planning" or "Kanban").
2.  Add your issues to the project.
3.  Move issues through columns: **Todo** -> **In Progress** -> **Done**.

### 3. Creating Issues
You can manually create issues or use the GitHub CLI:
```bash
gh issue create --template feature_request.md
```

---

## 🧪 How to Test

We use Python's `unittest` to verify the application structure.

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run Tests
```bash
python -m unittest discover tests
```
**What gets tested?**
-   Page title ("Periodic Table").
-   Presence of key elements (Hydrogen, Helium).
-   HTML file integrity.

### 3. CI/CD Pipeline
Every push to the `main` branch triggers the workflow in `.github/workflows/ci.yml`:
1.  **Checkout Code**: Pulls the latest code.
2.  **Test**: Runs the unit tests.
3.  **Build**: Builds the Docker image.

Check the **Actions** tab in your repository to see the results.

---

## 📂 Project Structure

```
periodic-table/
├── .github/
│   ├── ISSUE_TEMPLATE/    # Bug report & Feature request templates
│   └── workflows/ci.yml   # CI/CD pipeline configuration
├── tests/                 # Unit tests
├── Dockerfile             # Docker configuration
├── elements.json          # Data source for all 118 elements
├── index.html             # Main Periodic Table grid
├── details.html           # Element details page
├── requirements.txt       # Python test dependencies
└── README.md              # Project documentation
```

---

## 📝 License

This project is open-source and available under the standard MIT License.
