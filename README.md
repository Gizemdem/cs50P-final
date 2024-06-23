# Meme Online, What do you meme?

#### Description:
The ["Meme Online" project](https://cs50pfinal-what-do-you-meme.streamlit.app/) is a web application built using Streamlit, a popular Python library for creating web applications. The aim of the project is to provide users with a platform where they can generate memes online by adding captions to random meme templates fetched from a JSON file download from [meme source](https://api.memegen.link/templates). The application allows users to submit their captions, which are then overlaid onto the selected meme template, and finally, users can download meme. The Pillow library, a Python Imaging Library (PIL), is used for image processing tasks such as inserting user captions onto meme templates and exporting the customized memes.

#### Design Choices:

1. **Streamlit**: Streamlit was chosen as the framework for building the web application due to its simplicity and ease of use for creating web applications in Python. Its reactive programming model allows for quick prototyping and development of interactive interfaces without the need for complex frontend code.

2. **External API for Meme Templates**: The project utilizes an external API to fetch random meme templates. This decision was made to ensure a diverse and constantly updated collection of meme templates without the need for manual maintenance. By fetching templates dynamically from an API, the application remains fresh and engaging for users.

3. **Caption Overlay**: The Meme class overlays user-submitted captions onto the selected meme templates. This design choice enables users to personalize the memes according to their sense of humor or context. By allowing users to add captions, the application enhances user engagement and provides a more interactive experience.

4. **Download Functionality**: The application includes a download button that allows users to download the customized meme with their caption.

5. **Reload**: When the user does not like the meme, reload button allows to fetch new random meme.

#### File Descriptions:

1. **project.py**: This file contains the main code for the Streamlit web application. It sets up the user interface and handles user interactions. Here's a breakdown of its components:

        Initialization: Initializes the Streamlit application and sets page configuration.

        Header and Buttons: Displays the application title and provides buttons for downloading memes and reloading for a new template.

        Meme Display and Caption Form: Displays the meme template and allows users to submit captions. After submission, the caption is overlaid onto the meme template, and the customized meme is displayed for download.

        Footer: Credits the creator of the application.

2. **meme.py**: This file defines the Meme class responsible for fetching meme templates from an external API and processing them. Here's an explanation of its functionalities:

        Random Meme Selection: Selects a random meme template from a JSON file containing meme data fetched from an external API.

        Caption Overlay: Overlays user-submitted captions onto the template using Pillow, an image processing library.

        Export Meme: Saves the meme with caption text.

3. **memes.json**: This JSON file contains data fetched from the external API and serves as a local cache of meme templates. Each entry in the JSON file represents a meme template, including its URL and other relevant information.
