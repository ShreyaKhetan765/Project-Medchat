import sqlite3
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionIdentifyDisease(Action):
    def name(self) -> Text:
        return "action_identify_disease"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        symptoms = tracker.latest_message.get('text')
        disease = self.get_disease(symptoms)

        if disease:
            dispatcher.utter_message(template="utter_disease", disease=disease)
        else:
            dispatcher.utter_message(template="utter_unknown_symptoms")

        return []

    def get_disease(self, symptoms):
        connection = sqlite3.connect("Symptom2Diseas.db")  # Update this with your SQLite database file name
        cursor = connection.cursor()

        query = "SELECT label FROM symptoms WHERE text = ?"
        cursor.execute(query, (symptoms,))
        result = cursor.fetchone()

        connection.close()

        return result[0] if result else None
