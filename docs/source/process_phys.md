# 5. Working with Physiological Data
Ideally, you have recorded physiological data throughout the entire scan session and trigger data to identify when scanning occurred. Furthermore, depending on the time of physiological and neuroimaging signals that you collected, you may have to account for possible delays between them, both technical and physiological.

It is useful to organize and standardize the format of your physiological data files along with any neuroimaging files acquired concurrently. Phys2bids can be used to organize the various physiological data traces that you have collected. With this tool, your data will have the appropriate BIDS labels to describe physiological information. As a sanity check, you may quickly inspect the phys2bids output plot when called with the `-info` flag to ensure that it matches the type of information and the period you aimed to collect.

After this restructuring of the data, there are numerous tools available to process each type of physiological trace, for instance, identifying end-tidal values for O2 and CO2, or phases of the cardiac and respiratory cycles. These data are then further processed via smoothing or convolution to create physiological regressors.

In the subsections below, you may find a summary detailing the various methods and guidelines related to the utilization of cardiac and respiratory (ventilation and gas concentration) data in the context of fMRI signals. Each method is accompanied by a description and a brief discussion of its pros and cons. Data-driven methods not based on the measurement of peripheral physiology are presented in a different section.

In summary, several models and methods exist for analyzing the effects of cardiac pulsation and respiration (ventilation and/or gas concentration) on fMRI signal changes. Each approach has its strengths and limitations, ranging from specific denoising capabilities to the complexity of calculations and the need for manual peak detection. Researchers should carefully select and validate the appropriate approach based on their specific research questions and the characteristics of their data. 

## Cardiac pulsation 
Cardiac contractions can influence fMRI signals due to the pulsatility generating small movements in brain tissue as well as inflow effects in and near blood vessels. These cardiac pulsation phenomena localize in tissue regions close to large arteries and draining veins, such as the sagittal sinus or the circle of Willis, as well as the edges of the brain and sulci (Bhattacharyya and Lowe, 2004, Dagli et al., 1999, Glover et al., 2000).

### Model-based approaches
* RETROICOR (Retrospective Image Correction) and phase-based models
    * About: this method relies on modeling cardiac (and respiratory) phases based on the recorded cardiac data, accounting for quasi-periodic patterns using a low-order Fourier series (Glover et al., 2000). It is a more specific denoising approach than others. 
    * Cons: Slice-wise regressors are more complicated to deal with and sometimes have a more negligible effect than other correction techniques. 
    * Note: Other phase-based algorithms have expanded from RETROICOR as described in Caballero-Gaudes and Reynolds 2017. One such extension is DRIFTER (Särkkä et al., 2012). 

* Cardiac Rate (CR) and peak-based models
    * About: accounting for cardiac-related variability may improve the reliability of fMRI analysis, since low-frequency cardiac rate fluctuations have been shown to explain BOLD signal variance (Shmueli et al., 2007).This may be performed by using time-shifted cardiac rate regressors (across a range of delays) and/or by convolving a cardiac rate time-course with the cardiac response function (CRF) (Chang et al., 2009). Usually, the peak detection step employed to compute the cardiac rate may be done using either the EEG (heart rate) or the ECG (pulse rate).
    * Cons: peak-based models are dependent on the quality of the peak detection. Moreover, the established CRF may not hold for all population types or tasks. Furthermore, since heart rate variability (HRV) is closely linked to autonomic function, it may also covary with the functional connectivity of regions involved in arousal (Chang et al., 2013). Therefore, regressing out heart rate- based time-courses should be done cautiously, as it may remove signals of interest and not only non-neuronal information.

## Respiration: Ventilation
**There are three primary ways by which breathing can influence the fMRI signals:**  
1. Breathing often leads to **bulk motion** of the body and head, leading to undesired artifacts in the images. To mitigate these effects, volume registration and motion correction algorithms are typically employed during data preprocessing (Brosch et al. 2002). 
2. Breathing changes the **chest position** which can influence the success of the shim, continuously changing **B0 homogeneity** throughout the scan and in turn affecting signal amplitude (Brosch et al. 2002, Raj et al. 2001). These effects are also modeled using techniques like RETROICOR.
3. **Changes in breathing rate and depth can affect the levels of blood gasses**, such as oxygen and carbon dioxide, which can in turn drive vasodilation or vasoconstriction. These vascular changes have a substantial impact on the amplitude of the fMRI signal (Chang and Glover 2009). Respiratory volume per time (RVT) correction (Birn et al. 2008) estimates the change in breathing rate/depth to model these effects.

