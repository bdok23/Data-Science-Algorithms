import ray
from ray.rllib.agents.ppo import PPOTrainer
config = {
    "env": "CartPole-v0", 
    # Change the following line to '"framework": "tf"' to use tensorflow
    "framework": "torch", 
    "model": {
        "fcnet_hiddens": [32], 
        "fcnet_activation": "linear",
    },
}

stop = {"episode_reward_mean": 195}
ray.shutdown()
ray.init(
    num_cpus=3,
    include_dashboard=False,
    ignore_reinit_error=True, 
    log_to_driver=False,
)
# execute training
analysis = ray.tune.run(
    "PPO", 
    config=config, 
    stop=stop,
    checkpoint_at_end=True,
)

print(2)