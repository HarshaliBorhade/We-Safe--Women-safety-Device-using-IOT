# We Safe - Women Safety Device 🚨

This project is aimed at enhancing women's safety using real-time monitoring and emergency alert systems. The device continuously monitors various environmental and health parameters and sends an emergency alert to a designated contact in case of distress. The system uses sensor data, including location, temperature, and vital health signs like blood pressure and pulse rate, to trigger an alert. A camera is also integrated to capture images in critical situations and send them along with the alert.

---

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Hardware Requirements](#hardware-requirements)
5. [Installation](#installation)
6. [Usage](#usage)
7. [Results](#results)
8. [Contributing](#contributing)
9. [License](#license)

---

## Overview
**We Safe - Women Safety Device** is an intelligent system that helps keep women safe by monitoring their environment and health in real time. If the device detects abnormal values—such as a dangerous temperature, abnormal blood pressure, or distress signals—it automatically sends an emergency alert. The system also uses a camera to capture an image during an emergency and sends the photo along with location information to a trusted contact.

This system is intended to help in situations where quick intervention is required, improving overall safety and peace of mind for women.

---

## Features
- **Real-time Monitoring**: Continuously tracks environmental conditions such as temperature and health parameters like blood pressure and pulse rate.
- **Emergency Alerts**: Sends automatic email alerts with health information and location details when critical thresholds are crossed (e.g., abnormal temperature or pulse rate).
- **Camera Integration**: Takes a snapshot and attaches it to the alert email in case of an emergency.
- **Location Tracking**: Sends latitude and longitude information as part of the email for better identification of the situation.
- **Threshold Detection**: Configurable threshold for temperature, pulse rate, and other health metrics to trigger alerts.
- **Email Integration**: Uses Gmail's SMTP server to send email alerts.

---

## Technologies Used
- **Python**: Core programming language for developing the system.
- **OpenCV**: For capturing images from the connected camera.
- **smtplib**: For sending emergency email notifications.
- **serial**: For interfacing with sensors and serial communication.
- **cv2 (OpenCV)**: For image capturing and processing.
- **IMAP**: For handling email sending with attachments.
  
---

## Hardware Requirements
- **Temperature Sensor**: To monitor the temperature and detect critical heat levels.
- **Pulse Rate and Blood Pressure Sensors**: To measure the user's pulse rate and blood pressure for detecting health-related emergencies.
- **Camera (e.g., Webcam or IP Camera)**: For capturing an image in case of an emergency.
- **Arduino or Microcontroller**: To interface with the sensors and send data through serial communication.
- **PC or Raspberry Pi**: For running the Python script and interacting with the hardware.

---

## Installation

### 1. Clone the Repository
Clone the project repository to your local machine:
```bash
git clone https://github.com/your-username/we-safe-women-safety-device.git
cd we-safe-women-safety-device
