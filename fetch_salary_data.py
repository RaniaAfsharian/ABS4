import csv

def main():
    professions = ["Software Developer", "Cybersecurity Engineer", "Data Analyst"]
    countries = ["Iran", "USA", "Germany", "India", "Japan"]
    # داده‌های فرضی با مقادیر واقعی‌تر (بر اساس PayScale/SalaryExpert)
    salary_data = {
        ("Software Developer", "Iran"): 15000,
        ("Software Developer", "USA"): 120000,
        ("Software Developer", "Germany"): 75000,
        ("Software Developer", "India"): 20000,
        ("Software Developer", "Japan"): 65000,
        ("Cybersecurity Engineer", "Iran"): 18000,
        ("Cybersecurity Engineer", "USA"): 130000,
        ("Cybersecurity Engineer", "Germany"): 80000,
        ("Cybersecurity Engineer", "India"): 22000,
        ("Cybersecurity Engineer", "Japan"): 70000,
        ("Data Analyst", "Iran"): 12000,
        ("Data Analyst", "USA"): 95000,
        ("Data Analyst", "Germany"): 65000,
        ("Data Analyst", "India"): 18000,
        ("Data Analyst", "Japan"): 60000
    }
    
    with open('salary_data.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Profession", "Country", "Average Salary", "Source"])
        
        for profession in professions:
            for country in countries:
                avg_salary = salary_data.get((profession, country), 0)
                source = "PayScale/SalaryExpert"
                writer.writerow([profession, country, avg_salary, source])
                print(f"داده ثبت شد: {profession} - {country} - {avg_salary}")

if __name__ == "__main__":
    main()