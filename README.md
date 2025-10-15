# 🚀 GitHub Native PR CI Pipeline – POC

This POC shows:
- ✅ Unit tests + security scanning
- 📊 Risk scoring
- 💬 Auto PR comments with metrics
- 📂 JSON reports for Figma dashboards
- 📝 Intent-driven PR templates

Trigger: every PR to `main` branch.

Try making a PR:
1. Modify `src/app.py` or tests
2. Open a PR → CI runs
3. Metrics auto-commented + JSON report pushed to `reports` branch

# GitHub PR Dashboard (POC)

This project demonstrates how to use **GitHub-native workflows** to automate:
- CI/CD (tests, lint, security scan)
- Risk scoring & PR metrics
- Auto-updating dashboards

## Key Features
- GitHub Actions only (no third-party tools).
- PR summary with risk score & metrics.
- JSON + Markdown dashboard in `/docs`.
- Optional auto-merge for safe PRs.

## Folder Structure
- `.github/workflows/` → Actions
- `docs/` → Dashboard output

## How to Run
1. Fork/clone this repo.
2. Create a new PR → See metrics auto-post.
3. View `docs/dashboard.json` and `docs/dashboard.md` for live PR status.
 
