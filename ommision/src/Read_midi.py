from mido import MidiFile
import numpy as np
from numpy.core._multiarray_umath import dtype
from numpy.core.numeric import array_equal

mid = MidiFile(r"D:\MIDI_Project\resources\LoveMeLikeYouDo.mid")
outfile = open("D:\MIDI_Project\ommision\data\outfile.txt", "w")

outfile.write("Midi file: {}\n".format(mid.filename))
outfile.write("Midi play length in seconds: {}\n".format(mid.length))
outfile.write("midi ticks; {}\n".format(mid.ticks_per_beat))
outfile.write("midi tracks: {}\n".format(len(mid.tracks)))

piano_keys = np.zeros((88,1),dtype = np.int8)
note_map = np.zeros(piano_keys.shape,dtype=np.int8)
for key in range(len(piano_keys)):
    piano_keys[key] = key+1
print(piano_keys.shape)

print(mid.tracks)

for i, track in enumerate(mid.tracks):
    outfile.write('track {}:{}\n'.format(i, track.name))
    print('track {}:{}'.format(i, track.name))
    if i == 0:
        for msg in track:
            if msg.is_meta:
                if msg.type == "time_signature":
                    outfile.write("midi time signature num: {} den: {}\n".format(msg.numerator, msg.denominator))
                if msg.type == "key_signature":
                    outfile.write("midi key_signature:{}\n".format(msg.key))
                if msg.type == "set_tempo":
                    outfile.write("midi tempo: {}\n".format(msg.tempo))
    if i != 0:
        for msg in track:
            if msg.is_meta:
                pass
            else:
                print("{}".format(msg))
                note_map[msg.note-1] = 1
                print(msg.note)
                piano_keys = np.append(piano_keys,note_map,axis=1)
                note_map = np.zeros(note_map.shape,dtype= np.int8)
        for raw in piano_keys:
            print(raw)
            
            if (True = array_equal(raw,))
        print(piano_keys.shape)
        temp = np.zeros(piano_keys.shape[1])
        print(temp.shape)
        temp[0] = msg.note
#         np.savetxt(outfile,piano_keys,delimiter=',',fmt='%d')
#         outfile.write("{}\n".format(piano_keys))
#             print(piano_keys.shape)
            #outfile.write("{}\n".format(msg))
outfile.close()
