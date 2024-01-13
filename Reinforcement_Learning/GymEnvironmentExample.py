from gym.wrappers.monitoring.video_recorder import VideoRecorder
from pyvirtualdisplay import Display
import gym
from base64 import b64encode
from IPython.display import HTML
import ray
from ray.rllib.agents.ppo import PPOTrainer
from tenacity import stop_after_attempt

"""
def render_mp4(videopath: str) -> str:
   
        mp4 = open(videopath, 'rb').read()
        base64_encoded_mp4 = b64encode(mp4).decode()
        return f'<video width=400 controls><source src="data:video/mp4;' 
            f'base64,{base64_encoded_mp4}" type="video/mp4"></video>'



display = Display(visible=False, size=(1400, 900))
_ = display.start()
before_training = "before_training.mp4"


env = gym.make('CartPole-v0')
video = VideoRecorder(env, before_training)
# returns an initial observation
env.reset()
for i in range(200):
    env.render()
    video.capture_frame()
    #env.action_space.sample() produces either 0 (left) or 1 (right).
    observation, reward, done, info = env.step(env.action_space.sample())
    # Not printing this time

video.close()
env.close()

html = render_mp4(before_training)
HTML(html)
"""
parameter_search_config = {
    "env": "CartPole-v0",
    "framework": "torch",

    #Hyperparameter tuning
    "model": {
        "fcnet_hiddens": ray.tune.grid_search([[32], [64]]),
        "fcnet_activation": ray.tune.grid_search(["linear", "relu"]),
    },
    "lr": ray.tune.uniform(1e-7, 1e-2)
}

# To explicitly stop or restart Ray, use the shutdown API.
ray.shutdown()

ray.init(
    num_cpus=12,
    include_dashboard=False,
    ignore_reinit_error=True,
    log_to_driver=False,
)

paramter_search_analysis = ray.tune.run(
    "PPO",
    config=parameter_search_config,
    stop=stop,
    num_samples=5,
    metric="timesteps_total",
    mode="min",
)

print(
    "Best hyperparamters found:",
    parameter_search_analysis.best_config,
)

print(2)