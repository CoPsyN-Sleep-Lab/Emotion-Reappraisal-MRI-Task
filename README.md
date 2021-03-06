# Emotion-Reappraisal-MRI-Task
This repository contains the code and documentation for the Emotion Reappraisal Task adapted from McRae et al. 2012 and Minkel et al. 2012. It was adapted from Eprime to PsychoPy version by Kathleen O'Hora using PsychoPy version 1.8.3.

# Task Design
This task measures emotion reactivity and regulation based on the psychological principles of weakening and appraising negative emotional states. In short, participants are asked to look and respond naturally or decrease their emotional response to 30 negatively- and 15 neutrally- valanced images. Trials begin with a 2-second cue prompting them to either “LOOK” or “DECREASE”, followed by either a negative or neutral image presented for 7 seconds. In the LOOK conditions, participants look at the image and respond naturally. In the DECREASE condition, participants look at the picture and try to decrease negative affect. After the image is presented, participants rate their level of emotional negativity on a scale from 1 (not at all negative) to 5 (very much negative).  A 1-6s variable duration RELAX screen precedes the onset of the next trial. Images are presented in a pseudorandom order such that no more than two of the same instruction or 4 negative stimuli could be presented consecutively. Of the negative images, 15 are paired with the instruction “LOOK” and 15 are paired with the instruction to “DECREASE.” All 15 neutral images are presented with the instruction “LOOK.” Prior to entering the scanner, participants are given instructions on strategies for both the LOOK and DECREASE conditions and complete practice trials. Participants are asked to describe emotion regulation strategies after the scan to confirm proper strategies were used.

# Running the Task 
- Requirements: 
    - PsychoPy Version 1.8.3 
    - Mac OS Catalina or earlier (as of May 2021, the script does not support Big Sur)
    - Script runs best when it is saved locally instead of on Box
-  Instructions
   1. Open task in PsychopyPy 
   2. Press the Green "Run" button
   3. A window will pop up asking for participant ID and session. It is important to only enter numbers for the participant ID and session. For example, if the ID is TIRED001 and its baseline, enter 001 in ID and 1 for the session. 
   4. Press run to begin instructions

# How the Script Works
- Counterbalancing
  - The stimuli set and button box responses are counterbalanced based on participant ID and timepoint. This is why only integers can be entered for ID and timepoint
  - Stimuli Sets: 
    - Participants with ODD IDs will have stimuli set A at session 1 and stimuli set B at session 2. 
    - Participants with EVEN IDs will have stimuli set B at session 1 and stimuli set A at session 2. 
    - Practice stimuli is the same in every condition
  - Buton Box Response: 
    - All participants will rate the images on a 5-point scale using the 5-button button box in their dominant hand but, which button represents which response will be counterbalanced.
    - Participants with ODD IDs will have the Thumb button correspond to one and the Pinky respond to five at both sessions.
    - Participants with EVEN IDs will have the Pinky button correspond to one and the THinb respond to five at both sessions.
    - In the task, this is represented in the image of the scale. The script will show different scale images based on the ID. One will say "(pinky)" under the number 1 and "(thumb)" under the number 5. The other scale will say "(thumb)" under the number 1 and "(pinky)" under the number 5. 
- Routines
  - The script is organized into "Routines" for each phase of the task. The routines are: 
  1. Instructions
    - This routine shows the first set of task instructions before the practice trials
  3. Countdown
    - This routine contains the 3,2,1 countdown before the task begins
  5. CueRoutine
    - This routine presents the fixation cross and Cue Text (either LOOK or DECREASE)
  7. Trial
    - This routine presents the image, rating scale, rating instructions, and button response
  9. Relax
    - This routine contains the RELAX screen after each individual trial. This also contains a jittered time interval
  11. Instructions2
    - This routine contains text after the practice trials asking if there are any questions about the task and the key response 's' to continue the task.
  13. Trigger
    - This routine contains the 'Get Ready' text and key response 's' to trigger the scanner. The cni_trigger() function is in this routine.
  14. Well Done
    - This routine contains the screen with the Well Done text at the end of the task.
  - The order of routines is: Instructions, countdown, CueRoutine, Trial, Relax, Instructions2, Trigger, Countdown, CueRoutine, Trial, Relax, Well Done
