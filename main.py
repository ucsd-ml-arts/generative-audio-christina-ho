import os
import sys
import yaml
import argparse
import platform

from voice_cloning import voiceClone

import tensorflow as tf
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)


def main(text):
    tts = voiceClone()
    f = open(text, 'r')
    contents = f.read()
    tts.speak(contents)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('text', type=str)
    args = parser.parse_args()
    main(args.text)
                