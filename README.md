# 🔧 ACS Laptop Motherboard Debug Analyzer

**Professional tool for laptop motherboard debugging and diagnostics**

## Features
- 8-channel logic analyzer
- Real-time waveform display
- Protocol decoding (I2C, SPI, UART)
- Automated laptop diagnostics
- Professional reporting

## Installation
```bash
pip install -r requirements.txt

python logic_analyzer.py

🖥️ User Interface Guide
Main Window Layout
┌─────────────────────────────────────────────────────────────────────────┐
│  Menu Bar: File, Edit, View, Tools, Window, Help                       │
├─────────────────────────────────────────────────────────────────────────┤
│  Toolbar: [Connect] [Start] [Stop] [Measure] [Save] [Load] [Print]     │
├─────────────────────────────────────────────────────────────────────────┤
│  Status Bar: Connection status | Sample rate | Trigger | Memory | Time │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │  Tab Bar: 🌊 Waveforms ⚙️ Config 📏 Measure 🔍 Protocol 📊 Spectrum│   │
│  ├─────────────────────────────────────────────────────────────────┤   │
│  │                                                                 │   │
│  │                    Main Content Area                            │   │
│  │                    (Changes per tab)                            │   │
│  │                                                                 │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘

1. Menu Bar Functions
File Menu
New Session (Ctrl+N): Start fresh session

Open (Ctrl+O): Load saved capture file

Save Data (Ctrl+S): Save current capture

Save As (Ctrl+Shift+S): Save with new filename

Export: Export data in various formats

CSV: Comma-separated values

Excel: Microsoft Excel format

Report: HTML/PDF report

Image: Waveform screenshot

Exit (Ctrl+Q): Close application

Edit Menu
Copy (Ctrl+C): Copy selected data

Paste (Ctrl+V): Paste data from clipboard

Preferences: Application settings

View Menu
Full Screen (F11): Toggle fullscreen mode

Zoom In (Ctrl++): Increase zoom level

Zoom Out (Ctrl+-): Decrease zoom level

Reset Zoom (Ctrl+0): Auto-scale waveforms

Tools Menu
Device Manager: Hardware device management

Calibration: Signal calibration tools

Script Editor: Open scripting interface

Math Channels: Create mathematical channels

Measurements: Measurement tools

Help Menu
Documentation (F1): Open user manual

Video Tutorials: Learning resources

Check for Updates: Software updates

About: Application information

About Qt: Qt framework information

2. Toolbar Functions
Button	Icon	Function	Shortcut
Connect	🔗	Connect to hardware	-
Start	▶	Start capture	F5
Stop	⏹	Stop capture	F6
Single	⏺	Single capture	F7
Measure	📏	Take measurements	-
Cursors	✥	Toggle cursors	-
Auto Setup	⚡	Auto configure	-
Save	💾	Save data	Ctrl+S
Load	📂	Load data	Ctrl+O
Print	🖨️	Print report	Ctrl+P


3. Main Tabs Overview
Tab 1: 🌊 Waveforms
Real-time signal display

Zoom and pan functionality

Cursor measurements

Trigger controls

Display settings

Tab 2: ⚙️ Configuration
Channel configuration (8 channels)

Signal type selection

Voltage range settings

Trigger configuration

Acquisition settings

Tab 3: 📏 Measurements
Statistical measurements

Channel statistics

Histogram display

Measurement gating

Results table

Tab 4: 🔍 Protocol
Protocol decoding (I2C, SPI, UART, etc.)

Protocol settings

Decoded data display

Packet analysis

Protocol statistics

Tab 5: 📊 Spectrum
FFT analysis

Frequency domain display

Window functions

Harmonic analysis

Frequency measurements

Tab 6: 💻 Laptop Tests
Automated diagnostic tests

Power sequence verification

Voltage rail testing

Clock signal analysis

SMBus device scanning

Tab 7: 📝 Scripting
Python scripting interface

Script editor

Console output

Example scripts

Automation tools

Tab 8: 📋 Log & Data
Application logs

Data management

Capture history

Log filtering

Export capabilities

🔧 Detailed Feature Guide
1. Signal Capture and Display
Basic Capture Procedure
Configure Channels:

Go to Configuration tab

Enable desired channels (CH1-CH8)

Set signal type (Digital/Analog/PWM/etc.)

Configure voltage range and threshold

Set Trigger Conditions:

Select trigger source (any channel)

Choose trigger type (Rising/Falling/Either)

Set trigger level (0-30V)

Configure trigger mode (Auto/Normal/Single)

Adjust Display Settings:

Set timebase (1ns to 1s/div)

Adjust voltage scale (500mV to 20V/div)

Enable/disable grid

Set interpolation method

Start Capture:

Click "Start" button or press F5

Monitor real-time waveforms

Use zoom/pan for detailed view

Click "Stop" or press F6 to end capture

Advanced Display Features
Persistence Mode: Overlay multiple captures

Vector Display: Connect sample points

Color Coding: Each channel has unique color

Cursor Measurements: Vertical and horizontal cursors

Zoom Region: Select area for detailed view

Auto-scaling: Automatic axis adjustment


2. Channel Configuration
Channel Settings Table
Parameter	Options	Default	Description
Enable	On/Off	On	Enable/disable channel
Signal Type	Digital, Analog, PWM, I2C, SPI, UART, 1-Wire, CAN, LIN, PS/2	Digital	Signal type for decoding
Coupling	DC, AC, GND	DC	Input coupling
Voltage Range	Auto, 500mV, 1V, 2V, 5V, 10V, 20V	Auto	Input voltage range
Threshold	0-30V	1.8V	Digital threshold voltage
Bandwidth Limit	On/Off	Off	Limit bandwidth to 20MHz
Invert	On/Off	Off	Invert signal polarity
Channel Groups
Analog Channels (1-8): Standard voltage measurements

Digital Pod (D0-D7): Digital signal analysis

Math Channels: Calculated from other channels

Reference Channels: Saved waveforms for comparison

3. Measurement Tools
Available Measurements
Measurement	Formula	Unit	Description
Min	min(V)	V	Minimum voltage
Max	max(V)	V	Maximum voltage
Mean	avg(V)	V	Average voltage
RMS	sqrt(avg(V²))	V	Root mean square
Vpp	max(V) - min(V)	V	Peak-to-peak voltage
Frequency	1/period	Hz	Signal frequency
Period	T	s	Time period
Duty Cycle	(Ton/T)*100	%	Pulse width percentage
Rise Time	t(90%) - t(10%)	s	10%-90% rise time
Fall Time	t(10%) - t(90%)	s	90%-10% fall time
Overshoot	(Vmax - Vfinal)/Vfinal*100	%	Signal overshoot
Undershoot	(Vfinal - Vmin)/Vfinal*100	%	Signal undershoot
Measurement Procedures
Automatic Measurements:

Go to Measurements tab

Select measurement type

Enable desired measurements

View real-time results

Cursor Measurements:

Enable cursors in Waveforms tab

Position vertical cursors (V1, V2)

Position horizontal cursors (H1, H2)

Read Δ values in measurement panel

Gated Measurements:

Enable gating in Measurements tab

Define gate region using cursors

Measurements calculated only within gate


🔌 Hardware Connection Guide
Supported Hardware Devices
Logic Analyzers

1. Saleae Logic (Recommended)

Models: Logic 4, Logic 8, Logic Pro 8/16

Sample Rate: Up to 500 MS/s

Channels: 4-16 digital, 4 analog

Driver: libusb/WinUSB

2. Digilent Analog Discovery 2

Sample Rate: 100 MS/s

Channels: 16 digital, 2 analog

Features: Built-in power supplies

3. Cypress FX2LP based

Sample Rate: 24 MS/s typical

Channels: 8 digital

Common in DIY logic analyzers

4. FTDI based devices

Sample Rate: 1-30 MS/s

Channels: 4-8 digital

Widely available and inexpensive

Connection Procedure
Step 1: Safety Precautions
⚠️ WARNING: Always follow these safety guidelines
1. Power Off: Disconnect AC adapter and battery
2. Discharge: Press power button for 30 seconds
3. Grounding: Use anti-static wrist strap
4. Inspection: Check for visible damage
5. Isolation: Use isolation transformer if probing live circuits
