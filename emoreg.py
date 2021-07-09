#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.2),
    on Tue Aug 18 16:34:00 2020
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import NOT_STARTED, STARTED, FINISHED
from psychopy.visual import window

import os  # handy system and path functions
import sys  # to get file system encoding
import time
import serial
import re
from glob import glob
from os.path import basename, dirname, join

from get_usb import get_usb

# FIXME: please use `git` and `github` instead of adding date tags to files!!!
# This is huge I can't express this enough.  You want 100% confidence that the same
# stimuli was run through the whole study.  And if you make any changes you want that
# tracked as well as the date it was implemented.
# Please reach out if git advice

# Ensure that relative paths start from the same directory as this script
_thisDir = dirname(os.path.abspath(__file__))
img_dir = join(_thisDir, "img")
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '1.83.04'
expName = "emo_reg"  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '1'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion
subj_id = expInfo['participant']
session = expInfo['session']

import unicodedata
subj_id = unicodedata.normalize('NFKD', subj_id).encode('ascii', 'ignore')
print(type(expInfo['session']))
# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
odd = False
num_id = re.findall(r'\d+', subj_id)
if int(num_id[0])%2 ==1:
    odd = True
    filename = _thisDir + os.sep + u'data/%s_%s_%s_%s' % (subj_id, session, expName, expInfo['date']) #+ '_1thumb')
else:
    filename = _thisDir + os.sep + u'data/%s_%s_%s_%s' % (subj_id, session, expName, expInfo['date'] )#+ '_5thumb')


# FIXME: deleted ExperimentHandler here
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/apple/Box/Kathleen OHoras Files/CoPsyN Sleep Lab/LUNA Study/Study Materials/MRI Tasks/Event-related reapp task/emoreg_patrick/emoreg.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename, autoLog = True)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation
## Create window based on the site config .yaml file
import pyglet
display = pyglet.window.get_platform().get_default_display()
screens = display.get_screens()
resolution = [screens[-1].width, screens[-1].height]
import yaml
from psychopy import monitors
if not os.path.exists('siteConfig.yaml'): raise IOError('Missing siteConfig.yaml - Please copy configuration text file')
with open('siteConfig.yaml') as f:
    config = yaml.safe_load(f)
mon = monitors.Monitor('newMonitor')
mon.setWidth(config['monitor']['width'])
mon.setDistance(config['monitor']['distance'])
mon.setSizePix(resolution)

# Setup the Window
win = visual.Window(
    size=resolution, fullscr=True, screen=config['monitor']['screen'], 
    #winType='pyglet', 
    allowGUI=False, allowStencil=False,
    monitor=mon, color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='deg')

# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
    logging.exp('frame duration: {}'.format(frameDur))
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess
    logging.exp('frame duration was guessed: {}'.format(frameDur))
    logging.flush()
    #raise IOError('Frame duration could not be reliably measured! Please close the other windows on the computer and try again!')
if frameDur >= 0.020:
    logging.exp('Frame Rate Too Slow for Subliminal Stimuli!: {}'.format(frameDur))
    logging.flush()
    #raise IOError('Frame Rate Too Slow for Subliminal Stimuli! Please close the other windows on the computer and try again!')

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
logging.exp('Task Started at: {}'.format(core.getAbsTime())) #Log the task start time
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine

###### Triggering ######
#SCANNER_TRIGGER_NEEDED = False
DEVICE_ID = get_usb() # FIXME: don't trigger yet!

def cni_trigger():
    try:
        ser = serial.Serial(DEVICE_ID, 57600, timeout=1)
        time.sleep(.5)    ### wait for 2 sec to ensure scanner is ready; CNI wiki default 0.1
        logging.exp('Trigger Sent: {}'.format(globalClock.getTime()))
        ser.write(str.encode('[t][t][t]\n'))
        logging.exp('Trigger Connection Closed: {}'.format(globalClock.getTime()))
        ser.close()
        scannerClock.reset()
    except Exception as err:
        print(str(err))
        if not SCANNER_TRIGGER_NEEDED:
            pass
        else:
            core.quit()

########################

# Initialize components for Routine "Instructions"
# FIXME: some of these sizes might want to be set as variables
InstructionsClock = core.Clock()
Instructions1 = visual.TextStim(win=win, name='Instructions1',
    text='You will be shown a series of photos. Before each photo, you will be instructed to either LOOK or DECREASE',
    font='Arial',
    pos=(0, 0), height=2, wrapWidth=38, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    depth=0.0);
instructions2 = visual.TextStim(win=win, name='instructions2',
    text='When you see the word LOOK, \nlook at the picture and react naturally',
    font='Arial',
    pos=(0, 0), height=2, wrapWidth=38, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    depth=-1.0);
Instructions3 = visual.TextStim(win=win, name='Instructions3',
    text='When you see the word DECREASE, \nthink about the picture in a way to decrease any negative feelings',
    font='Arial',
    pos=(0, 0), height=2, wrapWidth=38, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    depth=-2.0);
