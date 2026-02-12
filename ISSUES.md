# Agile Project Issues

Use these to populate your GitHub Project board to simulate an Agile workflow.

## Epic: Containerization & CI/CD Setup

### Story 1: Containerize Application
**As a** developer
**I want** to package the application in a Docker container
**So that** it can run consistently across different environments.

**Acceptance Criteria:**
- [ ] Dockerfile exists
- [ ] Image builds successfully
- [ ] Container runs and serves `index.html` on port 80

### Story 2: Implement Automated Testing
**As a** QA engineer
**I want** automated tests for the periodic table
**So that** we can ensure the application structure remains valid.

**Acceptance Criteria:**
- [ ] `tests/test_periodic_table.py` created
- [ ] Tests verify title and key elements
- [ ] Tests can be run with `python -m unittest`

### Story 3: Set up CI/CD Pipeline
**As a** DevOps engineer
**I want** a CI/CD pipeline
**So that** tests and builds run automatically on every push.

**Acceptance Criteria:**
- [ ] `.github/workflows/ci.yml` created
- [ ] Workflow runs tests
- [ ] Workflow builds Docker image if tests pass

### Bug: Mobile Responsiveness (Future)
**As a** mobile user
**I want** the periodic table to stack vertically on small screens
**So that** I can read it easily.

**Acceptance Criteria:**
- [ ] CSS media queries added for screens < 768px
