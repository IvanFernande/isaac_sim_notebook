import numpy as np
import cv2
import os
import omni
from omni.isaac.core import World
from omni.isaac.core.objects import DynamicCuboid
from omni.isaac.sensor import Camera
from omni.isaac.core.utils.stage import add_reference_to_stage
from omni.isaac.core.utils.nucleus import get_assets_root_path

# Inicializar la aplicación de simulación
omni.timeline.get_timeline_interface().play()

# Crear el mundo de la simulación
world = World(stage_units_in_meters=1.0)

# Agregar el robot al escenario
robot_prim_path = "/World/kuka_lwr"
camera_prim_path = robot_prim_path + "/kuka_lwr_7_link/Camera"

# Crear e inicializar la cámara
camera = Camera(
    prim_path=camera_prim_path,
    frequency=30,  # Frecuencia de captura en Hz
    resolution=(512, 512)  # Resolución de la imagen
)
camera.initialize()
rgb_image = camera.get_rgb()
print(rgb_image)
print(f"Forma de la imagen RGB: {rgb_image.shape}")

ruta_guardado = '/home/javier/RL_docs/kuka_lwr_isaac_sim/kuka_lwr_isaac_project/img'
os.chdir(ruta_guardado)
cv2.imwrite('imagen_capturada.png', rgb_image)
