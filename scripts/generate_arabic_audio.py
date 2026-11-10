"""Generate Arabic letter names and UI phrases for SignBridge AI.
Run in GitHub Actions. MP3 files are served locally from GitHub Pages.
"""
from pathlib import Path
from gtts import gTTS
import time

out=Path("audio/ar");out.mkdir(parents=True,exist_ok=True)
letters={"ا":"ألف","ب":"باء","ت":"تاء","ث":"ثاء","ج":"جيم","ح":"حاء","خ":"خاء","د":"دال","ذ":"ذال","ر":"راء","ز":"زاي","س":"سين","ش":"شين","ص":"صاد","ض":"ضاد","ط":"طاء","ظ":"ظاء","ع":"عين","غ":"غين","ف":"فاء","ق":"قاف","ك":"كاف","ل":"لام","م":"ميم","ن":"نون","ه":"هاء","و":"واو","ي":"ياء"}
phrases={"test":"مرحباً، أنا ساين بريدج. الصوت العربي يعمل الآن.","auto":"تم تفعيل النطق التلقائي","empty":"لم يتم التعرف على إشارة بعد"}
for k,v in letters.items():phrases["letter-"+format(ord(k),"x")]=v
for key,value in phrases.items():
    dest=out/(key+".mp3")
    if dest.exists() and dest.stat().st_size>1000:continue
    for attempt in range(4):
        try:
            gTTS(text=value,lang="ar").save(str(dest))
            print(key,flush=True)
            break
        except Exception:
            if attempt==3:raise
            time.sleep(3*(attempt+1))
