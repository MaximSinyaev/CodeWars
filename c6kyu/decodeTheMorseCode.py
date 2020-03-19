"""
Description:
In this kata you have to write a simple Morse code decoder. While the Morse
code is now mostly superseded by voice and digital data communication channels,
it still has its use in some applications around the world.
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

def decodeMorse(morse_code):
    # words = morse_code.split("   ")
    return " ".join(["".join([morse[letter] for letter in word.split()])
                     for word in morse_code.split("   ")]).strip()

if __name__ == "__main__":
    print(decodeMorse('.... . -.--   .--- ..- -.. .'))