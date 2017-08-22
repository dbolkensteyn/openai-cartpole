import gym
import time

env = gym.make('CartPole-v0')
observation = env.reset()

for t in range(1000):
    print observation

    env.render()
    observation, reward, done, info = env.step(observation[3] >= 0)

    if done:
        print "Episode finished after %d timesteps" % (t+1)
        break

    time.sleep(0.1)
