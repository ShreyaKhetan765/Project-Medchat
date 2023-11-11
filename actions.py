from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionDetermineMeaslesStage(Action):
    def name(self) -> Text:
        return "action_determine_measles_stage"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        symptoms = tracker.latest_message.get('text')
        eruptive_symptoms = ['High fever', 'Cough', 'Conjunctivitis', 'Sore throat', 'Photophobia', 'Enlarged lymph nodes', 'Body aches', 'Red eyes', 'Sensitivity to light', 'Rash spreading to extremities', 'Itchy skin']

        # Check if all eruptive symptoms are present in the user's input
        if all(symptom.lower() in symptoms.lower() for symptom in eruptive_symptoms):
            # User has symptoms indicative of the Eruptive stage
            dispatcher.utter_message("It seems based on your symptoms that you may be in the Eruptive stage of measles. During this stage, the characteristic measles rash appears, starting from the face and spreading to the extremities. It's important to consult with a healthcare professional for a proper diagnosis and guidance.")
        else:
            # User's symptoms do not match the criteria for the Eruptive stage
            dispatcher.utter_message("I'm sorry, I couldn't determine the stage based on the provided symptoms. Please consult with a healthcare professional for a proper diagnosis.")

        return []
