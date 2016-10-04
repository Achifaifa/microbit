import microbit

while 1:
  microbit.display.show("GAMAKER", delay=200, wait=True, loop=False, clear=False)
  microbit.display.scroll(" LEMA AQUI", delay=80)
  for i in range(3):
    microbit.display.show(microbit.Image.HEART)
    microbit.sleep(500)
    microbit.display.show(microbit.Image.HEART_SMALL)
    microbit.sleep(500)
  microbit.display.scroll("<--", delay=80)