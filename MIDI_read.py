'''
Created on 01-Nov-2017

@author: Lenovo
'''
import midi
import mido     

msg = mido.Message('note_on', note=60)
msg.note
msg.bytes()
msg.copy(channel=2)

port = mido.open

mid = mido.MidiFile('churaliya.mid')
for msg in mid.play():
    port.send(msg)