### Model-based approaches [RESP_DENOISING_210722] 
* RETROICOR (Retrospective Image Correction) and phase-based models
    * About: RETROICOR offers a more specific denoising approach compared to other methods and is complementary to measures such as CO2 (carbon dioxide), RV (respiration volume), and RVT (respiration volume per time) estimations. As this method treats each pixel separately, it has the advantage of preventing the artificial coupling of noise corrections across signal regions. 
    * Cons: one drawback of RETROICOR is that slice-wise regressors can be more complicated to handle, and their effects may sometimes be negligible.

* Respiratory volume per time (RVT) and peak-based models
    * About: RVT and peak-based models utilize peak detection on the respiratory trace to estimate the rate and depth of breaths, which enables an indirect estimation of gas volume exchange (Birn et al., 2006). These models rely on a respiratory response function (RRF) derived from empirical observations, considering inter-individual differences (Birn et al., 2008). They are advantageous in capturing time-delayed effects interacting with CO2 levels. 
    * Cons: peak detection in these models may require manual effort, and efforts should be made to automate this process.

* Respiration variation (RV) and other models (standard deviation/signal property based)
    * About: RV (standard deviation of the respiratory trace over a window) (Chang and Glover, 2009) and other signal property-based models such as ENV (envelope of the respiratory trace over a window) (Power et al., 2018) provide an alternative to RVT-based approaches. These models do not rely on peak detection, reducing the need for manual intervention.
    * Cons: they are more susceptible to biases introduced by noise, which can affect the accuracy of the analysis.

## Respiration: Gas concentration
Importantly, the respiratory signals sampled show the fluctuations in CO2 and O2 occurring during each breathing cycle. In order to **retrieve the corresponding end-tidal signals** it is necessary to perform some processing. Most of the processing steps are performed using in-house algorithms and highly dependent on the goal of the experiment. Nevertheless, there are steps that are commonly performed in most experiments, such as extracting the end-tidal points from the respiratory trace collected. This can be performed by identifying the **lowest point per breath from the oxygen trace** and the **highest point per breath of the CO2 trace.** 

Afterwards, it is necessary to adjust this trace for the **sampling delay.** Every gas analysis system will have its own sampling delay, mainly determined by the length of the sampling line used and the power of the pump pulling the gas into the analysis device. The simplest way of estimating this delay is to use a **breath-hold task** (e.g. “breathe in”, “breathe out”, “breathe in and hold your breath”), set a marker (before the “hold your breath” cue) and measure the corresponding respiratory order to identify the delay between the marker and the expected respiratory signal changes (increase due to the “breathe in'' cue and decrease due to the “hold your breath” cue). In order for this trace to be used as a regressor, it is also necessary to **interpolate the end-tidal points and downsample the time course to match the fMRI resolution.** 

## Data-driven approaches for accounting for cardiac and respiratory effects
### Cardiac Pulsation
* Principal Component Analysis (PCA)
    * About: Defining multiple spatially uncorrelated nuisance regressors based on the principal component analysis (PCA) decomposition of voxels where no BOLD fMRI signals of neuronal origin are expected to originate (e.g., WM and CSF). The widely-used CompCor approach (Behzadi et al., 2007; Muschelli et al., 2014) defines multiple nuisance regressors from the principal components (PCs) of voxels within WM and CSF in the ventricles.
    * Cons: An important question for debate is how many principal components (PCs) must be considered in the model. 
* Independent Component Analysis (ICA)
    * About: Once the ICA is computed, the basis of these denoising approaches is to first distinguish between independent components (IC) arising from neuronal-related BOLD signal and ICs related to noise sources, and then remove the latter before reconstructing the dataset (Beckmann, 2012, McKeown et al., 2003).
    * Cons: Manual classification of ICs is very time consuming, difficult to reproduce and requires expertise (Kelly Jr. et al., 2010). Automatic classification does help, however, it could mis-classify components and again, it is difficult to discern the number of components you need.
* Global Signal Regression (GSR)
    * About: Removes the average fMRI signal across all the voxels in the brain under the assumption that the global signal mainly represents all the processes that confound the BOLD fMRI signals, including all instrumental, motion-related and physiological fluctuations.
    * Cons: Use of GSR has always been debated since the global signal also includes neuronal-related BOLD fluctuations.
### Respiration: Ventilation
* Respiratory effects may also be accounted for by using image-based data-driven methods, by extracting CSF and white matter time courses as regressors of no interest or by decomposing the data using PCA or ICA to find respiration-related components. More recently, machine learning and deep learning models are also being applied to infer respiratory information based on fMRI spatiotemporal patterns (Bayrak et al., 2020; Addeh et al., 2023).

