# helper.py

# This dictionary maps the keys from sample_data to the field IDs and types used in the PDF form.
key_to_field_info = {
    "Name": {"field_id": "First Name", "type": "Text Field"},
    "Home Address": {"field_id": "Home Address_pg1", "type": "Text Field"},
    "City, State, Zip Code_Home": {"field_id": "City State Zip Code_Home", "type": "Text Field"},
    "Mailing Address": {"field_id": "Mailing Address_if different", "type": "Text Field"},
    "City State Zip Code if_mailing": {"field_id": "City State Zip Code if_mailing", "type": "Text Field"},
    "Phone Number": {"field_id": "Phone Number", "type": "Text Field"},
    "Are you homeless": {"field_id_prefix": "Are you homeless_", "type": "Yes/No"},
    "Do you have a Massachusetts Electronic Benefits Transfer (EBT) card?": {"field_id_prefix": "Do you have a Massachusetts Electronic Benefits Transfer (EBT) card?_", "type": "Yes/No"},
   
   # I have only checked them, though they are not in the file you have sent #########
    
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
    "Disability": {"field_id_prefix": "Are you a person with a disability?_", "type": "Multiple Options"},
    "Has anyone worked in the last 60 days?": {"field_id_prefix": "Has anyone worked in the last 60 days?_", "type": "Yes/No"},
    "Does anyone receive any other type of income such as Unemployment Compensation, Child Support, Social Security, SSI, Workers’ Compensation, Veterans’ Benefits, Pensions or Rental Income?": {"field_id_prefix": "Does anyone receive any other type of income such as Unemployment Compensation, Child Support, Social Security, SSI, Workers’ Compensation, Veterans’ Benefits, Pensions or Rental Income?_", "type": "Yes/No"},
    "Is the household responsible to pay the shelter cost?": {"field_id_prefix": "Shelter costs_", "type": "Yes/No"},
    "Is the household responsible to pay utility costs separate from shelter costs?": {"field_id_prefix": "Is the household responsible to pay utility costs separate from shelter costs?_", "type": "Yes/No"},
    "Is anyone responsible to pay for adult or child care costs?": {"field_id_prefix": "Is anyone responsible to pay for adult or child care costs?_", "type": "Yes/No"},
    "Does anyone travel to and/or from a dependent care provider?": {"field_id_prefix": "Does anyone travel to and/or from a dependent care provider?_", "type": "Yes/No"},
    "Does anyone who is at least 60 years old and/or disabled have out-of-pocket medical expenses?": {"field_id_prefix": "Does anyone who is at least 60 years old and/or disabled have out-of-pocket medical expenses?_", "type": "Yes/No"},
    "Is anyone in a training program at least 80 hours per month?": {"field_id_prefix": "Is anyone in a training program at least 80 hours per month?_", "type": "Yes/No"},
    "Is anyone working in exchange for goods and services (in-kind work)?": {"field_id_prefix": "Is anyone working in exchange for goods and services (in-kind work)?_", "type": "Yes/No"},
    "Is anyone doing an unpaid internship?": {"field_id_prefix": "Is anyone doing an unpaid internship?_", "type": "Yes/No"},
    "Is anyone volunteering?": {"field_id_prefix": "Is anyone volunteering?_", "type": "Yes/No"},
    "Does anyone travel to and/or from medical care such as a pharmacy, doctor, therapist, etc.)?": {"field_id_prefix": "Does anyone travel to and/or from medical care such as a pharmacy, doctor, therapist, etc.)?_", "type": "Yes/No"},
    "Has anyone received SNAP benefits outside of MA within past 30 days?": {"field_id_prefix": "Has anyone received SNAP benefits outside of MA within past 30 days?_", "type": "Yes/No"},
    "Do you want to give us permission to contact a person or agency if we cannot reach you by phone?": {"field_id_prefix": "Do you want to give us permission to contact a person or agency if we cannot reach you by phone?_", "type": "Yes/No"},
    "Do you want to give a person or agency permission to speak with DTA and get relevant confidential information about your case?": {"field_id_prefix": "Do you want to give a person or agency permission to speak with DTA and get relevant confidential information about your case?_", "type": "Yes/No"},
    "Do you want to give an agency or someone you trust permission to sign forms, report changes, complete interviews, and talk about your case with us?": {"field_id_prefix": "Do you want to give an agency or someone you trust permission to sign forms, report changes, complete interviews, and talk about your case with us?_", "type": "Yes/No"},
    "Do you want to give someone you trust permission to get an EBT card to food shop for you using your SNAP benefits?": {"field_id_prefix": "Do you want to give someone you trust permission to get an EBT card to food shop for you using your SNAP benefits?_", "type": "Yes/No"},
    "If you do not want DTA to text you, please check this box": {"field_id": "If you do not want DTA to text you, please check this box", "type": "Single Checkbox"},
    
    

}

