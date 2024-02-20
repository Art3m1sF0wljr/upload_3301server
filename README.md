#for linux<br>
xxd -p file.asd > dump.txt<br>
cat dump.txt | python3 script_tor.py<br>

#else<br>
#usage<br>
#linux: base64 -w 0 file.txt | python3 script_tor.py<br>
#or :python3 script_tor.py <message><br>
#windows (untested): certutil -encode -f "file.txt" "file_wncoded.txt" and then idk<br> 
#
