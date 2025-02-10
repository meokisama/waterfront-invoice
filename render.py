import os
import pandas as pd
import pdfkit
from jinja2 import Environment, FileSystemLoader
import glob

wkhtmltopdf_path = os.path.join(os.path.dirname(__file__), "wkhtmltox", "bin", "wkhtmltopdf.exe")
pdfkit_config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)

input_dir = "data"
output_dir = "output"

os.makedirs(output_dir, exist_ok=True)

csv_files = glob.glob(os.path.join(input_dir, "*.csv"))

if not csv_files:
    print("✕ Không tìm thấy file CSV nào trong thư mục data/")
    exit()

latest_csv = max(csv_files, key=lambda x: os.path.basename(x))
latest_filename = os.path.basename(latest_csv).replace(".csv", "")

print(f"✓ Đang xử lý file: {latest_csv}")

df = pd.read_csv(latest_csv)
df["Value"] = pd.to_numeric(df["Value"], errors="coerce")
df = df.dropna(subset=["Value"])
df["Time stamp"] = pd.to_datetime(df["Time stamp"], format="%m/%d/%Y %I:%M:%S %p", errors="coerce")
df = df.dropna(subset=["Time stamp"])
df = df.sort_values(by="Time stamp", ascending=True)

start_of_month_reading = df.iloc[0]["Value"]
current_reading = df.iloc[-1]["Value"]

# Tính tiền điện
price_per_unit = 3000
total_price = (current_reading - start_of_month_reading) * price_per_unit

env = Environment(loader=FileSystemLoader("."))
template = env.get_template("invoice_template.html")
html_output = template.render(
    invoice_id=latest_filename,
    customer="Nguyễn Văn A",
    address="Hà Nội",
    previous_reading=start_of_month_reading,
    current_reading=current_reading,
    price_per_unit=price_per_unit,
    total_price=total_price
)

html_file = os.path.join(output_dir, f"{latest_filename}.html")
pdf_file = os.path.join(output_dir, f"{latest_filename}.pdf")

with open(html_file, "w", encoding="utf-8") as f:
    f.write(html_output)

pdfkit.from_file(html_file, pdf_file, configuration=pdfkit_config)

print(f"✓ Hóa đơn đã được tạo: {pdf_file}")
