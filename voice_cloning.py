import sys
import yaml
from voicecloning.encoder import inference as encoder
from voicecloning.vocoder import inference as vocoder
from voicecloning.synthesizer.inference import Synthesizer
from pathlib import Path
import numpy as np
import librosa
import argparse
import torch


class voiceClone:
    def __init__(self):
        # CUDA check.
        if not torch.cuda.is_available():
            print('[TTS] Your PyTorch installation is not configured to use CUDA.'
                  'Unfortunately, CPU-only inference is not supported.', file=sys.stderr)
            quit(-1)

        # Read config.
        config = yaml.load(open('config.yaml', 'r'), Loader=yaml.FullLoader)
        syn_model_dir = config['syn_model_dir']
        voc_model_fpath = config['voc_model_fpath']
        enc_model_fpath = config['enc_model_fpath']

        # Load models.
        self.synthesizer = Synthesizer(
            Path(syn_model_dir).joinpath('taco_pretrained'), low_mem=False)
        vocoder.load_model(Path(voc_model_fpath))
        encoder.load_model(Path(enc_model_fpath))
        in_fpath = Path('obama1hr.wav');
        preprocessed_wav = encoder.preprocess_wav(in_fpath)
        self.embed = encoder.embed_utterance(preprocessed_wav)
        
    def speak(self, text, write_audio=True):
        spec = self.synthesizer.synthesize_spectrograms([text], [self.embed])[0]
        generated_wav = vocoder.infer_waveform(spec)
        generated_wav = np.pad(
            generated_wav, (0, self.synthesizer.sample_rate), mode='constant')
        if write_audio:
            import librosa
            words = text.split()
            fname = 'generated' if not words else words[min(3, len(words) - 1)]
            while len(fname) > 1 and not fname[-1].isalpha():
                fname = fname[:-1]
            librosa.output.write_wav(fname + '.wav',
                                     generated_wav.astype(np.float32),
                                     self.synthesizer.sample_rate)
