sierpinski-music-sketch
=======================

This is an experimental random music generator using a [Sierpinski carpet pattern](http://en.wikipedia.org/wiki/Sierpinski_carpet), the [EarSketch](http://earsketch.gatech.edu/) library and, the [Reaper](http://www.reaper.fm/) DAW.

It was created for the Survey of Music Technology course on Coursera in the Fall of 2013.

### Configuration

- **TEMPO_BPM:** set this to the tempo in beats per measure (bpm)
- **RANDOM\_SOUND\_CHOICE:** Set to one of the **RND_*** constants at the top of the script
- **MEASURE\_PATTERN:** a pattern of 8 sub lists, each with depth in the first index and skip(tru/false) in the second index.

### Usage

You need [Reaper](http://www.reaper.fm/) with [EarSketch](http://earsketch.gatech.edu/) installed to run this.

Then, choose Action --&gt; Run EarSketch script... and choose this script.

