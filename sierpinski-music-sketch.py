from earsketch import *
from random import *
from math import *

# Don't change RND_* constants. They are needed
# for the random sounds generator, but made available
# here so tha that you can use them for setting the RANDOM_SOUND_CHOICE variable
RND_RANDOM_BEATS = 0       # Chooses random sounds from any of the following 3 sets
RND_ELECTRO_BEATS = 1      # 128 BPM
RND_HOUSE_BEATS = 2        # 120 BPM
RND_TECHNO_BEATS = 3       # 125 BPM

# -------------------------
# Configuration Constants
# -------------------------
TEMPO_BPM = 128                           # Tempo to set in Beats per Minute (BPM)
USE_RANDOM_PATTERN = False                # Change to True for a truly random pattern
RANDOM_SOUND_CHOICE = RND_ELECTRO_BEATS   # Change to one of the RND_* choices

def in_carpet(x, y):
    # Used to indicate if a beat should be included
    # when making the Sierpinski carpet
    # parameters: current depth, current beat
    while True:
        if x == 0 or y == 0:
            return True
        elif x % 3 == 1 and y % 3 == 1:
            return False

        x /= 3
        y /= 3

def makeSierpinskiCarpet(audioclips, n, depth, start, skip=False):
    # creates a pattern based off of the Sierpinski carpet pattern
    # parameters: list of audioclips, Sierpinski order of n, depth of carpet, starting measure, skip rows?
    # depth = d
    d = depth
    for i in xrange(3 ** n):
        if d == 0:                  # max depth reached
            return
        if skip and i % 2 != 0:     # skip every other row if requested
            d = d - 1
            continue
        beatString = ''
        addAudionum = False
        for j in xrange(3 ** n):
            if j == 0:
                beatString += str(depth - d)
            elif in_carpet(i, j):
                if addAudionum:
                    beatString += str(depth - d)
                    addAudionum = False
                else:
                    beatString += '+'
            else:
                beatString += '-'
                addAudionum = True
        # ensure that we get at least 16 beats per measure
        # by padding the beatString - this actually produces
        # an interesting emphasis on the last beats of the measure
        ensure16 = 16 - (len(beatString) % 16)
        for k in range(ensure16):
            beatString += '+'
        makeBeat(audioclips, i+1, start, beatString)
        d = d - 1

def getRandomElectroBeats():
    # Creates a random list of sounds
    drumList = [ELECTRO_DRUM_MAIN_BEAT_001,
                ELECTRO_DRUM_MAIN_BEAT_002,
                ELECTRO_DRUM_MAIN_BEAT_003,
                ELECTRO_DRUM_MAIN_BEAT_004,
                ELECTRO_DRUM_MAIN_BEAT_005,
                ELECTRO_DRUM_MAIN_BEAT_006,
                ELECTRO_DRUM_MAIN_BEAT_007,
                ELECTRO_DRUM_MAIN_BEAT_008,
                ELECTRO_DRUM_MAIN_BEAT_009,
                ELECTRO_DRUM_MAIN_BEAT_010]
    bassList = [ELECTRO_ANALOGUE_BASS_001,
                ELECTRO_ANALOGUE_BASS_002,
                ELECTRO_ANALOGUE_BASS_003,
                ELECTRO_ANALOGUE_BASS_004,
                ELECTRO_ANALOGUE_BASS_005,
                ELECTRO_ANALOGUE_BASS_006,
                ELECTRO_ANALOGUE_BASS_007,
                ELECTRO_ANALOGUE_BASS_008,
                ELECTRO_ANALOGUE_BASS_009,
                ELECTRO_ANALOGUE_BASS_010]
    phaserList = [ELECTRO_ANALOGUE_PHASERBASS_001,
                  ELECTRO_ANALOGUE_PHASERBASS_002,
                  ELECTRO_ANALOGUE_PHASERBASS_003,
                  ELECTRO_ANALOGUE_PHASERBASS_004]
    spaceList  = [ELECTRO_ANALOGUE_SPACELEAD_001,
                  ELECTRO_ANALOGUE_SPACELEAD_002,
                  ELECTRO_ANALOGUE_SPACELEAD_003,
                  ELECTRO_ANALOGUE_SPACELEAD_004,
                  ELECTRO_ANALOGUE_SPACELEAD_005]
    leadList   = [ELECTRO_ANALOGUE_LEAD_001,
                  ELECTRO_ANALOGUE_LEAD_002,
                  ELECTRO_ANALOGUE_LEAD_003,
                  ELECTRO_ANALOGUE_LEAD_004,
                  ELECTRO_ANALOGUE_LEAD_005,
                  ELECTRO_ANALOGUE_LEAD_006,
                  ELECTRO_ANALOGUE_LEAD_007,
                  ELECTRO_ANALOGUE_LEAD_008,
                  ELECTRO_ANALOGUE_LEAD_009,
                  ELECTRO_ANALOGUE_LEAD_010]
    motorList  = [ELECTRO_MOTORBASS_001,
                  ELECTRO_MOTORBASS_002,
                  ELECTRO_MOTORBASS_003,
                  ELECTRO_MOTORBASS_004,
                  ELECTRO_MOTORBASS_005]
    sfxList    = [ELECTRO_SFX_WHITENOISE_SCATTER_001,
                  ELECTRO_SFX_WHITENOISE_SCATTER_002,
                  ELECTRO_SFX_WHITENOISE_SCATTER_003,
                  ELECTRO_SFX_WHITENOISE_SCATTER_004,
                  ELECTRO_SFX_WHITENOISE_SCATTER_005,
                  ELECTRO_SFX_WHITENOISE_SCATTER_006,
                  ELECTRO_SFX_WHITENOISE_SCATTER_007,
                  ELECTRO_SFX_WHITENOISE_SCATTER_008,
                  ELECTRO_SFX_WHITENOISE_SCATTER_009,
                  ELECTRO_SFX_WHITENOISE_SCATTER_010]

    drums = randint(0, len(drumList )-1)
    bass  = randint(0, len(bassList)-1)
    phase = randint(0, len(phaserList)-1)
    space = randint(0, len(spaceList)-1)
    lead  = randint(0, len(leadList)-1)
    motor = randint(0, len(motorList)-1)
    sfx   = randint(0, len(sfxList)-1)

    return [drumList[drums],
            bassList[bass],
            phaserList[phase],
            spaceList[space],
            leadList[lead],
            motorList[motor],
            sfxList[sfx]]

