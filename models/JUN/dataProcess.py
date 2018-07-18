import librosa
import glob


class Sound(object):

    # Constructor
    def __init__(self, path = None, extension = None):
        self.raw = []               # Get sound data
        self.path = path            # Get data path
        self.extension = extension  # Get data extension
        self.dataNames = glob.glob(self.path + "*." + self.extension)  # Make name package
        print(self.path)        # For debugging
        print(self.extension)   # For debugging

    # Load raw data & attach to one chunk
    def load(self):
        for i in range(self.dataNames.__len__()):
            self.raw.append(librosa.load(self.dataNames.pop(0)))
        print(self.dataNames)   # For debugging
        print(self.raw)         # For debugging

    # process data
    # Method:
    def process(self):
        return
