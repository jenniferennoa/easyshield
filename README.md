# EasyShield

EasyShield is a simple Python application designed to enhance your privacy by blocking access to user-specified applications on Windows. By terminating these applications when they are detected running, EasyShield helps to prevent unauthorized use and ensures your system's privacy.

## Features

- Block access to specified applications.
- Log each blocking action with a timestamp.
- Simple and easy to use.

## Installation

1. Ensure you have Python installed on your Windows system.
2. Install the required Python package `psutil` by running:
   ```bash
   pip install psutil
   ```

## Usage

1. Clone this repository or download the `easyshield.py` file.
2. Open `easyshield.py` in a text editor.
3. Modify the `block_list` variable to include the names of the applications you want to block. For example:
   ```python
   block_list = ['notepad.exe', 'calc.exe']
   ```
4. Run the script with administrator privileges to allow it to terminate processes:
   ```bash
   python easyshield.py
   ```

## Note

- The script requires administrative privileges to terminate certain processes. Make sure to run the script as an administrator.
- The script checks for blocked applications every 5 seconds and logs each blocking action in `blocked_apps_log.txt`.

## Disclaimer

This software is provided "as-is" and is intended for educational purposes only. The author is not responsible for any damage or data loss caused by the use of this software.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.