Instructions4 = visual.TextStim(win=win, name='Instructions4',
    text='After each photo, you will be asked to rate how negative you feel on a scale of 1 to 5 like this:\n\n\n\n\n\n',
    font='Arial',
    pos=(0, 0), height=2, wrapWidth=38, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    depth=-3.0);
#show correct scale from counterbalancing based on record ID
#counter balancing fingers used for scale in scale image, define if odd ID 

if odd:
    Scale = visual.ImageStim(
        win=win,
        name='Scale',
        image=join(img_dir, 'scale.png'),
        mask=None,
        ori=0, pos=(0, -3), size=(40, 11),
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-3.0)
else:
    Scale = visual.ImageStim(
        win=win,
        name='Scale',
        image=join(img_dir, 'scale2.png'),
        mask=None,
        ori=0, pos=(0, -3), size=(40, 11),
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-3.0)

text = visual.TextStim(win=win, name='text',
    text='Press the button on the button box that corresponds with your choice',
    font='Arial',
    pos=(0, 0), height=2, wrapWidth=38, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    depth=-5.0);
text_2 = visual.TextStim(win=win, name='text_2',
    text='When you see the word RELAX, you can rest until the next trial begins',
    font='Arial',
    pos=(0, 0), height=2, wrapWidth=38, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    depth=-6.0);
text_3 = visual.TextStim(win=win, name='text_3',
    text="Let's practice!\n\nReady to begin? ",
    font='Arial',
    pos=(0, 0), height=2, wrapWidth=38, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    depth=-7.0);
# Initialize components for Routine "Countdown"
CountdownClock = core.Clock()
Countdown_5 = visual.TextStim(win=win, name='Countdown_5',
    text='5',
    font='Arial',
    pos=(0, 0), height=3, wrapWidth=38, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    depth=0.0);
Countdown_4 = visual.TextStim(win=win, name='Countdown_4',
    text='4',
    font='Arial',
    pos=(0, 0), height=3, wrapWidth=38, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    depth=0.0);
Countdown_3 = visual.TextStim(win=win, name='Countdown_3',
    text='3',
    font='Arial',
    pos=(0, 0), height=3, wrapWidth=38, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    depth=0.0);
countdown_2 = visual.TextStim(win=win, name='countdown_2',
    text='2',
    font='Arial',
    pos=(0, 0), height=3, wrapWidth=38, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    depth=-1.0);
countdown_1 = visual.TextStim(win=win, name='countdown_1',
    text='1',
    font='Arial',
    pos=(0, 0), height=3, wrapWidth=38, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    depth=-2.0);

# Initialize components for Routine "CueRoutine"
CueRoutineClock = core.Clock()
FixationCross1 = visual.ImageStim(
    win=win,
    name='FixationCross1', 
    image=join(img_dir, 'fixation.png'),
    mask=None,
    ori=0, pos=(0, 0), size=(15, 15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
ImgCue1 = visual.TextStim(win=win, name='ImgCue1',
    text='default text',
    font='Arial',
    pos=[0,0], height=4, wrapWidth=38, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    depth=-1.0);

# Initialize components for Routine "Trial"
TrialClock = core.Clock()

# set up handler to look after randomisation of conditions etc
# We move this up here to avoid any timing impact from loading conditions from disk.
practice_stimuli = join(_thisDir, "stimuli_order", "practiceStimuliList.xlsx")
Practicetrials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(practice_stimuli, selection='0:5'),
    seed=None, name='Practicetrials')

# Creates Counter Balancing  of Stimuli Sets
# set up handler to look after randomisation of conditions etc
stimuli_order = "stimuli_order"
listA = "StimuliListA.csv"
listB = "StimuliListB.csv"
study_stimuliA = join(_thisDir, stimuli_order, listA)
study_stimuliB = join(_thisDir.encode('UTF-8'), stimuli_order.encode('UTF-8'), listB.encode('UTF-8'))
if odd and int(expInfo['session']) ==1:
    study_stimuli= study_stimuliA
elif not odd and int(expInfo['session']) ==1:
    study_stimuli= study_stimuliB
elif odd and int(expInfo['session'])==2:
    study_stimuli= study_stimuliB
else:
    study_stimuli= study_stimuliA

StudyTrials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    # FIXME: don't like selection!
    trialList=data.importConditions(study_stimuli, selection='0:45'),
    seed=None, name='StudyTrials')

# We preload all images to avoid performance issues during display.
# We load the images into two different caches to avoid any issues with the `name` kwarg for the ImageStim.
emotion_image_cache = {}
for image_path in glob(join(img_dir, "iaps", '*.jpg')):
    short_name = join(basename(image_path))
    emotion_image_cache[short_name] = visual.ImageStim(
        win=win, name='emotion_image',
        image=image_path, mask=None, # FLAG why not 'sin'
        ori=0, pos=[0, 0], size=[512, 384], units='pix', 
        color=[1, 1, 1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=0.0) 
# Now that images and other things are loaded, we record frames.

win.recordFrameIntervals = True
win.refreshThreshold = frameDur + 0.004
# HACK we increase the number of dropped frames that need to be reported
# to more easily monitor rendering issues.
window.reportNDroppedFrames = 300
space = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='space')
Rating_inst = visual.TextStim(win=win, name='Rating_inst',
    text='default text',
    font='Arial',
    pos=[0,0], height=2, wrapWidth=38, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    depth=-1.0);

