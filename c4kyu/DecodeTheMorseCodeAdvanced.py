"""
Description:
In this kata you have to write a Morse code decoder for wired electrical
telegraph.

Electric telegraph is operated on a 2-wire line with a key that, when
pressed, connects the wires together, which can be detected on a remote station.
The Morse code encodes every character being transmitted as a sequence of "dots"
(short presses on the key) and "dashes" (long presses on the key).
"""

morse = {
    ".-": "A",
    "-...": "B",
    "-.-.": "C",
    "-..": "D",
    ".": "E",
    "..-.": "F", "-----": "0",
    "--.": "G", ".----": "1",
    "....": "H", "..---": "2",
    "..": "I", "...--": "3",
    ".---": "J", "....-": "4",
    "-.-": "K", ".....": "5",
    ".-..": "L", "-....": "6",
    "--": "M", "--...": "7",
    "-.": "N", "---..": "8",
    "---": "O", "----.": "9",
    ".--.": "P", ".-.-.-": ".",
    "--.-": "Q", "--..--": ",",
    ".-.": "R", "..--..": "?",
    "...": "S", "-....-": "-",
    "-": "T", ".----.": "\"",
    "..-": "U", "---...": ":",
    "...-": "V", ".-..-.": "'",
    ".--": "W", "-..-.": "/",
    "-..-": "X", ".--.-.": "@",
    "-.--": "Y",
    "--..": "Z",
    "...---...": "SOS"
}


def decodeBits(bits):
    bits = bits.strip('0')
    words_length = [len(x) for x in bits.split('0') if x]
    pause_length = [len(x) for x in bits.split('1') if x]
    dot_unit_length = min(words_length)
    pause_min_len = min(pause_length) if pause_length else dot_unit_length
    unit_length = min(dot_unit_length, pause_min_len)

    result = bits
    pauses = {
        7: '   ',
        3: ' ',
        1: '',
    }
    chars = {
        3: '-',
        1: '.'
    }
    print(unit_length, words_length)
    for char in chars:
        result = result.replace('1' * (char * unit_length), chars[char])
    for pause in pauses:
        result = result.replace('0' * (pause * unit_length), pauses[pause])
    print(result)
    return decodeMorse(result)


def decodeMorse(morse_code):
    # words = morse_code.split("   ")
    return " ".join(["".join([morse[letter] for letter in word.split()])
                     for word in morse_code.split("   ")]).strip()


if __name__ == "__main__":
    bits = '1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011'
    # print(decodeMorse('.... . -.--   .--- ..- -.. .'))
    print(decodeBits('000000011100000'))
