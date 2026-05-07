"""
Automotive Quality & Process Intelligence Dashboard
====================================================
Author  : Sheelalipi Panda
Purpose : Generate synthetic automotive manufacturing quality KPI data
          and produce a structured Excel report with analysis.
Covers  : Quality Management | Process Audit | Supplier Data | Defect Tracking
          Relevant to: BMW, Mercedes-Benz, Audi, Trench Group applications
"""

import pandas as pd
import numpy as np
import openpyxl
from openpyxl.styles import (PatternFill, Font, Alignment, Border, Side,
                              GradientFill)
from openpyxl.utils import get_column_letter
from openpyxl.chart import BarChart, LineChart, Reference
from openpyxl.chart.series import DataPoint
import random
from datetime import datetime, timedelta
import os

random.seed(42)
np.random.seed(42)

# ── CONFIG ────────────────────────────────────────────────────────────────────
OUTPUT_PATH = os.path.join(os.path.dirname(__file__), '..', 'reports',
                           'Automotive_Quality_Intelligence_Dashboard.xlsx')

PLANTS     = ['Munich', 'Ingolstadt', 'Stuttgart', 'Sindelfingen', 'Untertürkheim']
COMPONENTS = ['Crankshaft', 'Cylinder Head', 'Crankcase', 'eATS Motor',
              'Transmission', 'Bushing', 'Instrument Transformer', 'Coil Assembly']
SUPPLIERS  = ['Supplier A', 'Supplier B', 'Supplier C', 'Supplier D', 'Supplier E']
DEFECT_TYPES = ['Surface Corrosion', 'Dimensional Deviation', 'Assembly Error',
                'Coating Failure', 'Contamination', 'Missing Component',
                'Torque Non-conformance', 'Weld Defect']
AUDIT_CRITERIA = ['Process Documentation', 'Cleanliness Standards',
                  'Corrosion Protection', 'Dimensional Accuracy',
                  'Tool Calibration', 'Operator Training', 'Traceability Records',
                  'Non-conformance Handling']
MONTHS = pd.date_range('2024-01-01', periods=12, freq='MS')

# ── 1. DEFECT LOG ─────────────────────────────────────────────────────────────
def make_defect_log(n=120):
    rows = []
    for i in range(1, n+1):
        date = MONTHS[0] + timedelta(days=random.randint(0, 364))
        component = random.choice(COMPONENTS)
        defect = random.choice(DEFECT_TYPES)
        plant = random.choice(PLANTS)
        supplier = random.choice(SUPPLIERS)
        severity = random.choice(['Critical', 'Major', 'Minor'])
        status = random.choice(['Closed', 'Closed', 'Closed', 'Open', 'In Progress'])
        days_to_close = random.randint(1, 30) if status == 'Closed' else None
        rows.append({
            'Defect ID': f'DEF-{i:04d}',
            'Date': date.strftime('%Y-%m-%d'),
            'Month': date.strftime('%B %Y'),
            'Plant': plant,
            'Component': component,
            'Supplier': supplier,
            'Defect Type': defect,
            'Severity': severity,
            'Status': status,
            'Days to Close': days_to_close
        })
    return pd.DataFrame(rows)

# ── 2. MONTHLY KPI SUMMARY ────────────────────────────────────────────────────
def make_kpi_summary():
    rows = []
    for i, month in enumerate(MONTHS):
        defects_found    = random.randint(8, 20)
        defects_closed   = random.randint(6, defects_found)
        first_pass_yield = round(random.uniform(92, 99), 2)
        audit_score      = round(random.uniform(75, 98), 1)
        supplier_score   = round(random.uniform(80, 97), 1)
        otd              = round(random.uniform(88, 99), 1)  # On-Time Delivery %
        rows.append({
            'Month': month.strftime('%b %Y'),
            'Defects Found': defects_found,
            'Defects Closed': defects_closed,
            'Open Defects': defects_found - defects_closed,
            'First Pass Yield (%)': first_pass_yield,
            'Process Audit Score (%)': audit_score,
            'Supplier Quality Score (%)': supplier_score,
            'On-Time Delivery (%)': otd
        })
    return pd.DataFrame(rows)

