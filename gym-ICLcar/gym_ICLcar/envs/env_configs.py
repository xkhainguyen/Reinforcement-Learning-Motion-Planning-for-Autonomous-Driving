# Game settings
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
CAPTION = "2D Car Simulation Environment"

CAR_LENGTH = 10
CAR_WIDTH = 10

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GRAY = (100, 100, 100)
YELLOW = (255, 255, 0)
ORANGE = (255, 125, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

ICY = (225, 225, 240) # plus/minus 10

TEXTURES = {
  'icy': ['assets/icy.bmp', 0.01],
  'rocky': ['assets/rocky.bmp', 3]
}

TRACK_FILE = "assets/track_template.bmp"
CAR_FILE = "assets/car.bmp"
CENTER_LANE_FILE = "assets/center_lane.bmp"

LATERAL_FORCE  = 20
FORWARD_FORCE = 100

START_X = 740
START_Y = 240

NUM_RANGE_SENSORS = 10
ANGLE_BETWEEN_SENSORS = 25

# reward constant definition 