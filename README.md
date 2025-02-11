### 1. Run automatically

- `install.bat`: Install the required virtual environment and libraries.
- `run.bat`: Generate invoices and display the terminal.
- `auto.vbs`: Generate invoices silently without displaying the terminal.

### 2. Manual installation

- Create a virtual environment

  In the project directory, run the following command to create a virtual environment:

  ```sh
  python -m venv env
  ```

  `env` is the name of the folder containing the virtual environment, which can be renamed as needed.

- Activate the virtual environment (Windows CMD)

  ```sh
  env\Scripts\activate
  ```

- Deactivate the virtual environment

  ```sh
  deactivate
  ```

- Delete the virtual environment

  If no longer needed, delete the `env` folder:

  ```sh
  rd /s /q env
  ```