#counter balancing fingers used for scale in scale image: 
if odd:
    Scale2 = visual.ImageStim(
        win=win,
        name='Scale2',
        image=join(img_dir, 'scale.png'),
        mask=None,
        ori=0, pos=(0, -3), size=(40, 11),
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-3.0)
else:
    Scale2 = visual.ImageStim(
        win=win,
        name='Scale2',
        image=join(img_dir, 'scale2.png'),
        mask=None,
        ori=0, pos=(0, -5), size=(25, 6.5),
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-3.0)

# Initialize components for Routine "Relax"
RelaxClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='default text',
    font='Arial',
    pos=[0,0], height=2, wrapWidth=38, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    depth=0.0);

# Initialize components for Routine "Instructions_2"
Instructions_2Clock = core.Clock()
Task_Instructions = visual.TextStim(win=win, name='Task_Instructions',
    text='Do you have any questions before we begin? ',
    font='Arial',
    pos=(0, 0), height=2, wrapWidth=38, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    depth=0.0);

# Initialize components for Routine "Trigger"
TriggerClock = core.Clock()
trigger_text = visual.TextStim(win=win, name='trigger_text',
    text='default text',
    font='Arial',
    pos=[0,0], height=2, wrapWidth=38, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    depth=0.0);


### Set SCANNER_TRIGGER_NEEDED to False to bypass program abortion when scanner exception is thrown


# Initialize components for Routine "Relax"
RelaxClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='default text',
    font='Arial',
    pos=[0,0], height=2.5, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    depth=0.0);

#Initialize components for Routine Well Done
well_doneClock = core.Clock()
well_done = visual.TextStim(win=win, name='well_done',
    text="Well Done!",
    font='Arial',
    pos=(0, 0), height=2, wrapWidth=38, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    depth=-7.0);

#Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instructions"-------
t = 0
InstructionsClock.reset()  # clock
frameN = -1
# update component parameters for each repeat
# keep track of which components have finished
InstructionsComponents = [Instructions1, instructions2, Instructions3, Instructions4, Scale, text, text_2, text_3]
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# reset timers
t = 0
InstructionsClock.reset()
frameN = -1
INSTRUCTIONS_TIME = [0, 7, 14, 21, 28, 35, 42, 49, 56]

# -------Run Routine "Instructions"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *Instructions1* updates
    if Instructions1.status == NOT_STARTED and t>= INSTRUCTIONS_TIME[0]:
        # keep track of start time/frame for later
        Instructions1.tStart = t  # local t and not account for scr refresh
        Instructions1.frameNStart = frameN  # exact frame index
        Instructions1.setAutoDraw(True)
    if Instructions1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if t>=INSTRUCTIONS_TIME[1]:
            # keep track of stop time/frame for later
            Instructions1.tStop = t  # not accounting for scr refresh
            Instructions1.frameNStop = frameN  # exact frame index
            Instructions1.setAutoDraw(False)

    # *instructions2* updates
    if instructions2.status == NOT_STARTED and t >= INSTRUCTIONS_TIME[1]:
        # keep track of start time/frame for later
        instructions2.tStart = t  # local t and not account for scr refresh
        instructions2.frameNStart = frameN  # exact frame index
        instructions2.setAutoDraw(True)
    if instructions2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if t >= INSTRUCTIONS_TIME[2]:
            # keep track of stop time/frame for later
            instructions2.tStop = t  # not accounting for scr refresh
            instructions2.frameNStop = frameN  # exact frame index
            instructions2.setAutoDraw(False)

    # *Instructions3* updates
    if Instructions3.status == NOT_STARTED and t >= INSTRUCTIONS_TIME[2]:
        # keep track of start time/frame for later
        Instructions3.frameNStart = frameN  # exact frame index
        Instructions3.tStart = t  # local t and not account for scr refresh
        Instructions3.setAutoDraw(True)
    if Instructions3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if t >= INSTRUCTIONS_TIME[3]:
            # keep track of stop time/frame for later
            Instructions3.tStop = t  # not accounting for scr refresh
            Instructions3.frameNStop = frameN  # exact frame index
            Instructions3.setAutoDraw(False)

    # *Instructions4* updates
    if Instructions4.status == NOT_STARTED and t >= INSTRUCTIONS_TIME[3]:
        # keep track of start time/frame for later
        Instructions4.frameNStart = frameN  # exact frame index
        Instructions4.tStart = t  # local t and not account for scr refresh
        Instructions4.setAutoDraw(True)
    if Instructions4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if t >= INSTRUCTIONS_TIME[4]:
            # keep track of stop time/frame for later
            Instructions4.tStop = t  # not accounting for scr refresh
            Instructions4.frameNStop = frameN  # exact frame index
            Instructions4.setAutoDraw(False)

    # *Scale* updates
    if Scale.status == NOT_STARTED and t >= INSTRUCTIONS_TIME[3]:
        # keep track of start time/frame for later
        Scale.frameNStart = frameN  # exact frame index
        Scale.tStart = t  # local t and not account for scr refresh
        Scale.setAutoDraw(True)
    if Scale.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if t >= INSTRUCTIONS_TIME[4]:
            # keep track of stop time/frame for later
            Scale.tStop = t  # not accounting for scr refresh
            Scale.frameNStop = frameN  # exact frame index
            Scale.setAutoDraw(False)

    # *text* updates
    if text.status == NOT_STARTED and t >= INSTRUCTIONS_TIME[4]:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if t >= INSTRUCTIONS_TIME[5]:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            text.setAutoDraw(False)

    # *text_2* updates
    if text_2.status == NOT_STARTED and t >= INSTRUCTIONS_TIME[5]:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.setAutoDraw(True)
    if text_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if t >= INSTRUCTIONS_TIME[6]:
            # keep track of stop time/frame for later
            text_2.tStop = t  # not accounting for scr refresh
            text_2.frameNStop = frameN  # exact frame index
            text_2.setAutoDraw(False)

    # *text_3* updates
    if text_3.status == NOT_STARTED and t >= INSTRUCTIONS_TIME[6]:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.setAutoDraw(True)
    if text_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if t >= INSTRUCTIONS_TIME[7]:
            # keep track of stop time/frame for later
            text_3.tStop = t  # not accounting for scr refresh
            text_3.frameNStop = frameN  # exact frame index
            text_3.setAutoDraw(False)

    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "Countdown"-------
