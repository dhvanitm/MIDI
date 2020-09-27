from mido import MidiFile

# octave = []
# note = {}
#
# for i in range(0,122,12):
#     note['C']  = i
#     note['C#'] = i+1
#     note['D']  = i+2
#     note['D#'] = i+3
#     note['E']  = i+4
#     note['F']  = i+5
#     note['F#'] = i+6
#     note['G']  = i+7
#     note['G#'] = i+8
#     note['A']  = i+9
#     note['A#'] = i+10
#     note['B']  = i+11
#     octave.append(note)
#
# print(octave)
# C:\DATA\DHVANIT\projects\MIDI

out = open('C:\DATA\DHVANIT\projects\MIDI\output.csv', 'w')
In = open('C:\DATA\DHVANIT\projects\MIDI\palpal.mid', 'r')
sample = open('C:\DATA\DHVANIT\projects\MIDI\sample.txt', 'w')
mid = MidiFile('C:\DATA\DHVANIT\projects\MIDI\palpal.mid')

for _ in range(50):
    #     print Out.readline()
    #     sample.write(Out.readline())

    InLine = In.readline()
    #     print InLine
    #     print ' '.join(format(ord(x),'b') for x in InLine)
    sample.write('\n***********')
    sample.write(InLine)
    sample.write("------------")
    sample.write(' '.join(format(ord(x), 'x') for x in InLine))
#     for i in InLine:
#         print number


#  port = mido.ports.BasePort()
# port._open()
for i, track in enumerate(mid.tracks):
    k = 1
    print('Track {}: {}:{}'.format(i, track.name, track))
    for msg in track:
        print('msg', msg)
        out.write(str(msg) + '\n')
        if k == 50:
            break
        k = k + 1
#         out.write('u\'' + str(msg) + '\'')


# Out.close()
In.close()
sample.close()
#        raw_input("next")
#     port.send(ms1)
# for ms1 in mid.play():
# port.close()
