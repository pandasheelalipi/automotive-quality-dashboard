# 📐 Methodology & Data Dictionary

## Quality Framework

This project follows standard automotive quality management principles aligned with:
- **IATF 16949** — Automotive Quality Management System standard
- **VDA 6.3** — Process Audit standard used by German OEMs (BMW, Mercedes-Benz, Audi, VW Group)
- **APQP** — Advanced Product Quality Planning framework

---

## Module Descriptions

### 1. Defect Log
Tracks individual quality non-conformances across plants, components, and suppliers.

| Field | Description |
|---|---|
| Defect ID | Unique identifier (DEF-XXXX) |
| Component | Automotive component affected |
| Severity | Critical / Major / Minor |
| Status | Open / In Progress / Closed |
| Days to Close | Resolution time in days |

### 2. Monthly KPI Summary
Aggregated quality performance indicators tracked monthly.

| KPI | Definition | Target |
|---|---|---|
| First Pass Yield (%) | Components passing QC first time / total inspected | ≥ 95% |
| Process Audit Score (%) | Average score across all audit criteria | ≥ 85% |
| Supplier Quality Score (%) | Weighted supplier performance average | ≥ 88% |
| On-Time Delivery (%) | Deliveries on schedule / total deliveries | ≥ 92% |

### 3. Process Audit Log
Structured scoring of manufacturing process compliance based on VDA 6.3 criteria.

**Scoring:**
- 90–100: Pass — No action required
- 75–89: Pass — Monitor next cycle
- < 75: Fail — Corrective action required

### 4. Supplier Scorecard
Multi-criteria evaluation framework for supplier quality management.

**Rating System:**
- A (≥ 90%): Preferred supplier
- B (80–89%): Approved supplier — improvement targets set
- C (< 80%): Conditional — corrective action plan required

### 5. Corrosion Risk Register
Preventive risk assessment framework for component corrosion protection monitoring.

**Risk Score (1–10):**
- 8–10: High risk — Apply protective coating immediately
- 5–7: Medium risk — Increase inspection frequency
- 1–4: Low risk — Standard monitoring cycle

---

## Data Notes
All data in this project is **synthetically generated** for demonstration purposes.
No proprietary or confidential data from any company is used.
The framework mirrors real automotive quality management structures but all values are simulated.
