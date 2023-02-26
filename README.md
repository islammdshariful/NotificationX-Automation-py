# Selenium Python Test Automation (NotificationX)

This repository contains an automated testing framework for web applications using Selenium and Python 3.10. It includes sample test cases for creating notifications for [NotificationX Plugin](https://notificationx.com/).

## Requirements

- Python 3.10
- virtualenv
- selenium 
- pytest

Please note that you do not have to install the any Chrome driver separately, as this repository uses Selenium v4.8.2, which automatically downloads and runs the driver during test execution.

## Installation

1. Clone this repository to your local machine.
2. Create a virtual environment using `virtualenv`:

```sh
$ virtualenv venv
```
3. Activate the virtual environment:
```sh
$ source venv/bin/activate
```
4. Install the required packages using pip:
```sh
$ pip install -r requirements.txt
```

## Usage
(Make sure that your website's URL are provided in `./utils/config/`.)

1. Activate the virtual environment:
```sg
$ source venv/bin/activate
```
2. Run the tests:
```sh
$ pytest test/test_nx_create_notice_without_queue.py
```
3. Deactivate the virtual environment:
```sh
$ deactivate
```

## Sample Test Cases
The repository includes the following sample test cases:

- test_nx_create_notice_without_queue.py: Creates all notification without enabling global queue feature.
- test_nx_create_notices_with_queue.py: Creates all notification with enabling global queue feature.
- test_nx_with_advanced_design.py: Creates all notification using advcned deasign.
- test_nx_without_advanced_design.py: Creates all notification without advcned deasign.

## Contributions
Contributions to this repository are welcome. If you find any issues or have any suggestions for improvements, please submit a pull request or create an issue.