# ── 3. PROCESS AUDIT SHEET ────────────────────────────────────────────────────
def make_audit_log():
    rows = []
    for i in range(1, 31):
        date = MONTHS[0] + timedelta(days=random.randint(0, 364))
        plant = random.choice(PLANTS)
        criteria = random.choice(AUDIT_CRITERIA)
        score = random.randint(60, 100)
        status = 'Pass' if score >= 75 else 'Fail'
        action = (
            'No action required' if score >= 90
            else 'Monitor next cycle' if score >= 75
            else 'Corrective action required'
        )
        rows.append({
            'Audit ID': f'AUD-{i:03d}',
            'Date': date.strftime('%Y-%m-%d'),
            'Plant': plant,
            'Criteria': criteria,
            'Score (%)': score,
            'Status': status,
            'Action Required': action,
            'Auditor': 'S. Panda'
        })
    return pd.DataFrame(rows)

# ── 4. SUPPLIER SCORECARD ─────────────────────────────────────────────────────
def make_supplier_scorecard():
    rows = []
    for supplier in SUPPLIERS:
        quality   = round(random.uniform(78, 98), 1)
        delivery  = round(random.uniform(82, 99), 1)
        documentation = round(random.uniform(75, 97), 1)
        responsiveness = round(random.uniform(70, 95), 1)
        overall   = round((quality + delivery + documentation + responsiveness) / 4, 1)
        rating    = 'A' if overall >= 90 else 'B' if overall >= 80 else 'C'
        rows.append({
            'Supplier': supplier,
            'Quality Score (%)': quality,
            'Delivery Score (%)': delivery,
            'Documentation Score (%)': documentation,
            'Responsiveness Score (%)': responsiveness,
            'Overall Score (%)': overall,
            'Rating': rating
        })
    return pd.DataFrame(rows)

# ── 5. CORROSION RISK REGISTER ────────────────────────────────────────────────
def make_corrosion_register():
    materials = ['Aluminum 6061', 'Steel (S355)', 'Cast Iron', 'Copper Alloy', 'Titanium']
    environments = ['High Humidity', 'Salt Spray', 'Thermal Cycling', 'Chemical Exposure']
    coatings = ['HVOF Cr₂O₃+TiC', 'Zinc Phosphate', 'Powder Coat', 'Anodizing', 'None']
    rows = []
    for i in range(1, 21):
        material = random.choice(materials)
        env = random.choice(environments)
        coating = random.choice(coatings)
        risk_score = random.randint(1, 10)
        mitigation = (
            'Apply protective coating' if risk_score >= 8
            else 'Increase inspection frequency' if risk_score >= 5
            else 'Standard monitoring'
        )
        rows.append({
            'Risk ID': f'COR-{i:03d}',
            'Component': random.choice(COMPONENTS),
            'Material': material,
            'Environment': env,
            'Coating Applied': coating,
            'Risk Score (1-10)': risk_score,
            'Risk Level': 'High' if risk_score >= 8 else 'Medium' if risk_score >= 5 else 'Low',
            'Mitigation Action': mitigation,
            'Review Date': (datetime.now() + timedelta(days=random.randint(30, 180))).strftime('%Y-%m-%d')
        })
    return pd.DataFrame(rows)

# ── EXCEL WRITER ──────────────────────────────────────────────────────────────
def style_header(ws, row, cols, fill_hex="1B4F72", font_color="FFFFFF"):
    fill = PatternFill("solid", fgColor=fill_hex)
    font = Font(bold=True, color=font_color, size=10)
    border = Border(
        bottom=Side(style='medium', color='FFFFFF'),
        right=Side(style='thin', color='FFFFFF')
    )
    for col in range(1, cols+1):
        cell = ws.cell(row=row, column=col)
        cell.fill = fill
        cell.font = font
        cell.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
        cell.border = border

def style_data_rows(ws, start_row, end_row, cols):
    light = PatternFill("solid", fgColor="EBF5FB")
    white = PatternFill("solid", fgColor="FFFFFF")
    font  = Font(size=9, color="1A1A2E")
    border = Border(
        bottom=Side(style='thin', color='D5D8DC'),
        right=Side(style='thin', color='D5D8DC')
    )
    for r in range(start_row, end_row+1):
        fill = light if r % 2 == 0 else white
        for c in range(1, cols+1):
            cell = ws.cell(row=r, column=c)
            cell.fill = fill
            cell.font = font
            cell.alignment = Alignment(horizontal='center', vertical='center')
            cell.border = border

