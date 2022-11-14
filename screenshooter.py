import mss.tools


def take_screnshot(x0,y0,x1,y1):
    with mss.mss() as sct:
        if x1 > x0:
            width = x1 - x0
            left = x0
        else:
            width = x0 - x1
            left = x1
        if y1 > y0:
            height = y1 - y0
            top = y0
        else:
            height = y0 - y1
            top = y1
        monitor = {"top": top, "left": left, "width": width, "height": height}
        # output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)
        output = "sct.png".format(**monitor)
        # Grab the data
        sct_img = sct.grab(monitor)

        # Save to the picture file
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
        print(output)