def getRandomHouseBeats():
    # Creates a random list of sounds
    drumList  = [HOUSE_BREAKBEAT_001,
                 HOUSE_BREAKBEAT_002,
                 HOUSE_BREAKBEAT_003,
                 HOUSE_BREAKBEAT_004]
    fillList  = [HOUSE_BREAK_FILL_001,
                 HOUSE_BREAK_FILL_002,
                 HOUSE_BREAK_FILL_003,
                 HOUSE_BREAK_FILL_004]
    pianoList = [HOUSE_ROADS_PIANO_001,
                 HOUSE_ROADS_PIANO_002,
                 HOUSE_ROADS_PIANO_003,
                 HOUSE_ROADS_PIANO_007]
    chordList = [HOUSE_DEEP_AIRYCHORD_001,
                 HOUSE_DEEP_AIRYCHORD_002,
                 HOUSE_DEEP_CHORD_001,
                 HOUSE_DEEP_CHORD_002]
    leadList  = [HOUSE_DEEP_MOOGLEAD_001,
                 HOUSE_DEEP_MOOGLEAD_002,
                 HOUSE_DEEP_MOOGLEAD_003,
                 HOUSE_DEEP_MOOGLEAD_004,
                 HOUSE_DEEP_MOOGLEAD_005,
                 HOUSE_DEEP_MOOGLEAD_006,
                 HOUSE_DEEP_MOOGLEAD_007,
                 HOUSE_DEEP_MOOGLEAD_009,
                 HOUSE_DEEP_MOOGLEAD_010]
    bassList  = [HOUSE_DEEP_BASS_001,
                 HOUSE_DEEP_BASS_002,
                 HOUSE_DEEP_BASS_003,
                 HOUSE_DEEP_BASS_004]
    sfxList   = [HOUSE_SFX_WHOOSH_001,
                 HOUSE_SFX_WHOOSH_002,
                 HOUSE_SFX_WHOOSH_003,
                 HOUSE_SFX_WHOOSH_004,
                 HOUSE_SFX_WHOOSH_005,
                 HOUSE_SFX_WHOOSH_006,
                 HOUSE_SFX_WHOOSH_007,
                 HOUSE_SFX_WHOOSH_008,
                 HOUSE_SFX_WHOOSH_009,
                 HOUSE_SFX_WHOOSH_010,
                 HOUSE_SFX_WHOOSH_011]

    drums = randint(0, len(drumList)-1)
    fills = randint(0, len(fillList)-1)
    piano = randint(0, len(pianoList)-1)
    chord = randint(0, len(chordList)-1)
    lead  = randint(0, len(leadList)-1)
    lead2 = randint(0, len(leadList)-1)
    bass  = randint(0, len(bassList)-1)
    sfx   = randint(0, len(sfxList)-1)
    return [drumList [drums],
              fillList[fills],
              pianoList[piano],
              chordList[chord],
              leadList[lead],
              leadList[lead2],
              bassList[bass]]

