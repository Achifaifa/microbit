import microbit

while 1:
  microbit.display.scroll("PKT TEAM", delay=80)
  for i in range(3):
    microbit.display.show(microbit.Image.HEART)
    microbit.sleep(500)
    microbit.display.show(microbit.Image.HEART_SMALL)
    microbit.sleep(500)
  microbit.display.show("ACHIFAIFA", delay=200)
  for i in range(3):
    microbit.display.show(microbit.Image.SILLY)
    microbit.sleep(1000)
