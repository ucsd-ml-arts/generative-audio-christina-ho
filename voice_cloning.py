from encoder.params_model import model_embedding_size as speaker_embedding_size
from utils.argutils import print_args
from synthesizer.inference import Synthesizer
from encoder import inference as encoder
from vocoder import inference as vocoder
from pathlib import Path
import numpy as np
import librosa
import argparse
import torch
import sys

class voiceClone:
    def __init__(self):
        # For playing audio.
        # Only import if a TTS object is created.
        self.sd = __import__('sounddevice')

        # CUDA check.
        if not torch.cuda.is_available():
            print('[TTS] Your PyTorch installation is not configured to use CUDA.'
                  'Unfortunately, CPU-only inference is not supported.', file=sys.stderr)
            quit(-1)

        # Read config.
        config = yaml.load(open('config.yaml', 'r'), Loader=yaml.FullLoader)
        syn_model_dir = config['syn_model_dir']
        voc_model_fpath = config['voc_model_fpath']

        # Load models.
        self.synthesizer = Synthesizer(
            Path(syn_model_dir).joinpath('taco_pretrained'), low_mem=False)
        vocoder.load_model(Path(voc_model_fpath))
        self.synthesizer.synthesize_spectrograms(['test 1'], self.embed)
        in_fpath = Path()
        preprocessed_wav = encoder.preprocess_wav(in_fpath)
        # - If the wav is already loaded:
        original_wav, sampling_rate = librosa.load(in_fpath)
        preprocessed_wav = encoder.preprocess_wav(original_wav, sampling_rate)
        embed = encoder.embed_utterance(preprocessed_wav)
        
    def speak(self, text, write_audio=False):
        try:
            spec = self.synthesizer.synthesize_spectrograms([text], [embed])[0]
            generated_wav = vocoder.infer_waveform(spec)
            generated_wav = np.pad(
                generated_wav, (0, self.synthesizer.sample_rate), mode='constant')
            self.sd.stop()
            self.sd.play(generated_wav, self.synthesizer.sample_rate)
            if write_audio:
                import librosa
                words = text.split()
                fname = words[min(3, len(words) - 1)] or 'generated'
                while len(fname) > 1 and not fname[-1].isalpha():
                    fname = fname[:-1]
                librosa.output.write_wav(fname + '.wav',
                                         generated_wav.astype(np.float32),
                                         self.synthesizer.sample_rate)
        except Exception as e:
            print('TTS exception: %s' % repr(e))