- Stimuli order and sets 
  - The script gets information about the stimuli, stimuli location, cue, and inter-stimulus-interval (for RELAX screen) from .csv files that are saved in the stimuli_order folder. 
  - There are seperate files for practice stimuli, stimuli set A, and stimuli set B. 
  - The script reads these csv files in the order they are presented in the file. There is no randomization within sessions. So, stimuli sets will be presented in the same order for each participant. This means the first cue and image in Set A will always be the same. Each image will have the same cue assigned to it every run. 
  - The script pre-loads all images before the trial to improve timing
# Task Components: 
Component Name |Type| Description
------------ | ------------- | -------------
Instructions1 | Text object | First instruction screen: 'You will be shown a series of photos. Before each photo, you will be instructed to either LOOK or DECREASE', 
instructions2 | Text Object | Second instruction screen: 'When you see the word LOOK, \nlook at the picture and react naturally'
Instructions3 | Text Object | Third instruction screen: 'When you see the word DECREASE, \nthink about the picture in a way to decrease any negative feelings'
Instructions4 | Text Object | Fourth instruction screen: 'After each photo, you will be asked to rate how negative you feel on a scale of 1 to 5 like this:\n\n\n\n\n\n',
text | Text Object | Fifth instruction screen: 'Press the button on the button box that corresponds with your choice'
text_2 | Text Object | Sixth instruction screen: 'When you see the word RELAX, you can rest until the next trial begins'
text_3 | Text Object | Seventh instruction screen: "Let's practice!\n\nReady to begin? "
Countdown_5 | Text Object | Number 5 in the countdown before begininng trail
Countdown_4 | Text Object | Number 4 in the countdown before begininng trail
Countdown_3 | Text Object | Number 3 in the countdown before begininng trail
countdown_2 | Text Object | Number 2 in the countdown before begininng trail
Countdown_1 | Text Object | Number 1 in the countdown before begininng trail
Rating_inst | Text Object | Text shown during rating 
text_4 | Text object | RELAX text
Task_Instructions | Text Object | 'Do you have any questions before we begin? '
trigger_text | Text Object | Text shown while waiting for trigger: 'Get Ready!'
well_done | Text Object | Text for end screen: 'Well Done!'
scale | Image Object | Image of rating scale shown during instruction screen 5.
FixationCross1 | Image Object | Image of fixation cross
ImageCue1 | Text Object | Text for the cue before image (look vs. decrease)
Scale2 | Image Object | Image of rating scale shown during trials. Image shown is dependent on ID entered
emotion_image | Image Object | Image of stimuli for each trial. Each image is a component of the list emotion_image_cache (emotion_image_cache[Picture])
key_resp | Response Object | Allows a key response during rating screen (The actual key response is saved as **theseKeys**. The rating that the key response corresponds to is **key_resp_rev**
key_resp_start | Response Object | Allows for key response during Task_Instructions. If key 's' is pressed, experiment advances
key_resp_2 | Response Object | Allows for key response for trigger during the Get Ready screen. If key 's' is pressed, experiment advances and scanner is triggered. 



# How Data is Logged
- There are two output files in the 'data' folder that contain information about the experiment:
  1. .log File
    - Logs information about the experiment such as key presses, timing of each screen, and experiment information
    - Difficult to read, but we use a parsing script that pulls out relevant information for the data analysis
    - Used for data analysis
    - Autologging is turned on at the experiment level. See troubleshooting guide for more information on autologging. 
    - Includes variable **key_resp_rev**, which is coded as 'rating= XX." This variable is the participant's rating for each trial. The rating is properly coded according to counter balancing. A rating of 0 signifies that the participant did not respond.
  2. .csv File
    - Logs information about key press, timing of stimuli etc. 
    - Easy to read, so can be used for data quality checks immediately after running the task. 
    - Not used in data analysis
# How to Read the Output of Parser Script
- Syntax: 
    - stimulus.COMPONENT.on and stiumulus.COMPONENT.off: time each component started/stopped
    - key.time: time that the key response started. In other words, the time the participant could have made a key response 
    - key.rt: the reaction time of the key response- how long it took to press the button
    - trial.Picture: filename of the image shown (taken from stimuli list)
    - trial.Cue: Type of cue shown (look vs. decrease; taken from stimuli list)
    - trial.ISI: The interstimulus interval for trial. This is also the duration of the Relax screen.  (taken from stimuli list)
    - trial.Valence: Valance rating for image of that trial (taken from stimuli list)
    - trial.Type: type of image (negative vs. neutral; taken from stimuli list))

