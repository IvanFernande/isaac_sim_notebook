import numpy as np
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
camera_prim_path = robot_prim_path + "/kuka_lwr_7_link/camera"

# Crear e inicializar la cámara
camera = Camera(
    prim_path=camera_prim_path,
    frequency=20,  # Frecuencia de captura en Hz
    resolution=(1280, 720)  # Resolución de la imagen
)
camera.initialize()

# Agregar un objeto dinámico al escenario para interacción
cube = world.scene.add(
    DynamicCuboid(
        prim_path="/World/Cube",
        name="cube",
        position=np.array([0.5, 0.0, 0.5]),  # Posición inicial del cubo
        size=0.05,  # Tamaño del cubo
        color=np.array([1.0, 0.0, 0.0])  # Color rojo
    )
)

# Iniciar la simulación
world.reset()

# Bucle principal de la simulación
while omni.timeline.get_timeline_interface().is_playing():
    # Avanzar un paso en la simulación
    world.step(render=True)

    # Obtener la imagen RGB de la cámara
    rgb_image = camera.get_rgba()

    # Procesar la imagen según sea necesario
    # Por ejemplo, mostrar la forma de la imagen
    print(f"Forma de la imagen RGB: {rgb_image.shape}")

    # Detener la simulación después de un tiempo
    if world.current_time_step_index >= 100:
        break

# Finalizar la aplicación de simulación
omni.timeline.get_timeline_interface().stop()
