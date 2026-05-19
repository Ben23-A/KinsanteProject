import sys
import heapq
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem

# Importation of the converted Graphical User Interface
from interface import Ui_MainWindow

class Patient:
    def __init__(self, name, patient_id, priority, condition):
        self.name = name
        self.patient_id = patient_id
        # Inversion to create Max-Heap behavior (priority 5 handled first)
        self.priority = -int(priority)
        self.condition = condition

    # Operator overloading for the heapq sorting algorithm
    def __lt__(self, other):
        return self.priority < other.priority

class HospitalApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Main Core Data Structure (Heap Queue)
        self.patient_queue = []

        # Control Flow Initialization onto the Main Menu (Page Index 0)
        self.ui.stackedWidget.setCurrentIndex(0)

        # Main Menu button interactions mapping
        self.ui.btn_go_to_register.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.btn_go_to_queue.clicked.connect(self.display_queue_page)
        self.ui.btn_treat_next.clicked.connect(self.treat_patient)
        self.ui.btn_exit.clicked.connect(self.close)

        # Mandatory "Back" navigation system to prevent infinite processing loops
        self.ui.btn_back_from_reg.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.btn_back_from_queue.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))

        # Core Patient Registration submission trigger
        self.ui.btn_save_patient.clicked.connect(self.save_patient)

    def save_patient(self):
        name = self.ui.input_name.text().strip()
        patient_id = self.ui.input_id.text().strip()
        condition = self.ui.input_condition.text().strip()
        priority_val = self.ui.combo_priority.currentIndex() + 1

        if not name or not patient_id:
            QMessageBox.warning(self, "Input Error", "All primary fields are mandatory!")
            return

        # Backend Data Structure Manipulation: Push operation into the Heap array
        new_patient = Patient(name, patient_id, priority_val, condition)
        heapq.heappush(self.patient_queue, new_patient)

        QMessageBox.information(self, "Success", f"Patient {name} successfully sorted into triage.")

        # Clear field parameters and redirect the navigation safely back to the Main Menu
        self.ui.input_name.clear()
        self.ui.input_id.clear()
        self.ui.input_condition.clear()
        self.ui.stackedWidget.setCurrentIndex(0)

    def display_queue_page(self):
        self.ui.table_queue.setRowCount(0)
        sorted_patients = sorted(self.patient_queue)

        # Dynamic mapping and parsing of the backend structure into the visual QTableWidget component
        for row, patient in enumerate(sorted_patients):
            self.ui.table_queue.insertRow(row)
            self.ui.table_queue.setItem(row, 0, QTableWidgetItem(str(-patient.priority)))
            self.ui.table_queue.setItem(row, 1, QTableWidgetItem(patient.patient_id))
            self.ui.table_queue.setItem(row, 2, QTableWidgetItem(patient.name))
            self.ui.table_queue.setItem(row, 3, QTableWidgetItem(patient.condition))

        self.ui.stackedWidget.setCurrentIndex(2)

    def treat_patient(self):
        if not self.patient_queue:
            QMessageBox.information(self, "Queue Empty", "No patients currently waiting in triage.")
            return

        # Backend Data Structure Manipulation: Pop operation extracting the highest priority patient
        next_patient = heapq.heappop(self.patient_queue)
        QMessageBox.information(
            self,
            "Next Patient Called",
            f"Proceeding to Treatment:\n\nName: {next_patient.name}\nPriority Level: {-next_patient.priority}"
        )

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HospitalApp()
    window.show()
    sys.exit(app.exec())