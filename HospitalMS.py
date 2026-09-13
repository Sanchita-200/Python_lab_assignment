import os
import json
from datetime import datetime

# =====================================================================
# 1. PATIENT REGISTRATION 
# =====================================================================
patients_db = {}

def register_patient(patient_id, name, age, gender):
    patients_db[patient_id] = {
        "name": name,
        "age": age,
        "gender": gender,
        "registration_date": datetime.now().strftime("%Y-%m-%d")
    }
    print(f"[Success] Patient {name} registered with ID: {patient_id}")

# =====================================================================
# 2. APPOINTMENT SCHEDULING 
# =====================================================================
appointments_list = []

def schedule_appointment(patient_id, doctor_name, date, time):
    if patient_id not in patients_db:
        print(f"[Error] Patient ID {patient_id} not found. Please register first.")
        return
    
    appointment = {
        "patient_id": patient_id,
        "patient_name": patients_db[patient_id]["name"],
        "doctor": doctor_name,
        "date": date,
        "time": time
    }
    appointments_list.append(appointment)
    print(f"[Success] Appointment scheduled with {doctor_name} for Patient {patient_id}")

# =====================================================================
# 3. DOCTOR INFORMATION
# =====================================================================

doctors_registry = (
    ("D101", "Dr. Alex", "Cardiology"),
    ("D102", "Dr. Bhanu", "Neurology"),
    ("D103", "Dr. Chloe", "Pediatrics")
)

def display_doctors():
    print("\n--- Available Doctors ---")
    for doc_id, name, specialty in doctors_registry:
        print(f"ID: {doc_id} | Name: {name} | Specialty: {specialty}")

# =====================================================================
# 4. MEDICAL RECORDS STORAGE (Using File Handling)
# =====================================================================
RECORDS_FILE = "medical_records.txt"

def save_medical_record(patient_id, diagnosis, prescription):
    if patient_id not in patients_db:
        print(f"[Error] Patient ID {patient_id} not found.")
        return
        
    record_entry = f"ID: {patient_id} | Diagnosis: {diagnosis} | Prescription: {prescription} | Date: {datetime.now().strftime('%Y-%m-%d')}\n"
    with open(RECORDS_FILE, "a") as file:
        file.write(record_entry)
    print(f"[Success] Medical record saved to {RECORDS_FILE}")

def view_medical_records():
    print("\n--- Medical Records Archive ---")
    if not os.path.exists(RECORDS_FILE):
        print("No medical records found.")
        return
    with open(RECORDS_FILE, "r") as file:
        print(file.read())

# =====================================================================
# 5. BILLING SYSTEM 
# =====================================================================
class Invoice:
    tax_rate = 0.05  
    def __init__(self, invoice_id, patient_id, consultation_fee, room_charges=0):
        self.invoice_id = invoice_id
        self.patient_id = patient_id
        self.consultation_fee = consultation_fee
        self.room_charges = room_charges

    def calculate_total(self):
        subtotal = self.consultation_fee + self.room_charges
        tax = subtotal * self.tax_rate
        return subtotal + tax

    def generate_bill_invoice(self):
        p_name = patients_db.get(self.patient_id, {}).get("name", "Unknown Patient")
        total = self.calculate_total()
        
        print("\n====================================")
        print(f"       INVOICE: {self.invoice_id}        ")
        print("====================================")
        print(f"Patient ID : {self.patient_id}")
        print(f"Patient Name: {p_name}")
        print(f"Consultation: INR {self.consultation_fee}")
        print(f"Room Charges: INR {self.room_charges}")
        print(f"Tax (5%)    : INR { (self.consultation_fee + self.room_charges) * self.tax_rate }")
        print("------------------------------------")
        print(f"TOTAL DUE   : INR {total:.2f}")
        print("====================================\n")

# =====================================================================
# 6. REPORT GENERATION
# =====================================================================
def generate_summary_report():
    report_data = {
        "report_generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "total_registered_patients": len(patients_db),
        "active_appointments_count": len(appointments_list),
        "registered_patients_list": patients_db,
        "scheduled_appointments": appointments_list
    }
    return json.dumps(report_data, indent=4)


# =====================================================================
# --- SIMULATION RUN ---
# =====================================================================
if __name__ == "__main__":
    print("--- Hospital Management System ---\n")
    
    if os.path.exists(RECORDS_FILE):
        os.remove(RECORDS_FILE)

    # 1. Patient Registration (Dict)
    register_patient("P001", "Rahul Sharma", 34, "Male")
    register_patient("P002", "Priya Patil", 29, "Female")
    
    # 2. Doctor Information 
    display_doctors()
    
    # 3. Appointment Scheduling 
    schedule_appointment("P001", "Dr. Alex", "2026-09-05", "10:30 AM")
    schedule_appointment("P002", "Dr. Chloe", "2026-09-06", "02:15 PM")
    
    # 4. Medical Records Storage 
    save_medical_record("P001", "Chronic Hypertension", "Alcohol as needed")
    save_medical_record("P002", "Mild Seasonal Allergy", "Cetirizine 10mg as needed")
    view_medical_records()
    
    # 5. Billing System 
    invoice1 = Invoice(invoice_id="INV-2026-001", patient_id="P001", consultation_fee=800, room_charges=1500)
    invoice1.generate_bill_invoice()
    
    # 6. Report Generation 
    print("--- Generating System Summary JSON Report ---")
    summary = generate_summary_report()
    print(summary)
