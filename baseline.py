def baseline_model():
  model =Sequential()
  model.add(Dense(13,input_dim=1,activation='tanh'))
  model.add(Dense(1))
  opt=Adagrad(learning_rate=0.001,inititial_accumulator_value=0.1,epsilon=1e-6,name='Adagrad')
  model.compile(loss='mean_squared_error',optimizer=opt)
  return model
