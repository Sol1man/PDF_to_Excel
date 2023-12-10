import PyPDF2
import pandas as pd

# Load the existing Excel file
excel_file_path = "all_data.xlsx"
existing_data = pd.read_excel(excel_file_path)
data = {

}

print("-------------PDF to EXCEL CONVERTER---------------")
machine_list = ["WEIGHT", "SCRAB", "MACHIN ING TIME"]
with open('data.pdf', 'rb') as pdf_file:
    reader = PyPDF2.PdfReader(pdf_file)
    page = reader.pages[0]
    text = page.extract_text()
    lines = text.split('\n')
    print("-------LIST LINES------")
    for line in lines:
        # if "SCRAP" in line:
        #     print(line)
        for item in machine_list:
            if item in line:
                data[item] = line.replace(item,'')
print(data)


if data:
    # Check if the data dictionary is not empty before creating a DataFrame
    merged_data = pd.concat([existing_data, pd.DataFrame([data])], ignore_index=True, sort=False)
    existing_data = merged_data.reset_index(drop=True)  # Resetting index to ensure proper update
    existing_data.to_excel(excel_file_path, index=False)
    print(existing_data)
    print("Data imported successfully")
else:
    print("No data to update.")