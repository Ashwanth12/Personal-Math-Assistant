# Personal Math Assistant

This project is a personal math assistant built using Streamlit and OpenAI's GPT-3.5 Turbo model. The assistant allows users to ask math questions and provides answers based on the conversation with the GPT-3.5 Turbo model.

## Features
- **Ask a Math Question**: Users can ask math questions in English, Spanish, or French. The assistant generates responses using the GPT-3.5 Turbo model.
- **Educational Resources**: Users can explore educational resources for various math topics such as Algebra, Calculus, Geometry, Trigonometry, Statistics, and Linear Algebra.

## How it Works
The project uses the Streamlit framework for the user interface. The main function is responsible for rendering the sidebar navigation and content based on the user's choice.

### Asking a Math Question
- The user selects the language and preferred units (imperial or metric) from the sidebar.
- The user enters a math question in the text area and clicks the "Submit" button.
- The question is passed to the `ask_math_question` function, which creates a conversation with the GPT-3.5 Turbo model.
- The model generates a response based on the conversation and the user's question.
- The answer is displayed to the user.

### Exploring Educational Resources
- The user selects the "Educational Resources" option from the sidebar.
- The user selects a math topic from the dropdown menu.
- The user clicks the "Explore" button.
- If the selected topic is available in the `educational_resources` dictionary, the assistant displays the corresponding educational resources link.
- If the selected topic is not found, an error message is displayed.

## Setup
To run this project, follow these steps:
1. Install the required packages by running `pip install -r requirements.txt`.
2. Set up your OpenAI API key by replacing `your api key` in the `api_key` variable.
3. Run the `streamlit_app.py` function to start the Streamlit app.

## Dependencies
The project uses the following dependencies:
- Streamlit: Used for building the user interface.
- Decouple: Used for managing environment variables.
- OpenAI: Used for integrating with the GPT-3.5 Turbo model.

## Educational Resources
This project provides educational resources for the following math topics:
- Algebra: [Khan Academy - Algebra](https://www.khanacademy.org/math/algebra)
- Calculus: [Khan Academy - Calculus](https://www.khanacademy.org/math/calculus-1)
- Geometry: [Khan Academy - Geometry](https://www.khanacademy.org/math/geometry)
- Trigonometry: [Khan Academy - Trigonometry](https://www.khanacademy.org/math/trigonometry)
- Statistics: [Khan Academy - Statistics](https://www.khanacademy.org/math/statistics-probability)
- Linear Algebra: [MIT OpenCourseWare - Linear Algebra](https://ocw.mit.edu/courses/mathematics/18-06-linear-algebra-spring-2010/)

Feel free to explore these resources to enhance your math skills!

