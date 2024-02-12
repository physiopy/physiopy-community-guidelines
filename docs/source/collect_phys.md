# 4. Setting up and acquiring physiological data 

In this section, we discuss common methods of setting up and acquiring physiological data, along with important practices to ensure you are collecting high quality data. For all signals, acquiring a continuous time course is recommended for the greatest impact on your MR data. However, if that is not possible, it is helpful to record for anywhere from 15-30 seconds before and after each distinct functional acquisition to capture subject-specific features of physiological data. 
 
Prior to the start of each distinct scan, the physiological recordings should be assessed for any data quality issues and fixed prior to the acquisition. Often this can occur from slightly misplaced or loose equipment caused by either subject movement or hardware malfunction. If you are not careful to ensure high quality in your data acquisition, then the signals you have taken the extra time and attention to collect will not be usable to model your MR data. 

## Cardiac pulsation
Cardiac pulsation can be collected using an optical technique called photoplethysmography (PPG) or electrocardiography (ECG), which records electrical activity.  

## PPG
PPG depends on the interaction between light and the circulation of blood through superficial- tissues (usually the fingertip) and is more robust to MRI interference.

PPG relies on the interaction of light with nearby tissues, using a light source and a photodetector placed on the fingertip (or ear lobe, toe, or other pulse point). The source (usually an infra-red or green LED) emits light towards the tissue and the photodetector captures the transmitted/reflected light (for transmissive and reflective sensor types, respectively). This allows us to monitor variations in blood circulation in shallow regions of tissue, since they affect the amount of light that is detected. Since the acquisition and transmission are conducted by optical fiber, the signal suffers less from MRI interference while scanning. These devices are typically included in the MRI scanner infrastructure. The data can thus be collected by the scanner, or recorded by a separate device.

The PPG waveform has a pulsatile and a non-pulsatile component.
The pulsatile component, also known as alternating current (AC),  of the PPG represents changes in blood volume which depend on the systolic and diastolic phases of the cardiac activity, being synchronized with the cardiac cycle.  The non-pulsatile component, sometimes referred to as the direct current (DC), is affected by tissue composition and blood volume, as well as other external factors, and is usually disregarded in this context. 