t = 0
CountdownClock.reset()  # clock
frameN = -1
#update component parameters for each repeat
#keep track of which components have finished
CountdownComponents = [Countdown_3, countdown_2, countdown_1]
for thisComponent in CountdownComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
#reset timers
t = 0
CountdownClock.reset()  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Countdown"-------
while continueRoutine:
    # get current time
    t = CountdownClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Countdown_3* updates
    if t >= 0.0  and Countdown_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        Countdown_3.frameNStart = frameN  # exact frame index
        Countdown_3.tStart = t  # local t and not account for scr refresh
        Countdown_3.setAutoDraw(True)
    if Countdown_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if t >= 1.0 :
            # keep track of stop time/frame for later
            Countdown_3.tStop = t  # not accounting for scr refresh
            Countdown_3.frameNStop = frameN  # exact frame index
            Countdown_3.setAutoDraw(False)
    
    # *countdown_2* updates
    if t >= 1.0 and countdown_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        countdown_2.frameNStart = frameN  # exact frame index
        countdown_2.tStart = t  # local t and not account for scr refresh
        countdown_2.setAutoDraw(True)
    if countdown_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if t >= 2.0 :
            # keep track of stop time/frame for later
            countdown_2.tStop = t  # not accounting for scr refresh
            countdown_2.frameNStop = frameN  # exact frame index
            countdown_2.setAutoDraw(False)
    
    # *countdown_1* updates
    if t >= 2.0 and countdown_1.status == NOT_STARTED:
        # keep track of start time/frame for later
        countdown_1.frameNStart = frameN  # exact frame index
        countdown_1.tStart = t  # local t and not account for scr refresh
        countdown_1.setAutoDraw(True)
    if countdown_1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if t >= 3.0 :
            # keep track of stop time/frame for later
            countdown_1.tStop = t  # not accounting for scr refresh
            countdown_1.frameNStop = frameN  # exact frame index
            countdown_1.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in CountdownComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Countdown"-------
for thisComponent in CountdownComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
thisPracticetrial = Practicetrials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPracticetrial.rgb)
if thisPracticetrial != None:
    for paramName in thisPracticetrial:
        exec('{} = thisPracticetrial[paramName]'.format(paramName))

