import gym
import time

env = gym.make('CartPole-v0')
observation = env.reset()

print(env.action_space)

print(env.observation_space)
print(env.observation_space.high)
print(env.observation_space.low)

for t in range(1000):
    print observation

    env.render()
    observation, reward, done, info = env.step(t % 2)

    if done:
        print "Episode finished after %d timesteps" % (t+1)
        break

    time.sleep(0.1)
