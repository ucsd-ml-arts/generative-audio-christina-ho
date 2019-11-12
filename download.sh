code=$(wget --save-cookies cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1n1sPXvT34yXFLT47QZA6FIRGrwMeSsZc' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')
wget -O pretrained.zip --load-cookies cookies.txt "https://docs.google.com/uc?export=download&confirm=${code}&id=1n1sPXvT34yXFLT47QZA6FIRGrwMeSsZc"
unzip pretrained.zip
mv encoder/saved_models voicecloning/encoder
mv synthesizer/saved_models voicecloning/synthesizer
mv vocoder/saved_models voicecloning/vocoder
rmdir encoder
rmdir synthesizer
rmdir vocoder
rm pretrained.zip