def write_sheet(wb, title, df, color="1B4F72"):
    ws = wb.create_sheet(title=title)
    ws.sheet_view.showGridLines = False
    ws.row_dimensions[1].height = 30

    # Title row
    ws.merge_cells(f'A1:{get_column_letter(len(df.columns))}1')
    title_cell = ws['A1']
    title_cell.value = title
    title_cell.fill = PatternFill("solid", fgColor="1A1A2E")
    title_cell.font = Font(bold=True, color="FFFFFF", size=13)
    title_cell.alignment = Alignment(horizontal='center', vertical='center')

    # Header
    ws.row_dimensions[2].height = 28
    for col_idx, col_name in enumerate(df.columns, 1):
        ws.cell(row=2, column=col_idx, value=col_name)
    style_header(ws, 2, len(df.columns), fill_hex=color)

    # Data
    for r_idx, row in df.iterrows():
        for c_idx, value in enumerate(row, 1):
            ws.cell(row=r_idx+3, column=c_idx, value=value)
    style_data_rows(ws, 3, len(df)+2, len(df.columns))

    # Column widths
    for col_idx, col_name in enumerate(df.columns, 1):
        max_len = max(len(str(col_name)), df[df.columns[col_idx-1]].astype(str).str.len().max())
        ws.column_dimensions[get_column_letter(col_idx)].width = min(max_len + 4, 28)

    return ws

def add_kpi_charts(wb, kpi_df):
    ws = wb['Monthly KPI Summary']
    data_end = len(kpi_df) + 2

    # ── Bar Chart: Defects Found vs Closed
    bar = BarChart()
    bar.type = "col"
    bar.grouping = "clustered"
    bar.title = "Monthly Defects: Found vs Closed"
    bar.style = 10
    bar.y_axis.title = "Count"
    bar.x_axis.title = "Month"
    bar.width = 18
    bar.height = 10

    cats = Reference(ws, min_col=1, min_row=3, max_row=data_end)
    found  = Reference(ws, min_col=2, min_row=2, max_row=data_end)
    closed = Reference(ws, min_col=3, min_row=2, max_row=data_end)
    bar.add_data(found, titles_from_data=True)
    bar.add_data(closed, titles_from_data=True)
    bar.set_categories(cats)
    ws.add_chart(bar, "J3")

    # ── Line Chart: Quality KPIs over time
    line = LineChart()
    line.title = "Quality KPI Trends (12-Month)"
    line.style = 10
    line.y_axis.title = "Score (%)"
    line.x_axis.title = "Month"
    line.width = 18
    line.height = 10

    fpy  = Reference(ws, min_col=5, min_row=2, max_row=data_end)
    audit = Reference(ws, min_col=6, min_row=2, max_row=data_end)
    sup   = Reference(ws, min_col=7, min_row=2, max_row=data_end)
    line.add_data(fpy,  titles_from_data=True)
    line.add_data(audit, titles_from_data=True)
    line.add_data(sup,  titles_from_data=True)
    line.set_categories(cats)
    ws.add_chart(line, "J20")

