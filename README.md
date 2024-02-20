#for linux<br>
xxd -p file.asd > dump.txt<br>
cat dump.txt | python3 script_tor.py<br>

#else<br>
#usage
#linux: base64 -w 0 file.txt | python3 script_tor.py
#or :python3 script_tor.py <message>
#windows (untested): certutil -encode -f "file.txt" "file_wncoded.txt" and then idk 
#