def getRandomTechnoBeats():
    # Creates a random list of sounds
    drumList = [TECHNO_MAINLOOP_001,
                 TECHNO_MAINLOOP_002,
                 TECHNO_MAINLOOP_003,
                 TECHNO_MAINLOOP_004,
                 TECHNO_MAINLOOP_005,
                 TECHNO_MAINLOOP_006,
                 TECHNO_MAINLOOP_007,
                 TECHNO_MAINLOOP_008,
                 TECHNO_MAINLOOP_009,
                 TECHNO_MAINLOOP_010]
    bassList = [TECHNO_ACIDBASS_001,
                TECHNO_ACIDBASS_002,
                TECHNO_ACIDBASS_003,
                TECHNO_ACIDBASS_004,
                TECHNO_ACIDBASS_005,
                TECHNO_ACIDBASS_006,
                TECHNO_ACIDBASS_007,
                TECHNO_ACIDBASS_008,
                TECHNO_ACIDBASS_009,
                TECHNO_ACIDBASS_010]
    leadList = [TECHNO_CLUB_ANALOGLEAD_001,
                TECHNO_CLUB_ANALOGLEAD_002,
                TECHNO_CLUB_ANALOGLEAD_003,
                TECHNO_CLUB_ANALOGLEAD_004,
                TECHNO_CLUB_ANALOGLEAD_005,
                TECHNO_CLUB_ANALOGLEAD_006]
    loopList = [TECHNO_LOOP_PART_001,
                TECHNO_LOOP_PART_002,
                TECHNO_LOOP_PART_003,
                TECHNO_LOOP_PART_004,
                TECHNO_LOOP_PART_005,
                TECHNO_LOOP_PART_006,
                TECHNO_LOOP_PART_007,
                TECHNO_LOOP_PART_008,
                TECHNO_LOOP_PART_009,
                TECHNO_LOOP_PART_010]
    clubList = [TECHNO_CLUBRICH_PAD_001,
                TECHNO_CLUBRICH_PAD_002,
                TECHNO_CLUBRICH_PAD_003,
                TECHNO_CLUBRICH_PAD_004]
    pluckList = [TECHNO_SYNTHPLUCK_001,
                 TECHNO_SYNTHPLUCK_002,
                 TECHNO_SYNTHPLUCK_003,
                 TECHNO_SYNTHPLUCK_004]
    rollList  = [TECHNO_KICKROLL_001,
                 TECHNO_KICKROLL_002,
                 TECHNO_SNAREROLL_001,
                 TECHNO_SNAREROLL_002,
                 TECHNO_SNAREROLL_003,
                 TECHNO_SNAREROLL_004,
                 TECHNO_SNAREROLL_005]

    drums = randint(0, len(drumList)-1)
    bass  = randint(0, len(bassList)-1)
    lead  = randint(0, len(leadList)-1)
    loop  = randint(0, len(loopList)-1)
    club  = randint(0, len(clubList)-1)
    pluck = randint(0, len(pluckList)-1)
    roll  = randint(0, len(rollList)-1)

    return [drumList[drums],
            bassList[bass],
            leadList[lead],
            loopList[loop],
            clubList[club],
            pluckList[pluck],
            rollList[roll]]

def getRandomSounds(soundset=0):
    # Creates a random list of sounds
    # parameters: random set to use,
    # or 0 to take from a random choice of the available sets

    if soundset == RND_ELECTRO_BEATS:
        return getRandomElectroBeats()
    elif soundset == RND_HOUSE_BEATS:
        return getRandomHouseBeats()
    elif soundset == RND_TECHNO_BEATS:
        return getRandomTechnoBeats()
    else:
        choice = randint(RND_ELECTRO_BEATS, RND_TECHNO_BEATS)
        return getRandomSounds(choice)

def makePattern(sounds, start, depth, skip=False):
    # parameters: sound list, starting measure, depth of carpet, skip rows?
    end = start + 4
    for measure in range(start, end, 2):
        makeSierpinskiCarpet(sounds, 3, depth, measure, skip)

def getRandomDepth():
    # obtains a random depth to use in the carpet pattern
    return randint(1,7)

