import time
import simpleaudio
import math

# open the soundfiles
# TEST SOUNDS dowloaded from https://freesound.org/
# Snare sound by: cima
# Kick sound by: almela 
# Hi-hat sound by: sorinious-genious

sound_accent = simpleaudio.WaveObject.from_wave_file("244195__cima__snare1.wav")
sound_beat = simpleaudio.WaveObject.from_wave_file("250547__almela__kick-bass-drum.wav")
sound_subdivision = simpleaudio.WaveObject.from_wave_file("561236__sorinious-genious__hat-2.wav")

# main variables
# Note length: default is 4, so calculations are based on the quarter note.

note_length = [1, 2, 4, 8, 16, 32, 64]

beats_per_measure = 6
beat_duration = note_length[3]  # how long a beat lasts, in musical notation

# selected bpm number is based on the quarter note. given bpm needs to be 
# recalculated for each of the musical note durations.

selected_beats_per_minute = 90 

# a beat in eight notes will feel double tempo compared to the quarter note.
# based on that, we can calculate an actual_bpm based on the selected note_length.
# note_length is a series of power of 2. if we shift the exponent left by two,
# we actually get the value with which we need to multiply the selected_bpm.
actual_beats_per_minute = selected_beats_per_minute * 2 ** (math.log2(beat_duration) - 2)

beats_per_second =  60 / actual_beats_per_minute   # derived from beats per minute

accent = [1, 4]      # which note(s) are accented in the beat

# Subdivision: how many notes are played per beat. 3 -triplets, 5 - quintuplets,
# 6 - sexttuplets.

subdivision = 2

sleep_time = beats_per_second / subdivision

if __name__ == '__main__':
    while True:
        for beat in range(beats_per_measure):
            if beat + 1 in accent:
                sound_accent.play()
            else:
                sound_beat.play()
            time.sleep(sleep_time)
            for sub in range(subdivision - 1):
                sound_subdivision.play()
                time.sleep(sleep_time)
                