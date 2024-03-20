# helper.py

# This dictionary maps the keys from sample_data to the field IDs and types used in the PDF form.
key_to_field_info = {
    "Name": {"field_id": "First Name", "type": "Text Field"},
    "Phone Number": {"field_id": "Phone Number", "type": "Text Field"},
    "Are you homeless": {"field_id_prefix": "Are you homeless_", "type": "Yes/No"},
    "If you do not want DTA to text you, please check this box": {"field_id": "If you do not want DTA to text you, please check this box", "type": "Single Checkbox"},
    "Disability": {"field_id_prefix": "Are you a person with a disability?_", "type": "Multiple Options"},
    "Impairment Types": {"field_id_prefix": "If yes, please check off your impairment type(s)_", "type": "Multiple Options"},
    "Impairment Other": {"field_id": "Other:", "type": "Text Field"},  # Add a new entry for the Other text field
    "Communication Methods":{"field_id_prefix":"What is your preferred method of communication?_", "type" : "Multiple Options"},
    "VRS Phone Number": {"field_id": "VRS Phone Number", "type": "Text Field"},  # Add a new entry for the Other text field
    "Has Massachusetts certified that you have a disability?": {"field_id_prefix": "Has Massachusetts certified that you have a disability?_", "type": "Yes/No"},
    "Social Security Number": {"field_id": "Social Security Number", "type": "Text Field"},
    "Date of Birth": {"field_id": "Date of Birth", "type": "Text Field"},
    "Gender": {"field_id_prefix": "Gender_", "type": "Gender"},
    "Are you pregnant?": {"field_id_prefix": "Are you pregnant?_", "type": "Yes/No"},
    "Are you a U.S. citizen": {"field_id_prefix": "Are you a U.S. Citizen?_", "type": "Yes/No"},
    "Language preference": {"field_id": "What language do you prefer to speak", "type": "Text Field"},
     "Ethnicity": {
        "field_id_prefix": "Ethnicity_",
        "type": "Single Select",
        "options": ["HispanicOrLatino", "NotHispanicOrLatino"]
    },
     "Race": {
        "field_id_prefix": "Race_",
        "type": "Single Select",
        "options": ["Black or African American", "American Indian or Alaska Native", "White","Asian","Native Hawaiian or Other Pacific Islander"]
    },
        "Do other poeple live with you": {"field_id_prefix": "Do you live with other people?_", "type": "Yes/No"},

}

# This function takes the sample_data and uses key_to_field_info to create a mapped_data dictionary.
# helper.py
def map_fields(json_data):
    mapped_data = {}
    for key, values in json_data.items():
        field_info = key_to_field_info.get(key)
        if not field_info:
            continue

        # Handle text fields
        if field_info["type"] == "Text Field":
            mapped_data[field_info["field_id"]] = {"value": values["value"], "type": "Text Field"}

        # Handle Yes/No fields
        elif field_info["type"] == "Yes/No":
            yes_field_id = f"{field_info['field_id_prefix']}Yes"
            no_field_id = f"{field_info['field_id_prefix']}No"
            if values["value"] == "Yes":
                mapped_data[yes_field_id] = {"value": "check", "type": "Checkbox"}
                mapped_data[no_field_id] = {"value": "", "type": "Checkbox"}
            elif values["value"] == "No":
                mapped_data[no_field_id] = {"value": "check", "type": "Checkbox"}
                mapped_data[yes_field_id] = {"value": "", "type": "Checkbox"}

        # Handle Gender fields
        elif field_info["type"] == "Gender":
            male_field_id = f"{field_info['field_id_prefix']}Male"
            female_field_id = f"{field_info['field_id_prefix']}Female"
            if values["value"] == "Male":
                mapped_data[male_field_id] = {"value": "check", "type": "Checkbox"}
                mapped_data[female_field_id] = {"value": "", "type": "Checkbox"}
            elif values["value"] == "Female":
                mapped_data[female_field_id] = {"value": "check", "type": "Checkbox"}
                mapped_data[male_field_id] = {"value": "", "type": "Checkbox"}

        # Handle single checkboxes
        elif field_info["type"] == "Single Checkbox":
            mapped_data[field_info["field_id"]] = {"value": "check" if values["value"] else "", "type": "Checkbox"}

        # Handle multiple options
        elif field_info["type"] == "Multiple Options":
            for option in values["value"]:  # Expecting a list of selected options
                full_field_id = f"{field_info['field_id_prefix']}{option.replace(' ', '')}"  # Spaces removed for key consistency
                mapped_data[full_field_id] = {"value": "check", "type": "Checkbox"}

        # Handle Single Select fields
        elif field_info["type"] == "Single Select":
            # Assuming the options are provided in the values under a 'options' key
            for option in field_info['options']:
                option_id = f"{field_info['field_id_prefix']}{option.replace(' ', '')}"  # Spaces removed for key consistency
                if values["value"] == option:
                    mapped_data[option_id] = {"value": "check", "type": "Checkbox"}
                else:
                    mapped_data[option_id] = {"value": "", "type": "Checkbox"}

    return mapped_data