def createFunkyDelayEffect():
    # creates a simple delay effet with an
    # added bandpass that can be changed via an
    # envelope to create a tinny, loudspeaker effect
    # on the resulting echos

    effect = initEffect('funkyDelay')

    # creat ugens
    inbound    = createUGen(effect, INPUT)
    echo       = createUGen(effect, ECHO)
    multiplier = createUGen(effect, TIMES)
    outbound   = createUGen(effect, OUTPUT)
    bpfilter   = createUGen(effect, BANDPASS)

    #connections
    connect(effect, inbound, echo)
    connect(effect, echo, multiplier)
    connect(effect, multiplier, echo)
    connect(effect, echo, bpfilter)
    connect(effect, bpfilter, outbound)

    # min/max ECHO
    setParamMin(echo, TIME, 10)
    setParamMax(echo, TIME, 1000)
    setParam(echo, TIME, 500)

    # min/max TIMES
    setParamMin(multiplier, VALUE, 0)
    setParamMax(multiplier, VALUE, 1)
    setParam(multiplier, VALUE, 0.8)

    # min/max filter
    setParamMin(bpfilter, FREQUENCY, 5)
    setParamMax(bpfilter, FREQUENCY, 20000)
    setParam(bpfilter, FREQUENCY, 2000)

    setParamMin(bpfilter, RESONANCE, 0)
    setParamMax(bpfilter, RESONANCE, 2.0)
    setParam(bpfilter, RESONANCE, 2.0)

    # delay control
    createControl(effect, echo, TIME, 'Delay Time')

    # feedback control
    createControl(effect, multiplier, VALUE, 'Feedback Amount')

    # filter control
    createControl(effect, bpfilter, FREQUENCY, 'Filter Frequency')
    createControl(effect, bpfilter, RESONANCE, 'Filter Resonance')

    finishEffect(effect)

    return effect

# Start the project!
init()
setTempo(TEMPO_BPM)

if USE_RANDOM_PATTERN:
    # set USE_RANDOM_PATTERN to True
    # to create a random pattern on each track
    makePattern(getRandomSounds(RANDOM_SOUND_CHOICE), 1, getRandomDepth(), True)
    makePattern(getRandomSounds(RANDOM_SOUND_CHOICE), 5, getRandomDepth(), True)
    makePattern(getRandomSounds(RANDOM_SOUND_CHOICE), 9, getRandomDepth())
    makePattern(getRandomSounds(RANDOM_SOUND_CHOICE), 13, getRandomDepth())
    makePattern(getRandomSounds(RANDOM_SOUND_CHOICE), 17, getRandomDepth(), True)
    makePattern(getRandomSounds(RANDOM_SOUND_CHOICE), 21, getRandomDepth(), True)
    makePattern(getRandomSounds(RANDOM_SOUND_CHOICE), 25, getRandomDepth(), True)
else:
    # When USE_RANDOM_PATTERN is False,
    # this creates a nice repetitive pattern
    makePattern(getRandomSounds(RANDOM_SOUND_CHOICE), 1, 1, True)
    makePattern(getRandomSounds(RANDOM_SOUND_CHOICE), 5, 3, True)
    makePattern(getRandomSounds(RANDOM_SOUND_CHOICE), 9, 5, True)
    makePattern(getRandomSounds(RANDOM_SOUND_CHOICE), 13, 7)
    makePattern(getRandomSounds(RANDOM_SOUND_CHOICE), 17, 7)
    makePattern(getRandomSounds(RANDOM_SOUND_CHOICE), 21, 5, True)
    makePattern(getRandomSounds(RANDOM_SOUND_CHOICE), 25, 3, True)
    makePattern(getRandomSounds(RANDOM_SOUND_CHOICE), 29, 1, True)

# Obrain some random speaak n spell voicings
fitMedia(selectRandomFile(RICHARDDEVINE__EIGHTBIT_115_BPM__EIGHTVIDEOSPEAKNSPELL), 8, 3, 7)
fitMedia(selectRandomFile(RICHARDDEVINE__EIGHTBIT_115_BPM__EIGHTVIDEOSPEAKNSPELL), 8, 27, 31)


# set volume on the 1st track to fade in and out
setEffect(1, VOLUME, GAIN, -20, 1, 0, 2)
setEffect(1, VOLUME, GAIN, 0, 31, -60, 33)

# Set the funky delay effect on the speaak n spell track
# this adds both the delay and makes the voice echoes gradually
# become more tinny over time
funkyDelay = createFunkyDelayEffect()
setEffect(8, funkyDelay, 'Delay Time', 375)
setEffect(8, funkyDelay, 'Feedback Amount', 0.4)
setEffect(8, funkyDelay, 'Filter Resonance', 0.5)
setEffect(8, funkyDelay, 'Filter Frequency', 500, 3, 15000, 7)
setEffect(8, funkyDelay, 'Filter Frequency', 500, 27, 18000, 31)
setEffect(8, VOLUME, GAIN, 30)

# finish the project!
finish()
