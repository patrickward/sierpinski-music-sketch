"""
Sierpinski Music Sketch is a simple random music experiment built for
the Survey of Music Technology course on Coursera. The patterns are based
off of the Sierpinski Carpet.

This file requires the EarSketch library and the Reaper DAW to run.

:author: Patrick Ward
:copyright: (c) 2013 Patrick Ward
:license: MIT (http://opensource.org/licenses/MIT)
:url: http://github.com/patrickward/sierpinski-music-sketch

You can play around with the various configuration constants
TEMPO_BPM, RANDOM_SOUND_CHOICE, and MEASURE_PATTERN to generate new
music each time the script is run.

Have fun!
"""
from earsketch import *
from random import *
from math import *

# Don't change RND_* constants. They are needed
# for the random sounds generator, but made available
# here so tha that you can use them for setting the RANDOM_SOUND_CHOICE variable
RND_RANDOM_BEATS = 0       # Chooses random sounds from any of the following sets
RND_ELECTRO_BEATS = 1      # 128 BPM
RND_HOUSE_BEATS = 2        # 120 BPM
RND_TECHNO_BEATS = 3       # 125 BPM
RND_EIGHTBIT_BEATS = 4     # 115 BPM
RND_HIPHOP_BEATS = 5       # 98 BPM
RND_DUBSTEP_BEATS = 6      # 140 BPM

# -------------------------
# Configuration Constants
# -------------------------
TEMPO_BPM = 120                         # Tempo to set in Beats per Minute (BPM)
# Random Sound choice can be one of the RND_* constants above,
# or a list made up of the RND_* constants (except RND_RANDOM_BEATS)
# (e.g. [RND_HIPHOP_BEATS,, RND_HOUSE_BEATS]
# RANDOM_SOUND_CHOICE = RND_HOUSE_BEATS
RANDOM_SOUND_CHOICE = [RND_HIPHOP_BEATS, RND_TECHNO_BEATS]
# Measure pattern determines the track patterns that
# get generated (still using random files though)
# Each element in the list contains [depth, skip],
# where depth is the depth of the Sierpinski carpet
# and skip, if True, will skip every other row
# An empty MEASURE_PATTERN creates a random set
MEASURE_PATTERN = [[1, True], [3, True], [5, True], [7, False], [7, False], [5, True], [3, True], [1, True]]
# MEASURE_PATTERN = [[1, True], [3, True], [7, False], [7, True], [7, True], [7, False], [3, True], [1, True]]
# MEASURE_PATTERN = [] # choose random patterns

SIERPINSKI_ORDER = 3      # The Sierpinski order variable for the carpet (3 provides a nice 2-bar pattern)

def in_carpet(x, y):
    """
    Used to indicate if a beat should be included when making the Sierpinski carpet
    parameters: current depth, current beat
    """
    while True:
        if x == 0 or y == 0:
            return True
        elif x % 3 == 1 and y % 3 == 1:
            return False

        x /= 3
        y /= 3

def makeSierpinskiCarpet(audioclips, n, depth, start, skip=False):
    """
    creates a pattern based off of the Sierpinski carpet pattern
    parameters: list of audioclips, Sierpinski order of n, depth of carpet, starting measure, skip rows?
    """
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

def createSoundList(prefix, start, end):
    """
    creates a simple list of sound files by creating the EarSketch
    constants as a string and then evaluating them
    """
    soundList = []
    for i in range(start, end+1):
        f = prefix + '%(number)03d' % {"number": i}
        soundList.append(globals()[f])
    return soundList

