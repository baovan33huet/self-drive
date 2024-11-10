import GameEnv
import pygame
import numpy as np
from keras.models import load_model
from keras.losses import MeanSquaredError
from tensorflow.keras.activations import softmax


# Tải mô hình và chỉ định custom_objects để xử lý 'mse'
# model = load_model('ddqn_model.h5', custom_objects={'mse': MeanSquaredError, 'softmax_v2': softmax})

# model = load_model('ddqn_model_real.h5', custom_objects={'mse': MeanSquaredError, 'softmax_v2': softmax})


# Khởi tạo môi trường
game = GameEnv.RacingEnv()
game.reset()

done = False
while not done:
    # Lấy trạng thái hiện tại từ môi trường (observation)
    observation = np.array([game.get_state()])  # Thay 'game.get_state()' bằng phương thức trả về trạng thái hiện tại
    
    # Mô hình dự đoán hành động từ trạng thái hiện tại
    action = np.argmax(model.predict(observation))

    # Thực hiện hành động trong môi trường
    observation_, reward, done = game.step(action)
    
    # Vẽ môi trường (render)
    game.render(action)
