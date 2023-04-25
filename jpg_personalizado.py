import st7789
import tft_config

tft = tft_config.config(1)

def main():
    try:
        tft.init()
        tft.jpg(f'ImagenT-Display-S3.jpg', 0, 0, st7789.SLOW)

    finally:
        tft.deinit()

main()
