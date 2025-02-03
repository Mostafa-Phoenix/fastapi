# Project Name (Replace with Your Project's Name)

## Overview

This project is a Python-based application built using FastAPI and Uvicorn, leveraging a virtual environment for dependency management. It's designed to run within the Project IDX environment and can also be containerized using Docker.

## Project IDX Setup

The project is configured for seamless development within Google's Project IDX environment. The environment setup is defined in the `.idx/dev.nix` file.

### Key Features in IDX

-   **Nix-based Environment:** The `.idx/dev.nix` file specifies the project's dependencies using Nix, ensuring a consistent and reproducible development environment.
-   **Python Environment:** Python 3.11 is used as the main development language, along with `pip` for package management.
-   **FastAPI and Uvicorn:** The application leverages FastAPI for building the web API and Uvicorn as the ASGI server.
-   **System Tools:** Several useful system tools are pre-installed:
    -   `wget`: For downloading files.
    -   `tree`: For displaying directory structures.
    -   `nano`: A simple text editor.
    -   `llama-cpp`: For running the llama model locally.
    -   `gcc`: For compiling code.
    -   `cmake`: For building packages.
    -   `ccache`: For code caching.
    -   `busybox`: Common linux utilities.
    -   `util-linux`: For common linux system utilities.
-   **VS Code Extensions:** The following VS Code extensions are pre-installed:
    -   `ms-python.python`: For Python development support.
    -   `rangav.vscode-thunder-client`: A REST API client for testing API endpoints.
-   **Preview Server:** IDX's preview functionality is enabled with the following setup:
    -   Command: `./devserver.sh` (starts the Uvicorn server).
    -   Environment variable `PORT` is passed to the server.
-   **Default on Create:**
    -   On workspace creation, the system will create a virtual environment, activate it, and install packages from the `requirements.txt` file.
    -   The `app.py` file will be opened in the editor by default if it exists.

### How to Use in IDX

1.  **Clone:** Clone the project repository in IDX.
2.  **Environment Build:** IDX will automatically detect the `dev.nix` file and prompt you to rebuild the environment. Click "Rebuild Environment" to install all packages and extensions.
3.  **Run:** Once the environment is rebuilt, the preview server will automatically start, and you can access it via the IDX preview URL. You can make changes to the `app.py`, and `uvicorn` will reload the server. If the server isn't running, you can start it from the terminal by running `./devserver.sh`.

### Manual Virtual Environment Setup (If Needed)

While IDX will handle the virtual environment setup automatically upon creation, it's useful to know how to do it manually. Here's how:

1.  **Create the Virtual Environment:**

This command creates a virtual environment named `.venv` in your project directory.

bash python3 -m venv .venv

2.  **Activate the Virtual Environment:**
    -   **Linux/macOS:**
bash source .venv/bin/activate

After activation, your terminal prompt should change to indicate that you're working within the virtual environment (e.g., `(.venv) user@host:~/project$`).

3.  **Install Dependencies:**

bash pip install -v -r requirements.txt

This command installs all the packages listed in your `requirements.txt` file into the virtual environment.

### Automating Virtual Environment Activation (Optional)

For convenience, you can automatically activate the virtual environment whenever you open a new terminal in the project directory. Here's how to add it to your `.bashrc` (or `.zshrc`, etc.):

1.  **Add to `.bashrc`:**

bash echo 'source .venv/bin/activate' >> ~/.bashrc

This command adds the activation command to the end of your `.bashrc` file.

2.  **Apply Changes:**

bash source ~/.bashrc

This command reloads your `.bashrc` file to apply the changes.

**Important Notes:**

- The automation of the `.venv` is only for the users machine outside of the idx environment.
- Using this method will activate the `.venv` in all terminals.
- You can add a if statement to `~/.bashrc` or `~/.zshrc` if you only want to activate the `.venv` when you are inside the project directory.
- It's generally recommended to manually activate the virtual environment if you have multiple projects with different environments.
- It is also important to note that IDX will do this automatically for you in its environment.

## Docker Containerization

This project can also be run within a Docker container.

### Dockerfile

A sample `Dockerfile` would be provided below, but first, be sure to create a `requirements.txt` file and add any packages you have installed in the `dev.nix` file.

-   **requirements.txt**

fastapi uvicorn[standard]

### Building and Running the Docker Container

1.  **Build:**


bash docker build -t your-project-name .

2.  **Run:**

bash docker run -p 8000:8000 your-project-name

This command runs the container and maps port 8000 on the host to port 8000 in the container.

### Additional Details

-   **`.idx/dev.nix`:** This file specifies the complete development environment setup for Project IDX. It handles package installations, environment variables, and VS Code extensions.
-   **`devserver.sh`:** This script is used to start the Uvicorn server in IDX's preview mode. It activates the virtual environment and runs the `uvicorn` command with the `--reload` flag.
-   **`requirements.txt`:** This file will hold the python packages that are needed for the project to run inside the docker container.

## Contributing

[Add your contribution guidelines here]

## License

[Add your project's license here]
