import sys 
 
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QLineEdit, QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout 
 
class PatientForm(QWidget): 
    def __init__(self): 
        super().__init__() 
 
        # Врачи 
        self.doctors = { 
            'Иванов Иван Иванович': {'специализация': 'терапевт', 'расписание': 'пн-ср 9:00-13:00'}, 
            'Петров Петр Петрович': {'специализация': 'хирург', 'расписание': 'вт-чт 14:00-18:00'}, 
            'Сидорова Елена Викторовна': {'специализация': 'гинеколог', 'расписание': 'пн-пт 10:00-15:00'}, 
        } 
 
        # Заголовок формы 
        self.title = QLabel('Форма учета пациентов в больнице') 
 
        # ФИО пациента 
        self.name_label = QLabel('ФИО пациента:') 
        self.name_input = QLineEdit() 
 
        # Пол пациента 
        self.gender_label = QLabel('Пол:') 
        self.gender_input = QComboBox() 
        self.gender_input.addItem('Мужской') 
        self.gender_input.addItem('Женский') 
 
        # Возраст пациента 
        self.age_label = QLabel('Возраст:') 
        self.age_input = QLineEdit() 
 
        # Выбор врача 
        self.doctor_label = QLabel('Выберите врача:') 
        self.doctor_input = QComboBox() 
        for specialization in self.doctor_specializations(): 
            self.doctor_input.addItem(specialization) 
 
        # Расписание врача 
        self.schedule_label = QLabel('Расписание приема:') 
        self.schedule_text = QLabel() 
 
        # Кнопка добавления пациента 
        self.add_button = QPushButton('Добавить пациента') 
        self.add_button.clicked.connect(self.save_patient_data)  # связываем кнопку с функцией сохранения данных 
 
        # Отображение выбранной специализации и расписания врача 
        self.doctor_input.currentIndexChanged.connect(self.show_doctor_info) 
 
        # Расположение элементов на форме 
        form_layout = QVBoxLayout() 
        form_layout.addWidget(self.title) 
        form_layout.addWidget(self.name_label) 
        form_layout.addWidget(self.name_input) 
        form_layout.addWidget(self.gender_label) 
        form_layout.addWidget(self.gender_input) 
        form_layout.addWidget(self.age_label)
        form_layout.addWidget(self.age_input) 
        form_layout.addWidget(self.doctor_label) 
        form_layout.addWidget(self.doctor_input) 
        form_layout.addWidget(self.schedule_label) 
        form_layout.addWidget(self.schedule_text) 
        form_layout.addWidget(self.add_button) 
 
        # Расположение формы на окне 
        main_layout = QHBoxLayout() 
        main_layout.addLayout(form_layout) 
        self.setLayout(main_layout) 
        self.setWindowTitle('Учет пациентов в больнице') 
 
    def doctor_specializations(self): 
        return list(set([doc['специализация'] for doc in self.doctors.values()])) 

    def show_doctor_info(self): 
        specialization = self.doctor_input.currentText() 
        for doctor, info in self.doctors.items(): 
            if info['специализация'] == specialization: 
                self.schedule_text.setText(info['расписание']) 
                break 
 
    def save_patient_data(self): 
        name = self.name_input.text() 
        gender = self.gender_input.currentText() 
        age = self.age_input.text() 
        doctor = self.doctor_input.currentText() 
        with open('lol.txt', 'w') as f: 
            f.write(f'{name}, {gender}, {age}, {doctor}\n') 
        self.name_input.clear() 
        self.age_input.clear() 
 
app = QApplication(sys.argv) 
ex = PatientForm() 
ex.show() 
sys.exit(app.exec_())