def map_fields(json_data):
    mapped_data = {}
    for key, values in json_data.items():
        field_info = key_to_field_info.get(key)
        if not field_info:
            continue

        # Handle NAME here as 
        if key == "Name":
            names = values["value"].split()
            first_name = names[0]
            last_name = names[-1] if len(names) > 1 else ''
            middle_names = ' '.join(names[1:-1]) if len(names) > 2 else ''

            mapped_data["First Name"] = {"value": first_name, "type": "Text Field"}
            if middle_names:
                mapped_data["Middle Name_pg1"] = {"value": middle_names, "type": "Text Field"}
            if last_name:
                mapped_data["Last Name_pg1"] = {"value": last_name, "type": "Text Field"}
            continue 

        # Handle text fields
        if field_info["type"] == "Text Field":
            mapped_data[field_info["field_id"]] = {"value": values["value"], "type": "Text Field"}

        # Handle Yes/No fields
        elif field_info["type"] == "Yes/No":
            yes_field_id = f"{field_info['field_id_prefix']}Yes"
            no_field_id = f"{field_info['field_id_prefix']}No"
            if values["value"] == "Yes":
                mapped_data[yes_field_id] = {"value": "x", "type": "Checkbox"}
                mapped_data[no_field_id] = {"value": "", "type": "Checkbox"}
            elif values["value"] == "No":
                mapped_data[no_field_id] = {"value": "x", "type": "Checkbox"}
                mapped_data[yes_field_id] = {"value": "", "type": "Checkbox"}

        # Handle Gender fields
        elif field_info["type"] == "Gender":
            male_field_id = f"{field_info['field_id_prefix']}Male"
            female_field_id = f"{field_info['field_id_prefix']}Female"
            if values["value"] == "Male":
                mapped_data[male_field_id] = {"value": "x", "type": "Checkbox"}
                mapped_data[female_field_id] = {"value": "", "type": "Checkbox"}
            elif values["value"] == "Female":
                mapped_data[female_field_id] = {"value": "x", "type": "Checkbox"}
                mapped_data[male_field_id] = {"value": "", "type": "Checkbox"}

        # Handle single checkboxes
        elif field_info["type"] == "Single Checkbox":
            mapped_data[field_info["field_id"]] = {"value": "check" if values["value"] else "", "type": "Checkbox"}

        # Handle multiple options
        elif field_info["type"] == "Multiple Options":
            for option in values["value"]:  # Expecting a list of selected options
                full_field_id = f"{field_info['field_id_prefix']}{option.replace(' ', '')}"  # Spaces removed for key consistency
                mapped_data[full_field_id] = {"value": "x", "type": "Checkbox"}

        # Handle Single Select fields
        elif field_info["type"] == "Single Select":
            for option in field_info['options']:
                option_id = f"{field_info['field_id_prefix']}{option.replace(' ', '')}"  # Spaces removed for key consistency
                if values["value"] == option:
                    mapped_data[option_id] = {"value": "check", "type": "Checkbox"}
                else:
                    mapped_data[option_id] = {"value": "", "type": "Checkbox"}

    return mapped_data

