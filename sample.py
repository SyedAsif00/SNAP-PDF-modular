# sample.py

# This is a sample data dictionary that contains the form field values to be filled in the PDF.
# The keys correspond to the form field names, and the values are what we want to set for those fields.

sample_data = {
    "Name": {
        "value": "Muhammad Wasil",
        "type": "Text Field"
    },
    "Phone Number": {
        "value": "0198989898989889",
        "type": "Text Field"
    },
    "Are you homeless": {
        "value": "No",
        "type": "Yes/No"
    },
    "If you do not want DTA to text you, please check this box": {
        "value": True,
        "type": "Single Checkbox"
    },  
    "Disability": {
        "value": ["Physical", "Intellectual/Cognitive"],
        "type": "Multiple Options"
    },
    "Impairment Types": {
        "value": ["Hearing", "Visual"],
        "type": "Multiple Options"
    },
     "Impairment Other": {
        "value": "other is here", 
        "type": "Text Field"
    },
     "Communication Methods": {
        "value": ["InPerson"],
        "type": "Multiple Options"
    },
     "VRS Phone Number": {
        "value": "21212154545",
        "type": "Text Field"
    },
     "Has Massachusetts certified that you have a disability?": {
        "value": "Yes",
        "type": "Yes/No"
    },
    "Social Security Number": {
        "value": "123-45-6789",
        "type": "Text Field"
    },
    "Date of Birth": {
        "value": "01/01/1990",
        "type": "Text Field"
    },
    "Gender": {
        "value": "Female",  # Can be Male/Female, one at a time
        "type": "Gender"
    },
    "Are you pregnant?": {
        "value": "Yes",  # Can be Yes/No
        "type": "Yes/No"
    },
    "Are you a U.S. citizen": {
        "value": "Yes",  # Can be Yes/No
        "type": "Yes/No"
    },
    "Language preference" : {
        "value" : "english",
        "type":"Text Field"
    },
    "Ethnicity": {
        "value": "HispanicOrLatino",  
        "type": "Single Select"
    },
    "Race": {
        "value": "White",  
        "type": "Single Select"
    },
    "Do other poeple live with you" : {
        "value" : "Yes",
        "type" : "Yes/No"
    }
}
