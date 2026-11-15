import csv
from datetime import datetime

INPUT_FILE = "data/sales.csv"
CLEANED_FILE = "data/cleaned.csv"
LOG_FILE = "data/run_log.txt"

# ---------------------------------------------------------
# EXERCISE 2: Read and print raw rows
# ---------------------------------------------------------
print("--- Exercise 2: Raw Rows ---")
with open(INPUT_FILE, mode="r", newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# ---------------------------------------------------------
# EXERCISE 3: Skip the header
# ---------------------------------------------------------
print("\n--- Exercise 3: Skip Header ---")
with open(INPUT_FILE, mode="r", newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)
    print("Header:", header)
    for row in reader:
        print(row)

# ---------------------------------------------------------
# EXERCISE 4: Compute totals
# ---------------------------------------------------------
print("\n--- Exercise 4: Compute Totals ---")
overall_revenue = 0.0

with open(INPUT_FILE, mode="r", newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)  # Skip header
    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])
        line_total = price * quantity
        overall_revenue += line_total
        print(f"{product}: {quantity} units × ${price:.2f} = ${line_total:.2f}")

print(f"Overall Total Revenue: ${overall_revenue:.2f}")

# ---------------------------------------------------------
# EXERCISE 5: Filter and write cleaned.csv
# ---------------------------------------------------------
print("\n--- Exercise 5: Filter and Write ---")
total_rows = 0
written_rows = 0

with open(INPUT_FILE, mode="r", newline="", encoding="utf-8") as infile, \
     open(CLEANED_FILE, mode="w", newline="", encoding="utf-8") as outfile:
    
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    next(reader)  # Skip original header
    writer.writerow(["Product", "Price", "Qty", "Total"])
    
    for row in reader:
        total_rows += 1
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])
        line_total = price * quantity
        
        if line_total > 100:
            writer.writerow([product, f"{price:.2f}", quantity, f"{line_total:.2f}"])
            written_rows += 1

print(f"Wrote {written_rows} qualifying rows out of {total_rows} original rows.")

# ---------------------------------------------------------
# EXERCISE 6: csv.DictReader
# ---------------------------------------------------------
print("\n--- Exercise 6: DictReader ---")
dict_overall_revenue = 0.0

with open(INPUT_FILE, mode="r", newline="", encoding="utf-8") as f:
    dict_reader = csv.DictReader(f)
    for row in dict_reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])
        line_total = price * quantity
        dict_overall_revenue += line_total
        print(f"{product}: {quantity} units × ${price:.2f} = ${line_total:.2f}")

print(f"DictReader Total Revenue: ${dict_overall_revenue:.2f}")

# Comparison: csv.reader is slightly faster and works well for simple CSVs with fixed column positions,
# while csv.DictReader is more readable and resilient if column order changes in the source file.

# ---------------------------------------------------------
# EXERCISE 7: Sales summary by product
# ---------------------------------------------------------
print("\n--- Exercise 7: Summary by Product ---")
product_summary = {}

with open(INPUT_FILE, mode="r", newline="", encoding="utf-8") as f:
    dict_reader = csv.DictReader(f)
    for row in dict_reader:
        product = row["product"]
        revenue = float(row["price"]) * int(row["quantity"])
        product_summary[product] = product_summary.get(product, 0.0) + revenue

for product in sorted(product_summary):
    print(f"{product}: ${product_summary[product]:.2f}")

# ---------------------------------------------------------
# EXERCISE 8: Append mode log
# ---------------------------------------------------------
print("\n--- Exercise 8: Append Log ---")
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open(LOG_FILE, mode="a", encoding="utf-8") as log_f:
    log_f.write(f"[{timestamp}] Total Revenue: ${overall_revenue:.2f}\n")

print(f"Logged run to {LOG_FILE}")


# Reflection
# 1. Python automates repetitive cleaning and scales easily to millions of rows without crashing or manual clicking whereas Excel is better for quick visual inspections, ad hoc, formulas, and interactive charts.
# 2. For example, a point of scale check out system or user login. Audit trail benefits from append mode because every transaction or access event is preserved chronologically without overwriting historical records.