for thisPracticetrial in Practicetrials:
    currentLoop = Practicetrials
    # abbreviate parameter names if possible (e.g. rgb = thisPracticetrial.rgb)
    if thisPracticetrial != None:
        for paramName in thisPracticetrial:
            exec('{} = thisPracticetrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "CueRoutine"-------
    t = 0
    CueRoutineClock.reset()  # clock
    frameN = -1
    # update component parameters for each repeat
    ImgCue1.setColor('white', colorSpace='rgb')
    ImgCue1.setPos((0, 0))
    ImgCue1.setText(Cue)
    ImgCue1.setFont('Arial')
    ImgCue1.setHeight(3)
#keep track of which components have finished
    CueRoutineComponents = [FixationCross1, ImgCue1]
    for thisComponent in CueRoutineComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    CueRoutineClock.reset()  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "CueRoutine"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = CueRoutineClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *FixationCross1* updates
        if t>= 0.0 and FixationCross1.status == NOT_STARTED:
            # keep track of start time/frame for later
            FixationCross1.frameNStart = frameN  # exact frame index
            FixationCross1.tStart = t  # local t and not account for scr refresh
            FixationCross1.setAutoDraw(True)
        if FixationCross1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if t>= 2.0:
                # keep track of stop time/frame for later
                FixationCross1.tStop = t  # not accounting for scr refresh
                FixationCross1.frameNStop = frameN  # exact frame index
                FixationCross1.setAutoDraw(False)
        
        # *ImgCue1* updates
        if t>= 2.0 and ImgCue1.status == NOT_STARTED:
            # keep track of start time/frame for later
            ImgCue1.frameNStart = frameN  # exact frame index
            ImgCue1.tStart = t  # local t and not account for scr refresh
            ImgCue1.setAutoDraw(True)
        if ImgCue1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if t>= 4.0:
                # keep track of stop time/frame for later
                ImgCue1.tStop = t  # not accounting for scr refresh
                ImgCue1.frameNStop = frameN  # exact frame index
                ImgCue1.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in CueRoutineComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "CueRoutine"-------
    for thisComponent in CueRoutineComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "Trial"-------
    t = 0
    TrialClock.reset()  # clock
    frameN = -1
    # update component parameters for each repeat
    emotion_image = emotion_image_cache[Picture]
    Rating_inst.setColor('white', colorSpace='rgb')
    Rating_inst.setPos((0, 0))
    Rating_inst.setText('How negative did you feel? \n\n\n\n')
    Rating_inst.setFont('Arial')
    Rating_inst.setHeight(2)
    # keep track of which components have finished
    key_resp = event.BuilderKeyResponse()
    key_resp.status = NOT_STARTED
    TrialComponents = [emotion_image, Rating_inst, key_resp, Scale2]
    for thisComponent in TrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    TrialClock.reset()  # t0 is time of first possible flip
    frameN = -1
    # update component parameters for each repeat
    # -------Run Routine "Trial"-------
    continueRoutine = True
    emotion_image = emotion_image_cache[Picture]

    while continueRoutine:
        # get current time
        t = TrialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *emotion_image* updates
        if t >= 0.0 and emotion_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            emotion_image.frameNStart = frameN  # exact frame index
            emotion_image.tStart = t  # local t and not account for scr refresh
            emotion_image.setAutoDraw(True)
        if emotion_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if emotion_image.status == STARTED and t >= 7.0:
                # keep track of stop time/frame for later
                emotion_image.setAutoDraw(False)

        # *Rating_inst* updates
        if t >= 7.0 and Rating_inst.status == NOT_STARTED:
            # keep track of start time/frame for later
            Rating_inst.frameNStart = frameN  # exact frame index
            Rating_inst.tStart = t  # local t and not account for scr refresh
            Rating_inst.setAutoDraw(True)
        if Rating_inst.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if t >= 11.0:
                # keep track of stop time/frame for later
                Rating_inst.tStop = t  # not accounting for scr refresh
                Rating_inst.frameNStop = frameN  # exact frame index
                Rating_inst.setAutoDraw(False)

        # *Scale2* updates
        if t >= 7.0 and Scale2.status == NOT_STARTED:
            # keep track of start time/frame for later
            Scale2.frameNStart = frameN  # exact frame index
            Scale2.tStart = t  # local t and not account for scr refresh
            Scale2.setAutoDraw(True)
        if Scale2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if t >= 11.0:
                # keep track of stop time/frame for later
                Scale2.tStop = t  # not accounting for scr refresh
                Scale2.frameNStop = frameN  # exact frame index
                Scale2.setAutoDraw(False)
        #*key_resp* updates
        waitOnFlip = False
        if t>= 7.0 and key_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.status = STARTED
#            # keyboard checking is just starting
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '2', '3', '4', '5'])
            print(theseKeys)
        if t>= 11.0:
                # keep track of stop time/frame for later
                key_resp.tStop = t  # not accounting for scr refresh
                key_resp.frameNStop = frameN  # exact frame index
                key_resp.status = FINISHED
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "Trial"-------
    for thisComponent in TrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

    # ------Prepare to start Routine "Relax"-------
    t = 0
    RelaxClock.reset()  # clock
    frameN = -1
    # update component parameters for each repeat
    text_4.setColor('white', colorSpace='rgb')
    text_4.setPos((0, 0))
    text_4.setText('RELAX')
    text_4.setFont('Arial')
    text_4.setHeight(3)
    # keep track of which components have finished
    RelaxComponents = [text_4]
    for thisComponent in RelaxComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    RelaxClock.reset()  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Relax"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = RelaxClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_4* updates
        if t >= 0.0 and text_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.setAutoDraw(True)
        if text_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if t >= ISI:
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.frameNStop = frameN  # exact frame index
                text_4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RelaxComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Relax"-------
    for thisComponent in RelaxComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Relax" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1 repeats of 'Practicetrials'