# Stimuli Characteristics and Presentation
All images in this task were taken from the International Affective Picture System (IAPS) and are stored in the img/iaps folder.
- Timings 
  - Countdown= 1s for each number
  - Fixation Cross = 2s
  - Cue = 2s
  - Image = 7s
  - Rating = 4s
  - Relax = 1-6s jittered duraiton (mean for each set: A=1.862 B=2.33s)
  - Total task time= 
- Stimuli sets were created using the exact images in the original Eprime task. Mean valance was matched between stimuli sets 
  - Average Valence set A: 3.12
  - Average Valence set B: 3.08
- Sizes: 
  - Instruction text: 
  - Cue text: 
  - Relax text: 
  - Images: 1024 x 768 pixels (recommended size by IAPS, but unclear if this is optimal for scanner)

# What is in the Task Folder/Repo?
- **emo_reg.py** is the main script for the task
- **get_usb.py** is a script for a function that finds a USB device. This file is called in the main script and must be in the same folder as the **emo_reg.py** file. 
- **siteConfig.yaml** contains the configuration informaiton for the monitor at CNI. This file is called in the main script and must be in the same folder as the **emo_reg.py** file. 
- The **img** folder contains all the images used for the task including: 
  - Images of rating scales
  - Fixation cross
  - iaps folder containing all stimuli
 - The **stimuli_order** folder contains the csv files for identifying the stimuli, stimuli order, cue, and inter-stimulus-interval for each sitmulus set.
  - **StimuliListA.csv** and **StimuliListB.csv** contain columns for image name, cue (LOOK vs. DECREASE), valence, image typre (negative vs. neutral), and inter-stimulus-interval for each trial within each Stimuli Set. 
  - **practiceStimuliList.xlsx** contains the image name, cue, and inter-stimulus-interval for practice trials.
  - **StimuliList061820.csv** is a file that contains information for all stimuli used in the the task.
- The **data** folder contains all log and csv files from each run of the task. The files are organized by date and record ID. 

# What is in the Event-Related Reapp Task Box Folder?
- The **Instructions** Folder contains files with the original task instructions (from Eprime task)
- The **Papers** folder contains pdfs of useful papers for the task:
    - *McRae 2012* and *Minkel 2012* are the papers this task was adapted from. *Minkel 2012* was used in a scanner, so it was used to guide scanning-related aspects of task.
    - *Redies 2020* reports about stimulus size in IAPs compared to other image sets and recommendations for experiments
    - *Bradley 2001* is a paper from the IAPs group about affective response to pictures
- The **Original Task and Stimuli** folder contains the original Eprime files and stimuli files from the McRae paper
- The **IAPS_Stimuli_2020** folder contains all images downloaded from the IAPS database
- The **EmoReappTask.psyexp** file is the PsychoPy Experiment Builder (GUI) file originally used as the basis of the task script in the coder. 
