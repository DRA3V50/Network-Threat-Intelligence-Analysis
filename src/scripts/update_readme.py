name: NTIA Pipeline

on:
  schedule:
    - cron: "0 13 * * *"   # 08:00 EST
    - cron: "0 1 * * *"    # 20:00 EST
  workflow_dispatch:       # manual trigger

jobs:
  run_pipeline:
    runs-on: ubuntu-latest

    env:
      NTIA_KEY: ${{ secrets.NTIA_Key }}  # classic token for HTTPS push

    steps:
      # 1️⃣ Checkout repository
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          persist-credentials: false

      # 2️⃣ Setup Python
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      # 3️⃣ Install dependencies
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      # 4️⃣ Run NTIA pipeline
      - name: Run NTIA pipeline
        run: python -m src.run

      # 5️⃣ Run README update script
      - name: Update README
        run: python src/scripts/update_readme.py

      # 6️⃣ Commit & push updates
      - name: Commit & push changes
        run: |
          git config user.name "github-actions"
          git config user.email "github-actions@github.com"

          # Stage all updated files, force-add outputs if ignored
          git add README.md build outputs -f

          # Commit only if there are changes
          git diff --cached --quiet || git commit -m "Automated update: pipeline outputs + README"

          # Push to main branch using token
          git push https://$NTIA_KEY@github.com/DRA3V50/Network-Threat-Intelligence-Analysis.git main