### Practice 1: Get to know your data (and the effect of your noise sources).
Prior to using a PPG device in the scanner it is helpful to visualize what a normal PPG signal might look like by testing on yourself. You may also mimic common noise scenarios such as finger twitching, movement, or an ill-fitting device so that you can anticipate issues during the scan. Once the subject is in the scanner, a continuous signal containing periodic features with clear peaks and troughs is expected. Typically the peaks of the cardiac pulsation trace are identified (e.g., the timing of each heart beat). The amplitude should be sufficient to detect peaks, and it should always be evaluated after each scan to ensure there is no need to reposition [QC_190522]  (see: https://www.biopac.com/knowledge-base/ppg-setup-and-calibration/).

### Practice 2: For PPG sensors secured by a strap, ensure it is not too loose or too tight.
When the strap is too loose, it may let ambient light in or reduce sensor contact with tissues, which would reduce thesensitivity of the measurements. Likewise, if the strap is too tight, it may lead to vasoconstriction, which would eventually result in a straight line signal. Moreover, it should be ensured that the subject does not experience any discomfort, which could affect the task performance, potentially induce motion and even lead to the need for repositioning the sensor later in the acquisition.
 
### Practice 3: Avoid motion and be consistent regarding sensor placement.
To avoid motion artifacts, when using a fingertip sensor, it is advisable to place the PPG sensor in the fingertip of a hand that is not going to move throughout the experiment (ex. not needed for button presses required by a task). The same finger of the same hand should be used for every subject if feasible, provided that there are no subject handedness constraints associated with the task that is being recorded. 

### Practice 4: Mitigate the effects of skin temperature and other factors on the PPG waveform.
A cold measurement site may be affected by vasoconstriction which reduces perfusion, likely degrading the signal quality. This may be addressed by massaging that site or employing other warming methods such as providing the subject with blankets during the scan, since these techniques have shown to be effective in increasing blood flow and improving signal quality. The posture of the subject may also contribute to variations in blood flow to the area of measurement. Additionally, note that skin pigmentation and, for finger sensors, any nail polish worn by the subject may also affect the measurement. 

**For an extensive review about PPG data (not specific to the MRI environment), see Park et al. (2022).**

## ECG
ECG is based on electrical activity and allows a reliable monitoring of cardiac cycle features.
ECG traces the potential change over the heart generated by the sinoatrial (SA) and atrioventricular (AV) nodes. It provides very precise beat-by-beat HR information. Depending on the system you are using and whether it is connected to another device (e.g., EEG cap), the electrodes can be placed on the chest or on the back of the subject. The ECG allows us to clearly monitor the entire QRS complex and cardiac cycle of the patient. 

Inside the MRI environment, the ECG will be distorted by magnetic induction and RF pulses.
It is important to note that like most signals, the ECG is susceptible to artifacts introduced by magnetic induction and RF pulses and to cardio-ballistic effects from the mechanical movement of the heart and flow of blood in the magnetic field that need to be cleaned appropriately after the scan (Kugel et al., 2003). Certain commercial devices have built in filters to suppress MRI-related artifacts; however, understanding what is real and noise in your signal is essential prior to using it for any kind of analysis (Abacherli, et al., 2005; Gray et al., 2009; Odille et al., 2007). 

### Practice 1: Prevent subject motion and optimize the experimental setup to avoid additional artifacts.
To best avoid motion artifacts you should ask the subject to remain as still as possible while in the scanner. Additionally, the conductive cables should be minimized in length, fastened well with tape to the body, and should never be looped. Visual inspection of proper peak detection is highly recommended to ensure that post-processed peak classification was not due to any residual artifact or signal distortion (Wong et al., 2011).

## PPG vs ECG		
Both PPG and ECG methods are commonly used by the neuroimaging community. In a recent meta-analysis of cardiac function and cortical thickness that pooled structural MRI and heart rate data from 20 research groups, half of the groups used PPG to estimate heart rate data; the other half, ECG (Koenig et al., 2021). Both ECG and PPG have strengths and weaknesses, however, and the choice between the two depends on investigators’ intended use of the data. Cardiac data can be useful in mitigating the effect of cardiac pulsations on the BOLD signal itself (i.e., for denoising fMRI data) or to investigate the neural correlates of cardiac function. For denoising concurrently collected fMRI data using approaches like RETROICOR (Glover et al., 2000) or DRIFTER (Särkkä et al., 2012), cardiac pulse estimates from either ECG or PPG can be used. In this case, PPG has the advantage as its sensor is easier to place and its signal is less susceptible to MR-induced artifacts (Caballero-Gaudes et al., 2017). In fact, the ECG pads may be more difficult to set-up (especially in female/pediatric populations) and the signal itself is more easily disrupted by MR-induced noise particularly when using multiband and multi-echo MR sequences. 

On the other hand, data from ECG and PPG are not equally well-suited to some assessments of the neural bases of cardiac function. While they provide nearly equivalent estimates of heart rate, PPG does not provide reliable estimates of heart rate variability (Jan et al., 2019; Mejía-Mejía et al., 2021; Schumann et al., 2021; Yuda et al., 2020) and ECG may be more suitable for reliably studying autonomic function [SETUP_170322]. Finally, while placement of a PPG sensor on the finger or foot is easier, quicker, and less invasive than that of electrodes on the thorax, PPG is susceptible to motion-induced noise (Lu et al., 2009), which is greater in some populations than others. **Altogether, the choice of PPG or ECG for cardiac monitoring should depend on the data’s intended use and the concomitant MR sequence** (Bottenhorn et al., 2021).

**MRI cardiac data** is another common method to capture the cardiac cycle and heart rate peaks. Most groups using this method of acquisition work with scanner vendors for collecting these data as they have existing methods and materials on how to best use their system. While no method is perfect, the claim of MR cardiac acquisition is to provide an ideal method to bypass scanner noise [SETUP_170322].

## Respiration: Ventilation 
 	
Breathing is typically monitored using a respiratory belt around the participant's chest/diaphragm. 
The belt may be rigid or elastic, using MR compatible strain transducers or pressure transducers to generate a signal proportional to the chest diameter. Often a belt is incorporated into the MRI scanner infrastructure, and this data can be collected by the scanner or recorded by a separate device. In some cases, respiratory sensors are already embedded into the scanner, and the respiratory trace may be obtained without the need for a respiratory belt. 

The positioning of the belt should be consistent and adapted to the participant’s breathing type.
The optimal positioning of the belt depends on the device being used, however it is best to be fairly consistent in how the belt is worn throughout a study. In some labs, multiple belts are used to better capture different types of breathing (e.g., "chest breathing" - thoracic versus "belly breathing" - abdominal). 

### Practice 1: Make sure to test the respiratory belt in the same configuration that will be used for the experiment! 
When used during fMRI, the breathing belt should be tested in the horizontal position, even if the preparation is performed while standing/sitting, since the supine position will likely be adopted throughout the whole scan and the breathing style or belt tightness may differ. 

Hopefully, your respiratory signal will look like a (unitless) sinusoid-like curve, with clear peaks and troughs.
After setting up the belt, a continuous sinusoidal shape is expected that should present clear peaks and troughs, corresponding to the subject’s specific breathing pattern. Usually, no standard units are used, and the metrics will rely on the relative changes between inhalation and exhalation. This will provide information about the breathing depth and frequency. Note that while belts are commonly referred to as capturing respiration, they are more aptly capturing ventilation via chest position.

### Practice 2: Look out for saturation! The respiratory belt may need an adjustment.
Before starting the experiment, the resting voltage of the respiration belt should be checked to assess the dynamic range [SETUP_170322]. The subject should be asked to take a full breath in and out. If the tip of the curve is flat, the signal is probably saturating and the position of the belt should be adjusted. If the belt is too tight or too loose, it is more likely to saturate and produce plateau in the recorded signal. Nevertheless, it has to be tight enough for the correct detection of peaks and troughs that will be needed afterwards [QC_190522]. For particularly thin subjects, adding a pad between the belt and the chest might be necessary to avoid saturation due to loosen belts. 

It is recommended that you are familiar with the values at which your belt saturates on both ends, as well as with the polarity of the recorded signal. This can be evaluated through trial and error when testing your equipment after purchase. Depending on the application, it may still be possible to work with imperfect data, even if the curve is slightly flat. Note that different types of belts might present different saturations.

### Practice 3: Get to know the limits of your subject.
For a sanity check, the normal breathing rate may be used as reference, since 10-20 breaths per minute, with each breath taking around 3 to 6 s, are expected. It is common for inhalation time to be faster than exhalation time. Note that certain clinical populations may have varied breathing rates, for example, faster breathing rates are expected for pediatric populations. Asking the subject to perform simple tests, such as holding their breath or following a paced breathing rhythm, will also ensure that the recording system is responding adequately [SETUP_170322].

If possible, give the subject some time for adaptation.
One should also bear in mind that the subjects may experience nervousness, especially if it is their first scan, which may cause hyperventilation at the beginning of the acquisition. If possible, they should have some time to adapt to the new environment or the experiment could start with a structural scan to leave some adaptation time before the first functional scan [QC_190522].

**ECG-derived respiration signal (EDR) - Get 2 for 1:** Respiration modulates the ECG, changing the morphology of the heartbeats and the electrical impedance of the thoracic cavity, due to filling/emptying of the lungs, and affecting the heart rate. Therefore, an ECG-derived respiration (EDR) may be obtained (Varon et al., 2020), which has already been tested in the MRI environment, showing the feasibility of using physiological models relying exclusively on ECG data to explain both respiratory and cardiac effects (Abreu et al., 2016).

## Respiration: Gas concentration
CO2 and O2 concentrations may influence the BOLD signal through vasodilation and vasoconstriction, respectively.
Information related to the level of blood gasses is also an important factor when analyzing fMRI data. An increase in arterial carbon dioxide (CO2) levels is known to have vasodilatory effects, driving large variability in blood flow and the BOLD signal (Birn et al. 2006, Wise et al. 2004). Although oxygen (O2) levels are known to have mild vasoconstrictive effects on the cerebrovasculature, these O2 levels can directly influence BOLD signal contrast (Bulte et al. 2007). 

**Surrogates of arterial pressures of carbon dioxide and oxygen may be obtained non-invasively.**
Arterial pressures of carbon dioxide and oxygen (PaCO2 and PaO2, respectively) can be measured directly through the invasive process of arterial sampling. Non-invasive approaches include measurement of the end-tidal pressure of carbon dioxide at the end of an exhalation and oxygen at the end of an inhalation (PetCO2 and PetO2) (Bengtsson et al. 2001, McSwain et al. 2010). These measurements are commonly used as surrogates of PaCO2 and PaO2 and are sampled with the use of a nasal cannula/face mask that is connected through a long tube to a gas analyser located in the control room. A nasal cannula is the simplest way to sample and/or monitor respiratory gasses. Consider using a nasal cannula with a mouth scoop to better capture mouth breathing. When using only a nasal cannula, be sure to instruct your subject to breath through the nose only [RESP_DATA_171122].

**Sampling of respiratory gasses can be performed in combination with the delivery of gasses, and this might lead to some issues/challenges when collecting and analyzing data. Given that delivery of gasses is not our focus, if you are interested in combining delivery and sampling of respiratory gasses, we recommend reading (Liu et al., 2019)**

### Practice 1: Ensure that the gas sampling lines and/or cords are long enough and secured to the floor, avoiding loops.
The distance between the control room and the scanner room should be measured beforehand to ensure the appropriate length of tubing and cords. Do not forget to take into account that during an acquisition the cannula will be placed on the nose/mouth of the subject and they will be inside the scanner bore when the acquisition starts. Since the length of the sampling lines will likely introduce a delay in the signals, the same length should be used for all acquisitions done with the same setup.

Moreover, the CO2/O2 traces may be noisier when tubes are hanging loose compared to laying on the floor. Furthermore, looping of cords can create eddy currents that increase noise, so they should be taped down or placed on hooks to keep them in place [SETUP_170322]. 

### Practice 2: Ensure proper setup of your gas analyzer.

Your gas analyzer may require calibration. Before starting your experiment, check your manufacturer’s recommendations on how and how often you should calibrate your system. There are different methods for this purpose, including using a closed chamber or placing a nasal cannula into the opening of the gas cylinder, and you may also need to get a gas sample with a specific concentration [SETUP_170322].  

When measuring gasses with several pumps, be sure to carefully balance all of them. In terms of gas analysis devices, these can be split into two different design groups based on the number of pumps per gas. There can be one pump per gas or one pump for all gasses. If two air pumps are connected to the same sample line, they must be carefully balanced, with all pumps having similar drawing power and no blockage being observed in any of the pump’s lines. 

In general, a sampling frequency of 100 Hz should be adequate. Regarding sampling frequencies, most acquisition systems sample at a default frequency (usually 1kHz) that is much higher than the normal respiration rate (~0.2Hz). A frequency of 100Hz should provide sufficient temporal resolution but, if necessary, this value might be decreased and still provide a good signal (e.g. 10Hz provides 50 to 100 points per breathing cycle).

### Practice 3: Check your data!

The CO2 trace should look like a rounded rectangle: the right vertice should be higher than the left and provide the end-tidal CO2 measurement.
When measuring blood gasses you should not see a sinusoidal wave as it might indicate too much vacuum or a sampling line that is too long. The exhalation should trigger a steep increase in CO2, followed by a very small increase that looks like a plateau. In fact, the waveform should be a good indicator for quality control. You should measure a moderately periodic curve and its frequency will be similar to that of the respiration signal, though the shape of the signal will be different for different gasses. A typical range for a CO2 trace is 35-45 mmHg. For more information, check Bulte and Wartolowska (2017) [QC_190522]. 

If your CO2 signal looks like a sinusoid, try to combine it with different data, for example the respiratory belt, and look for the same dynamic changes that you see with CO2 trace, to compare with and help understanding the recording (e.g. perform breath-holds and check the response). If not possible to use the CO2 at all, you may also consider to use the respiratory effort measured by the belt as a surrogate measure of PetCO2 (Zvolanek et al., NeuroImage, 2023) [RESP_DENOISING_210722]. 

**For additional information on using PetCO2 for cerebrovascular reactivity mapping, see Liu et al., 2017 and  Pinto et al. 2021.**

