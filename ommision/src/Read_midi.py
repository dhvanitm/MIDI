from mido import MidiFile
import os

mid = MidiFile(r"D:\MIDI_Project\resources\ekpal.mid")
outfile = open("D:\MIDI_Project\ommision\data\outfile.txt", "w")
line_no = 1
for i, track in enumerate(mid.tracks):
    print('track {}:{}'.format(i, track.name))
    for msg in track:
        outfile.write(str(line_no) + "\t")
        if msg.is_meta:
            print(msg)
        else:
            outfile.write(str(msg))
        line_no = line_no +1
        outfile.write("\n")
outfile.close()
