import microbit

while 1:
  microbit.display.scroll("GAMAKER.ORG", delay=80)
  for i in range(3):
    microbit.display.show(microbit.Image.HEART)
    microbit.sleep(500)
    microbit.display.show(microbit.Image.HEART_SMALL)
    microbit.sleep(500)