# ------Prepare to start Routine "Instructions_2"-------
t = 0
Instructions_2Clock.reset()  # clock
frameN = -1
# update component parameters for each repeat
# keep track of which components have finished
key_resp_Start = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_Start.status = NOT_STARTED
Instructions_2Components = [Task_Instructions, key_resp_Start]
for thisComponent in Instructions_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
Instructions_2Clock.reset()  # t0 is time of first possible flip
frameN = -1
# -------Run Routine "Instructions_2"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = Instructions_2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Task_Instructions* updates
    if t>= 0.0 and Task_Instructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        Task_Instructions.frameNStart = frameN  # exact frame index
        Task_Instructions.tStart = t  # local t and not account for scr refresh
        Task_Instructions.setAutoDraw(True)
    
    if t >= 0.0 and key_resp_Start.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_Start.tStart = t  # underestimates by a little under one frame
        key_resp_Start.frameNStart = frameN  # exact frame index
        key_resp_Start.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_Start.clock.reset)  # t=0 on next screen flip
    if key_resp_Start.status == STARTED:
        theseKeys = event.getKeys(keyList=['s'])
        if len(theseKeys):
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instructions_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions_2"-------
for thisComponent in Instructions_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "Instructions_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Trigger"-------
t = 0
TriggerClock.reset()  # clock
frameN = -1
# update component parameters for each repeat
trigger_text.setColor('white', colorSpace='rgb')
trigger_text.setPos((0, 0))
trigger_text.setText('Get ready!')
trigger_text.setFont('Arial')
trigger_text.setHeight(3)

key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_2.status = NOT_STARTED

# keep track of which components have finished
TriggerComponents = [trigger_text, key_resp_2]
for thisComponent in TriggerComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
TriggerClock.reset()  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Trigger"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = TriggerClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *trigger_text* updates
    if t>= 0.0 and trigger_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        trigger_text.frameNStart = frameN  # exact frame index
        trigger_text.tStart = t  # local t and not account for scr refreshh
        trigger_text.setAutoDraw(True)
    
    # *key_resp_2* updates
    if t>= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['s'])

        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_2.keys = theseKeys[-1]  # just the last key pressed
            key_resp_2.rt = key_resp_2.clock.getTime()
            # Start Image Acquisition
            #cni_trigger()
            continueRoutine = False

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in TriggerComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Trigger"-------
for thisComponent in TriggerComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None

# the Routine "Trigger" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Countdown"-------
t = 0
CountdownClock.reset()  # clock
frameN = -1
routineTimer.add(5.000000)
# update component parameters for each repeat.  Keep track of which components have finished
CountdownComponents = [Countdown_5, Countdown_4, Countdown_3, countdown_2, countdown_1]
for thisComponent in CountdownComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

t = 0
CountdownClock.reset()  # t0 is time of first possible flip
frameN = -1
# -------Run Routine "Countdown"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = CountdownClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *Countdown_5* updates
    if t>=0.0 and Countdown_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        Countdown_5.frameNStart = frameN  # exact frame index
        Countdown_5.tStart = t  # local t and not account for scr refresh
        Countdown_5.setAutoDraw(True)
    if Countdown_5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if t>= 1.0:
            # keep track of stop time/frame for later
            Countdown_5.tStop = t  # not accounting for scr refresh
            Countdown_5.frameNStop = frameN  # exact frame index
            Countdown_5.setAutoDraw(False)
    # *Countdown_4* updates
    if t>=1.0 and Countdown_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        Countdown_4.frameNStart = frameN  # exact frame index
        Countdown_4.tStart = t  # local t and not account for scr refresh
        Countdown_4.setAutoDraw(True)
    if Countdown_4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if t>= 2.0:
            # keep track of stop time/frame for later
            Countdown_4.tStop = t  # not accounting for scr refresh
            Countdown_4.frameNStop = frameN  # exact frame index
            Countdown_4.setAutoDraw(False)
    
    # *Countdown_3* updates
    if t>=2.0 and Countdown_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        Countdown_3.frameNStart = frameN  # exact frame index
        Countdown_3.tStart = t  # local t and not account for scr refresh
        Countdown_3.setAutoDraw(True)
    if Countdown_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if t>= 3.0:
            # keep track of stop time/frame for later
            Countdown_3.tStop = t  # not accounting for scr refresh
            Countdown_3.frameNStop = frameN  # exact frame index
            Countdown_3.setAutoDraw(False)
    
    # *countdown_2* updates
    if t>=3.0 and countdown_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        countdown_2.frameNStart = frameN  # exact frame index
        countdown_2.tStart = t  # local t and not account for scr refresh
        countdown_2.setAutoDraw(True)
    if countdown_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if t>=4.0:
            # keep track of stop time/frame for later
            countdown_2.tStop = t  # not accounting for scr refresh
            countdown_2.frameNStop = frameN  # exact frame index
            countdown_2.setAutoDraw(False)
    
    # *countdown_1* updates
    if t>= 4.0 and countdown_1.status == NOT_STARTED:
        # keep track of start time/frame for later
        countdown_1.frameNStart = frameN  # exact frame index
        countdown_1.tStart = t  # local t and not account for scr refresh
        countdown_1.setAutoDraw(True)
    if countdown_1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if t>= 5.0:
            # keep track of stop time/frame for later
            countdown_1.tStop = t  # not accounting for scr refresh
            countdown_1.frameNStop = frameN  # exact frame index
            countdown_1.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in CountdownComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Countdown"-------
for thisComponent in CountdownComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# FIXME: deleting randomization lines here

