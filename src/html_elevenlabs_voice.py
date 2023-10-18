import elevenlabs
import json
text = "On 12th November 2009, we bid a sorrowful farewell to Tatiana Antonovna Kuznetsova, who succumbed to her battle with cancer at the age of 86. Born in Bobruisk in 1923, she was a pillar of strength and bravery throughout her life, overcoming tremendous adversities with an enduring spirit. \n\nTatiana contributed significantly to the war effort as a factory worker during the Second World War and continued her tireless service afterwards. A devoted Eastern Orthodox Christian, her faith and active participation in the local church community positively influenced many lives. As the devoted wife of Nikolai and the loving mother to Igor and Elena, she molded a traditional nuclear family and was a guiding light to her children.\n\nTatiana will be remembered as a symbol of resilience, faith, and a mother's unwavering love. Her spirit will continue to shine within those who knew her. Our thoughts and prayers go out to Nikolai, Igor, Elena, and the rest of her grieving family. May she find eternal peace in the arms of the Lord. Rest in Peace, Tatiana Kuznetsova. "

# split into sentences by "\n", ".", "?", "!"
sentences = []
sentence = ""
for char in text:
    sentence += char
    if char in ["\n", ".", "?", "!"]:
        sentences.append(sentence)
        sentence = ""
sentences.append(sentence)

sentences = [s.strip() for s in sentences]
sentences = [s for s in sentences if s != ""]


# concatenate sentences into paragraphs
paragraphs = []
max_len = 250
paragraph = ""
for s in sentences:
    if len(paragraph + " " + s) > max_len:
        paragraphs.append(paragraph)
        paragraph = ""
    paragraph += " " + s
paragraphs.append(paragraph)

paragraphs = [p.strip() for p in paragraphs]
paragraphs = [p for p in paragraphs if p != ""]
for p in paragraphs:
    print(p)
    print("")

from typing import List

audios: List[bytes] = []
for p in paragraphs[:2]:
    audio = elevenlabs.generate(
        text=p,
        voice="Bella",
        model="eleven_multilingual_v2"
    )
    audios.append(audio)

# play audio
for audio in audios:
    elevenlabs.play(audio)

audio_all = audios[0] + audios[1]
elevenlabs.play(audio_all)