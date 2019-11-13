import os
import sys
import yaml
import argparse
import platform


op_sys = platform.system()
if op_sys == 'Darwin':
    from Foundation import NSURL

from voice_cloning import TTS

import tensorflow as tf
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)


def main(text):
 
    self.tts = TTS()
    self.tts.speak(text)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('text', type=str)
    args = parser.parse_args()
    main(args.text)
                