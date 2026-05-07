# 🚗 Automotive Quality & Process Intelligence Dashboard

**Author:** Sheelalipi Panda  
**Programme:** M.Sc. Electromobility (ACES), FAU Erlangen-Nürnberg  
**Status:** 🟢 Ongoing Project  
**Last Updated:** May 2026

---

## 📌 Project Overview

This project simulates a real-world **automotive quality management intelligence system**, built to demonstrate practical skills in data analysis, quality assurance, process auditing, and structured reporting — directly relevant to OEM production environments at companies like **BMW, Mercedes-Benz, Audi**, and **Trench Group**.

The project generates, analyses, and visualises quality KPIs across five interconnected areas:

| Module | Description |
|---|---|
| 📊 Executive Dashboard | High-level KPI summary across all quality dimensions |
| 📉 Monthly KPI Trends | First Pass Yield, Audit Score, Supplier Score over 12 months |
| 🔍 Defect Log | 120-entry defect tracking across plants, components, and severity levels |
| ✅ Process Audit Log | 30 structured process audits with pass/fail scoring and corrective actions |
| 🏭 Supplier Scorecard | Multi-criteria supplier quality rating system (A/B/C ratings) |
| 🧪 Corrosion Risk Register | Component-level corrosion risk assessment (linked to published research) |

---

## 🎯 Why This Project Exists

Quality management roles at automotive OEMs require:
- **Data collection and analysis** — tracking defects, KPIs, and trends
- **Structured documentation** — audit logs, scorecards, risk registers
- **Cross-functional reporting** — dashboards for management decision-making
- **Process improvement thinking** — identifying patterns and recommending actions

This project was built independently to demonstrate all of these capabilities using real manufacturing quality frameworks — and to apply skills from my M.Sc. coursework and published research in a practical, visible way.

---

## 🛠️ Tools & Technologies

| Tool | Usage |
|---|---|
| Python 3 | Data generation, analysis, and automation |
| pandas | Data manipulation and aggregation |
| openpyxl | Excel report generation with charts and styling |
| MS Excel | Dashboard visualisation and KPI tracking |
| Power BI | *(planned)* Interactive visual dashboard |
| GitHub | Version control and project documentation |

---

## 📁 Project Structure

```
automotive-quality-dashboard/
│
├── scripts/
│   └── generate_data.py          # Main Python script — generates all data & Excel report
│
├── reports/
│   └── Automotive_Quality_Intelligence_Dashboard.xlsx   # Output Excel dashboard
│
├── data/                         # Raw / intermediate data files (CSV exports)
│
├── docs/
│   └── methodology.md            # Quality framework methodology and data dictionary
│
└── README.md
```

---

## 📊 Key Metrics Tracked

- **First Pass Yield (FPY%)** — % of components passing quality checks first time
- **Process Audit Score** — structured scoring of manufacturing process compliance
- **Supplier Quality Score** — multi-criteria evaluation of supplier performance
- **On-Time Delivery (OTD%)** — supplier delivery reliability
- **Defect Severity Distribution** — Critical / Major / Minor breakdown
- **Corrosion Risk Score** — component-level preventive risk assessment

---

## 🔗 Relevance to Published Research

The **Corrosion Risk Register** module is directly connected to my peer-reviewed publication:

> *Panda, S. et al. (2023). Corrosion Behavior of HVOF-Sprayed Cr₂O₃ + 10% TiC Composite Coatings on Al-6061. **Materials Today: Proceedings**, Elsevier.*

The project applies the same analytical framework — material, environment, coating, and risk scoring — in a simulated production quality context.

---

## 🚀 Planned Next Steps

- [ ] Add Power BI `.pbix` dashboard file
- [ ] Add CSV data exports for each module
- [ ] Build a corrosion prediction model using Python (scikit-learn)
- [ ] Add a certification checklist module (relevant to type approval / VET processes)
- [ ] Translate key sections to German

---

## 📬 Contact

**Sheelalipi Panda**  
panda.sheelalipi@gmail.com  
[LinkedIn](#) | FAU Erlangen-Nürnberg | Erlangen, Germany