# set up handler to look after randomisation of conditions etc
thisStudyTrial = StudyTrials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisStudyTrial.rgb)
if thisStudyTrial != None:
    for paramName in thisStudyTrial:
        exec('{} = thisStudyTrial[paramName]'.format(paramName))

for thisStudyTrial in StudyTrials:
    currentLoop = StudyTrials
    # abbreviate parameter names if possible (e.g. rgb = thisStudyTrial.rgb)
    if thisStudyTrial != None:
        for paramName in thisStudyTrial:
            exec('{} = thisStudyTrial[paramName]'.format(paramName))

    # ------Prepare to start Routine "CueRoutine"-------
    t = 0
    CueRoutineClock.reset()  # clock
    frameN = -1
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    ImgCue1.setColor('white', colorSpace='rgb')
    ImgCue1.setPos((0, 0))
    ImgCue1.setText(Cue)
    ImgCue1.setFont('Arial')
    ImgCue1.setHeight(3)
    # keep track of which components have finished
    CueRoutineComponents = [FixationCross1, ImgCue1]
    for thisComponent in CueRoutineComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    CueRoutineClock.reset()  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "CueRoutine"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = CueRoutineClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *FixationCross1* updates
        if t>0.0 and FixationCross1.status == NOT_STARTED:
            # keep track of start time/frame for later
            FixationCross1.frameNStart = frameN  # exact frame index
            FixationCross1.tStart = t  # local t and not account for scr refresh
            FixationCross1.setAutoDraw(True)
        if FixationCross1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if t>= 2.0:
                # keep track of stop time/frame for later
                FixationCross1.tStop = t  # not accounting for scr refresh
                FixationCross1.frameNStop = frameN  # exact frame index
                FixationCross1.setAutoDraw(False)

        # *ImgCue1* updates
        if t>= 2.0 and ImgCue1.status == NOT_STARTED:
            # keep track of start time/frame for later
            ImgCue1.frameNStart = frameN  # exact frame index
            ImgCue1.tStart = t  # local t and not account for scr refresh
            ImgCue1.setAutoDraw(True)
        if ImgCue1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if t>=4.0:
                # keep track of stop time/frame for later
                ImgCue1.tStop = t  # not accounting for scr refresh
                ImgCue1.frameNStop = frameN  # exact frame index
                ImgCue1.setAutoDraw(False)

        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in CueRoutineComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "CueRoutine"-------
    for thisComponent in CueRoutineComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

    # ------Prepare to start Routine "Trial"-------
    continueRoutine = True
    routineTimer.add(13.000000)
    emotion_image = emotion_image_cache[Picture]
    # update component parameters for each repeat
    #emotion_image.setImage(Picture)
    Rating_inst.setColor('white', colorSpace='rgb')
    Rating_inst.setPos((0, 0))
    Rating_inst.setText('How negative did you feel? \n\n\n\n')
    Rating_inst.setFont('Arial')
    Rating_inst.setHeight(2)
    
    key_resp = event.BuilderKeyResponse()
    key_resp.status = NOT_STARTED
    # keep track of which components have finished
    TrialComponents = [emotion_image, Rating_inst, Scale2, key_resp] #add keyresp
    for thisComponent in TrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    TrialClock.reset()  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "Trial"-------
    continueRoutine = True
    emotion_image = emotion_image_cache[Picture]
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = TrialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *emotion_image* updates
        if t>= 0.0 and emotion_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            emotion_image.frameNStart = frameN  # exact frame index
            emotion_image.tStart = t  # local t and not account for scr refresh
            emotion_image.setAutoDraw(True)

        if emotion_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if t>=7.0:
                # keep track of stop time/frame for later
                emotion_image.tStop = t  # not accounting for scr refresh
                emotion_image.frameNStop = frameN  # exact frame index
                emotion_image.setAutoDraw(False)



        # *Rating_inst* updates
        if t>= 7.0 and Rating_inst.status == NOT_STARTED:
            # keep track of start time/frame for later
            Rating_inst.frameNStart = frameN  # exact frame index
            Rating_inst.tStart = t  # local t and not account for scr refresh
            Rating_inst.setAutoDraw(True)
        if Rating_inst.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if t>= 11.0:
                # keep track of stop time/frame for later
                Rating_inst.tStop = t  # not accounting for scr refresh
                Rating_inst.frameNStop = frameN  # exact frame index
                Rating_inst.setAutoDraw(False)

        # *Scale2* updates
        if t>= 7.0 and Scale2.status == NOT_STARTED:
            # keep track of start time/frame for later
            Scale2.frameNStart = frameN  # exact frame index
            Scale2.tStart = t  # local t and not account for scr refresh
            Scale2.setAutoDraw(True)
        if Scale2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if t>= 11.0:
                # keep track of stop time/frame for later
                Scale2.tStop = t  # not accounting for scr refresh
                Scale2.frameNStop = frameN  # exact frame index
                Scale2.setAutoDraw(False)
        #*key_resp* updates
        waitOnFlip = False
        if t>= 7.0 and key_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.status = STARTED
