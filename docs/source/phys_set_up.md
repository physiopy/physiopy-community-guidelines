# 3. Where to start in setting up a physiological monitoring system?  

This section will help you navigate the following questions: 
* How should I organize my data collection? 
* Which physio signals do I want? 
* What systems are there?
  
When establishing a physiological monitoring setup, it is essential to follow a systematic approach. Once you have identified the signals you intend to capture, and prior to initiating data collection from a subject, it is imperative to ensure that all necessary checks from the essentials list have been completed.

You will require **peripheral devices**, typically attached to the subject, and **recording devices** (often connected to a computer/laptop) for data acquisition and storage. Moreover, additional **synchronization** may be necessary, unless it is already integrated into the software you are utilizing. Post-recording, it is crucial to accurately track events corresponding to both physiological and neuroimaging recordings at equivalent time points.  

In the context of a **neuroimaging experiment conducted within an MRI environment,** it is vital to keep all non-MRI-compatible devices outside the scanner room (ex. long cables may be employed for this purpose). Additionally, even if the peripheral and recording devices are MRI-compatible, it is advisable to inspect physiological and neuroimaging recordings for interference artifacts during pilot sessions aimed at optimizing the overall setup. 

For detailed information about a particular brand, be sure to consult the manuals thoroughly.

## a. Peripheral devices
* Cardiac
    * finger photoplethysmography (pulse-oximeter)
    * ECG electrodes (for EEG-fMRI recordings, these may be included in the EEG cap) 
    * pressure pad

* Respiration: Ventilation
    * digital respiratory belt (based on a potentiometer)
    * analog respiratory belt (based on pressure change in a tube)
    * pressure pad
    * disposable nasal cannula

* Respiration: Gas Concentration
    * disposable nasal cannula
    * disposable mask
    * disposable mouthpiece
    * long sample line to connect from the scan room to the control room
    * desiccant cartridge or desiccant tube

Some peripheral devices can be passed through a waveguide in the penetration panel from the control room to the scan room (e.g., gas sampling line); others must be plugged into the penetration panel for noise filtering (e.g., some pulse sensors). Devices native to the MRI scanner may communicate wirelessly with the scanner. When adding non-native peripheral devices to the scanner environment, we recommend that you check that you are not bringing any outside noise into the scan room or bringing too much scanner noise into the physiological recordings. It may be necessary to develop additional devices or mechanisms to shield these connections. Furthermore, looping of cords can create eddy currents that increase noise, so they should be taped down or placed on hooks to keep them in place. <!-- (SETUP_170322) -->

## b. Recording devices
* Cardiac
    * analog-to-digital converter (ADC) or other data acquisition (DAQ) device
    * associated signal recording/analysis software
* Respiration: Ventilation
    * analog-to-digital converter (ADC) or other data acquisition (DAQ) device
    * associated signal recording/analysis software
* Respiration: Gas Concentration
    * CO2 and O2 analyser
    * analog-to-digital converter (ADC) or other data acquisition (DAQ) device
    * associated signal recording/analysis software

There are several devices that can be used for physiological data acquisition as listed below. Nevertheless, the community recommended practices stated here should be valid independently of the acquisition system used. If you are aware of any system that is not listed here, feel free to reach out and we will include it.

* [ADInstruments](https://www.adinstruments.com/), using LabChart software.
* [Biopac](https://www.biopac.com/), using the AcqKnowledge software. 
* [Brain Vision](https://brainvision.com/)
* [CED Spike](https://ced.co.uk/products/testimspk)

## c. Syncing with the neuroimaging acquisition
In most cases, it is important to sync the physiological recordings with the neuroimaging recordings. In the case of fMRI, scan triggers indicating the acquisition of each volume, or sometimes slice, may be used for this purpose. To do this, it will be necessary to extract the trigger pulses from your MRI scanner, typically inputting these analog signals using a coaxial cable with BNC connectors into the same ADC that is recording the physiological information. If this option cannot be used, another way of obtaining some information from the scanner is to send a volt pulse as a block for the whole duration of the scan. <!-- ([SETUP_170322]) --> 

Depending on the physiological acquisition equipment, this process may be more or less challenging. When the integration of volume triggers is not straightforward, we may use a USB sniffer to record changes in signal in the USB stream. For other systems, the physiological recording files may present a timestamp (such as full date, milliseconds since 12 AM or other formats). In these cases, they may be matched with the acquisition time stored in the DICOM/NIfTI files, for fMRI, or equivalent files for other neuroimaging modalities. Additionally, some third-party softwares for the integration of behavioral stimuli in the experiment may also aid in this process. <!-- ([SETUP_170322]) -->
