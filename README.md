# Code-Guru

## Features
- **Interactive Code Generation**: Create custom coding exercises from natural language prompts.
- **Step-by-Step Guidance**: Ghost text guides users through coding exercises one step at a time.
- **Multi-Language Support**: Works with HTML, CSS, JavaScript, Python, and other languages.
- **Real-Time Code Execution**: Run code directly in the browser for supported languages.
- **AI-Powered Execution**: Simulate execution results for non-browser languages using OpenAI.
- **Progress Tracking**: Track completion progress through generated exercises.
- **Helpful Hints**: Get assistance when stuck on challenging sections.

## Tech Stack
- **Frontend**: HTML5, CSS3, Vanilla JavaScript.
- **UI**: Custom responsive design with CSS Grid/Flexbox.
- **API Integration**: OpenAI API (GPT-4) for code generation and execution simulation.
- **Code Execution**: In-browser execution for web technologies (HTML/CSS/JS).
- **Local Storage**: Browser `localStorage` for API key persistence.

## Setup and Usage
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo.git
   ```
2. Open `index.html` in a web browser.
3. Enter your OpenAI API key in the designated field.
4. Enter a prompt describing what you want to build (e.g., "A login page with form validation").
5. Click **"Generate Structure"** to create your custom coding exercise.
6. Follow the ghost text guidance to complete each section.
7. Use the **"Run Code"** button to see your code in action.
8. Click **"Skip to Next"** when ready to move to the next section.

## Problems Faced & Solutions
### Ghost Text Implementation
- **Challenge**: Creating an intuitive typing experience with ghost text that doesn't disappear prematurely.
- **Solution**: Implemented a token-based approach that shows just the next word/token and maintains visibility throughout typing.

### Language Detection & Execution
- **Challenge**: Supporting various programming languages with appropriate execution environments.
- **Solution**: Created a hybrid system using browser execution for web technologies and OpenAI API for non-browser languages.

### API Response Parsing
- **Challenge**: Consistently parsing structured content from OpenAI API responses.
- **Solution**: Developed robust parsing logic with multiple fallback mechanisms to handle various response formats.

### Code Execution Isolation
- **Challenge**: Safely executing user-written JavaScript without affecting the main application.
- **Solution**: Implemented sandboxed execution environments with console output redirection.

### OpenAI Prompt Engineering
- **Challenge**: Getting consistently formatted, executable code from the API.
- **Solution**: Refined system prompts with explicit formatting instructions and lower temperature settings.

## Future Improvements
- Add support for more programming languages.
- Implement user accounts to save progress.
- Create predefined learning paths and tutorials.
- Add collaborative coding features.
- Integrate with version control systems.
- Include testing frameworks for generated code.

## License
MIT License - See `LICENSE` file for details.

## Credits
Created by **NoPlayButton**  
Powered by **OpenAI API**

