import joblib
import json
import pandas as pd
import numpy as np
from statistics import mode
from tkinter import *
from fuzzywuzzy import fuzz
import time
import random
import warnings
from sklearn.exceptions import DataConversionWarning

# Disable the warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=DataConversionWarning)
warnings.filterwarnings("ignore", category=UserWarning)

df = pd.read_csv('training.csv')
# Replace underscores with spaces in column names
df.columns = df.columns.str.replace('_', ' ')
symptoms_list = df.columns

'''
for symptom in symptoms_list:
    print(symptom)
    
'''

# Load the machine learning models and data dictionary
loaded_svm_model = joblib.load('final_svm_model.pkl')
loaded_nb_model = joblib.load('final_nb_model.pkl')
loaded_rf_model = joblib.load('final_rf_model.pkl')
data_dict = joblib.load('data_dict.pkl')

with open('disease_info.json', 'r') as file:
    disease_data = json.load(file)
    
with open('intents.json', 'r') as file:
    intents = json.load(file)
    
def get_response(user_input):
    user_input = user_input.lower()

    # Initialize an empty list to store responses
    matched_responses = []

    # Check if the user input matches any intent in the intents.json file
    for intent, data in intents.items():
        for phrase in data['phrases']:
            if phrase.lower() in user_input:
                matched_responses.extend(data['responses'])

    # If no intent is found, return a default response
    if not matched_responses:
        return ["I'm sorry, I don't understand your question."]

    # Return a random response from the matched responses
    return [random.choice(matched_responses)]


def get_disease_info(disease_name):
    best_match = None
    best_score = 0

    for known_disease_name in disease_data.keys():
        similarity_score = fuzz.ratio(disease_name.lower(), known_disease_name.lower())
        if similarity_score > best_score:
            best_score = similarity_score
            best_match = known_disease_name
    if best_score >= 70: 
        return disease_data[best_match]
    else:
        return "Disease not found in the database."


def predictDisease(input_symptoms):
    input_symptoms = input_symptoms.lower()
    symptoms = input_symptoms.split(",")

    input_data = [0] * len(data_dict["symptom_index"])
    for symptom in symptoms:
        symptom = symptom.strip() 
        if symptom in data_dict["symptom_index"]:
            index = data_dict["symptom_index"][symptom]
            input_data[index] = 1
        else:
            return "Symptom '{}' not in the database.".format(symptom)

    if sum(input_data) == 0:
        return "None of the input symptoms are in the database."

    input_data = np.array(input_data).reshape(1, -1)

    rf_prediction = data_dict["predictions_classes"][loaded_rf_model.predict(input_data)[0]]
    nb_prediction = data_dict["predictions_classes"][loaded_nb_model.predict(input_data)[0]]
    svm_prediction = data_dict["predictions_classes"][loaded_svm_model.predict(input_data)[0]]

    final_prediction = mode([rf_prediction, nb_prediction, svm_prediction])

    if final_prediction not in data_dict["predictions_classes"]:
        return "Disease '{}' is not in the database.".format(final_prediction)

    pre = "You may be suffering from " + final_prediction + "\n"
    disease_info = get_disease_info(final_prediction)

    if isinstance(disease_info, dict):
        for key, value in disease_info.items():
            if isinstance(value, list):
                pre += key + ":\n"
                for item in value:
                    pre += "- " + item + "\n"
            else:
                pre += key + ": " + value + "\n"

    pre += "\n If you are still unsure about the prediction, please contact a medical professional for better advice."
    time.sleep(1)
    return pre


def process_user_input(user_input):
    user_input = user_input.lower()
    input_symptoms = [symptom.strip() for symptom in user_input.split(',')]

    # Check if user input is in the symptoms list
    valid_symptoms = [symptom for symptom in input_symptoms if symptom in symptoms_list]

    if valid_symptoms:
        prediction = predictDisease(','.join(valid_symptoms))
    else:
        # If the user input is not in the symptoms list, use the get_response function
        response = get_response(user_input)
        return response[0]  # Return the first response without brackets

    return "Disease Prediction: " + prediction  # Return the first prediction without brackets

'''
user_input = ("high fever, dizziness, vomiting")  
response = process_user_input(user_input)
print(response)
'''

from tkinter import *
BG_GRAY = "white"
BG_COLOR = "white"
TEXT_COLOR = "black"
bot_name = "Meddy"

FONT = "Poppins 14"
FONT_BOLD = "Helvetica 13 bold"
wel = "Welcome to Meddy Disease Predictor ! \n\n"

class ChatApplication:

    def __init__(self):
        self.window = Tk()
        self._setup_main_window()

    def run(self):
        self.window.mainloop()

    def _setup_main_window(self):
        self.window.title("Meddy")
        self.window.resizable(width=True, height=True)
        self.window.configure(width=470, height=550, bg=BG_COLOR)

        # head label
        head_label = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR,
                           text="Meddy Disease Predictor", font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)

        # tiny divider
        line = Label(self.window, width=450, bg=BG_GRAY)
        line.place(relwidth=1, rely=0.07, relheight=0.012)

        # text widget
        self.text_widget = Text(self.window, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR,
                                font=FONT, padx=5, pady=5)
        self.text_widget.place(relheight=0.745, relwidth=0.954, rely=0.08)
        self.text_widget.insert(END, wel)

        # scroll bar
        scrollbar = Scrollbar(self.window)
        scrollbar.place(relheight=0.745, relx=0.964, rely=0.08)
        self.text_widget.configure(yscrollcommand=scrollbar.set)
        scrollbar.configure(command=self.text_widget.yview)

        self.text_widget.configure(cursor="arrow", state=DISABLED)

        # bottom label
        bottom_label = Label(self.window, bg=BG_GRAY, height=80)
        bottom_label.place(relwidth=1, rely=0.825)

        # message entry box
        self.msg_entry = Entry(bottom_label, bg="white", fg=TEXT_COLOR, font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

        # send button
        send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=20, bg=BG_GRAY,
                             command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)

    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "You")

    def _insert_message(self, msg, sender):
        if not msg:
            return

        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)
        print(msg)
        msg2 = f"{bot_name}: {process_user_input(msg)}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)

        self.text_widget.see(END)


if __name__ == "__main__":
    app = ChatApplication()
    app.run()
    
