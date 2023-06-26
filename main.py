import mido
import time

output_ports = mido.get_output_names()

if len(output_ports) < 2:
    print("Não há portas MIDI suficientes disponíveis.")
    exit()

port_name = output_ports[1]

try:
    out = mido.open_output(port_name)
except OSError as e:
    print("Erro ao abrir a porta MIDI:", e)
    exit()

with out:
    note_on = mido.Message('note_on', note=99, velocity=127)
    note_off = mido.Message('note_off', note=99, velocity=0)
    out.send(note_on)
    time.sleep(1.0)
    out.send(note_off)
    time.sleep(0.1)
