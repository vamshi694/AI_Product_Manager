# Dylan - AI_Product_Manager
## Your virtual employee available at a moment's notice to brainstorm
    1) New feature request
    2) New product development plan
    3) Root cause  analysis for an issue in the current product


[def]: images/Dylan_Flow.png
![alt text][def]

## Team Members

1. [Vamshi Mugala](https://github.com/vamshi694)
2. [Jahnavi Cheethirala](https://github.com/JaanviR)
3. [Jenny](https://github.com/JenPink25)
4. [Sahil Mahey](https://github.com/SahilMahey)

## Table of Contents

- [Key Features](#key-features)
- [Concept Covered](#concept-covered)
- [Technical Stack](#technical-stack)
- [Getting Started](#getting-started)
- [Video Demo](#video-demo)
- [License](#license)

## Key Features

- **Brainstorming New Product Ideas:**
  - Facilitates the generation of new product ideas and technical specifications.
  
- **Feature Request / New Products:**
  - Streamlines collecting and prioritizing new feature requests for existing products..

- **KPI Analysis:**
  - Utilizes AI to perform root cause analysis on KPI drops and synthesizes user feedback studies, providing actionable insights.

- **Integration with Tools:**
  - Seamlessly connecting with Jira and other project management tools to fetch data and manage storyboards effectively. Summarizes the conversation to send it via email to the desired individual.

- **Avatar Interface:**
  - Creating a user-friendly, avatar-based interface to humanize interactions with AI and enhance user engagement..

## Concept Covered

1. **User Experience and PM knowledge:** - Interviewed real TPMs and PMs about pain points and other day-in-life things.
2. **Gemini AI:** -We utilized Gemini AI's language generation (Gemini 1.5 Pro for better conversation build).
3. **API Integrations:** - We utilized several Email APIs, Jira APIs & D-ID Avatar APIs to stream the Text--> Speech Avatar into UI.

## Technical Stack

- **UI and Logic Development:** Python, Streamlit, Gemini API, JIRA API, Email API, D-ID Avatar API

## Getting Started

1. Clone the repository.
2. Open the terminal and navigate to the code directory.
3. Run the following command to install the required dependencies:

   ```bash
    pip install -r requirements.txt
   ```

4. Navigate to Dylan Folder.
5. Add .env file in the folder with following requirements. These API Keys will be provided by the used:
   ```
    API_KEY = "Gemini API KEY"
    API_KEY_D_ID = "D_ID Avatar API Key"
    JIRA_API = "JIRA API Key"
    JIRA_EMAIL_ID = "JIRA email id"
   ```
6. In the same .env file, to send an email, create a create an app passcode from your gmail id and use those details here. Add the senders and receivers email id's here too:
FROM_ADD = "from address (email)"
TO_ADD = "to address email":
    ```
    APP_PASSCODE = "Gmail Passcode"
    APP_MAIL_ID = "Your App email Id"
    FROM_ADD = "Sender email id"
    TO_ADD = "Receiver email id"
    ```
7. Run app.py in Dylan folder:
   ```bash
    streamlit run app.py
   ```

## Video Demo

1. [Full Video Demonstration]()
2. [Full Project Demonstration](https://devpost.com/sahilmahey929?ref_content=user-portfolio&ref_feature=portfolio&ref_medium=global-nav)

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code. We appreciate your contributions and hope Dylan brings joy to your product management journey! 🍲🚀



