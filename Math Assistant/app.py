import streamlit as st
from decouple import config
import openai

# OpenAI API configuration
# replace your api key  in OPENAI_API_KEY
api_key = config('OPENAI_API_KEY')
openai.api_key = api_key

educational_resources = {
    "Algebra": "https://www.khanacademy.org/math/algebra",
    "Calculus": "https://www.khanacademy.org/math/calculus-1",
    "Geometry": "https://www.khanacademy.org/math/geometry",
    "Trigonometry": "https://www.khanacademy.org/math/trigonometry",
    "Statistics": "https://www.khanacademy.org/math/statistics-probability",
    "Linear Algebra": "https://ocw.mit.edu/courses/mathematics/18-06-linear-algebra-spring-2010/"
}


def ask_math_question(question):
    conversation = [
        {"role": "system", "content": "You are a math tutor."},
        {"role": "user", "content": question}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )

    reply = response['choices'][0]['message']['content']
    return reply


def main():
    user_profile = {
        "language": "English",
        "preferred_units": "imperial",
    }

    st.sidebar.title("Your Personal Math Assistant")
    choice = st.sidebar.radio("Navigation", ["Ask a Math Question", "Educational Resources"])

    if choice == "Ask a Math Question":
        st.title("Ask a Math Question")
        user_profile["language"] = st.selectbox("Language", ["English", "Spanish", "French"])
        user_profile["preferred_units"] = st.selectbox("Preferred Units", ["Metric"])

        st.subheader("Ask a math question:")
        question = st.text_area("", height=200, key="math_question")

        if st.button("Submit"):
            answer = ask_math_question(question)
            st.write(f"**Answer:** {answer}")

    elif choice == "Educational Resources":
        st.header("Explore Educational Resources")
        topic = st.selectbox("Select a topic:", list(educational_resources.keys()))

        if st.button("Explore"):
            if topic in educational_resources:
                st.write(f"Here are some educational resources for {topic}:")
                st.write(f"[{topic} on Khan Academy]({educational_resources[topic]})")
            else:
                st.error("Topic not found. Please select a valid topic.")


if __name__ == "__main__":
    main()
