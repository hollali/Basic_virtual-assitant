# Hollali - Virtual Assistant

Hollali is a simple virtual assistant built in Python that responds to voice commands using text-to-speech and speech recognition. It can provide information about the current time, date, and open Notepad. Feel free to extend its functionality based on your needs.

## Prerequisites

Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

Install the required Python packages using the following command:

```bash
pip install pyttsx3 datetime json random SpeechRecognition
```

Additionally, for speech recognition, you might need to install the necessary dependencies based on your operating system. Check the [SpeechRecognition documentation](https://pypi.org/project/SpeechRecognition/) for more details.

## Usage

1. Run the script:

    ```bash
    python hollali.py
    ```

2. Hollali will greet you and wait for your voice command.

3. You can ask Hollali about the time, date, or instruct it to open Notepad.

4. To exit the virtual assistant, simply say "exit" or "quit."

## Functionality

- **Greeting:** Hollali greets you upon startup and asks how it can assist you.

- **Time and Date:** Ask Hollali about the current time or date, and it will provide you with the information.

- **Open Notepad:** Instruct Hollali to open Notepad, and it will launch the application.

- **Exit:** You can say "exit" or "quit" to terminate the virtual assistant.

## Customization

Feel free to customize the script and add more functionalities based on your requirements. You can extend the `main()` function to handle additional commands and responses.

```python
# Example:
# elif 'your_custom_command' in query:
#     # Your custom logic here
#     speak("I can handle your custom command!")
```

## Notes

- This script uses the `pyttsx3` library for text-to-speech and `SpeechRecognition` for speech recognition. Ensure that your microphone is correctly set up for speech recognition to work effectively.

- The script is set up to use the Google Speech Recognition API. You may need an internet connection for this feature to work.

- The `speak()` function is responsible for both printing messages to the console and speaking them aloud. Adjust it according to your preferences.

Enjoy using Hollali! If you have any suggestions or improvements, feel free to contribute.
