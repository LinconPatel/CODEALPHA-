import numpy as np
import magenta
import tensorflow as tf
from magenta.models.music_vae import configs
from magenta.models.music_vae.trained_model import TrainedModel
import pretty_midi
import mido

# Load a pre-trained model
print("Loading MusicVAE model...")
music_vae = TrainedModel(
                configs.CONFIG_MAP['cat-mel_2bar_big'],
                batch_size=4,
                checkpoint_dir="https://storage.googleapis.com/magentadata/models/music_vae/checkpoints/cat-mel_2bar_big"
            )

# Generate music sequences
            print("Generating music sequence...")
            z = music_vae.sample(n=1, length=16)  # Generate a sequence
                midi_data = music_vae.decode(z)

# Save as a MIDI file
                            midi_filename = "generated_music.mid"
                                    print(f"Saving MIDI file: {midi_filename}")
                                    with open(midi_filename, 'wb') as f:
                                    f.write(midi_data[0].SerializeToString())

# Play the MIDI file (optional)
                                    try:
                                        import pygame
                                        pygame.init()
                                        pygame.mixer.init()
                                        pygame.mixer.music.load(midi_filename)
                                        pygame.mixer.music.play()
                                        print("Playing generated music...")
                                        while pygame.mixer.music.get_busy():
                                                continue
                                    except ImportError:
                                                print("pygame not installed. MIDI file saved, but cannot be played.")

                                                print("Music generation complete!")