#            # keyboard checking is just starting
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '2', '3', '4', '5'])
            print(theseKeys)
        if t>= 11.0:
                # keep track of stop time/frame for later
                key_resp.tStop = t  # not accounting for scr refresh
                key_resp.frameNStop = frameN  # exact frame index
                key_resp.status = FINISHED
        # check for quit (typically the Esc key)
        if "escape" in theseKeys:
            endExpNow = True
            continueRoutine = False
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp.keys = theseKeys[-1]  # just the last key pressed
            key_resp.rt = key_resp.clock.getTime()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        #if statement to reverse score odd ID based on counterbalancing of fingers
        key_resp_rev= 0
        if not odd:
            if key_resp.keys==5:
                key_resp_rev=1
            if key_resp.keys==4:
                key_resp_rev=2
            if key_resp.keys==2:
                key_resp_rev=4
            if key_resp.keys==1:
                key_resp_rev=5
        elif odd: 
            key_resp_rev=key_resp.keys
            # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp_rev = None
        thisExp.addData('key_resp.keys',key_resp_rev)
        #else:
            #thisExp.addData('key_resp.keys',key_resp.keys)
            
        if key_resp.keys != None:  # we had a response
            thisExp.addData('key_resp', key_resp.rt)
#        # refresh the screen
    #log key response etc. to csv
        thisExp.addData('image_path', image_path)
        thisExp.addData('image.started', emotion_image.tStart)
        thisExp.addData('image.stopped', emotion_image.tStop)
        thisExp.addData('Rating_inst.started', Rating_inst.tStart)
        thisExp.addData('Rating_inst.stopped', Rating_inst.tStop)
        logging.log(level=logging.EXP, msg='Rating ='+ format(key_resp_rev))
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
        if key_resp.keys != None:  # we had a response
            thisExp.addData('key_resp.rt', key_resp.rt)
        thisExp.nextEntry()
    # -------Ending Routine "Trial"-------
    for thisComponent in TrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    #thisExp.addData('image.started', emotion_image.tStart)
    #thisExp.addData('image.stopped', emotion_image.tStop)
    #thisExp.addData('Rating_inst.started', Rating_inst.tStart)
    #thisExp.addData('Rating_inst.stopped', Rating_inst.tStop)
    #thisExp.addData('key_resp.keys', key_resp_rev)
    #if key_resp.keys != None:  # we had a response
    #    thisExp.addData('key_resp.rt', key_resp.rt)
    # check responses
    #if key_resp.keys in ['', [], None]:  # No response was made
     #   key_resp.keys = None

    #StudyTrials.addData('key_resp.started', key_resp.tStartRefresh)
    #StudyTrials.addData('key_resp.stopped', key_resp.tStopRefresh)
    #StudyTrials.addData('Scale2.started', Scale2.tStartRefresh)
    #StudyTrials.addData('Scale2.stopped', Scale2.tStopRefresh)
    # ------Prepare to start Routine "Relax"-------
    t = 0
    RelaxClock.reset()  # clock
    frameN = -1
    # update component parameters for each repeat
    text_4.setColor('white', colorSpace='rgb')
    text_4.setPos((0, 0))
    text_4.setText('RELAX')
    text_4.setFont('Arial')
    text_4.setHeight(3)
    # keep track of which components have finished
    RelaxComponents = [text_4]
    for thisComponent in RelaxComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    RelaxClock.reset()  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "Relax"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = RelaxClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *text_4* updates
        if t>= 0.0 and text_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.setAutoDraw(True)
        if text_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if t >= float(ISI):
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.frameNStop = frameN  # exact frame index
                text_4.setAutoDraw(False)

        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            if odd:
                thisExp.saveAsWideText(filename+'_1thumb_'+'.csv')
            else:
                thisExp.saveAsWideText(filename+'_5thumb_'+'.csv')
            core.quit()


        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RelaxComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "Relax"-------
    for thisComponent in RelaxComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Relax" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()



    # ------Prepare to start Routine "well_done"-------
    t = 0
    well_doneClock.reset()  # clock
    frameN = -1
    # keep track of which components have finished
    well_doneComponents = [well_done]
    for thisComponent in well_doneComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    well_doneClock.reset()  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "well_done"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = well_doneClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *text_4* updates
        if t >= 0.0 and well_done.status == NOT_STARTED:
            # keep track of start time/frame for later
            well_done.frameNStart = frameN  # exact frame index
            well_done.tStart = t  # local t and not account for scr refresh
            well_done.setAutoDraw(True)
        elif t >= 8.0 and well_done.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            # keep track of stop time/frame for later
            well_done.tStop = t  # not accounting for scr refresh
            well_done.frameNStop = frameN  # exact frame index
            well_done.setAutoDraw(False)

        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            if odd:
                thisExp.saveAsWideText(filename+'_1thumb_'+'.csv')
            else:
                thisExp.saveAsWideText(filename+'_5thumb_'+'.csv')
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RelaxComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "well_done"-------
    for thisComponent in well_doneComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Relax" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()


win.flip()
thisExp.saveAsWideText(filename+'.csv')
logging.flush()

# make sure everything is closed down
win.close()
core.quit()
