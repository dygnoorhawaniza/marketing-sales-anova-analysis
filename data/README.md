# Data

Place the dataset here as:

`marketing_sales_data.csv`

Expected columns:

- `TV` — categorical TV promotion budget (`Low`, `Medium`, `High`)
- `Social Media` — social media promotion budget
- `Radio` — radio promotion budget
- `Sales` — sales outcome
- `Influencer` — influencer size (`Mega`, `Macro`, `Nano`, `Micro`)

The original exercise references the **Dummy Marketing and Sales Data** dataset by Saragih, H.S. The dataset itself is not included in this repository so the repository does not redistribute the source data.

After adding the CSV, run:

```bash
python src/anova_analysis.py
```