soundLists = []
def setupSoundLists():
    """ Sets up the sound lists used throughout the script """

    # Electro
    electro = [createSoundList('ELECTRO_DRUM_MAIN_BEAT_', 1, 10),
               createSoundList('ELECTRO_ANALOGUE_BASS_', 1, 10),
               createSoundList('ELECTRO_ANALOGUE_PHASERBASS_', 1, 4),
               createSoundList('ELECTRO_ANALOGUE_SPACELEAD_', 1, 5),
               createSoundList('ELECTRO_ANALOGUE_LEAD_', 1, 10),
               createSoundList('ELECTRO_MOTORBASS_', 1, 5),
               createSoundList('ELECTRO_SFX_WHITENOISE_SCATTER_', 1, 10)]

    # House
    houseChords = createSoundList('HOUSE_DEEP_AIRYCHORD_', 1, 2)
    houseChords.extend(createSoundList('HOUSE_DEEP_CHORD_', 1, 2))
    houseChords.extend(createSoundList('HOUSE_DEEP_CRYSTALCHORD_', 1, 4))
    house   = [createSoundList('HOUSE_BREAKBEAT_', 1, 26),
               createSoundList('HOUSE_BREAK_FILL_', 1, 4),
               createSoundList('HOUSE_ROADS_PIANO_', 1, 7),
               houseChords,
               createSoundList('HOUSE_DEEP_MOOGLEAD_', 1, 10),
               createSoundList('HOUSE_DEEP_BASS_', 1, 4),
               createSoundList('HOUSE_SFX_WHOOSH_', 1, 11)]

    # Techno
    techLeads = createSoundList('TECHNO_CLUB_ANALOGLEAD_', 1, 6)
    techLeads.extend(createSoundList('TECHNO_POLYLEAD_', 1, 7))
    techPads  = createSoundList('TECHNO_CLUBRICH_PAD_', 1, 4)
    techPads.extend(createSoundList('TECHNO_SOFTPAD_', 1, 3))
    techno  = [createSoundList('TECHNO_MAINLOOP_', 1, 22),
               createSoundList('TECHNO_ACIDBASS_', 1, 16),
               techLeads,
               createSoundList('TECHNO_LOOP_PART_', 1, 22),
               techPads,
               createSoundList('TECHNO_SYNTHPLUCK_', 1, 4),
               createSoundList('TECHNO_WHITENOISESFX_', 1, 11)]


    # Eight Bit
    eightbit = [createSoundList('EIGHT_BIT_ANALOG_DRUM_LOOP_', 1, 20),
                createSoundList('EIGHT_BIT_ATARI_BASSLINE_', 1, 5),
                createSoundList('EIGHT_BIT_ATARI_LEAD_', 1, 13),
                createSoundList('EIGHT_BIT_ATARI_SYNTH_', 1, 5),
                createSoundList('EIGHT_BIT_VIDEO_GAME_LOOP_', 1, 25),
                createSoundList('EIGHT_BIT_ATARI_PAD_', 1, 4),
                createSoundList('EIGHT_BIT_ATARI_SFX_', 1, 13)]

    # Hip Hop
    hiphopLeads = createSoundList('HIPHOP_DUSTYPIANOLEAD_', 1, 3)
    hiphopLeads.extend(createSoundList('HIPHOP_GUITARLEAD_', 1, 2))
    hiphop   = [createSoundList('HIPHOP_DUSTYGROOVE_', 1, 12),
                createSoundList('HIPHOP_SYNTHBASS_', 1, 5),
                createSoundList('HIPHOP_SYNTHPLUCKLEAD_', 1, 7),
                createSoundList('HIPHOP_HITS_', 1, 7),
                createSoundList('HIPHOP_MUTED_GUITAR_', 1, 10),
                createSoundList('HIPHOP_TRAPHOP_BEAT_', 1, 10),
                hiphopLeads]

    # Dubstep
    dubstep  = [createSoundList('DUBSTEP_DRUMLOOP_MAIN_', 1, 13),
                createSoundList('DUBSTEP_PERCDRUM_', 1, 6),
                createSoundList('DUBSTEP_LEAD_', 1, 20),
                createSoundList('DUBSTEP_BASS_WOBBLE_', 1, 46),
                createSoundList('DUBSTEP_SUBBASS_', 1, 15),
                createSoundList('DUBSTEP_PAD_', 1, 4),
                createSoundList('DUBSTEP_SFX_', 1, 8)]

    soundLists.append([])
    soundLists.append(electro)
    soundLists.append(house)
    soundLists.append(techno)
    soundLists.append(eightbit)
    soundLists.append(hiphop)
    soundLists.append(dubstep)

def getRandomSounds(soundset=0):
    """
    Creates a random list of sounds
    parameters: random set to use, or 0 to take from a random choice of the available sets
    """

    # checks to see if soundset is not an integer, if not
    # it is assumed that soundset is a list
    if not isinstance(soundset, int):
        rndset   = randint(0, len(soundset)-1)
        soundset = soundset[rndset]

    if soundset > 0:
        set1 = randint(0, len(soundLists[soundset][0])-1)
        set2  = randint(0, len(soundLists[soundset][1])-1)
        set3 = randint(0, len(soundLists[soundset][2])-1)
        set4 = randint(0, len(soundLists[soundset][3])-1)
        set5  = randint(0, len(soundLists[soundset][4])-1)
        set6 = randint(0, len(soundLists[soundset][5])-1)
        set7   = randint(0, len(soundLists[soundset][6])-1)

        return [soundLists[soundset][0][set1],
                soundLists[soundset][1][set2],
                soundLists[soundset][2][set3],
                soundLists[soundset][3][set4],
                soundLists[soundset][4][set5],
                soundLists[soundset][5][set6],
                soundLists[soundset][6][set7]]
    else:
        choice = randint(1, len(soundLists) - 1)
        return getRandomSounds(choice)

def makePattern(sounds, start, depth, skip=False):
    """ parameters: sound list, starting measure, depth of carpet, skip rows? """
    end = start + 4
    for measure in range(start, end, 2):
        makeSierpinskiCarpet(sounds, SIERPINSKI_ORDER, depth, measure, skip)

def getRandomDepth():
    """ obtains a random depth to use in the carpet pattern """
    return randint(1,7)

def createFunkyDelayEffect():
    """
    creates a simple delay effet with an added bandpass that can be changed via an
    envelope to create a tinny, loudspeaker effect on the resulting echos
    """

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

def createTrackPatterns():
    """ Creates the track patterns for each measure """

    # if measure pattern is empty, create random depths
    if not MEASURE_PATTERN:
        for p in range(8):
            MEASURE_PATTERN.append([getRandomDepth(), randint(0,1)])

    pattern = 0
    for measure in range(1, 30, 4):
        makePattern(getRandomSounds(RANDOM_SOUND_CHOICE),
                measure, MEASURE_PATTERN[pattern][0], MEASURE_PATTERN[pattern][1])
        pattern = pattern + 1


# Start the project!
init()
setupSoundLists()
setTempo(TEMPO_BPM)
createTrackPatterns()

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
setEffect(8, VOLUME, GAIN, 6)

# finish the project!
finish()