def add_dashboard_sheet(wb, kpi_df, defect_df, audit_df, supplier_df):
    ws = wb.create_sheet(title="📊 Executive Dashboard", index=0)
    ws.sheet_view.showGridLines = False

    # Background
    dark_fill  = PatternFill("solid", fgColor="1A1A2E")
    accent_fill = PatternFill("solid", fgColor="1B4F72")
    light_fill  = PatternFill("solid", fgColor="EBF5FB")
    green_fill  = PatternFill("solid", fgColor="1E8449")
    amber_fill  = PatternFill("solid", fgColor="D4AC0D")
    red_fill    = PatternFill("solid", fgColor="C0392B")
    white_fill  = PatternFill("solid", fgColor="FFFFFF")

    # Set column widths
    for col in range(1, 16):
        ws.column_dimensions[get_column_letter(col)].width = 14
    for row in range(1, 40):
        ws.row_dimensions[row].height = 22

    # ── TITLE BANNER
    ws.merge_cells('A1:O2')
    tc = ws['A1']
    tc.value = "🚗  AUTOMOTIVE QUALITY & PROCESS INTELLIGENCE DASHBOARD"
    tc.fill = dark_fill
    tc.font = Font(bold=True, color="FFFFFF", size=16)
    tc.alignment = Alignment(horizontal='center', vertical='center')

    ws.merge_cells('A3:O3')
    sc = ws['A3']
    sc.value = f"Author: Sheelalipi Panda  |  M.Sc. Electromobility, FAU Erlangen-Nürnberg  |  Generated: {datetime.now().strftime('%B %Y')}  |  github.com/pandasheelalipi"
    sc.fill = accent_fill
    sc.font = Font(italic=True, color="FFFFFF", size=9)
    sc.alignment = Alignment(horizontal='center', vertical='center')

    # ── KPI CARDS ROW
    ws.merge_cells('A5:A6')
    ws['A5'].value = "KPI SUMMARY"
    ws['A5'].fill = accent_fill
    ws['A5'].font = Font(bold=True, color="FFFFFF", size=9)
    ws['A5'].alignment = Alignment(horizontal='center', vertical='center')

    kpis = [
        ("Total Defects\n(12 months)", kpi_df['Defects Found'].sum(), "B5"),
        ("Avg First Pass\nYield (%)", f"{kpi_df['First Pass Yield (%)'].mean():.1f}%", "D5"),
        ("Avg Audit\nScore (%)", f"{kpi_df['Process Audit Score (%)'].mean():.1f}%", "F5"),
        ("Avg Supplier\nScore (%)", f"{kpi_df['Supplier Quality Score (%)'].mean():.1f}%", "H5"),
        ("Open Defects\n(Current)", kpi_df['Open Defects'].sum(), "J5"),
        ("Audits\nConducted", len(audit_df), "L5"),
        ("Suppliers\nTracked", len(supplier_df), "N5"),
    ]

    for label, value, cell_ref in kpis:
        col = cell_ref[0]
        row = int(cell_ref[1])
        # label cell
        label_cell = ws[f'{col}{row}']
        ws.merge_cells(f'{col}{row}:{col}{row}')
        label_cell.value = label
        label_cell.fill = light_fill
        label_cell.font = Font(bold=True, color="1A1A2E", size=8)
        label_cell.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
        # value cell
        val_cell = ws[f'{col}{row+2}']
        ws.merge_cells(f'{col}{row+2}:{col}{row+2}')
        val_cell.value = value
        val_cell.fill = accent_fill
        val_cell.font = Font(bold=True, color="FFFFFF", size=14)
        val_cell.alignment = Alignment(horizontal='center', vertical='center')

    # ── DEFECT BY COMPONENT TABLE
    ws.merge_cells('A9:C9')
    ws['A9'].value = "Defects by Component"
    ws['A9'].fill = accent_fill
    ws['A9'].font = Font(bold=True, color="FFFFFF", size=10)
    ws['A9'].alignment = Alignment(horizontal='center', vertical='center')

    comp_summary = defect_df.groupby('Component').size().reset_index(name='Count').sort_values('Count', ascending=False)
    for i, row_data in comp_summary.iterrows():
        r = 10 + list(comp_summary.index).index(i)
        ws.cell(r, 1, row_data['Component']).fill = light_fill if r%2==0 else white_fill
        ws.cell(r, 1).font = Font(size=9, color="1A1A2E")
        ws.cell(r, 2, row_data['Count']).fill = light_fill if r%2==0 else white_fill
        ws.cell(r, 2).font = Font(size=9, bold=True, color="1B4F72")
        ws.cell(r, 2).alignment = Alignment(horizontal='center')

    # ── SEVERITY BREAKDOWN
    ws.merge_cells('E9:G9')
    ws['E9'].value = "Defects by Severity"
    ws['E9'].fill = accent_fill
    ws['E9'].font = Font(bold=True, color="FFFFFF", size=10)
    ws['E9'].alignment = Alignment(horizontal='center', vertical='center')

    sev_summary = defect_df.groupby('Severity').size().reset_index(name='Count')
    sev_colors = {'Critical': 'C0392B', 'Major': 'D4AC0D', 'Minor': '1E8449'}
    for r_i, row_data in sev_summary.iterrows():
        r = 10 + r_i
        color = sev_colors.get(row_data['Severity'], '1B4F72')
        ws.cell(r, 5, row_data['Severity']).fill = PatternFill("solid", fgColor=color)
        ws.cell(r, 5).font = Font(size=9, bold=True, color="FFFFFF")
        ws.cell(r, 5).alignment = Alignment(horizontal='center')
        ws.cell(r, 6, row_data['Count']).fill = light_fill
        ws.cell(r, 6).font = Font(size=9, bold=True, color="1A1A2E")
        ws.cell(r, 6).alignment = Alignment(horizontal='center')

    # ── SUPPLIER RATINGS
    ws.merge_cells('I9:K9')
    ws['I9'].value = "Supplier Ratings"
    ws['I9'].fill = accent_fill
    ws['I9'].font = Font(bold=True, color="FFFFFF", size=10)
    ws['I9'].alignment = Alignment(horizontal='center', vertical='center')

    rating_colors = {'A': '1E8449', 'B': 'D4AC0D', 'C': 'C0392B'}
    for r_i, row_data in supplier_df.iterrows():
        r = 10 + r_i
        ws.cell(r, 9, row_data['Supplier']).fill = light_fill if r%2==0 else white_fill
        ws.cell(r, 9).font = Font(size=9, color="1A1A2E")
        ws.cell(r, 10, f"{row_data['Overall Score (%)']:.1f}%").fill = light_fill if r%2==0 else white_fill
        ws.cell(r, 10).font = Font(size=9, bold=True, color="1B4F72")
        ws.cell(r, 10).alignment = Alignment(horizontal='center')
        color = rating_colors.get(row_data['Rating'], '1B4F72')
        ws.cell(r, 11, row_data['Rating']).fill = PatternFill("solid", fgColor=color)
        ws.cell(r, 11).font = Font(size=9, bold=True, color="FFFFFF")
        ws.cell(r, 11).alignment = Alignment(horizontal='center')

    # ── PROJECT DESCRIPTION BOX
    ws.merge_cells('A22:O24')
    desc = ws['A22']
    desc.value = (
        "PROJECT: This dashboard simulates automotive quality management operations relevant to OEM production environments (BMW, Mercedes-Benz, Audi). "
        "It covers defect tracking, process audit scoring, supplier quality scorecards, corrosion risk assessment, and monthly KPI trend analysis. "
        "Built independently using Python (pandas, openpyxl) to demonstrate data analysis, structured reporting, and quality management capabilities."
    )
    desc.fill = light_fill
    desc.font = Font(italic=True, size=8, color="1A1A2E")
    desc.alignment = Alignment(horizontal='left', vertical='center', wrap_text=True)

