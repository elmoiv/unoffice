from unoffice import unlock
import os

os.chdir(os.path.dirname(os.path.realpath(__file__)))

for ext in ['docx', 'pptx', 'xlsx']:
    unlock(
        os.path.join(
            'tests',
            'test.' + ext
            )
        )