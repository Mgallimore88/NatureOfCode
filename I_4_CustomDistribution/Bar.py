from p5 import rect, rect_mode


class Bar:
    def __init__(self, barWidth=10, windowHeight=100, barHeight=50, index=0):
        self.barWidth = barWidth
        self.index = index
        self.windowHeight = windowHeight
        self.xPos = self.index * barWidth
        self.barHeight = barHeight
        self.yPos = windowHeight - barHeight

    def drawBar(self):
        rect_mode("CORNER")
        rect((self.xPos, self.yPos), self.barWidth, self.windowHeight)

    def grow(self):
        self.barHeight += 3
        self.yPos = self.windowHeight - self.barHeight
