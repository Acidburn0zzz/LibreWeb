# Send email dialog
dialog_model_props = {"PositionX": 0, "PositionY": 0,
                      "Width": 400, "Height": 300,
                      "Title": "Send me an email"}
# Dialog have 5 elements
SubjectLabel_props = {"Label": "Subject", "FontHeight": 15, "Align": 0, "Border": 0,
                      "Width": 80, "Height": 20, "PositionX": 40, "PositionY": 15,
                      "VerticalAlign": 1}

Subject_props = {"Border": 3, "FontHeight": 15, "PositionX": 40, "Align": 1,
                 "PositionY": 35, "Width": 320, "Height": 20, "VerticalAlign": 1}

MessageLabel_props = {"Label": "Message", "FontHeight": 15, "Align": 0, "Border": 0,
                      "Width": 80, "Height": 20, "PositionX": 40, "PositionY": 70,
                      "VerticalAlign": 1}

Message_props = {"Border": 3, "FontHeight": 15, "PositionX": 40,
                 "Align": 0, "VerticalAlign": 0, "MultiLine": True,
                 "PositionY": 90, "Width": 320, "Height": 150, "AutoVScroll": True}

SendButton_props = {"Align": 1, "Label": "Send", "FontHeight": 15, "Width": 80,
                    "Height": 20, "PositionX": 280, "PositionY": 260,
                    "VerticalAlign": 1, "Enabled": True}
# All in one
dialog_items = (
    ("Subjectlabel", "FixedText", SubjectLabel_props),
    ("Subject", "Edit", Subject_props),
    ("MessageLabel", "FixedText", MessageLabel_props),
    ("Message", "Edit", Message_props),
    ("SendButton", "Button", SendButton_props)
)