def build_excel(output_path):
    # Generate data
    defect_df   = make_defect_log()
    kpi_df      = make_kpi_summary()
    audit_df    = make_audit_log()
    supplier_df = make_supplier_scorecard()
    corrosion_df = make_corrosion_register()

    wb = openpyxl.Workbook()
    wb.remove(wb.active)

    # Dashboard first
    add_dashboard_sheet(wb, kpi_df, defect_df, audit_df, supplier_df)

    # Data sheets
    write_sheet(wb, "Monthly KPI Summary",    kpi_df,       color="1B4F72")
    write_sheet(wb, "Defect Log",             defect_df,    color="2E4057")
    write_sheet(wb, "Process Audit Log",      audit_df,     color="1A5276")
    write_sheet(wb, "Supplier Scorecard",     supplier_df,  color="117A65")
    write_sheet(wb, "Corrosion Risk Register", corrosion_df, color="6E2F26")

    # Charts on KPI sheet
    add_kpi_charts(wb, kpi_df)

    wb.save(output_path)
    print(f"✅ Excel report saved to: {output_path}")
    return defect_df, kpi_df, audit_df, supplier_df, corrosion_df

if __name__ == '__main__':
    os.makedirs(os.path.join(os.path.dirname(__file__), '..', 'reports'), exist_ok=True)
    build_excel(OUTPUT_PATH)
